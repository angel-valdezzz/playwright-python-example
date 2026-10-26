from playwright.sync_api import expect
from .parabank import ParaBank

def test_registration(page):
    ParaBank(page).register()

def test_logout_login(page):
    bank = ParaBank(page)
    bank.register()
    page.get_by_role('link', name='Log Out', exact=True).click()
    bank.login()
    expect(page.locator('#rightPanel h1')).to_have_text('Accounts Overview')

def test_required_fields(page):
    bank = ParaBank(page)
    bank.home()
    page.get_by_role('link', name='Register', exact=True).click()
    bank.submit()
    expect(page.locator('[id="customer.firstName.errors"]')).to_have_text('First name is required.')

def test_password_mismatch(page):
    bank = ParaBank(page)
    bank.form(mismatch=True)
    bank.submit()
    expect(page.locator('[id="repeatedPassword.errors"]')).to_have_text('Passwords did not match.')

def test_invalid_login(page):
    bank = ParaBank(page)
    bank.home()
    bank.login()
    expect(page.locator('#rightPanel .error')).to_have_text('The username and password could not be verified.')

def test_open_savings(page):
    bank = ParaBank(page)
    bank.register()
    page.get_by_role('link', name='Open New Account', exact=True).click()
    expect(page.locator('#fromAccountId option').first).to_have_attribute('value', __import__('re').compile(r'\d+'))
    page.locator('#type').select_option('1')
    page.locator('#openAccountForm input.button').click()
    expect(page.locator('#newAccountId')).to_have_text(__import__('re').compile(r'^\d+$'))
    account = page.locator('#newAccountId').inner_text()
    page.locator('#newAccountId').click()
    expect(page.locator('#accountId')).to_have_text(account)
    expect(page.locator('#accountType')).to_have_text('SAVINGS')
