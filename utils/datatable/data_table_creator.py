from dataclasses import dataclass, make_dataclass
from utils.datatable.abstract_data_reader import AbstractDataReader
from utils.data_dir_content import DataDirContent

class DataTableCreator:
    @staticmethod
    def create_tables(reader: AbstractDataReader, data_dir_content: DataDirContent) -> list[dataclass]:
        """Create a DataTable from the CSV file."""
        data_file_path: str = data_dir_content.get_content()

        datatables: list[dataclass] = []
        testdata_rows = reader.read(data_file_path)

        for testdata_row in testdata_rows:
            DataTable: dataclass = make_dataclass("DataTable", testdata_row.keys())
            datatables.append(DataTable(**testdata_row))

        return datatables
    
    @staticmethod
    def create_table(reader: AbstractDataReader, data_dir_content: DataDirContent, index: int) -> dataclass:
        """Create a DataTable from the CSV file."""
        data_file_path: str = data_dir_content.get_content()

        testdata_row = reader.read(data_file_path)[index]
        DataTable: dataclass = make_dataclass("DataTable", testdata_row.keys())

        return DataTable(**testdata_row)
