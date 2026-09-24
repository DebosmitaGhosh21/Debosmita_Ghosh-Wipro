from pathlib import Path

import pytest
from selenium import webdriver
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import load_test_data
from login_page import LoginPage
from product_page import ProductPage
from cart_page import CartPage


# --------------------------------------------------
# Load test data from JSON
# --------------------------------------------------

TEST_DATA = load_test_data()

BASE_DIR = Path(__file__).resolve().parent.parent
SCREENSHOT_DIR = BASE_DIR / "screenshots"


# --------------------------------------------------
# Browser Fixture
# --------------------------------------------------

@pytest.fixture
def driver():
    """Create browser and safely close it after the test."""

    driver = None

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        yield driver

    except WebDriverException as error:
        pytest.fail(f"Browser/WebDriver error: {error}")

    finally:
        if driver:
            driver.quit()


# --------------------------------------------------
# Screenshot Function
# --------------------------------------------------

def take_screenshot(driver, filename):
    """Capture and save a screenshot."""

    SCREENSHOT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    path = SCREENSHOT_DIR / filename

    driver.save_screenshot(str(path))

    print(f"Screenshot saved: {path}")


# --------------------------------------------------
# Alert Handling
# --------------------------------------------------

def handle_alert_if_present(driver):
    """Handle JavaScript alert if one is present."""

    try:

        alert = WebDriverWait(driver, 2).until(
            EC.alert_is_present()
        )

        print("Alert detected:", alert.text)

        alert.accept()

        print("Alert accepted.")

    except TimeoutException:

        print("No browser alert present.")


# --------------------------------------------------
# Main E-Commerce Test
# --------------------------------------------------

def test_ecommerce_purchase_flow(driver):

    product_name = TEST_DATA["product_name"]
    expected_quantity = TEST_DATA["quantity"]

    try:

        # ==================================================
        # 1. Launch browser and open application
        # ==================================================

        driver.get(TEST_DATA["url"])

        # Wait until page title becomes available
        WebDriverWait(driver, 15).until(
            lambda d: d.title != ""
        )

        assert "Automation Exercise" in driver.title

        print("\nApplication opened successfully.")
        print("Page title:", driver.title)
        print("URL:", driver.current_url)

        take_screenshot(
            driver,
            "01_home_page.png"
        )

        # ==================================================
        # 2. Login
        # ==================================================

        login_page = LoginPage(driver)

        print("\nOpening login page...")

        login_page.open_login_page()

        print("Entering login credentials...")

        login_page.login(
            TEST_DATA["login_email"],
            TEST_DATA["login_password"]
        )

        assert login_page.verify_login_success(), \
            "Login verification failed."

        print("Login successful.")

        take_screenshot(
            driver,
            "02_login_success.png"
        )


        print("\nChecking and clearing existing cart...")

        cart_page = CartPage(driver)

        cart_page.clear_cart()


        # ==================================================
        # 3. Search product
        # ==================================================

        product_page = ProductPage(driver)

        print("\nOpening Products page...")

        product_page.open_products()

        print(
            f"Searching for product: {product_name}"
        )

        product_page.search_product(
            product_name
        )

        assert product_page.verify_product_visible(
            product_name
        ), f"Product '{product_name}' was not found."

        print(
            f"Product '{product_name}' found successfully."
        )

        take_screenshot(
            driver,
            "03_product_search.png"
        )

        # ==================================================
        # 4. Open product details
        # ==================================================

        print("\nOpening product details...")

        product_page.open_product_details(
            product_name
        )

        # ==================================================
        # 5. Update quantity
        # ==================================================

        print(
            f"Updating quantity to {expected_quantity}..."
        )

        product_page.update_quantity(
            expected_quantity
        )

        print(
            f"Quantity successfully set to "
            f"{expected_quantity}."
        )

        # ==================================================
        # 6. Add product to cart
        # ==================================================

        print("\nAdding product to cart...")

        product_page.add_product_from_details()

        print(
            f"'{product_name}' added to cart."
        )

        take_screenshot(
            driver,
            "04_product_added.png"
        )

        # ==================================================
        # 7. Handle popup/alert if available
        # ==================================================

        handle_alert_if_present(driver)

        # ==================================================
        # 8. Open cart
        # ==================================================

        print("\nOpening shopping cart...")

        product_page.view_cart()

        cart_page = CartPage(driver)

        assert cart_page.verify_cart_page(), \
            "Cart page was not displayed."

        print("Cart page opened successfully.")

        # ==================================================
        # 9. Verify product in cart
        # ==================================================

        product_names = cart_page.get_product_names()

        print(
            "Products present in cart:",
            product_names
        )

        assert product_name in product_names, (
            f"Expected product '{product_name}' "
            f"is not present in cart."
        )

        print(
            f"Product '{product_name}' "
            "verified in cart."
        )

        # ==================================================
        # 10. Verify quantity
        # ==================================================

        quantities = cart_page.get_quantities()

        print(
            "Quantities in cart:",
            quantities
        )

        assert cart_page.verify_product_and_quantity(
            product_name,
            expected_quantity
        ), (
            f"Expected quantity {expected_quantity} "
            f"for {product_name}, but cart contains "
            f"{quantities}."
        )

        print(
            f"Quantity verification successful: "
            f"{expected_quantity}"
        )

        # ==================================================
        # 11. Verify price and cart total
        # ==================================================

        prices = cart_page.get_prices()
        totals = cart_page.get_totals()

        print(
            "Product prices:",
            prices
        )

        print(
            "Cart totals:",
            totals
        )

        assert len(prices) > 0, (
            "Product price was not displayed."
        )

        assert len(totals) > 0, (
            "Cart total was not displayed."
        )

        print(
            "Price and cart total verification successful."
        )

        # ==================================================
        # 12. Final screenshot
        # ==================================================

        take_screenshot(
            driver,
            "05_cart_verification.png"
        )

        # ==================================================
        # 13. Final result
        # ==================================================

        print(
            "\n=============================================="
        )

        print(
            "E-COMMERCE AUTOMATION COMPLETED SUCCESSFULLY"
        )

        print(
            "=============================================="
        )

    except Exception as error:

        # Capture screenshot whenever test fails
        take_screenshot(
            driver,
            "failure_screenshot.png"
        )

        print(
            f"\nTest failed with error: {error}"
        )

        raise