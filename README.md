# banking-ui-test-suite
A production-style UI Test Automation Framework built with Python, Playwright, and Pytest, targeting a BFSI (Banking, Financial Services &amp; Insurance) domain web application. This project demonstrates real-world QA automation skills including framework design, test case structuring, and CI/CD integration.

Purpose
This project was built to simulate the kind of automated testing done in enterprise banking environments. It covers critical user flows such as login authentication, customer onboarding, and financial transactions — the same modules tested in real banking applications used by GCCs and product companies.
Architecture
The framework follows the Page Object Model (POM) design pattern, which separates the UI interaction logic from the test logic. This makes the codebase clean, reusable, and easy to maintain as the application grows. Each web page of the application has its own dedicated Python class that handles locators and actions, while the test files focus purely on assertions and test scenarios.
What Is Tested
The suite covers three core banking modules:

Login Module — Valid credentials, invalid credentials, blank field validations, and reset functionality
New Customer Module — Successful customer registration along with validations for name, PIN code, email format, and numeric input restrictions
Deposit Module — Account number validations and amount field error handling

A total of 13+ test cases are written following standard QA naming conventions with clear test IDs for traceability.
