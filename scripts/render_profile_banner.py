"""Render the bitmap assets used by the GitHub profile README."""

from __future__ import annotations

from pathlib import Path

from render_architecture_method import render_architecture
from render_profile_banner_options import render_option_a

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-banner.png"


def render_banner() -> None:
    render_option_a(OUTPUT)
    architecture_output = render_architecture()
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {architecture_output.relative_to(ROOT)}")


if __name__ == "__main__":
    render_banner()
