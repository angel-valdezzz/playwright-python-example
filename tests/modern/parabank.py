import os
from uuid import uuid4
from playwright.sync_api import expect

class ParaBank:
    def __init__(self, page):
        self.page = page
        self.username = 'qa' + uuid4().hex
        self.password = 'DemoPass42!'

    def home(self):
        self.page.goto(os.getenv('PARABANK_URL', 'https://parabank.parasoft.com/parabank') + '/index.htm')

    def form(self, mismatch=False):
        self.home()
        self.page.get_by_role('link', name='Register', exact=True).click()
        fields = {'customer.firstName': 'Automation', 'customer.lastName': 'Example', 'customer.address.street': '123 Fictional Street', 'customer.address.city': 'Demo City', 'customer.address.state': 'CA', 'customer.address.zipCode': '90210', 'customer.phoneNumber': '5551234567', 'customer.ssn': '123456789'}
        for field, value in fields.items():
            self.page.locator('[id="' + field + '"]').fill(value)
        self.page.locator('[id="customer.username"]').fill(self.username)
        self.page.locator('[id="customer.password"]').fill(self.password)
        self.page.locator('#repeatedPassword').fill('Different42!' if mismatch else self.password)

    def submit(self):
        self.page.locator('#customerForm input[type=submit]').click()

    def register(self):
        self.form()
        self.submit()
        expect(self.page.locator('#rightPanel h1')).to_have_text('Welcome ' + self.username)

    def login(self):
        self.page.locator('input[name=username]').fill(self.username)
        self.page.locator('input[name=password]').fill(self.password)
        self.page.locator('#loginPanel input[type=submit]').click()
