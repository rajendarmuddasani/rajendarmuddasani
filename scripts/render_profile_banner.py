"""Render the domain-specific bitmap banner used by the GitHub profile README."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-banner.png"

INK = "#13232d"
WHITE = "#f7f8f6"
TEAL = "#6cb4ad"
MINT = "#d9efe9"
CORAL = "#e56b46"
YELLOW = "#f3c969"
GRID = "#29414b"
BLUE = "#4ea5d9"
VIOLET = "#9b8afb"


def add_tile(axis, x_position: float, y_position: float, title: str, accent: str) -> None:
    axis.add_patch(
        FancyBboxPatch(
            (x_position, y_position),
            1.52,
            1.42,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor="#19323d",
            edgecolor=accent,
            linewidth=1.8,
        )
    )
    axis.add_patch(Rectangle((x_position, y_position), 1.52, 0.34, color=accent))
    axis.text(
        x_position + 0.76,
        y_position + 0.17,
        title,
        color=INK,
        fontsize=8.4,
        fontweight="bold",
        ha="center",
        va="center",
    )


def draw_ml_panel(axis, x_position: float, y_position: float) -> None:
    add_tile(axis, x_position, y_position, "ML", YELLOW)
    clusters = (
        (YELLOW, ((0.31, 0.80), (0.40, 0.91), (0.49, 0.79), (0.42, 1.06))),
        (CORAL, ((0.77, 0.69), (0.87, 0.82), (0.98, 0.72), (0.91, 0.96))),
        (TEAL, ((1.09, 1.09), (1.20, 1.00), (1.29, 1.14), (1.17, 1.23))),
    )
    axis.plot(
        [x_position + 0.18, x_position + 0.18, x_position + 1.36],
        [y_position + 0.48, y_position + 1.25, y_position + 0.48],
        color="#5d7680",
        linewidth=0.8,
    )
    for color, points in clusters:
        for x_offset, y_offset in points:
            axis.add_patch(
                Circle(
                    (x_position + x_offset, y_position + y_offset),
                    0.055,
                    facecolor=color,
                    edgecolor=WHITE,
                    linewidth=0.35,
                )
            )


def draw_dl_panel(axis, x_position: float, y_position: float) -> None:
    add_tile(axis, x_position, y_position, "DL", CORAL)
    highlighted = {(0, 3): YELLOW, (1, 3): YELLOW, (2, 2): CORAL, (3, 1): CORAL, (4, 0): MINT}
    die_size = 0.17
    for row in range(5):
        for column in range(5):
            color = highlighted.get((column, row), "#3a5661")
            axis.add_patch(
                Rectangle(
                    (x_position + 0.24 + column * 0.205, y_position + 0.51 + row * 0.17),
                    die_size,
                    0.135,
                    facecolor=color,
                    edgecolor=INK,
                    linewidth=0.35,
                )
            )
    axis.plot(
        [x_position + 0.22, x_position + 1.28],
        [y_position + 1.25, y_position + 0.52],
        color=WHITE,
        linewidth=1.2,
        alpha=0.8,
    )


def draw_genai_panel(axis, x_position: float, y_position: float) -> None:
    add_tile(axis, x_position, y_position, "GENAI", BLUE)
    axis.add_patch(
        Rectangle(
            (x_position + 0.22, y_position + 0.51),
            0.58,
            0.72,
            facecolor=WHITE,
            edgecolor=BLUE,
            linewidth=1.2,
        )
    )
    for line_y, width, color in (
        (1.08, 0.40, TEAL),
        (0.91, 0.46, GRID),
        (0.75, 0.35, GRID),
        (0.59, 0.43, GRID),
    ):
        axis.plot(
            [x_position + 0.30, x_position + 0.30 + width],
            [y_position + line_y, y_position + line_y],
            color=color,
            linewidth=2,
        )
    axis.add_patch(
        FancyBboxPatch(
            (x_position + 0.88, y_position + 0.70),
            0.42,
            0.36,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=MINT,
            edgecolor=BLUE,
            linewidth=1.1,
        )
    )
    axis.add_patch(
        Polygon(
            [
                (x_position + 0.98, y_position + 0.70),
                (x_position + 0.93, y_position + 0.58),
                (x_position + 1.09, y_position + 0.70),
            ],
            closed=True,
            facecolor=MINT,
            edgecolor=BLUE,
            linewidth=0.8,
        )
    )
    axis.text(
        x_position + 1.09,
        y_position + 0.88,
        "AI",
        color=INK,
        fontsize=8,
        fontweight="bold",
        ha="center",
        va="center",
    )


def draw_agentic_panel(axis, x_position: float, y_position: float) -> None:
    add_tile(axis, x_position, y_position, "AGENTIC AI", VIOLET)
    center = (x_position + 0.77, y_position + 0.87)
    nodes = (
        (x_position + 0.35, y_position + 1.13, YELLOW),
        (x_position + 1.18, y_position + 1.13, BLUE),
        (x_position + 0.35, y_position + 0.58, CORAL),
        (x_position + 1.18, y_position + 0.58, TEAL),
    )
    for node_x, node_y, color in nodes:
        axis.add_patch(
            FancyArrowPatch(
                center,
                (node_x, node_y),
                arrowstyle="-|>",
                mutation_scale=7,
                color=color,
                linewidth=1.1,
            )
        )
        axis.add_patch(Circle((node_x, node_y), 0.105, facecolor=color, edgecolor=WHITE, linewidth=0.6))
    axis.add_patch(Circle(center, 0.18, facecolor=WHITE, edgecolor=VIOLET, linewidth=1.5))
    axis.text(center[0], center[1], "GO", color=INK, fontsize=7.3, fontweight="bold", ha="center", va="center")


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
        "AI/ML Architect for Post-Silicon Engineering",
        color=TEAL,
        fontsize=20,
        fontweight="bold",
        va="center",
    )
    badge_x = 0.75
    for label, width, color in (
        ("ML", 0.72, YELLOW),
        ("DL", 0.72, CORAL),
        ("GENAI", 1.08, BLUE),
        ("AGENTIC AI", 1.55, VIOLET),
    ):
        axis.add_patch(Rectangle((badge_x, 1.38), width, 0.46, facecolor=color, edgecolor="none"))
        axis.text(
            badge_x + width / 2,
            1.61,
            label,
            color=INK,
            fontsize=9.2,
            fontweight="bold",
            ha="center",
            va="center",
        )
        badge_x += width + 0.12
    axis.text(
        0.75,
        0.82,
        "Senior Staff Engineer  |  AI/ML Lead  |  16+ years in semiconductor test engineering",
        color=WHITE,
        fontsize=11,
        va="center",
    )

    system_center = (13.53, 2.40)
    axis.add_patch(Circle(system_center, 2.16, facecolor="#172e38", edgecolor=TEAL, linewidth=2.6))
    axis.text(
        system_center[0],
        4.18,
        "POST-SILICON AI SYSTEMS",
        color=MINT,
        fontsize=8.8,
        fontweight="bold",
        ha="center",
        va="center",
    )
    draw_ml_panel(axis, 11.93, 2.43)
    draw_dl_panel(axis, 13.62, 2.43)
    draw_genai_panel(axis, 11.93, 0.83)
    draw_agentic_panel(axis, 13.62, 0.83)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(OUTPUT, dpi=160, bbox_inches="tight", pad_inches=0, facecolor=INK)
    plt.close(figure)
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    render_banner()
