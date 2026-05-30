from abc import ABC, abstractmethod
from typing import List, Dict


class BaseDataset(ABC):
    """
    Abstract dataset interface for all disaster datasets.
    Ensures consistent loading across frameworks.
    """

    @abstractmethod
    def load(self) -> List[Dict]:
        """
        Load dataset samples in standardized format.

        Returns:
            List of dict samples with at least:
            - id
            - image_path / pre_image_path / post_image_path
            - prompts / labels depending on dataset
        """
        raise NotImplementedError