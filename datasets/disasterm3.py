import json
from os.path import join
from typing import List, Dict
from datasets.base import BaseDataset


class DisasterM3Dataset(BaseDataset):
    """
    DisasterM3 dataset adapter.

    Responsible ONLY for:
    - loading JSON data
    - attaching sample IDs
    - filtering completed samples
    """

    def __init__(self, project_root: str, subset: str, finish_ids: List[str] = None):
        self.project_root = project_root
        self.subset = subset
        self.finish_ids = finish_ids or []

    def load(self) -> List[Dict]:
        dataset_path = join(self.project_root, "data", f"{self.subset}.json")

        with open(dataset_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Step 1: attach stable IDs (keeps compatibility with original pipeline)
        processed_data = [
            {
                "id": f"{self.subset}_{i}",
                **item
            }
            for i, item in enumerate(data)
        ]

        # Step 2: resume support (skip finished samples)
        if self.finish_ids:
            processed_data = [
                item for item in processed_data
                if item["id"] not in self.finish_ids
            ]

        return processed_data