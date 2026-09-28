# PROJECT REPORT

## Capstone Assignment 1: Automate a Web Application Using Selenium WebDriver with Python

### 1. Project Title

E-Commerce Web Application Automation Using Selenium WebDriver with Python



## 2. Introduction

Software testing is an important part of the software development lifecycle. Automation testing helps reduce manual effort, improve test execution speed, increase test coverage, and provide repeatable results.

This project demonstrates the automation of an e-commerce web application using **Selenium WebDriver with Python**. The application selected for automation is **Automation Exercise**, a practice e-commerce website designed for testing purposes.

The automation script performs a complete customer purchase flow, beginning with opening the application and logging in, followed by searching for a product, adding it to the cart, setting the required quantity, and verifying the cart details.

The project also demonstrates important Selenium concepts such as **Page Object Model (POM), explicit waits, locators, screenshots, exception handling, test data management, pytest, and HTML test reporting**.



## 3. Objectives

The main objectives of this project are:

1. To automate an e-commerce web application using Selenium WebDriver.
2. To implement the automation using Python.
3. To automate the login functionality.
4. To search for a specific product.
5. To open the product details page.
6. To update the product quantity.
7. To add the product to the shopping cart.
8. To verify the product and quantity in the cart.
9. To verify product prices and cart totals.
10. To capture screenshots during test execution.
11. To read test data from a JSON file.
12. To implement explicit waits for reliable synchronization.
13. To handle browser alerts when present.
14. To generate an HTML execution report.
15. To organize the automation framework using the Page Object Model.



## 4. Application Under Test

**Application:** Automation Exercise

**URL:** https://automationexercise.com/

The application provides an e-commerce environment containing features such as:

* User registration and login
* Product listing
* Product search
* Product details
* Shopping cart
* Quantity management
* Product prices
* Cart totals

The application was selected because it provides a suitable environment for demonstrating end-to-end Selenium automation.



## 5. Technologies and Tools Used

| Technology / Tool  | Purpose                        |
| ------------------ | ------------------------------ |
| Python             | Programming language           |
| Selenium WebDriver | Browser automation             |
| Pytest             | Test execution framework       |
| Chrome             | Browser used for testing       |
| Selenium Manager   | Automatic WebDriver management |
| JSON               | Test data storage              |
| VS Code            | Development environment        |
| HTML Report        | Test execution reporting       |
| Git                | Version control                |
| GitHub             | Source code repository         |



## 6. System Requirements

### Hardware Requirements

* Computer/Laptop
* Minimum 4 GB RAM
* Internet connection

### Software Requirements

* Windows operating system
* Python 3.x
* Google Chrome
* Visual Studio Code
* Selenium
* Pytest



## 7. Project Structure

The project is organized using a Page Object Model-based structure.

```text
Capstone_Project/
│
├── Demo_video/
│   └── Selenium_Capstone_Demo.mp4
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── test_ecommerce.py
│
├── test_data/
│   └── test_data.json
│
├── screenshots/
│   ├── 01_home_page.png
│   ├── 02_login_success.png
│   ├── 03_product_search.png
│   ├── 04_product_added.png
│   └── 05_cart_verification.png
│
├── reports/
│   └── test_report.html
│
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
└── .gitignore
```


## 8. Page Object Model

The project follows the **Page Object Model (POM)** design pattern.

Each major page or functionality is represented by a separate Python class.

### LoginPage

The `login_page.py` file contains the locators and methods related to login.

It handles:

* Opening the login page
* Entering email
* Entering password
* Clicking the login button
* Verifying successful login

### ProductPage

The `product_page.py` file handles product-related operations.

It performs:

* Opening the Products page
* Searching for a product
* Verifying the product
* Opening product details
* Updating quantity
* Adding the product to the cart
* Opening the shopping cart

### CartPage

The `cart_page.py` file handles shopping-cart operations.

It performs:

* Opening/verifying the cart
* Clearing existing cart items
* Reading product names
* Reading quantities
* Reading prices
* Reading cart totals
* Verifying the expected product and quantity

This structure improves code organization and makes the framework easier to maintain.

---

## 9. Test Data Management

Test data is stored separately in a JSON file.

