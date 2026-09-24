from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    # ==================================================
    # Cart Page
    # ==================================================

    CART_TITLE = (
        By.XPATH,
        "//li[contains(@class,'active') "
        "and contains(.,'Shopping Cart')]"
    )

    # ==================================================
    # Product Names
    # ==================================================

    CART_PRODUCT_NAMES = (
        By.CSS_SELECTOR,
        ".cart_description h4 a"
    )

    # ==================================================
    # Quantity
    # ==================================================

    CART_QUANTITY_INPUTS = (
        By.CSS_SELECTOR,
        "td.cart_quantity button"
    )

    # ==================================================
    # Product Prices
    # ==================================================

    CART_PRICES = (
        By.CSS_SELECTOR,
        ".cart_price p"
    )

    # ==================================================
    # Product Totals
    # ==================================================

    CART_TOTALS = (
        By.CSS_SELECTOR,
        ".cart_total_price"
    )

    # ==================================================
    # Remove Product
    # ==================================================

    REMOVE_BUTTONS = (
        By.CSS_SELECTOR,
        ".cart_quantity_delete"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ==================================================
    # Verify Cart Page
    # ==================================================

    def verify_cart_page(self):
        """
        Verify that the Shopping Cart page is displayed.
        """

        return self.wait.until(
            EC.visibility_of_element_located(
                self.CART_TITLE
            )
        ).is_displayed()

    # ==================================================
    # Clear Cart
    # ==================================================

    def clear_cart(self):
        """
        Remove all existing products from the cart.

        This makes the test independent of previous runs.
        """

        # Open cart directly
        self.driver.get(
            "https://automationexercise.com/view_cart"
        )

        print(
            "Checking for existing products in cart..."
        )

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.CART_TITLE
                )
            )

        except Exception:
            print(
                "Cart page could not be loaded."
            )
            return

        while True:

            remove_buttons = self.driver.find_elements(
                *self.REMOVE_BUTTONS
            )

            if not remove_buttons:
                break

            print(
                f"Removing {len(remove_buttons)} "
                "existing cart item(s)..."
            )

            remove_buttons[0].click()

            # Wait until the clicked remove button disappears
            try:
                self.wait.until(
                    EC.staleness_of(
                        remove_buttons[0]
                    )
                )
            except Exception:
                pass

        print(
            "Cart is empty and ready for the test."
        )

    # ==================================================
    # Get Product Names
    # ==================================================

    def get_product_names(self):
        """
        Return all product names present in the cart.
        """

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_PRODUCT_NAMES
            )
        )

        return [
            element.text.strip()
            for element in elements
        ]

    # ==================================================
    # Get Quantities
    # ==================================================

    def get_quantities(self):
        """
        Return all product quantities from the cart.
        """

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_QUANTITY_INPUTS
            )
        )

        return [
            element.text.strip()
            for element in elements
        ]

    # ==================================================
    # Get Prices
    # ==================================================

    def get_prices(self):
        """
        Return all product prices from the cart.
        """

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_PRICES
            )
        )

        return [
            element.text.strip()
            for element in elements
        ]

    # ==================================================
    # Get Cart Totals
    # ==================================================

    def get_totals(self):
        """
        Return all product total prices from the cart.
        """

        elements = self.wait.until(
            EC.presence_of_all_elements_located(
                self.CART_TOTALS
            )
        )

        return [
            element.text.strip()
            for element in elements
        ]

    # ==================================================
    # Verify Product and Quantity
    # ==================================================

    def verify_product_and_quantity(
        self,
        product_name,
        expected_quantity
    ):
        """
        Verify that the expected product has
        the expected quantity.
        """

        product_names = self.get_product_names()
        quantities = self.get_quantities()

        if product_name not in product_names:
            return False

        index = product_names.index(
            product_name
        )

        return quantities[index] == str(
            expected_quantity
        )