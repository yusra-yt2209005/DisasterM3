import json
from os.path import join
from typing import List, Dict

from datasets.base import BaseDataset


class DisasterM3Dataset(BaseDataset):
    """
    DisasterM3 dataset adapter.

    Responsible ONLY for:
    - loading JSON
    - assigning IDs
    - filtering completed samples
    """

    def __init__(self, project_root: str, subset: str, finish_ids: List[str] = None):
        self.project_root = project_root
        self.subset = subset
        self.finish_ids = finish_ids or []

    def load(self) -> List[Dict]:
        # 1. Locate dataset file
        subset_json = join(self.project_root, "data", f"{self.subset}.json")

        # 2. Load raw dataset
        with open(subset_json, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # 3. Standardize format (attach IDs)
        dataset = [
            {
                "id": f"{self.subset}_{i}",
                **item
            }
            for i, item in enumerate(raw_data)
        ]

        # 4. Resume capability (skip finished samples)
        if self.finish_ids:
            dataset = [
                item for item in dataset
                if item["id"] not in self.finish_ids
            ]

        return dataset