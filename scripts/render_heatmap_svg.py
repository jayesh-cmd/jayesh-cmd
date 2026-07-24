import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap():
    with open("data/contributions.json") as f: data = json.load(f)
    days = data.get("days", [])
    total_weeks, box_size, gap, padding = 53, 10, 3, 20
    width = padding * 2 + (total_weeks * (box_size + gap))
    height = 140
    rects = []
    
    for idx, day in enumerate(days):
        week, dow = idx // 7, idx % 7
        if week >= total_weeks: break
        x = padding + week * (box_size + gap)
        y = padding + dow * (box_size + gap) + 15
        color = PALETTE[min(day["level"], 5)]
        delay = (week + dow) * 0.012
        rects.append(f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" style="animation-delay: {delay:.3f}s;" class="box" />')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1px; }}
    .text {{ font-family: 'Fira Code', monospace; font-size: 11px; fill: #8b949e; }}
    .box {{ opacity: 0; transform: translateY(-4px); animation: slideIn 0.3s ease-out forwards; }}
    @keyframes slideIn {{ to {{ opacity: 1; transform: translateY(0); }} }}
  </style>
  <rect width="{width}" height="{height}" class="bg" />
  <text x="{padding}" y="25" class="text" font-weight="bold">Contribution Heatmap (Live)</text>
  {''.join(rects)}
</svg>"""
    with open("contrib-heatmap.svg", "w") as f: f.write(svg)

if __name__ == "__main__":
    render_heatmap()
