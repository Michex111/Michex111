#!/usr/bin/env python3
"""Render the profile's activity card (assets/generated/stats.svg).

The card is built from the public GitHub REST API so the README does not depend
on a third-party stats service. Standard library only; run by
.github/workflows/profile-assets.yml.

    GITHUB_TOKEN=... python scripts/generate_stats.py --user Michex111 \
        --out assets/generated/stats.svg

`--data file.json` renders from a saved snapshot instead of calling the API,
and `--dump file.json` saves the snapshot that was rendered.

Counted: the user's own public repositories, excluding forks, archived
repositories and the profile repository itself.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

API = "https://api.github.com"

SANS = "Inter, 'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'SFMono-Regular', Menlo, Consolas, 'Liberation Mono', monospace"
PALETTE = ["#3B82F6", "#22D3EE", "#8B5CF6", "#C084FC", "#6366F1", "#2DD4BF"]
OTHER = "#334155"
MAX_LANGS = 6
MIN_SHARE = 0.003


# --------------------------------------------------------------------------- data
def _get(path: str, token: str | None) -> tuple[object, dict[str, str]]:
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "profile-stats-card",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp), dict(resp.headers)


def _count_commits(owner: str, repo: str, author: str, since: str, token: str | None) -> int:
    try:
        body, headers = _get(
            f"/repos/{owner}/{repo}/commits?author={author}&since={since}&per_page=1", token)
    except urllib.error.HTTPError as exc:
        if exc.code == 409:  # empty repository
            return 0
        raise
    match = re.search(r'[?&]page=(\d+)>; rel="last"', headers.get("Link", ""))
    return int(match.group(1)) if match else len(body)  # type: ignore[arg-type]


def collect(user: str, token: str | None) -> dict:
    repos: list[dict] = []
    page = 1
    while True:
        batch, _ = _get(f"/users/{user}/repos?type=owner&per_page=100&page={page}", token)
        assert isinstance(batch, list)
        repos += batch
        if len(batch) < 100:
            break
        page += 1

    own = [r for r in repos
           if not r["fork"] and not r["archived"] and r["name"].lower() != user.lower()]
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ")

    languages: dict[str, int] = {}
    commits = 0
    for repo in own:
        langs, _ = _get(f"/repos/{user}/{repo['name']}/languages", token)
        assert isinstance(langs, dict)
        for name, size in langs.items():
            languages[name] = languages.get(name, 0) + int(size)
        commits += _count_commits(user, repo["name"], user, since, token)

    return {
        "user": user,
        "repos": len(own),
        "stars": sum(r["stargazers_count"] for r in own),
        "commits_12mo": commits,
        "languages": sorted(languages.items(), key=lambda kv: -kv[1]),
    }


# --------------------------------------------------------------------------- render
def _fingerprint(data: dict) -> str:
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]


def render(data: dict, updated: str) -> str:
    langs = [(n, b) for n, b in data["languages"] if b > 0]
    total = sum(b for _, b in langs) or 1
    # Name the biggest languages; fold slivers (< MIN_SHARE) into "Other".
    top = [(n, b) for n, b in langs[:MAX_LANGS] if b / total >= MIN_SHARE]
    rest = total - sum(b for _, b in top)
    segments = [(n, b, PALETTE[i % len(PALETTE)]) for i, (n, b) in enumerate(top)]
    if rest / total >= 0.0005:
        segments.append(("Other", rest, OTHER))

    # language bar
    bar_x, bar_y, bar_w, bar_h = 40, 168, 920, 14
    bar, x = [], float(bar_x)
    for _, size, color in segments:
        w = bar_w * size / total
        bar.append(f'<rect x="{x:.2f}" y="{bar_y}" width="{max(w, 0.5):.2f}" height="{bar_h}" fill="{color}"/>')
        x += w

    # legend (two rows of up to four)
    legend = []
    for i, (name, size, color) in enumerate(segments):
        col, row = i % 4, i // 4
        lx, ly = 40 + col * 232, 214 + row * 28
        legend.append(
            f'<circle cx="{lx + 6}" cy="{ly - 5}" r="6" fill="{color}"/>'
            f'<text x="{lx + 20}" y="{ly}" font-family="{SANS}" font-size="15" fill="#E6EDF7">{escape(name)}'
            f'<tspan font-family="{MONO}" font-size="13" fill="#7C8BAE"> {100 * size / total:.1f}%</tspan></text>'
        )

    def metric(x: int, value: str, label: str, color: str) -> str:
        return (
            f'<g transform="translate({x} 64)">'
            f'<rect width="290" height="72" rx="14" fill="#0F1630" stroke="#1E2A50"/>'
            f'<rect x="0" y="18" width="3" height="36" rx="1.5" fill="{color}"/>'
            f'<text x="22" y="44" font-family="{SANS}" font-size="30" font-weight="800" fill="#E6EDF7">{escape(value)}</text>'
            f'<text x="268" y="42" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="#9AA8C7">{escape(label)}</text>'
            f'</g>'
        )

    rows = 1 + (len(segments) - 1) // 4
    height = 214 + rows * 28 + 14
    fp = _fingerprint(data)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-labelledby="t d">
  <!-- fingerprint:{fp} -->
  <title id="t">GitHub activity for {escape(data['user'])}</title>
  <desc id="d">{data['repos']} original public repositories, {data['commits_12mo']} commits in the last 12 months, {data['stars']} stars. Languages by bytes of code: {escape(', '.join(f'{n} {100 * s / total:.1f}%' for n, s, _ in segments))}.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0B1122"/><stop offset="1" stop-color="#080C18"/></linearGradient>
    <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22D3EE" stop-opacity=".6"/><stop offset=".5" stop-color="#1B2547"/><stop offset="1" stop-color="#8B5CF6" stop-opacity=".6"/></linearGradient>
    <clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="7"/></clipPath>
  </defs>
  <rect x="1" y="1" width="998" height="{height - 2}" rx="21" fill="url(#bg)" stroke="url(#rim)" stroke-width="1.6"/>
  <text x="40" y="42" font-family="{MONO}" font-size="13" fill="#22D3EE" letter-spacing="2">ENGINEERING ACTIVITY</text>
  <text x="960" y="42" text-anchor="end" font-family="{MONO}" font-size="12" fill="#5B6888">updated {escape(updated)} · GitHub REST API</text>
  {metric(40, str(data['repos']), 'original repos', '#3B82F6')}
  {metric(355, f"{data['commits_12mo']:,}", 'commits · 12 months', '#22D3EE')}
  {metric(670, str(data['stars']), 'stars', '#8B5CF6')}
  <text x="40" y="156" font-family="{MONO}" font-size="12" fill="#7C8BAE" letter-spacing="1.5">LANGUAGES · BY BYTES OF CODE</text>
  <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="7" fill="#141C38"/>
  <g clip-path="url(#bar)">{''.join(bar)}</g>
  {''.join(legend)}
</svg>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--user", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--data", type=Path, help="render from a saved JSON snapshot")
    ap.add_argument("--dump", type=Path, help="save the snapshot that was rendered")
    args = ap.parse_args()

    if args.data:
        data = json.loads(args.data.read_text())
    else:
        data = collect(args.user, os.environ.get("GITHUB_TOKEN"))
    if args.dump:
        args.dump.write_text(json.dumps(data, indent=2) + "\n")

    # Leave the file untouched when the numbers have not changed, so the
    # scheduled workflow does not create a commit just to bump a date.
    if args.out.exists() and f"fingerprint:{_fingerprint(data)}" in args.out.read_text():
        print(f"{args.out}: unchanged")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(data, dt.date.today().isoformat()))
    print(f"{args.out}: written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
