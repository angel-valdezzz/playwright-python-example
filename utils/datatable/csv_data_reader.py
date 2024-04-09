import csv
from utils.datatable.abstract_data_reader import AbstractDataReader

class CSVDataReader(AbstractDataReader):
    """CSVDataReader class."""
    @staticmethod
    def read(source):
        """Read the data from the CSV file."""
        with open(source, "r") as file:
            return list(csv.DictReader(file))
