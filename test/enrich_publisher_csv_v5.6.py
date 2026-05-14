"""
enrich_publisher_csv_v5.6.py
Mục đích: Đọc CSV xuất từ Springer Link / Taylor & Francis (vốn không có trường abstract),
         làm giàu tóm tắt qua CrossRef → OpenAlex → Semantic Scholar,
         lấy URL truy cập mở qua Unpaywall, xuất ra RIS đầy đủ trường.

Đầu vào:  springer*.csv và/hoặc tf*.csv
Đầu ra:   tệp RIS tương ứng + báo cáo CSV trong thư mục --out
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
import time
import urllib.parse
from dataclasses import dataclass, field
from typing import Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

# Bảo đảm stdout/stderr UTF-8 trên Windows
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ---------------- Cấu hình ----------------
MAILTO = "hoatx611@gmail.com"
USER_AGENT = f"NCS-DT-Port-SR/5.6 (mailto:{MAILTO})"
REQ_TIMEOUT = 12

DELAY_CROSSREF = 0.05
DELAY_OPENALEX = 0.10
DELAY_SEMANTIC = 0.20
DELAY_UNPAYWALL = 0.10

SPRINGER_COLUMNS = {
    "title": "Item Title",
    "authors": "Authors",
    "year": "Publication Year",
    "doi": "Item DOI",
    "journal": "Publication Title",
    "book_series": "Book Series Title",
    "volume": "Journal Volume",
    "issue": "Journal Issue",
    "url": "URL",
    "type": "Content Type",
}
TF_COLUMNS = {
    "title": "Article title",
    "authors": "Authors",
    "year": "Volume year",
    "doi": "DOI",
    "journal": "Journal title",
    "volume": "Volume",
    "issue": "Issue",
    "pages": "Pages",
    "online_date": "Published online date",
    "url": "URL",
}


@dataclass
class Record:
    source: str
    title: str = ""
    authors_raw: str = ""
    authors: list[str] = field(default_factory=list)
    year: str = ""
    doi: str = ""
    journal: str = ""
    book_series: str = ""
    volume: str = ""
    issue: str = ""
    pages: str = ""
    url: str = ""
    content_type: str = ""
    abstract: str = ""
    abstract_source: str = ""
    oa_url: str = ""


def http_get_json(url: str, headers: dict | None = None) -> Optional[dict]:
    headers = headers or {}
    headers.setdefault("User-Agent", USER_AGENT)
    headers.setdefault("Accept", "application/json")
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=REQ_TIMEOUT) as resp:
            data = resp.read().decode("utf-8", errors="replace")
            return json.loads(data)
    except HTTPError as e:
        if e.code == 404:
            return None
        if e.code in (429, 500, 502, 503, 504):
            time.sleep(2.0)
        return None
    except (URLError, json.JSONDecodeError, TimeoutError):
        return None
    except Exception:
        return None


def clean_jats(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"</?\s*(jats:|html:)?\w+[^>]*>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"&[a-zA-Z]+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"^(Abstract|Summary)[\s:.\-]+", "", text, flags=re.IGNORECASE)
    return text


def normalize_doi(raw: str) -> str:
    if not raw:
        return ""
    s = raw.strip()
    s = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", s, flags=re.IGNORECASE)
    s = re.sub(r"^doi:\s*", "", s, flags=re.IGNORECASE)
    return s.strip()


def parse_authors(raw: str) -> list[str]:
    if not raw:
        return []
    if "," in raw:
        return [a.strip() for a in raw.split(",") if a.strip()]
    splits = re.split(r"(?<=[a-z])(?=[A-Z])", raw)
    return [s.strip() for s in splits if s.strip()]


def detect_source(csv_path: str, header: list[str]) -> str:
    h = [c.lower() for c in header]
    if "item title" in h and "item doi" in h:
        return "springer"
    if "article title" in h and "doi" in h:
        return "tf"
    name = os.path.basename(csv_path).lower()
    if "spring" in name:
        return "springer"
    if name.startswith("tf") or "tandf" in name:
        return "tf"
    raise ValueError(f"Không nhận diện được nguồn cho {csv_path}")


def read_csv(csv_path: str) -> tuple[list[Record], str]:
    with open(csv_path, "r", encoding="utf-8-sig", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames or []
        source = detect_source(csv_path, header)
        cols = SPRINGER_COLUMNS if source == "springer" else TF_COLUMNS
        records: list[Record] = []
        for row in reader:
            r = Record(source=source)
            r.title = (row.get(cols["title"]) or "").strip()
            r.authors_raw = (row.get(cols["authors"]) or "").strip()
            r.authors = parse_authors(r.authors_raw)
            r.year = (row.get(cols["year"]) or "").strip()
            r.doi = normalize_doi(row.get(cols["doi"]) or "")
            r.journal = (row.get(cols["journal"]) or "").strip()
            r.volume = (row.get(cols["volume"]) or "").strip()
            r.issue = (row.get(cols["issue"]) or "").strip()
            r.url = (row.get(cols["url"]) or "").strip()
            if source == "springer":
                r.book_series = (row.get(cols["book_series"]) or "").strip()
                r.content_type = (row.get(cols["type"]) or "").strip()
            else:
                r.pages = (row.get(cols["pages"]) or "").strip()
                if r.year and (not r.year.isdigit() or len(r.year) != 4 or int(r.year) > 2030):
                    online = (row.get(cols["online_date"]) or "").strip()
                    m = re.search(r"\b(20\d{2})\b", online)
                    r.year = m.group(1) if m else ""
            records.append(r)
        return records, source


def fetch_crossref_abstract(doi: str) -> str:
    if not doi:
        return ""
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}?mailto={urllib.parse.quote(MAILTO)}"
    data = http_get_json(url)
    time.sleep(DELAY_CROSSREF)
    if not data:
        return ""
    msg = data.get("message", {})
    return clean_jats((msg.get("abstract") or ""))


def fetch_openalex_abstract(doi: str) -> str:
    if not doi:
        return ""
    url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe='/')}?mailto={urllib.parse.quote(MAILTO)}"
    data = http_get_json(url)
    time.sleep(DELAY_OPENALEX)
    if not data:
        return ""
    inv = data.get("abstract_inverted_index")
    if not isinstance(inv, dict):
        return ""
    positions: list[tuple[int, str]] = []
    for token, idxs in inv.items():
        for i in idxs:
            positions.append((i, token))
    positions.sort()
    return clean_jats(" ".join(tok for _, tok in positions))


def fetch_semanticscholar_abstract(doi: str) -> str:
    if not doi:
        return ""
    url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(doi, safe='/')}?fields=abstract"
    data = http_get_json(url)
    time.sleep(DELAY_SEMANTIC)
    if not data:
        return ""
    return clean_jats((data.get("abstract") or ""))


def fetch_unpaywall_oa_url(doi: str) -> str:
    if not doi:
        return ""
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='/')}?email={urllib.parse.quote(MAILTO)}"
    data = http_get_json(url)
    time.sleep(DELAY_UNPAYWALL)
    if not data:
        return ""
    best = data.get("best_oa_location") or {}
    return (best.get("url_for_pdf") or best.get("url") or "").strip()


def enrich_record(r: Record) -> None:
    if not r.doi:
        r.abstract = ""
        r.abstract_source = "missing"
        return
    abs_text = fetch_crossref_abstract(r.doi)
    if abs_text:
        r.abstract = abs_text
        r.abstract_source = "crossref"
    else:
        abs_text = fetch_openalex_abstract(r.doi)
        if abs_text:
            r.abstract = abs_text
            r.abstract_source = "openalex"
        else:
            abs_text = fetch_semanticscholar_abstract(r.doi)
            if abs_text:
                r.abstract = abs_text
                r.abstract_source = "semanticscholar"
            else:
                r.abstract = ""
                r.abstract_source = "missing"
    r.oa_url = fetch_unpaywall_oa_url(r.doi)


def to_ris_record(r: Record) -> str:
    ty = "JOUR"
    if r.source == "springer" and r.content_type:
        ct = r.content_type.lower()
        if "chapter" in ct:
            ty = "CHAP"
        elif "book" in ct:
            ty = "BOOK"
        elif "conference" in ct or "proceeding" in ct:
            ty = "CPAPER"
    lines = [f"TY  - {ty}"]
    if r.title:
        lines.append(f"TI  - {r.title}")
    for a in r.authors:
        lines.append(f"AU  - {a}")
    if r.year:
        lines.append(f"PY  - {r.year}")
    if r.journal:
        lines.append(f"JF  - {r.journal}")
        lines.append(f"T2  - {r.journal}")
    if r.book_series:
        lines.append(f"T3  - {r.book_series}")
    if r.volume:
        lines.append(f"VL  - {r.volume}")
    if r.issue:
        lines.append(f"IS  - {r.issue}")
    if r.pages:
        lines.append(f"SP  - {r.pages}")
    if r.doi:
        lines.append(f"DO  - {r.doi}")
    if r.url:
        lines.append(f"UR  - {r.url}")
    if r.abstract:
        lines.append(f"AB  - {r.abstract}")
    src_label = "Springer Link" if r.source == "springer" else "Taylor & Francis"
    lines.append(f"DP  - {src_label}")
    if r.abstract_source:
        lines.append(f"N1  - abstract_source={r.abstract_source}")
    if r.oa_url:
        lines.append(f"N1  - oa_url={r.oa_url}")
    lines.append("ER  - ")
    return "\n".join(lines) + "\n"


def write_ris(records: list[Record], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(to_ris_record(r))


def write_report(records: list[Record], out_path: str) -> None:
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source", "doi", "year", "title_snippet", "abstract_source", "abstract_len", "oa_url"])
        for r in records:
            w.writerow([
                r.source,
                r.doi,
                r.year,
                (r.title[:100] + "...") if len(r.title) > 100 else r.title,
                r.abstract_source,
                len(r.abstract),
                r.oa_url,
            ])


def process(csv_path: str, out_dir: str, max_rows: Optional[int] = None) -> dict:
    print(f"[+] Đọc {csv_path}")
    records, source = read_csv(csv_path)
    if max_rows is not None:
        records = records[:max_rows]
    print(f"    Phát hiện nguồn: {source}; số bản ghi: {len(records)}")

    print(f"[+] Làm giàu tóm tắt qua CrossRef → OpenAlex → Semantic Scholar; Unpaywall lấy OA URL...")
    n_total = len(records)
    counters = {"crossref": 0, "openalex": 0, "semanticscholar": 0, "missing": 0, "no_doi": 0}
    n_oa = 0
    for i, r in enumerate(records, 1):
        if not r.doi:
            r.abstract_source = "no_doi"
            counters["no_doi"] += 1
        else:
            enrich_record(r)
            counters[r.abstract_source] = counters.get(r.abstract_source, 0) + 1
            if r.oa_url:
                n_oa += 1
        if i % 25 == 0 or i == n_total:
            print(f"    {i}/{n_total}  CR={counters['crossref']} OA={counters['openalex']} S2={counters['semanticscholar']} miss={counters['missing']} no_doi={counters['no_doi']} | OA_url={n_oa}")

    base = os.path.splitext(os.path.basename(csv_path))[0]
    ris_path = os.path.join(out_dir, base + ".ris")
    rep_path = os.path.join(out_dir, base + "_enrichment_report.csv")
    write_ris(records, ris_path)
    write_report(records, rep_path)
    print(f"[+] Đã ghi RIS: {ris_path}")
    print(f"[+] Đã ghi báo cáo: {rep_path}")

    pct = lambda n: f"{n}/{n_total} ({100*n/max(n_total,1):.1f}%)"
    summary = {
        "input": csv_path,
        "ris": ris_path,
        "report": rep_path,
        "total": n_total,
        "crossref": counters["crossref"],
        "openalex": counters["openalex"],
        "semanticscholar": counters["semanticscholar"],
        "missing": counters["missing"],
        "no_doi": counters["no_doi"],
        "oa_url": n_oa,
        "with_abstract": counters["crossref"] + counters["openalex"] + counters["semanticscholar"],
    }
    print(f"    → có tóm tắt: {pct(summary['with_abstract'])}")
    print(f"    → CrossRef: {pct(counters['crossref'])} | OpenAlex: {pct(counters['openalex'])} | S2: {pct(counters['semanticscholar'])}")
    print(f"    → thiếu tóm tắt: {pct(counters['missing'] + counters['no_doi'])}")
    print(f"    → có OA URL (Unpaywall): {pct(n_oa)}")
    return summary


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+", help="Các tệp CSV cần xử lý (Springer hoặc T&F).")
    p.add_argument("--out", default=".", help="Thư mục đầu ra.")
    p.add_argument("--max-rows", type=int, default=None, help="Giới hạn số bản ghi để chạy thử.")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    summaries = []
    for csv_path in args.inputs:
        summaries.append(process(csv_path, args.out, args.max_rows))

    print("\n" + "=" * 60)
    print("TỔNG KẾT")
    print("=" * 60)
    grand_total = sum(s["total"] for s in summaries)
    grand_with = sum(s["with_abstract"] for s in summaries)
    print(f"Tổng số bản ghi: {grand_total}")
    print(f"Có tóm tắt:      {grand_with} ({100*grand_with/max(grand_total,1):.1f}%)")
    print(f"Thiếu tóm tắt:   {grand_total - grand_with}")
    for s in summaries:
        name = os.path.basename(s["input"])
        print(f"  {name:30s} {s['total']:4d} bản ghi | có tóm tắt {s['with_abstract']:3d} ({100*s['with_abstract']/max(s['total'],1):.1f}%) | OA URL {s['oa_url']:3d}")


if __name__ == "__main__":
    main()
