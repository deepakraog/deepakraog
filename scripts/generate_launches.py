#!/usr/bin/env python3
"""Generate assets/launches.svg: animated space-shuttle launch history.

One flight lane per year (2017..current year). Each lane shows a shuttle
whose speed, size and contrail encode that year's GitHub contributions.
Fetches real counts from the GitHub GraphQL API using GITHUB_TOKEN.

Output is pure ASCII; special glyphs are written as XML numeric entities.
Uses only the Python standard library.
"""

import datetime
import json
import os
import random
import sys
import urllib.request

LOGIN = "deepakraog"
FIRST_YEAR = 2017
WIDTH = 1000
LANE_H = 46
TOP = 78
BOTTOM_PAD = 22

CYAN = "#5fd7ff"
PURPLE = "#9d6bff"
PINK = "#ff6ec7"
MUTED = "#7c8db0"
LANE_LINE = "#3d5a80"

LANE_X0 = 340   # left edge of flight lane (clear of the labels)
LANE_X1 = 985   # right edge of flight lane


def fetch_counts(token):
    """Return {year: total_contributions} for FIRST_YEAR..current year."""
    now = datetime.datetime.now(datetime.timezone.utc)
    counts = {}
    for year in range(FIRST_YEAR, now.year + 1):
        start = "%d-01-01T00:00:00Z" % year
        if year == now.year:
            end = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            end = "%d-12-31T23:59:59Z" % year
        query = (
            'query { user(login: "%s") { contributionsCollection('
            'from: "%s", to: "%s") { contributionCalendar '
            '{ totalContributions } } } }' % (LOGIN, start, end)
        )
        payload = json.dumps({"query": query}).encode("ascii")
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=payload,
            headers={
                "Authorization": "bearer " + token,
                "Content-Type": "application/json",
                "User-Agent": LOGIN,
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        counts[year] = data["data"]["user"]["contributionsCollection"][
            "contributionCalendar"]["totalContributions"]
    return counts


def stars(width, height, n=46):
    rng = random.Random(2017)
    parts = []
    for _ in range(n):
        cx = round(rng.uniform(8, width - 8), 1)
        cy = round(rng.uniform(8, height - 8), 1)
        r = round(rng.uniform(0.6, 1.5), 1)
        dur = round(rng.uniform(2.0, 4.8), 1)
        lo = round(rng.uniform(0.1, 0.5), 2)
        parts.append(
            '    <circle cx="%s" cy="%s" r="%s">'
            '<animate attributeName="opacity" values="%s;1;%s" dur="%ss" '
            'repeatCount="indefinite"/></circle>' % (cx, cy, r, lo, lo, dur)
        )
    return "\n".join(parts)


def shuttle(scale, flame_len):
    """A small right-facing shuttle with animated exhaust flame."""
    return (
        '<g transform="scale(%.2f)">'
        '<path d="M-14,0 L -20,0" stroke="#ffb45c" stroke-width="3.4" '
        'stroke-linecap="round" opacity="0.85">'
        '<animate attributeName="opacity" values="0.9;0.25;0.9" dur="0.4s" '
        'repeatCount="indefinite"/>'
        '<animate attributeName="stroke-width" values="3.4;2.2;3.4" dur="0.4s" '
        'repeatCount="indefinite"/></path>'
        '<path d="M-13,0 L %d,0" stroke="%s" stroke-width="1.6" '
        'stroke-linecap="round" opacity="0.5">'
        '<animate attributeName="opacity" values="0.55;0.15;0.55" dur="0.6s" '
        'repeatCount="indefinite"/></path>'
        '<path d="M-1,-3 L -9,-9 L -4,-2 Z" fill="%s"/>'
        '<path d="M-1,3 L -9,9 L -4,2 Z" fill="%s"/>'
        '<path d="M-13,0 Q 2,-8 20,0 Q 2,8 -13,0 Z" fill="#dfe7f1"/>'
        '<path d="M13,-3 L 20,0 L 13,3 Z" fill="#8fd3ff"/>'
        '<circle cx="5" cy="0" r="2.4" fill="#22384f"/>'
        '<circle cx="5" cy="0" r="1" fill="%s" opacity="0.9"/>'
        '</g>' % (scale, -13 - flame_len, PINK, PURPLE, PURPLE, CYAN)
    )


def render(counts):
    years = sorted(counts)
    max_count = max(max(counts.values()), 1)
    height = TOP + LANE_H * len(years) + BOTTOM_PAD

    lanes = []
    for i, year in enumerate(years):
        count = counts[year]
        frac = count / max_count
        cy = TOP + i * LANE_H + LANE_H // 2

        # data encoding: faster, bigger shuttle + longer contrail = more work
        dur = round(14.0 - 10.0 * frac, 1)          # 4s (max) .. 14s (zero)
        scale = round(0.8 + 0.55 * frac, 2)
        flame_len = int(8 + 30 * frac)
        trail_w = int((LANE_X1 - LANE_X0 - 20) * frac)
        begin = round(-(i * 1.7) % dur, 1)

        lane = []
        lane.append(
            '  <text x="18" y="%d" font-family="\'Courier New\', monospace" '
            'font-size="13" letter-spacing="1">'
            '<tspan fill="%s" font-weight="bold">%d</tspan>'
            '<tspan fill="%s"> &#9656; </tspan>'
            '<tspan fill="#c9d1d9">%s %s</tspan></text>'
            % (cy + 4, CYAN, year, MUTED, format(count, ","),
               "contribution" if count == 1 else "contributions")
        )
        lane.append(
            '  <line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" '
            'stroke-width="1" stroke-dasharray="3 7" opacity="0.35"/>'
            % (LANE_X0, cy, LANE_X1, cy, LANE_LINE)
        )
        if trail_w > 0:
            lane.append(
                '  <rect x="%d" y="%d" width="%d" height="3" rx="1.5" '
                'fill="url(#trailGrad)" opacity="0.45">'
                '<animate attributeName="opacity" values="0.3;0.55;0.3" '
                'dur="3s" repeatCount="indefinite"/></rect>'
                % (LANE_X0, cy - 1, trail_w)
            )
        lane.append(
            '  <g><animateTransform attributeName="transform" '
            'type="translate" values="%d,%d; %d,%d" dur="%ss" begin="-%ss" '
            'repeatCount="indefinite"/>%s</g>'
            % (LANE_X0 - 30, cy, LANE_X1 + 45, cy, dur, begin,
               shuttle(scale, flame_len))
        )
        lanes.append("\n".join(lane))

    svg = []
    svg.append(
        '<svg width="%d" height="%d" viewBox="0 0 %d %d" fill="none" '
        'xmlns="http://www.w3.org/2000/svg">' % (WIDTH, height, WIDTH, height)
    )
    svg.append(
        '  <defs>\n'
        '    <linearGradient id="space" x1="0" y1="0" x2="0" y2="1">\n'
        '      <stop offset="0%" stop-color="#03040c"/>\n'
        '      <stop offset="45%" stop-color="#0a1128"/>\n'
        '      <stop offset="100%" stop-color="#1b1035"/>\n'
        '    </linearGradient>\n'
        '    <radialGradient id="nebulaA" cx="0.15" cy="0.2" r="0.6">\n'
        '      <stop offset="0%" stop-color="#7b2ff7" stop-opacity="0.22"/>\n'
        '      <stop offset="100%" stop-color="#7b2ff7" stop-opacity="0"/>\n'
        '    </radialGradient>\n'
        '    <radialGradient id="nebulaB" cx="0.9" cy="0.85" r="0.55">\n'
        '      <stop offset="0%" stop-color="#00d4ff" stop-opacity="0.16"/>\n'
        '      <stop offset="100%" stop-color="#00d4ff" stop-opacity="0"/>\n'
        '    </radialGradient>\n'
        '    <linearGradient id="trailGrad" x1="0" y1="0" x2="1" y2="0">\n'
        '      <stop offset="0%" stop-color="' + CYAN + '"/>\n'
        '      <stop offset="50%" stop-color="' + PURPLE + '"/>\n'
        '      <stop offset="100%" stop-color="' + PINK + '"/>\n'
        '    </linearGradient>\n'
        '    <filter id="softGlow" x="-50%" y="-50%" width="200%" '
        'height="200%">\n'
        '      <feGaussianBlur stdDeviation="6" result="blur"/>\n'
        '      <feMerge><feMergeNode in="blur"/>'
        '<feMergeNode in="SourceGraphic"/></feMerge>\n'
        '    </filter>\n'
        '  </defs>'
    )
    svg.append('  <rect width="%d" height="%d" fill="url(#space)"/>'
               % (WIDTH, height))
    svg.append('  <rect width="%d" height="%d" fill="url(#nebulaA)"/>'
               % (WIDTH, height))
    svg.append('  <rect width="%d" height="%d" fill="url(#nebulaB)"/>'
               % (WIDTH, height))
    svg.append('  <g fill="#ffffff">\n%s\n  </g>' % stars(WIDTH, height))
    svg.append(
        '  <text x="%d" y="42" text-anchor="middle" '
        'font-family="\'Courier New\', monospace" font-size="17" '
        'letter-spacing="5" fill="#8fd3ff" opacity="0.95" '
        'filter="url(#softGlow)">LAUNCH HISTORY &#183; CONTRIBUTIONS PER '
        'YEAR</text>' % (WIDTH // 2)
    )
    svg.append(
        '  <text x="%d" y="62" text-anchor="middle" '
        'font-family="\'Courier New\', monospace" font-size="11" '
        'letter-spacing="2" fill="%s">&gt; one shuttle per year &#183; '
        'speed, size &amp; contrail scale with payload_</text>'
        % (WIDTH // 2, MUTED)
    )
    svg.extend(lanes)
    svg.append(
        '  <rect x="0" y="%d" width="%d" height="3" fill="url(#trailGrad)" '
        'opacity="0.75"><animate attributeName="opacity" '
        'values="0.4;0.95;0.4" dur="4s" repeatCount="indefinite"/></rect>'
        % (height - 3, WIDTH)
    )
    svg.append('</svg>')
    return "\n".join(svg) + "\n"


def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("error: set GITHUB_TOKEN (or GH_TOKEN) to query the "
                 "GitHub GraphQL API")
    counts = fetch_counts(token)
    for year in sorted(counts):
        print("%d: %d" % (year, counts[year]))
    out = render(counts)
    out.encode("ascii")  # hard guarantee: pure ASCII or we fail loudly
    out_path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "assets", "launches.svg")
    with open(out_path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(out)
    print("wrote %s (%d bytes)" % (out_path, len(out)))


if __name__ == "__main__":
    main()
