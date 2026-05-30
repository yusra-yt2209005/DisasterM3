# Reuse Analysis — EarthVQA

## 1. Overview

This document analyzes the **EarthVQA** dataset in the context of the DisasterM3 benchmarking framework. The goal is to identify a reusable design pattern and explain how EarthVQA can be integrated into the proposed modular evaluation architecture.

EarthVQA is a remote sensing Visual Question Answering (VQA) dataset where each sample typically consists of:

* A single satellite image
* A natural language question
* A set of candidate answers (optional in some variants)
* A ground-truth answer

This structure closely aligns with multiple tasks already present in DisasterM3 (e.g., landuse classification and relational reasoning QA).

---

## 2. Reusable Design Pattern: Dataset Adapter Pattern

The key reusable design pattern is the **Dataset Adapter Pattern**, where dataset-specific logic is encapsulated behind a unified interface.

### Core Idea

Instead of allowing each dataset to define its own processing pipeline, all datasets are normalized into a shared format through an adapter.

Each dataset implements:

* A `load()` function
* Dataset-specific preprocessing logic
* Conversion into a unified data representation

---

### Normalized Representation

EarthVQA can be mapped into the following unified structure:

```python id="earthvqa_format"
{
    "id": "...",
    "images": ["image.jpg"],
    "question": "...",
    "options": ["A", "B", "C", "D"],  # optional depending on task variant
    "answer": "B",
    "task_type": "vqa"
}
```

This format is fully compatible with the DisasterM3 VQA-style tasks.

---

## 3. Integration into the Proposed Framework

The proposed modular architecture follows:

```text id="framework_flow"
Dataset → Model Runner → Evaluator → Experiment Tracker
```

### Dataset Layer Integration

EarthVQA fits directly into the **Dataset layer** via a subclass of `BaseDataset`:

```python id="earthvqa_class"
class EarthVQADataset(BaseDataset):
    def load(self):
        ...
```

The adapter is responsible only for loading and normalizing data, while all downstream components remain unchanged.

---

## 4. Reusability Analysis

### Components Reused Without Modification

| Component           | Reusable  | Explanation                                |
| ------------------- | --------- | ------------------------------------------ |
| Model Runner        | Yes       | EarthVQA uses same VLM input format        |
| Prompt Structure    | Partially | Can reuse VQA prompt templates             |
| Evaluation Logic    | Yes       | Accuracy-based evaluation applies directly |
| Experiment Tracking | Yes       | Independent of dataset                     |

### Components Requiring Adaptation

| Component       | Change Required | Reason                          |
| --------------- | --------------- | ------------------------------- |
| Dataset Loader  | Yes             | EarthVQA file structure differs |
| Prompt Template | Minor           | Question formatting differences |

---

## 5. Key Insight

The most important observation is that **EarthVQA does not require changes to the core benchmarking pipeline**.

Only the dataset adapter layer changes, while all other components remain fully reusable.

This confirms that dataset abstraction is the correct architectural boundary for scaling the framework across multiple remote sensing benchmarks.

---

## 6. Conclusion

EarthVQA strongly validates the proposed modular design. Its structure aligns naturally with a Dataset Adapter Pattern, demonstrating that:

* Heterogeneous remote sensing datasets can be unified through normalization
* Model and evaluation layers remain dataset-agnostic
* Only the dataset adapter requires modification for integration

This reinforces the scalability of the framework and supports the design direction established in Task 3.
