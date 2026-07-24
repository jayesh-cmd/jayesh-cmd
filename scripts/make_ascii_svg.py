from PIL import Image

RAMP = " .`:-=+*cs#%@"

def make_ascii_svg():
    img = Image.open("source-prepped.png").convert("L").resize((90, 48))
    svg_lines = []
    
    for y in range(img.height):
        line = "".join([RAMP[int((img.getpixel((x, y)) / 255) * (len(RAMP) - 1))] for x in range(img.width)])
        line = line.replace('<', '&lt;').replace('>', '&gt;').replace('&', '&amp;').replace(' ', '&#160;')
        svg_lines.append(f'<tspan x="15" dy="1.15em" style="animation-delay: {y * 0.05:.2f}s;">{line}</tspan>')

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="370" height="370" viewBox="0 0 370 370">
  <style>
    .bg {{ fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1px; }}
    text {{ font-family: 'Fira Code', monospace; font-size: 6px; fill: #58a6ff; white-space: pre; }}
    tspan {{ opacity: 0; animation: type 0.1s ease-out forwards; }}
    @keyframes type {{ to {{ opacity: 1; }} }}
  </style>
  <rect width="370" height="370" class="bg" />
  <text x="15" y="10">{''.join(svg_lines)}</text>
</svg>"""
    with open("jayesh-ascii.svg", "w") as f: f.write(svg)

if __name__ == "__main__":
    make_ascii_svg()
