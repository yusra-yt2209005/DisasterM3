import json
from os.path import join
from typing import List, Dict

from datasets.base import BaseDataset


class EarthVQADataset(BaseDataset):
    """
    EarthVQA dataset adapter.

    Converts EarthVQA single-image QA format into DisasterM3-compatible
    bi-temporal structure for unified inference pipeline.
    """

    def __init__(self, project_root: str, subset: str = "earthvqa", finish_ids: List[str] = None):
        self.project_root = project_root
        self.subset = subset
        self.finish_ids = finish_ids or []

    def load(self) -> List[Dict]:
        dataset_path = join(self.project_root, "data", "earthvqa.json")

        with open(dataset_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        dataset = [
            {
                "pre_image_path": item.get("image_path"),
                "post_image_path": item.get("image_path"), # duplicate
                "prompts": item.get("question"),
                "options_str": item.get("options", "")
            }
            for i, item in enumerate(raw_data)
        ]

        # filter completed samples
        if self.finish_ids:
            dataset = [
                d for d in dataset
                if d["id"] not in self.finish_ids
            ]

        return dataset