from __future__ import annotations

import os
from pathlib import Path
import shutil


def copy_images_from_overrides(project_dir):
    """Copy images from overrides/assets/images to assets/images path expected by links."""
    source_dir = project_dir / "overrides/assets/images"
    target_dir = project_dir / "assets/images"

    if not source_dir.exists():
        return

    target_dir.mkdir(parents=True, exist_ok=True)

    for asset in source_dir.glob("*"):
        if asset.is_file():
            shutil.copy2(asset, target_dir / asset.name)


def on_pre_build(config, **kwargs):
    """Pre-build hook for Spanish version of the documentation."""
    base_dir = Path(config.config_file_path).parent.parent.parent

    project_dirs = (
        base_dir / "docs/.temp-es/paricia",
        base_dir / "docs/.temp-es/riverlabs",
    )

    for project_dir in project_dirs:
        copy_images_from_overrides(project_dir)
