"""Render two profile-banner previews from real selected-project artifacts."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

PROFILE_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PROFILE_ROOT.parents[1]
OUTPUT_DIR = PROFILE_ROOT / "assets" / "previews"

WIDTH = 1600
HEIGHT = 480

INK = "#13232d"
WHITE = "#f7f8f6"
TEAL = "#6cb4ad"
MINT = "#d9efe9"
CORAL = "#e56b46"
YELLOW = "#f3c969"
BLUE = "#4ea5d9"
VIOLET = "#9b8afb"
GRID = "#29414b"

ARTIFACTS = {
    "ml_a": WORKSPACE_ROOT
    / "repos/02_NLP_Root_Cause_Predictor/docs/assets/v2_policy_evidence.png",
    "ml_b": WORKSPACE_ROOT
    / "repos/05_Chip_Level_Test_Time_Optimizer/docs/assets/candidate_tradeoff.png",
    "dl": WORKSPACE_ROOT
    / "repos/04_Transfer_Learning_ResNet_STDF_Wafer_Map_Yield_Predictor/docs/assets/confirmation_samples.png",
    "genai": WORKSPACE_ROOT
    / "repos/10_GraphDB_GenAI_MCP_Test_Program_Development/assets/mcp-generation-workflow.png",
    "agentic_a": WORKSPACE_ROOT
    / "repos/07_AARCAR-Multi-Agent-RCA-Platform/docs/images/neo4j_graph_visualization.jpeg",
    "agentic_b": WORKSPACE_ROOT
    / "repos/08_LangGraph-Multi-Agent-Test-Failure-RCA-Platform/evidence/assets/candidate_comparison.png",
}

LANES = (
    ("MACHINE LEARNING", YELLOW),
    ("DEEP LEARNING", CORAL),
    ("GENERATIVE AI", BLUE),
    ("AGENTIC AI", VIOLET),
)


def font(size: int, *, serif: bool = False, bold: bool = False) -> ImageFont.FreeTypeFont:
    family = "georgiab.ttf" if serif and bold else "georgia.ttf" if serif else "seguisb.ttf" if bold else "segoeui.ttf"
    windows_font = Path("C:/Windows/Fonts") / family
    if windows_font.exists():
        return ImageFont.truetype(str(windows_font), size=size)
    return ImageFont.load_default(size=size)


def base_canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), INK)
    draw = ImageDraw.Draw(canvas)
    for x_position in range(0, WIDTH, 100):
        draw.line((x_position, 0, x_position, HEIGHT), fill=GRID, width=1)
    for y_position in range(80, HEIGHT, 80):
        draw.line((0, y_position, WIDTH, y_position), fill=GRID, width=1)
    draw.rectangle((0, 0, 16, HEIGHT), fill=YELLOW)
    return canvas, draw


def fitted_artifact(path: Path, size: tuple[int, int]) -> Image.Image:
    with Image.open(path) as source:
        return ImageOps.fit(source.convert("RGB"), size, method=Image.Resampling.LANCZOS)


def add_artifact_card(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    *,
    box: tuple[int, int, int, int],
    path: Path,
    lane: str,
    project: str,
    accent: str,
) -> None:
    left, top, right, bottom = box
    label_height = 34
    image = fitted_artifact(path, (right - left, bottom - top - label_height))
    canvas.paste(image, (left, top + label_height))
    draw.rectangle((left, top, right, top + label_height), fill=accent)
    draw.text((left + 12, top + 5), lane, fill=INK, font=font(16, bold=True))
    project_width = draw.textlength(project, font=font(13, bold=True))
    draw.rounded_rectangle(
        (right - project_width - 24, bottom - 28, right - 7, bottom - 7),
        radius=4,
        fill=INK,
    )
    draw.text(
        (right - project_width - 16, bottom - 27),
        project,
        fill=WHITE,
        font=font(13, bold=True),
    )
    draw.rectangle(box, outline=accent, width=3)


def add_identity(draw: ImageDraw.ImageDraw, *, compact: bool = False) -> None:
    if compact:
        draw.text((62, 30), "Rajendar Muddasani", fill=WHITE, font=font(50, serif=True, bold=True))
        draw.text(
            (64, 105),
            "Post-Silicon Validation AI/ML Architect",
            fill=TEAL,
            font=font(27, bold=True),
        )
        draw.text(
            (1095, 49),
            "Senior Staff Engineer  |  AI/ML Lead  |  16+ years",
            fill=WHITE,
            font=font(18),
        )
        return

    draw.text((70, 82), "Rajendar Muddasani", fill=WHITE, font=font(57, serif=True, bold=True))
    draw.text(
        (72, 174),
        "Post-Silicon Validation AI/ML Architect",
        fill=TEAL,
        font=font(29, bold=True),
    )
    draw.text(
        (72, 393),
        "Senior Staff Engineer  |  AI/ML Lead  |  16+ years in semiconductor test engineering",
        fill=WHITE,
        font=font(18),
    )


def render_option_a(output: Path | None = None) -> Path:
    canvas, draw = base_canvas()
    add_identity(draw)

    ribbon_left = 70
    ribbon_top = 272
    ribbon_width = 205
    ribbon_gap = 8
    for index, (label, accent) in enumerate(LANES):
        left = ribbon_left + index * (ribbon_width + ribbon_gap)
        draw.rectangle((left, ribbon_top, left + ribbon_width, ribbon_top + 50), fill=accent)
        text_width = draw.textlength(label, font=font(15, bold=True))
        draw.text(
            (left + (ribbon_width - text_width) / 2, ribbon_top + 14),
            label,
            fill=INK,
            font=font(15, bold=True),
        )

    cards = (
        ((955, 35, 1260, 226), ARTIFACTS["ml_a"], "ML", "NLP RCA", YELLOW),
        ((1274, 35, 1579, 226), ARTIFACTS["dl"], "DL", "RESNET WAFER", CORAL),
        ((955, 242, 1260, 445), ARTIFACTS["genai"], "GENAI", "GRAPH MCP", BLUE),
        ((1274, 242, 1579, 445), ARTIFACTS["agentic_a"], "AGENTIC AI", "AARCAR", VIOLET),
    )
    for box, path, lane, project, accent in cards:
        add_artifact_card(
            canvas,
            draw,
            box=box,
            path=path,
            lane=lane,
            project=project,
            accent=accent,
        )

    output = output or OUTPUT_DIR / "profile-banner-option-a.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, optimize=True)
    return output


def render_option_b() -> Path:
    canvas, draw = base_canvas()
    add_identity(draw, compact=True)

    card_top = 174
    card_bottom = 454
    card_width = 374
    card_gap = 12
    card_left = 40
    cards = (
        (ARTIFACTS["ml_b"], "MACHINE LEARNING", "CHIP OPTIMIZER", YELLOW),
        (ARTIFACTS["dl"], "DEEP LEARNING", "RESNET WAFER", CORAL),
        (ARTIFACTS["genai"], "GENERATIVE AI", "GRAPH MCP", BLUE),
        (ARTIFACTS["agentic_b"], "AGENTIC AI", "LANGGRAPH RCA", VIOLET),
    )
    for index, (path, lane, project, accent) in enumerate(cards):
        left = card_left + index * (card_width + card_gap)
        add_artifact_card(
            canvas,
            draw,
            box=(left, card_top, left + card_width, card_bottom),
            path=path,
            lane=lane,
            project=project,
            accent=accent,
        )

    output = OUTPUT_DIR / "profile-banner-option-b.png"
    canvas.save(output, optimize=True)
    return output


def render_lane_strip(output: Path) -> Path:
    canvas = Image.new("RGB", (1200, 88), INK)
    draw = ImageDraw.Draw(canvas)
    gap = 8
    cell_width = (canvas.width - gap * 3) // 4
    lane_counts = (
        ("MACHINE LEARNING", "3 SELECTED SYSTEMS", YELLOW),
        ("DEEP LEARNING", "1 SELECTED SYSTEM", CORAL),
        ("GENERATIVE AI", "1 SELECTED SYSTEM", BLUE),
        ("AGENTIC AI", "2 SELECTED SYSTEMS", VIOLET),
    )
    for index, (lane, count, accent) in enumerate(lane_counts):
        left = index * (cell_width + gap)
        right = canvas.width if index == 3 else left + cell_width
        draw.rectangle((left, 0, right, canvas.height), fill=accent)
        lane_width = draw.textlength(lane, font=font(20, bold=True))
        count_width = draw.textlength(count, font=font(14, bold=True))
        draw.text(
            (left + (right - left - lane_width) / 2, 17),
            lane,
            fill=INK,
            font=font(20, bold=True),
        )
        draw.text(
            (left + (right - left - count_width) / 2, 51),
            count,
            fill=INK,
            font=font(14, bold=True),
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, optimize=True)
    return output


def main() -> None:
    missing = [str(path) for path in ARTIFACTS.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing project artifacts: {missing}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for output in (render_option_a(), render_option_b()):
        print(f"Wrote {output.relative_to(PROFILE_ROOT)}")


if __name__ == "__main__":
    main()