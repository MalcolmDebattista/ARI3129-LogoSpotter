# Work Plan: LogoSpotter-G[N] (3 members)

Deadline: **Monday 11 January 2027**. Equal contribution is assumed, so every member annotates, trains one detector and writes their own report and journal sections.

| | Member |
|---|---|
| **M1** | Malcolm Debattista |
| **M2** | _Member 2_ |
| **M3** | _Member 3_ |

## Dependency chain

```
Phase 0  M1: set up Roboflow + repo ──┐
Phase 1  M1, M2, M3: annotate 300 each ─┤  (in parallel)
Phase 2  M1: dataset version + EDA ─────┤  ← unblocks everyone
Phase 3  M1, M2, M3: one detector each ─┤  (in parallel, same test set)
Phase 4  M3: comparison · M2: report assembly · everyone: own sections + journal
```

M1 sits at the start of the chain, so nobody waits on anyone except for M1's dataset version (Phase 2) and the three metric files (Phase 3 → 4).

## Phase 0: Setup (M1, now)

- [ ] Submit the Group Registration Form on the VLE and note the group number **N**.
- [ ] Create the Roboflow project **LogoSpotter-G[N]** (Object Detection, single class `Logo`) and invite M2 and M3.
- [ ] When the group's frames zip arrives, upload `images/` to Roboflow and assign **300 frames to each member** (Roboflow > Annotate > Assign).
- [ ] Commit `frame_metadata.csv` to `metadata/` in this repo.
- [ ] Add M2 and M3 as GitHub collaborators (Settings > Collaborators).

## Phase 1: Annotation (everyone, in parallel)

- [ ] M1 annotates frames 1–300
- [ ] M2 annotates frames 301–600
- [ ] M3 annotates frames 601–900
- [ ] Everyone attends the **mandatory in-class annotation session** (5%).

Rules (from the spec): manual boxes only, **no AI-assisted or automatic annotation**; tight boxes around the visible part; box every instance; frames with no logos are marked **null**, not skipped; overlays (channel logos, tickers, headlines) are excluded.

## Phase 2: Dataset version + EDA (M1)

- [ ] Review a sample of each member's frames for consistency.
- [ ] Generate one Roboflow version: **70 / 20 / 10** train / valid / test split, resize preprocessing, augmentation on the **training set only**. Record every setting.
- [ ] Make the Roboflow project **public** and put its link in `README.md`.
- [ ] Fill in `config.py` (workspace, project, version) and push, so M2 and M3 can start.
- [ ] Complete and run `1_EDA.ipynb`.

## Phase 3: Detectors (everyone, in parallel)

Only groups of four may use two YOLO versions, so this group uses **one** YOLO.

| Member | Detector | Framework | Notebook |
|---|---|---|---|
| M1 | YOLO11 | Ultralytics | `2_YOLO11_DebattistaMalcolm.ipynb` |
| M2 | Faster R-CNN (ResNet-50 FPN) | PyTorch / torchvision | `2_FasterRCNN_[M2Name].ipynb` |
| M3 | RF-DETR | PyTorch (rfdetr) | `2_RFDETR_[M3Name].ipynb` |

Each notebook starts from `2_ObjectDetector_template.ipynb`, uses the shared test set, and writes `results/<model>_<student>_metrics.json` in the template's format. Train locally or on Google Colab (T4 GPU), **not** on Roboflow or Ultralytics Hub.

## Phase 4: Comparison, report and journal

| Deliverable | Owner |
|---|---|
| `3_results_comparison.ipynb` | M3 |
| Final `README.md` and repository tidy-up | M2 |
| Technical report assembly (≤ 20 pages, one PDF) | M2 |
| AI journal assembly (≤ 10 pages, one PDF) | M3 |

**Technical report sections**

| Section | Owner |
|---|---|
| Introduction | M2 |
| Background on the Techniques Used | M2 (each member adds a paragraph on their own detector) |
| EDA & Annotation | M1 |
| Implementation of the Object Detectors | each member: their own detector |
| Evaluation & Comparison | M3 |
| Concluding Remarks | M2 |
| References | everyone adds their own |

**AI journal sections**

| Section | Owner |
|---|---|
| Introduction, Ethical Considerations, Methodology | M3 |
| Improvements, Errors and Contributions | M1 |
| Prompts and Responses | each member, under their own name |
| Individual Reflection | each member, under their own name |

Keep a record of the AI prompts you use from the start; the journal needs them per student.

## Suggested timeline

| By | Milestone |
|---|---|
| 2 Dec | Phase 0 done; annotation started |
| 16 Dec | All 900 frames annotated |
| 20 Dec | Dataset version public, `config.py` pushed, EDA done |
| 4 Jan | All three detectors trained, metrics files pushed |
| 8 Jan | Comparison notebook, report and journal drafts complete |
| 11 Jan | Submit |
