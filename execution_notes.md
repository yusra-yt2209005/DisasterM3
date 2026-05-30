# Execution Notes

## 1. Overview

As part of Task 4, an attempt was made to execute the DisasterM3 evaluation pipeline using the script `pyscripts/run_vllm.py`.

### Execution Summary

| Item             | Details                                                                   |
| ---------------- | ------------------------------------------------------------------------- |
| Script           | `pyscripts/run_vllm.py`                                                   |
| Model Attempted  | `OpenGVLab/InternVL2-2B`                                                  |
| Operating System | Windows 64-bit                                                            |
| Execution Status | Partial Execution                                                         |
| Result           | Script could not be fully executed due to missing vLLM support on Windows |

---

## 2. System Environment

### Hardware

| Component | Specification        |
| --------- | -------------------- |
| CPU       | Intel Core i7-8550U  |
| RAM       | 16 GB                |
| GPU       | NVIDIA GeForce MX130 |
| VRAM      | 2 GB                 |

### Software

| Component        | Version        |
| ---------------- | -------------- |
| Python           | 3.10.6         |
| PyTorch          | 2.12.0         |
| Transformers     | 5.9.0          |
| Accelerate       | 1.13.0         |
| Operating System | Windows 64-bit |

---

## 3. Dependencies

The following dependencies were successfully installed:

```bash
pip install torch transformers pillow tqdm accelerate
```

Installed packages included:

* torch
* transformers
* accelerate
* pillow
* tqdm
* numpy
* tokenizers
* huggingface-hub
* safetensors

### Missing Dependency

The repository depends on `vllm`, which could not be installed successfully on the Windows environment used for testing.

---

## 4. Execution Steps

### Step 1: Create Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
pip install torch transformers pillow tqdm accelerate
```

### Step 4: Run Evaluation Script

```bash
python pyscripts/run_vllm.py \
    --model_id "OpenGVLab/InternVL2-2B" \
    --subset "landuse" \
    --max_tokens 10 \
    --batch_size 1
```

---

## 5. Encountered Issues

### Issue 1: vLLM Not Available on Windows

The execution failed immediately during import:

```text
ModuleNotFoundError: No module named 'vllm'
```

The `run_vllm.py` script depends on the vLLM inference engine, which is primarily supported on Linux environments with CUDA-enabled GPUs.

**Impact:** Script execution could not proceed beyond the import stage.

### Issue 2: Insufficient GPU Memory

The available GPU was an NVIDIA GeForce MX130 with 2 GB VRAM.

Approximate requirements for supported models:

| Model        | Estimated VRAM |
| ------------ | -------------- |
| InternVL2-2B | ~6 GB          |
| Llava-7B     | ~14 GB         |
| Qwen2-VL-7B  | ~16 GB         |

Even if vLLM had been installed successfully, the available hardware would not be sufficient for model inference.

### Issue 3: Dataset Not Available

The repository expects a local `data/` directory containing benchmark JSON files and images.

Example structure:

```text
data/
├── images/
├── bearing_body.json
├── caption.json
└── ...
```

The dataset was not included in the repository, preventing complete execution.

---

## 6. Reproducibility and Running Limitations

Several requirements were not clearly documented in the original repository:

| Requirement                      | Status            |
| -------------------------------- | ----------------- |
| Linux environment                | Required for vLLM |
| CUDA-enabled GPU                 | Required          |
| 6+ GB VRAM minimum               | Required          |
| DisasterM3 dataset files         | Required          |
| Correct data directory structure | Required          |

These limitations significantly affect reproducibility for users attempting to run the framework on a standard Windows machine.

---

## 7. README Improvements

The original repository README did not clearly describe execution requirements.

The README was updated to include:

* System requirements
* Dependency installation instructions
* Dataset setup requirements
* Example execution commands
* Hardware recommendations
* Windows and WSL2 notes
* Common troubleshooting information

These additions improve reproducibility and reduce setup ambiguity for future users.

---

## 8. Recommendations

Based on the execution attempt, the following environments are recommended for running the framework successfully:

### Option 1: Google Colab

* Linux environment
* CUDA-enabled GPU
* Typically 16 GB GPU memory available
* Minimal setup effort

### Option 2: WSL2

* Linux compatibility on Windows
* Supports vLLM installation
* Still requires a sufficiently powerful GPU

### Option 3: Dedicated Linux Machine

* Ubuntu 20.04+
* CUDA installed
* NVIDIA GPU with at least 6 GB VRAM

---

## 9. Conclusion

A partial execution of the DisasterM3 framework was completed. Virtual environment creation, dependency installation, and script execution setup were successful. However, full execution was blocked by three primary factors:

1. vLLM is not supported on the tested native Windows environment.
2. The available GPU (NVIDIA GeForce MX130) does not provide sufficient VRAM for the supported Vision-Language Models.
3. The DisasterM3 dataset files were not available locally.

Despite these limitations, the execution attempt successfully identified the framework's software dependencies, hardware requirements, and reproducibility constraints. These findings were incorporated into the updated README documentation to improve future setup and execution.
