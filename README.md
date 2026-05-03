# 🏦 Banking UI Test Suite

Automated UI test suite for [Guru99 Bank Demo](https://demo.guru99.com/v4/) built with **Python + Playwright + Pytest**.

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python 3.11 | Core language |
| Playwright | Browser automation |
| Pytest | Test framework |
| Page Object Model | Design pattern |
| GitHub Actions | CI/CD pipeline |

## 📁 Project Structure
```
banking-ui-test-suite/
├── pages/                  # Page Object Model classes
│   ├── login_page.py
│   └── new_customer_page.py
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_new_customer.py
│   └── test_deposit.py
├── .github/workflows/
│   └── ci.yml             # GitHub Actions CI pipeline
├── conftest.py            # Shared Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Dependencies
└── README.md
```

## Setup & Run

# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest

# Run with HTML report
pytest --html=reports/report.html --self-contained-html
```

## ✅ Test Coverage

| Module | Test Cases |
|--------|-----------|
| Login | Valid login, blank fields, invalid credentials, reset |
| New Customer | Add customer, field validations (name, PIN, email) |
| Deposit | Account number and amount validations |

## 🔁 CI/CD
Tests run automatically on every push and pull request via **GitHub Actions**.
