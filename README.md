# LogoSpotter-G[N]: Automated Logo Detection in Television News Broadcasts

ARI3129 Advanced Computer Vision for AI, group project 2026/27, University of Malta.

This project detects logos that physically appear in television news footage (on signs, billboards, products, clothing, vehicles and microphones). Digitally overlaid graphics, such as channel watermarks, tickers and on-screen headlines, are excluded. The detectors are class-agnostic: they find logos without identifying the brand.

## Team

| Member | Object detector | Notebook |
|---|---|---|
| Malcolm Debattista | _TBD_ | `2_[Model]_DebattistaMalcolm.ipynb` |
| _TBD_ | _TBD_ | |
| _TBD_ | _TBD_ | |
| _TBD_ | _TBD_ | |

## Dataset

- **Roboflow project (public):** _link to be added_
- **Name:** LogoSpotter-G[N]
- **Class:** `Logo` (single class, bounding boxes)
- **Source:** frames from local and international news recordings in the News Graphics Dataset (NGD), with `frame_metadata.csv` giving each frame's video source, timestamp, broadcaster and region.
- **Splits:** train / validation / test, shared by all members. Augmentation is applied to the training set only.

All boxes were drawn manually in Roboflow, without AI-assisted or automatic annotation.

## Repository structure

```
.
├── README.md
├── requirements.txt
├── config.py                            # shared Roboflow version, paths and seed
├── 1_EDA.ipynb                          # Task 1: exploratory data analysis
├── 2_ObjectDetector_template.ipynb      # Task 2: copy and rename per student
├── 2_[Model]_[StudentName].ipynb        # Task 2: one notebook per student
├── 3_results_comparison.ipynb           # Task 2: comparison of all detectors
├── results/                             # metrics exported by each detector notebook (JSON)
└── data/                                # dataset downloaded from Roboflow (not committed)
```

## Setup

1. Install Python 3.10 or newer, then the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set your Roboflow API key as an environment variable, so it is never written into a notebook:

   ```bash
   export ROBOFLOW_API_KEY=your_key_here        # macOS / Linux / Git Bash
   setx ROBOFLOW_API_KEY your_key_here          # Windows (then reopen the terminal)
   ```

   In Google Colab, add it under **Secrets** (key icon) with the name `ROBOFLOW_API_KEY`.

3. Fill in the Roboflow workspace, project and version in `config.py` (once, for the whole group).
4. Run the notebooks in order. Each notebook downloads the same dataset version from Roboflow into `data/`.

Training is much faster on a GPU. Google Colab with a **T4 GPU** runtime is recommended (Runtime > Change runtime type).

## Reproducing the results

1. `1_EDA.ipynb`: dataset statistics and visualisations.
2. `2_[Model]_[StudentName].ipynb`: trains one detector, evaluates it on the shared test set and writes `results/<model>_metrics.json`.
3. `3_results_comparison.ipynb`: reads every file in `results/` and compares the detectors.

Pretrained weights, training settings and input resolution for each detector are documented in its notebook.

## Acknowledgements

- A. F. Lucas and D. Seychell, "A Hybrid Deterministic Framework for Named Entity Extraction in Broadcast News Video," in *2026 IEEE Conference on Artificial Intelligence (CAI)*, IEEE, 2026, pp. 1134–1139. Dataset: <https://universe.roboflow.com/ict3909-fyp/news-graphic-dataset>
- [Ultralytics](https://github.com/ultralytics/ultralytics), [Roboflow](https://roboflow.com), [PyTorch](https://pytorch.org)
