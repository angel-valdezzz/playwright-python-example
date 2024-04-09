from playwright.sync_api import Page
from keywords.login_keywords import LoginKeywords
from keywords.create_new_account_keywords import CreateNewAccountKeywords
from keywords.account_overview_keywords import AccountOverviewKeywords
from keywords.transfer_funds_keywords import TransferFundsKeywords
import pytest
from utils.datatable.data_table_creator import DataTableCreator
from utils.datatable.csv_data_reader import CSVDataReader
from utils.data_dir_content import DataDirContent
from dataclasses import dataclass

@pytest.fixture
def login(page: Page) -> None:
    """Fixture to log in to the application."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

@pytest.mark.parametrize("datatable", DataTableCreator.create_tables(CSVDataReader, DataDirContent("account.csv")))
def test_open_new_account(datatable: dataclass, login, page: Page) -> None:
    """Test opening a new account in Parabank."""
    create_new_account = CreateNewAccountKeywords(page)
    create_new_account.create_new_account(datatable.account_type, datatable.account_reference)

def test_account_overview(login, page: Page) -> None:
    """Test the account overview page in Parabank."""
    dt = DataTableCreator.create_table(CSVDataReader, DataDirContent("account.csv"), 0)

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview(dt.account_reference)

def test_transfer_funds(login, page: Page) -> None:
    """Test transferring funds in Parabank."""
    dt = DataTableCreator.create_table(CSVDataReader, DataDirContent("account.csv"), 0)

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds("100", dt.account_reference, dt.account_reference)
