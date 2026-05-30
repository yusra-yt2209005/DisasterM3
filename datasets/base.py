from abc import ABC, abstractmethod
from typing import List, Dict


class BaseDataset(ABC):
    @abstractmethod
    def load(self) -> List[Dict]:
        """
        Load dataset and return a list of standardized samples.
        Each sample is a dict containing:
        - id
        - image paths
        - prompts / questions
        - metadata (task-specific fields)
        """
        raise NotImplementedError