# Playwright with Python — ParaBank examples

Web automation practice using **Python, pytest, and Playwright** against ParaBank. Page interactions, business keywords, and test scenarios are separated, with CSV data converted into Python dataclass instances.

## Scenarios

- Open checking and savings accounts using parametrized CSV rows.
- View account details and transfer funds.
- Combine account creation, transfers, and account overview into longer workflows.

## Structure

| Location | Responsibility |
| --- | --- |
| [tests/test_e2e.py](tests/test_e2e.py) | Individual operations and parametrized tests |
| [tests/test_workflows.py](tests/test_workflows.py) | Combined business workflows |
| [keywords](keywords) | Reusable business actions |
| [pages](pages) | Playwright locators and page interactions |
| [data/account.csv](data/account.csv) | Account types, reference accounts, and amounts |
| [utils](utils) | CSV reading and dataclass creation |

## Setup

The project declares Python **3.9+**, pytest **7.4.4**, and pytest-playwright **0.4.3** version ranges in [pyproject.toml](pyproject.toml). Install Poetry, then run:

```bash
git clone https://github.com/angel-valdezzz/playwright-python-example.git
cd playwright-python-example
poetry install --with test --no-root
poetry run playwright install chromium
```

## Run

Run commands from the repository root:

```bash
poetry run pytest tests --browser chromium
poetry run pytest tests/test_e2e.py --browser chromium --headed
poetry run pytest tests/test_workflows.py --browser chromium
```

To use Firefox, install its browser binary first:

```bash
poetry run playwright install firefox
poetry run pytest tests --browser firefox
```

## Test data and environment

The login keyword targets the public ParaBank demo and uses its sample `john` / `demo` credentials in [login_keywords.py](keywords/login_keywords.py). Use demo data only.

Check the reference account IDs in [account.csv](data/account.csv) before running. Some workflows also contain fixed account IDs in the test code. ParaBank data can change or reset, so those values must match the available accounts. Tests create accounts and transfer demo funds; their outcome depends on the shared application's state and availability.

## Related projects

- [Robot Framework Selenium example](https://github.com/angel-valdezzz/robot-framework-selenium-testing)
- [Cypress ParaBank example](https://github.com/angel-valdezzz/cypress-web-e2e-demo1)
- [Portfolio map](https://github.com/angel-valdezzz/angel-valdezzz/blob/main/PORTFOLIO.md)
