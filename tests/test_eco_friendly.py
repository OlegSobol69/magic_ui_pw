import pytest


@pytest.mark.regression
def test_page_title(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_page_title("Eco Friendly")


@pytest.mark.regression
def test_product_items_displayed(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_product_items_displayed()


@pytest.mark.regression
def test_search_functionality(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.search_product_result("Bella")
