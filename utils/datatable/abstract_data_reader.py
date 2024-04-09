"""AbstractDataReader class."""
from abc import ABC, abstractmethod

class AbstractDataReader(ABC):
    """AbstractDataReader class."""
    @staticmethod
    @abstractmethod
    def read(source):
        """Read the data from the data source."""
