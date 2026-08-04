"""Render the domain-specific bitmap banner used by the GitHub profile README."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-banner.png"

INK = "#13232d"
WHITE = "#f7f8f6"
TEAL = "#6cb4ad"
MINT = "#d9efe9"
CORAL = "#e56b46"
YELLOW = "#f3c969"
GRID = "#29414b"


def render_banner() -> None:
    figure, axis = plt.subplots(figsize=(16, 4.8), facecolor=INK)
    axis.set_facecolor(INK)
    axis.set_xlim(0, 16)
    axis.set_ylim(0, 4.8)
    axis.axis("off")

    for x_position in range(0, 17):
        axis.plot([x_position, x_position], [0, 4.8], color=GRID, linewidth=0.35, alpha=0.5)
    for y_position in [0.8, 1.6, 2.4, 3.2, 4.0]:
        axis.plot([0, 16], [y_position, y_position], color=GRID, linewidth=0.35, alpha=0.5)

    axis.add_patch(Rectangle((0, 0), 0.16, 4.8, color=YELLOW))
    axis.text(
        0.72,
        3.35,
        "Rajendar Muddasani",
        color=WHITE,
        fontsize=36,
        fontweight="bold",
        family="DejaVu Serif",
        va="center",
    )
    axis.text(
        0.75,
        2.45,
        "AI/ML Architecture for Post-Silicon Engineering",
        color=TEAL,
        fontsize=20,
        fontweight="bold",
        va="center",
    )
    axis.text(
        0.75,
        1.62,
        "SEMICONDUCTOR TEST   |   MLOPS   |   AGENTIC AI   |   EVIDENCE-DRIVEN SYSTEMS",
        color=MINT,
        fontsize=10.5,
        va="center",
    )
    axis.text(
        0.75,
        0.82,
        "Senior Staff Engineer  |  AI/ML Lead  |  16+ years in semiconductor engineering",
        color=WHITE,
        fontsize=11,
        va="center",
    )

    wafer_center = (13.45, 2.45)
    wafer_radius = 1.78
    wafer = Circle(wafer_center, wafer_radius, facecolor="#1c333d", edgecolor=TEAL, linewidth=3)
    axis.add_patch(wafer)

    die_size = 0.34
    palette = [MINT, TEAL, YELLOW, CORAL]
    highlighted = {(1, 1): 2, (4, 2): 3, (2, 5): 1, (5, 4): 2, (3, 3): 0}
    for row in range(7):
        for column in range(7):
            die_x = wafer_center[0] - 1.19 + column * die_size
            die_y = wafer_center[1] - 1.19 + row * die_size
            corners = [
                (die_x, die_y),
                (die_x + die_size * 0.82, die_y),
                (die_x, die_y + die_size * 0.82),
                (die_x + die_size * 0.82, die_y + die_size * 0.82),
            ]
            if all(
                (corner_x - wafer_center[0]) ** 2 + (corner_y - wafer_center[1]) ** 2
                <= (wafer_radius - 0.08) ** 2
                for corner_x, corner_y in corners
            ):
                color = palette[highlighted[(column, row)]] if (column, row) in highlighted else "#35515b"
                axis.add_patch(
                    Rectangle(
                        (die_x, die_y),
                        die_size * 0.82,
                        die_size * 0.82,
                        facecolor=color,
                        edgecolor=INK,
                        linewidth=0.5,
                    )
                )

    axis.plot(
        [wafer_center[0] - 0.18, wafer_center[0] + 0.18],
        [wafer_center[1] - wafer_radius, wafer_center[1] - wafer_radius],
        color=INK,
        linewidth=5,
        solid_capstyle="round",
    )
    for x_position, y_position, color in [
        (11.4, 3.85, YELLOW),
        (15.32, 3.58, CORAL),
        (15.48, 1.25, TEAL),
        (11.55, 0.98, MINT),
    ]:
        axis.plot(
            [x_position, wafer_center[0]],
            [y_position, wafer_center[1]],
            color=color,
            linewidth=1.2,
            alpha=0.75,
        )
        axis.add_patch(Circle((x_position, y_position), 0.07, color=color))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=160, bbox_inches="tight", pad_inches=0, facecolor=INK)
    plt.close(figure)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    render_banner()