Example:

```json
{
    "url": "https://automationexercise.com/",
    "login_email": "YOUR_TEST_EMAIL",
    "login_password": "YOUR_TEST_PASSWORD",
    "product_name": "Blue Top",
    "quantity": 2
}
```

Separating test data from the automation code makes the test easier to modify and maintain.

For example, the product or quantity can be changed in the JSON file without modifying the main test logic.

---

## 10. Configuration Management

The `config.py` file is responsible for loading the JSON test data and defining important project paths.

It uses Python's `pathlib` module to create paths for:

* Test data
* Screenshots
* Output files

This avoids hard-coded machine-specific paths and improves portability.



## 11. Test Scenario

The main automated test follows this sequence:

```text
Launch Browser
      ↓
Open Application
      ↓
Verify Homepage
      ↓
Login
      ↓
Clear Existing Cart
      ↓
Open Products
      ↓
Search "Blue Top"
      ↓
Verify Product
      ↓
Open Product Details
      ↓
Set Quantity = 2
      ↓
Add Product to Cart
      ↓
Open Shopping Cart
      ↓
Verify Product
      ↓
Verify Quantity
      ↓
Verify Price and Total
      ↓
Capture Screenshot
      ↓
Test Passed
```



## 12. Detailed Test Execution

### Step 1: Launch Browser

Selenium WebDriver launches Google Chrome.

The browser window is maximized before the test begins.

### Step 2: Open Application

The test navigates to:

```text
https://automationexercise.com/
```

The page title is also verified to ensure that the application has loaded successfully.

### Step 3: Login

The test opens the login page and enters the configured email and password.

The login button is clicked and the test verifies the presence of the **Logged in as** text.

A screenshot is captured after successful login.

### Step 4: Clear Existing Cart

Before adding a new product, the automation checks the shopping cart and removes previously existing products.

This is important because the website can preserve cart contents between executions. Clearing the cart makes each test run independent and prevents quantities from accumulating across multiple runs.

### Step 5: Open Products Page

The automation navigates to the Products page and waits until the product search field becomes visible.

### Step 6: Search Product

The product name:

```text
Blue Top
```

is read from the JSON test data.

The product name is entered into the search field and the search button is clicked.

The test verifies that the searched product is displayed.

### Step 7: Open Product Details

The automation identifies the required product and opens its product details page.

An explicit wait is used to ensure that the page has loaded before continuing.

### Step 8: Update Quantity

The quantity field is located using its element ID.

The existing value is cleared and the required quantity is entered.

In this test:

```text
Expected Quantity = 2
```

### Step 9: Add Product to Cart

The **Add to cart** button is located and clicked.

The automation then proceeds to the shopping cart.

### Step 10: Verify Shopping Cart

The test verifies that the Shopping Cart page is displayed.

It retrieves the product names from the cart and verifies that:

```text
Blue Top
```

is present.

### Step 11: Verify Quantity

The quantity displayed in the cart is retrieved and compared with the expected quantity.

Expected:

```text
2
```

The test passes only when the actual quantity matches the expected quantity.

### Step 12: Verify Price and Total

The automation reads:

* Product price
* Cart total

The test verifies that these values are displayed successfully.

### Step 13: Capture Screenshots

Screenshots are captured at important stages of the test:

1. Homepage
2. Successful login
3. Product search
4. Product added to cart
5. Cart verification

A failure screenshot is also captured if an exception occurs during execution.



## 13. Explicit Waits

The project uses Selenium's `WebDriverWait` with expected conditions.

Examples include:

* `visibility_of_element_located`
* `element_to_be_clickable`
* `presence_of_element_located`
* `url_contains`
* `alert_is_present`

Explicit waits are used instead of relying only on fixed delays.

This improves synchronization between the automation script and the web application.



## 14. Exception Handling

Exception handling is implemented in the test script to make the automation more robust.

If an unexpected error occurs:

1. A failure screenshot is captured.
2. The error is printed.
3. The exception is raised again so that pytest correctly marks the test as failed.

The WebDriver is also closed in the `finally` block.

This ensures that browser resources are properly released after execution.



## 15. Alert Handling

The project includes a function for handling browser alerts.

