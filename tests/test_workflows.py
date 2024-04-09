from playwright.sync_api import Page
import pytest
from keywords.login_keywords import LoginKeywords
from keywords.create_new_account_keywords import CreateNewAccountKeywords
from keywords.account_overview_keywords import AccountOverviewKeywords
from keywords.transfer_funds_keywords import TransferFundsKeywords
from utils.datatable.data_table_creator import DataTableCreator
from utils.datatable.csv_data_reader import CSVDataReader
from utils.data_dir_content import DataDirContent

@pytest.fixture
def login(page: Page) -> None:
    """Fixture to log in to the application."""
    login = LoginKeywords(page)
    login.login_in_to_the_application()

def test_open_new_account_and_transfer_funds(login, page: Page) -> None:
    """Test opening a new account and transferring funds in Parabank."""
    dt = DataTableCreator.create_table(CSVDataReader, DataDirContent("account.csv"), 0)

    create_new_account = CreateNewAccountKeywords(page)
    new_account = create_new_account.create_new_account(dt.account_type, dt.account_reference)

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds("100", "13344", new_account)

def test_open_account_and_view_overview(login, page: Page) -> None:
    """Test opening an account and viewing the account overview in Parabank."""
    dt = DataTableCreator.create_table(CSVDataReader, DataDirContent("account.csv"), 0)

    create_new_account = CreateNewAccountKeywords(page)
    new_account = create_new_account.create_new_account(dt.account_type, dt.account_reference)

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview(new_account)

def test_open_new_account_transfer_funds_and_view_overview(login, page: Page) -> None:
    """Test opening a new account, transferring funds, and viewing the account overview in Parabank."""
    dt = DataTableCreator.create_table(CSVDataReader, DataDirContent("account.csv"), 0)

    create_new_account = CreateNewAccountKeywords(page)
    new_account = create_new_account.create_new_account(dt.account_type, dt.account_reference)

    transfer_funds = TransferFundsKeywords(page)
    transfer_funds.transfer_funds(dt.amount, dt.account_reference, new_account)

    account_overview = AccountOverviewKeywords(page)
    account_overview.open_account_overview(new_account)
