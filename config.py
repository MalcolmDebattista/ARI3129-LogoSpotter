"""Shared settings for every notebook, so the whole group uses the same dataset version and split."""
import os
from pathlib import Path

# Fill these in once the Roboflow project exists (Roboflow > project > Versions > Export > "show download code").
ROBOFLOW_WORKSPACE = "your-workspace"
ROBOFLOW_PROJECT = "logospotter-gn"
ROBOFLOW_VERSION = 1            # every member must use the same version (same train/valid/test split)
# Version used for EDA statistics. Creating a second version with the same split but no augmentation
# gives exact statistics on the original frames; otherwise leave it equal to ROBOFLOW_VERSION.
ROBOFLOW_EDA_VERSION = ROBOFLOW_VERSION

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = ROOT / "figures"
METADATA_CSV = Path(os.environ.get("LOGOSPOTTER_METADATA", ROOT / "metadata" / "frame_metadata.csv"))
SEED = 42


def _api_key():
    api_key = os.environ.get("ROBOFLOW_API_KEY")
    if not api_key:
        try:
            from google.colab import userdata  # only available in Colab
            api_key = userdata.get("ROBOFLOW_API_KEY")
        except ImportError:
            pass
    if not api_key:
        raise RuntimeError("Set the ROBOFLOW_API_KEY environment variable (see README.md).")
    return api_key


def download_dataset(export_format="yolov8", version=None):
    """Downloads the shared dataset version into data/ and returns its folder.

    export_format: "yolov8" for Ultralytics YOLO, "coco" for Faster R-CNN / RetinaNet / RF-DETR and the EDA.
    If the LOGOSPOTTER_DATASET environment variable points to an already-extracted export, that folder
    is used instead (it must be in the requested format).
    """
    local = os.environ.get("LOGOSPOTTER_DATASET")
    if local:
        return Path(local)

    version = version or ROBOFLOW_VERSION
    target = DATA_DIR / f"{ROBOFLOW_PROJECT}-v{version}-{export_format}"
    if target.exists():
        return target
    from roboflow import Roboflow

    project = Roboflow(api_key=_api_key()).workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)
    dataset = project.version(version).download(export_format, location=str(target))
    return Path(dataset.location)
