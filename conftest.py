from pages.account_create_page import AccountCreate
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale
import pytest


@pytest.fixture()
def account_create_page(page):
    return AccountCreate(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale_page(page):
    return Sale(page)
