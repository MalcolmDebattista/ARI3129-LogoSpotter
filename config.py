"""Shared settings for every notebook, so the whole group uses the same dataset version and split."""
import os
from pathlib import Path

# Fill these in once the Roboflow project exists (Roboflow > project > Versions > Export > "show download code").
ROBOFLOW_WORKSPACE = "your-workspace"
ROBOFLOW_PROJECT = "logospotter-gn"
ROBOFLOW_VERSION = 1            # every member must use the same version (same train/valid/test split)

DATA_DIR = Path(__file__).parent / "data"
RESULTS_DIR = Path(__file__).parent / "results"
SEED = 42


def download_dataset(export_format="yolov8"):
    """Downloads the shared dataset version into data/ and returns its folder.

    export_format: "yolov8" for Ultralytics YOLO, "coco" for Faster R-CNN / RetinaNet / RF-DETR, etc.
    The API key is read from the ROBOFLOW_API_KEY environment variable (or Colab Secrets).
    """
    from roboflow import Roboflow

    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if not api_key:
        try:
            from google.colab import userdata  # only available in Colab
            api_key = userdata.get("ROBOFLOW_API_KEY")
        except ImportError:
            pass
    if not api_key:
        raise RuntimeError("Set the ROBOFLOW_API_KEY environment variable (see README.md).")

    target = DATA_DIR / f"{ROBOFLOW_PROJECT}-v{ROBOFLOW_VERSION}-{export_format}"
    if target.exists():
        return target
    project = Roboflow(api_key=api_key).workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)
    dataset = project.version(ROBOFLOW_VERSION).download(export_format, location=str(target))
    return Path(dataset.location)
