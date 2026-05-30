# Evaluation Methodology for Vision-Language Models

## Introduction

Vision-Language Models (VLMs) combine visual understanding and natural language processing to perform tasks that require reasoning over both images and text. Examples include answering questions about images, generating captions, classifying disasters, and producing recovery recommendations from satellite imagery.

Evaluating VLMs is more challenging than evaluating traditional computer vision models because both image understanding and language generation must be assessed.

---

## Evaluation Data

### Benchmark Datasets

VLMs are typically evaluated using benchmark datasets designed to test different capabilities.

| Task Type                       | Description                                          |
| ------------------------------- | ---------------------------------------------------- |
| Visual Question Answering (VQA) | Answer questions about an image                      |
| Image Captioning                | Generate descriptions of image content               |
| Visual Reasoning                | Perform multi-step reasoning from visual information |
| Classification                  | Predict disaster or damage categories                |
| Counting                        | Estimate the number of damaged objects               |
| Disaster Assessment             | Analyze disaster impact from remote sensing imagery  |

For this internship, disaster-oriented datasets such as DisasterM3 are particularly important because they combine image understanding, reasoning, and domain-specific knowledge.

### Disaster-Specific Challenges

Evaluating VLMs on disaster datasets introduces additional challenges:

* Class imbalance between damaged and undamaged regions.
* Large variations in geographic locations and imaging conditions.
* Differences in satellite resolution and sensor types.
* Requirement to compare pre-disaster and post-disaster imagery.
* Multiple valid descriptions for the same scene.

---

## Evaluation Metrics

### Accuracy

Accuracy measures the percentage of correct predictions.

Used for:

* Disaster type classification
* Damage category classification
* Multiple-choice visual question answering

Accuracy is simple and interpretable but can be misleading when classes are imbalanced.

---

### F1 Score

The F1 score balances precision and recall.

It is particularly useful when severe damage cases are much less common than non-damage cases.

For disaster assessment tasks, F1 often provides a more meaningful evaluation than accuracy alone.

---

### Exact Match (EM)

Exact Match measures whether a generated answer exactly matches the reference answer.

Example:

Ground Truth: A

Prediction: A

Result: Correct

This metric is commonly used for multiple-choice question answering tasks.

---

### Text Similarity Metrics

For caption generation and recovery recommendation tasks, exact matching is insufficient because many valid responses may exist.

Common metrics include:

* BLEU
* ROUGE
* METEOR
* CIDEr

These metrics compare generated text with reference descriptions and measure linguistic similarity.

---

### Counting Metrics

For tasks involving damaged building counting or infrastructure estimation, numerical error metrics are used.

Examples:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

These metrics measure how far predictions deviate from ground-truth counts.

---

### Localization Metrics

When models identify affected regions, localization metrics become important.

Examples:

* Intersection over Union (IoU)
* Average Precision (AP)

These metrics evaluate how accurately the predicted locations match ground-truth regions.

---

## Evaluation Pipeline

A typical VLM evaluation workflow consists of:

1. Loading benchmark data.
2. Preparing prompts and images.
3. Running model inference.
4. Collecting model predictions.
5. Computing task-specific metrics.
6. Aggregating results across the dataset.
7. Logging and reporting performance.

This process should be standardized so that different models can be compared fairly.

---

## Reproducibility

A robust evaluation framework should ensure reproducible results through:

* Fixed random seeds.
* Consistent software environments.
* Version-controlled datasets.
* Documented hyperparameters.
* Automated experiment logging.

These practices improve reliability and allow meaningful comparison between models.

---

## Relevance to DisasterM3

The DisasterM3 benchmark evaluates Vision-Language Models on disaster-related remote sensing tasks such as classification, counting, reasoning, caption generation, and recovery recommendation.

Because these tasks produce different output types, no single metric is sufficient. A complete evaluation framework must support multiple metrics and standardized reporting procedures.

---

## Conclusion

Evaluating Vision-Language Models requires both task-specific metrics and standardized evaluation procedures. An effective framework should support multiple datasets, multiple model architectures, reproducible experiments, and comprehensive reporting. Such a framework enables fair comparison of VLMs and helps identify strengths and weaknesses across disaster assessment tasks.