The automation waits briefly for an alert. If an alert appears, its text is displayed and the alert is accepted.

If no alert is present, the test continues normally.

This allows the framework to handle optional JavaScript alerts without unnecessarily failing the test.



## 16. Test Execution

The test is executed using pytest.

Command:

```bash
pytest -v src/test_ecommerce.py
```

The `-v` option provides verbose information about the test execution.

For HTML reporting, the following command is used:

```bash
pytest -v src/test_ecommerce.py --html=reports/test_report.html --self-contained-html
```



## 17. Expected Test Result

A successful execution produces a result similar to:

```text
1 passed
```

The test confirms that the complete e-commerce purchase flow has executed successfully.

The successful flow includes:

* Application launch
* Login
* Cart cleanup
* Product search
* Product verification
* Quantity update
* Add to cart
* Cart verification
* Price and total verification



## 18. Test Evidence

The project captures screenshots as evidence of successful execution.

### Screenshot 1 – Homepage

Shows the Automation Exercise homepage after successful application launch.

### Screenshot 2 – Login Success

Shows the application after successful user login.

### Screenshot 3 – Product Search

Shows the searched product, **Blue Top**.

### Screenshot 4 – Product Added

Shows the product after it has been added to the shopping cart.

### Screenshot 5 – Cart Verification

Shows the shopping cart with the expected product and quantity.



## 19. HTML Test Report

An HTML test report is generated using the pytest HTML reporting plugin.

The report provides information about:

* Test name
* Test status
* Execution result
* Test duration
* Environment information





## 20. Challenges Encountered and Solutions

### Challenge 1: Page title was initially empty

The browser sometimes returned an empty title immediately after navigation.

**Solution:** An explicit wait was added until the page title became available.



### Challenge 2: Products page synchronization

The Products navigation element was not consistently ready for interaction.

**Solution:** The test navigates directly to the Products URL and waits for the search field to become visible.



### Challenge 3: Product details locator

The product details button required a more specific locator.

**Solution:** An XPath based on the product name and product container was used.



### Challenge 4: Cart quantity locator

The initial quantity locator did not correctly identify the quantity displayed in the cart.

**Solution:** The cart quantity button was identified using:

```text
td.cart_quantity button
```



### Challenge 5: Cart quantity increased between test runs

The website retained previously added products. Therefore, running the test repeatedly caused the quantity to accumulate.

**Solution:** A `clear_cart()` method was implemented. It removes existing cart products before starting the main purchase flow.

This makes the test more independent and repeatable.



## 21. Advantages of the Automation Framework

The developed framework provides several benefits:

* Reduces manual testing effort
* Provides repeatable test execution
* Improves test consistency
* Uses reusable Page Object classes
* Separates test data from test logic
* Provides screenshots as execution evidence
* Handles synchronization using explicit waits
* Provides automated pass/fail results
* Generates an HTML test report
* Can be extended with additional test cases



## 22. Future Enhancements

The framework can be improved further by adding:

1. Multiple test cases.
2. Parameterized testing with multiple products.
3. Excel-based test data.
4. Cross-browser testing.
5. Logging using Python's logging module.
6. CI/CD integration using GitHub Actions.
7. Better environment configuration.
8. Additional negative test cases.
9. Automated email/report notifications.
10. Integration with a test management system.



## 23. Conclusion

This project successfully demonstrates the automation of an end-to-end e-commerce workflow using **Selenium WebDriver with Python and pytest**.

The automation covers application launch, login, product search, product selection, quantity update, cart management, and verification of cart details.

The implementation uses the **Page Object Model**, explicit waits, JSON-based test data, screenshots, exception handling, alert handling, and HTML reporting.

The project provides practical experience in designing a maintainable Selenium automation framework and demonstrates how repetitive web application testing can be automated to improve efficiency, consistency, and reliability.



## 24. Final Deliverables

The completed project contains:

* Selenium automation source code
* Page Object Model classes
* JSON test data
* Screenshots
* HTML execution report
* Project documentation
* Screen-recording demonstration
* Requirements file
* GitHub repository

The project is therefore ready for submission as a complete Selenium WebDriver automation capstone.
