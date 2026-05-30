# Computer Vision Tasks: Classification, Detection, and Segmentation

## Overview

Computer vision enables machines to interpret and understand visual information from images. Three fundamental tasks form the backbone of most vision systems: classification, object detection, and segmentation. This document explains each task and their applications to natural disaster analysis.

---

## 1. Image Classification

**Definition:** Assigning a single label or category to an entire image.

**How it works:** The model analyzes the whole image and outputs a probability distribution over predefined classes (e.g., "flood," "earthquake," "wildfire").

**Output:** One label per image.

**Example:**
- Input: Satellite image of a flooded neighborhood
- Output: "Flood"

**Disaster application:** Rapidly categorizing large volumes of satellite imagery to identify which regions show signs of specific disaster types.

---

## 2. Object Detection

**Definition:** Identifying and localizing multiple objects within an image using bounding boxes.

**How it works:** The model predicts both:
- What each object is (classification)
- Where each object is located (bounding box coordinates)

**Output:** Multiple (class, x, y, width, height) tuples per image.

**Example:**
- Input: Aerial image of post-earthquake damage
- Output: 
  - "Collapsed building" at [100, 150, 200, 180]
  - "Blocked road" at [300, 200, 150, 50]
  - "Rescue vehicle" at [500, 400, 80, 80]

**Disaster application:** Counting damaged buildings, locating blocked roads, identifying emergency vehicles or survivors in search-and-rescue operations.

---

## 3. Segmentation

**Definition:** Classifying every pixel in an image into a category. Two main types:

### Semantic Segmentation
- Each pixel gets a class label
- **Does NOT** distinguish between separate objects of the same class
- Example: All "road" pixels are labeled the same, even if roads are disconnected

### Instance Segmentation
- Each pixel gets a class label **AND** object instance ID
- Distinguishes between separate objects of the same class
- Example: Road A pixels vs. Road B pixels are differentiated

**Output:** Pixel-wise class map (same dimensions as input image).

**Example (Semantic):**
- Input: Satellite image of wildfire
- Output: Each pixel labeled as "burned_area," "vegetation," "smoke," "infrastructure"

**Disaster application:** Precise mapping of flood extent, burned area calculation, damage severity per building (partial vs. complete collapse), evacuation route planning.

---

## Comparison Table

| Feature | Classification | Detection | Segmentation |
|---------|---------------|-----------|--------------|
| **Output granularity** | Image-level | Object-level | Pixel-level |
| **Object counting** | No | Yes (per detected box) | Yes (precise) |
| **Spatial localization** | None | Bounding boxes | Exact boundaries |
| **Computational cost** | Low | Medium | High |
| **Annotation difficulty** | Easy | Medium | Hard |

---

## Disaster-Specific Examples

| Disaster Type | Classification | Detection | Segmentation |
|---------------|----------------|-----------|--------------|
| **Flood** | "Flood present" | Boats, submerged cars | Flood water extent |
| **Earthquake** | "Earthquake damage" | Collapsed buildings, cracks | Rubble area, building damage per pixel |
| **Wildfire** | "Active fire" | Fire fronts, fire trucks | Burned scar, active flame zone |
| **Hurricane** | "Storm damage" | Downed trees, damaged roofs | Debris-covered area |
| **Landslide** | "Landslide detected" | Blocked roads, displaced rocks | Landslide perimeter |

---

## When to Use Which Task in Disaster Response

| Phase | Best Task | Why |
|-------|-----------|-----|
| **Early warning** | Classification | Fast, low-resource screening |
| **Damage assessment** | Detection + Segmentation | Need precise localization and quantification |
| **Resource allocation** | Detection | Identifying specific assets (vehicles, equipment) |
| **Recovery mapping** | Segmentation | Detailed change detection over time |
| **Humanitarian corridors** | Segmentation | Pixel-perfect passable route mapping |

---

## Vision-Language Models (VLM) Connection

Modern VLMs combine these vision capabilities with natural language:
- **Visual Question Answering (VQA):** "How many collapsed buildings are in this image?" (requires detection-like reasoning)
- **Disaster captioning:** "This satellite image shows extensive flooding with submerged vehicles" (requires understanding all three tasks)
- **Referring expression comprehension:** "Show me the area with the most severe damage" (requires segmentation-like output)

The evaluation framework you'll build must assess VLMs on their ability to perform these tasks in disaster contexts.