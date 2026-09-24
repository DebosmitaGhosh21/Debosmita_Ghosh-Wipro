from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Signup / Login")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_TEXT = (By.XPATH, "//a[contains(., 'Logged in as')]")
    LOGIN_ERROR = (By.XPATH, "//*[contains(text(),'Your email or password is incorrect!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self):
        """Open the Signup/Login page."""
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_LINK)
        ).click()

    def login(self, email, password):
        """Login using supplied credentials."""

        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        ).send_keys(email)

        self.driver.find_element(
            *self.PASSWORD_FIELD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def verify_login_success(self):
        """Verify that the user is logged in."""
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN_TEXT)
        ).is_displayed()