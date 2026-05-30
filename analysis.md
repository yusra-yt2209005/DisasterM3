# DisasterM3 Repository Analysis

## 1. Current Repository Structure

The repository currently contains two primary implementation components:

```text
DisasterM3/
├── models/
│   └── __init__.py
├── pyscripts/
│   └── run_vllm.py
├── __init__.py
└── README.md
```

### 1.1 Code Organization Analysis

The repository follows a relatively simple architecture consisting of a benchmarking script and a model abstraction layer.

#### 1.1.1 Model Layer

The `models/__init__.py` file contains:

* An abstract model interface (`ModelConfig`)
* Implementations for multiple Vision-Language Models (VLMs)
* Model-specific prompt formatting logic
* Image and video preprocessing utilities
* Factory methods for model creation

The use of an abstract interface and factory pattern provides a consistent API across different model architectures and simplifies model replacement.

#### 1.1.2 Benchmark Pipeline

The `pyscripts/run_vllm.py` script is responsible for:

* Loading benchmark data
* Constructing prompts
* Preparing model inputs
* Running inference using vLLM
* Saving generated predictions

Most benchmarking responsibilities are centralized within this file.

The overall workflow can be summarized as:

```text
Dataset
   ↓
Prompt Construction
   ↓
Model Configuration
   ↓
VLM Inference
   ↓
Results Storage
```

### 1.2 Positive Aspects

The repository already contains several good design choices:

#### 1.2.1 Model Abstraction Layer

The framework provides a common interface for multiple Vision-Language Models, making it easier to add or switch between supported model families.

#### 1.2.2 Use of Software Design Patterns

The implementation uses an abstract base class and a factory pattern to standardize model creation and interaction. This improves code organization and reduces duplication.

#### 1.2.3 Clear and Readable Structure

The codebase is relatively small and easy to understand. New contributors can quickly identify the main execution flow and understand how benchmarking is performed.

#### 1.2.4 Multi-Modal Support

The framework includes support for both image and video inputs, making it flexible enough to support different benchmark tasks.

### 1.3 Dataset Dependency Analysis

The framework is currently tightly coupled to the DisasterM3 dataset.

Evidence of this coupling includes:

* Direct use of dataset-specific fields such as:

  * `pre_image_path`
  * `post_image_path`
  * `prompts`
  * `options_str`
* Hardcoded DisasterM3 task categories.
* Assumptions about the dataset directory structure and image organization.

As a result, additional datasets cannot be integrated without modifying the source code.

#### 1.3.1 Supporting Additional Datasets

To support other datasets such as MONITRS, EarthVQA, or future disaster-related benchmarks, the framework would benefit from a dataset abstraction layer.

For example:

```python
class BaseDataset:
    def load_data(self):
        pass

    def build_prompt(self):
        pass
```

Dataset-specific implementations could then inherit from this interface:

```python
class DisasterM3Dataset(BaseDataset):
    ...

class MONITRSDataset(BaseDataset):
    ...
```

The benchmarking pipeline would interact with the common dataset interface rather than directly accessing dataset-specific fields.

---

## 2. Identified Limitations

### 2.1 Strong Dataset Coupling

The benchmarking pipeline assumes the structure and task definitions of DisasterM3, limiting reuse with other datasets.

### 2.2 Mixed Responsibilities

Dataset loading, prompt generation, inference execution, and result storage are all handled within `run_vllm.py`, reducing separation of concerns and making future maintenance more difficult.

### 2.3 Missing Evaluation Layer

The repository generates predictions but does not provide dedicated evaluation modules for computing benchmark metrics or comparing model performance.

### 2.4 Limited Experiment Management

Results are stored as output files, but there is no built-in mechanism for experiment tracking, configuration management, or run comparison.

### 2.5 Limited Extensibility

Adding new datasets, evaluation methods, or benchmarking workflows would require modifications to existing scripts rather than extending independent modules.

---

## 3. Proposed Modular Redesign

To improve maintainability and extensibility, the repository could be reorganized into dedicated modules:

```text
datasets/
    base_dataset.py
    disasterm3.py
    monitrs.py

models/
    base_model.py
    qwen.py
    internvl.py
    llava.py

prompts/
    templates.py

evaluation/
    metrics.py

experiments/
    tracking.py

pyscripts/
    run_benchmark.py
```

### 3.1 Dataset Abstraction Layer

A common dataset interface should be introduced:

```python
class BaseDataset:
    def load_data(self):
        pass

    def build_prompt(self):
        pass
```

Each dataset would implement its own loading and prompt-generation logic while exposing the same interface to the benchmarking pipeline.

### 3.2 Separation of Responsibilities

The redesigned architecture separates dataset handling, prompt generation, model execution, evaluation, and experiment tracking into dedicated modules.

This reduces coupling and improves maintainability.

### 3.3 Proposed Workflow

The redesigned benchmarking workflow would be:

```text
Dataset
   ↓
Prompt Builder
   ↓
Model Runner
   ↓
Evaluator
   ↓
Experiment Tracker
```

### 3.4 Expected Benefits

The proposed redesign would provide:

* Easier integration of new datasets.
* Improved code maintainability.
* Dedicated support for evaluation metrics.
* Better experiment management and reproducibility.
* Clearer separation of responsibilities across the framework.

---

## 4. Conclusion

The DisasterM3 repository provides a functional benchmarking framework with a well-designed model abstraction layer and support for multiple Vision-Language Models. The existing model architecture is a strong foundation for future development.

However, the current implementation is tightly coupled to the DisasterM3 dataset and lacks dedicated dataset, evaluation, and experiment-management components. Introducing dataset abstractions and separating responsibilities into dedicated modules would improve scalability, maintainability, and support for future benchmarking tasks.
