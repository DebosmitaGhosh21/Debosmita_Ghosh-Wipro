from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    # Search product
    SEARCH_INPUT = (
        By.ID,
        "search_product"
    )

    SEARCH_BUTTON = (
        By.ID,
        "submit_search"
    )

    # Search results heading
    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//h2[contains(., 'Searched Products')]"
    )

    # Cart popup
    VIEW_CART_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'modal-content')]"
        "//a[contains(.,'View Cart')]"
    )

    CONTINUE_SHOPPING_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'modal-content')]"
        "//button[contains(.,'Continue Shopping')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ==================================================
    # Open Products Page
    # ==================================================

    def open_products(self):
        """
        Open the Products page directly.
        """

        self.driver.get(
            "https://automationexercise.com/products"
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        print(
            "Products page opened successfully."
        )

    # ==================================================
    # Search Product
    # ==================================================

    def search_product(self, product_name):
        """
        Search for a product using the search box.
        """

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        search_box.clear()

        search_box.send_keys(
            product_name
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCHED_PRODUCTS
            )
        )

        print(
            f"Search completed for: {product_name}"
        )

    # ==================================================
    # Verify Product
    # ==================================================

    def verify_product_visible(self, product_name):
        """
        Verify that the searched product is visible.
        """

        locator = (
            By.XPATH,
            f"//div[contains(@class,'productinfo')]"
            f"//p[normalize-space()='{product_name}']"
        )

        return self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        ).is_displayed()

    # ==================================================
    # Open Product Details
    # ==================================================

    def open_product_details(self, product_name):
        """
        Open the details page of the selected product.
        """

        locator = (
            By.XPATH,
            f"//p[normalize-space()='{product_name}']"
            f"/ancestor::div[contains(@class,'product-image-wrapper')]"
            f"//a[contains(.,'View Product')]"
        )

        element = self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.wait.until(
            EC.element_to_be_clickable(
                locator
            )
        ).click()

        self.wait.until(
            EC.url_contains(
                "/product_details/"
            )
        )

        print(
            f"Opened details for: {product_name}"
        )

    # ==================================================
    # Update Quantity
    # ==================================================

    def update_quantity(self, quantity):
        """
        Set the required product quantity.
        """

        quantity_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "quantity")
            )
        )

        quantity_field.clear()

        quantity_field.send_keys(
            str(quantity)
        )

        print(
            f"Quantity set to: {quantity}"
        )

    # ==================================================
    # Add Product To Cart
    # ==================================================

    def add_product_from_details(self):
        """
        Add the product from its details page to the cart.
        """

        add_button = (
            By.XPATH,
            "//button[contains(.,'Add to cart')]"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                add_button
            )
        ).click()

        print(
            "Product added to cart."
        )

    # ==================================================
    # View Cart
    # ==================================================

    def view_cart(self):
        """
        Click View Cart from the Add to Cart popup.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.VIEW_CART_BUTTON
            )
        ).click()

        print(
            "Opening shopping cart..."
        )

    # ==================================================
    # Continue Shopping
    # ==================================================

    def continue_shopping(self):
        """
        Close the Add to Cart popup and continue shopping.
        """

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_SHOPPING_BUTTON
            )
        ).click()

        print(
            "Continuing shopping..."
        )