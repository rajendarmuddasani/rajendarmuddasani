"""Render the readable architecture workflow used by the profile README."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw
from render_profile_banner_options import GRID, INK, WHITE, font

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "architecture-method.png"

WIDTH = 1200
HEIGHT = 650

YELLOW = "#f3c969"
MINT = "#d9efe9"
CORAL = "#e56b46"
VIOLET = "#9b8afb"
BLUE = "#4ea5d9"
TEAL = "#6cb4ad"


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    *,
    color: str = WHITE,
) -> None:
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    distance = math.hypot(delta_x, delta_y)
    unit_x = delta_x / distance
    unit_y = delta_y / distance
    head_length = 18
    wing = 9
    base_x = end[0] - unit_x * head_length
    base_y = end[1] - unit_y * head_length
    draw.line((start, (base_x, base_y)), fill=color, width=6)
    draw.polygon(
        (
            end,
            (base_x - unit_y * wing, base_y + unit_x * wing),
            (base_x + unit_y * wing, base_y - unit_x * wing),
        ),
        fill=color,
    )


def centered_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    heading: str,
    body: str,
    *,
    fill: str,
) -> None:
    left, top, right, _bottom = box
    center_x = (left + right) // 2
    draw.rounded_rectangle(box, radius=12, fill=fill, outline=WHITE, width=2)
    heading_size = 25
    heading_font = font(heading_size, bold=True)
    while draw.textlength(heading, font=heading_font) > right - left - 30:
        heading_size -= 1
        heading_font = font(heading_size, bold=True)
    body_font = font(18)
    heading_box = draw.textbbox((0, 0), heading, font=heading_font)
    draw.text(
        (center_x - (heading_box[2] - heading_box[0]) / 2, top + 34),
        heading,
        fill=INK,
        font=heading_font,
    )
    body_box = draw.multiline_textbbox((0, 0), body, font=body_font, spacing=8, align="center")
    body_width = body_box[2] - body_box[0]
    body_height = body_box[3] - body_box[1]
    draw.multiline_text(
        (center_x - body_width / 2, top + 103 - body_height / 2),
        body,
        fill=INK,
        font=body_font,
        spacing=8,
        align="center",
    )


def render_architecture(output: Path = OUTPUT) -> Path:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), INK)
    draw = ImageDraw.Draw(canvas)
    for x_position in range(0, WIDTH, 100):
        draw.line((x_position, 0, x_position, HEIGHT), fill=GRID, width=1)
    for y_position in range(0, HEIGHT, 100):
        draw.line((0, y_position, WIDTH, y_position), fill=GRID, width=1)

    boxes = (
        ((45, 55, 355, 235), "3. Model & agent orchestration", "Predictive ML  .  DL  .  RAG\nMCP tools  .  agent workflows", CORAL),
        ((445, 55, 755, 235), "2. Data & provenance", "STDF  .  logs  .  specifications\nContext  .  lineage  .  evidence", MINT),
        ((845, 55, 1155, 235), "1. Post-silicon problem", "Failure analysis  .  yield\nTest time  .  silicon quality", YELLOW),
        ((45, 345, 355, 525), "4. Evaluation & safety gates", "Accuracy  .  grounding  .  citations\nUncertainty  .  confidence gates", VIOLET),
        ((445, 345, 755, 525), "5. APIs & engineering workflow", "FastAPI  .  CI/CD  .  dashboards\nReview queues  .  traceability", BLUE),
        ((845, 345, 1155, 525), "6. Engineer review & decision", "Approve  .  investigate  .  act\nFeedback  .  monitoring", TEAL),
    )
    for box, heading, body, fill in boxes:
        centered_text(draw, box, heading, body, fill=fill)

    draw_arrow(draw, (845, 145), (755, 145))
    draw_arrow(draw, (445, 145), (355, 145))
    draw_arrow(draw, (200, 235), (200, 345))
    draw_arrow(draw, (355, 435), (445, 435))
    draw_arrow(draw, (755, 435), (845, 435))

    draw.rounded_rectangle((190, 567, 1010, 622), radius=10, fill="#1d3540", outline=TEAL, width=2)
    feedback = "Continuous feedback updates evidence, thresholds, retrieval, and models"
    feedback_font = font(20, bold=True)
    feedback_width = draw.textlength(feedback, font=feedback_font)
    draw.text(((WIDTH - feedback_width) / 2, 582), feedback, fill=WHITE, font=feedback_font)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, optimize=True)
    return output


if __name__ == "__main__":
    result = render_architecture()
    print(f"Wrote {result.relative_to(ROOT)}")