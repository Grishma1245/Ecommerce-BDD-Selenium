<<<<<<< HEAD
# 🛒 E-Commerce BDD Test Suite - SauceDemo

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=flat-square&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Behave](https://img.shields.io/badge/Behave-BDD-E34F26?style=flat-square&logo=cucumber&logoColor=white)](https://behave.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

A robust and professional automated testing suite for the [SauceDemo](https://www.saucedemo.com) e-commerce application. This project utilizes the **Behavior-Driven Development (BDD)** approach with the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability.
=======
A robust and professional automated testing suite for the [SauceDemo]https://www.saucedemo.com e-commerce application. This project utilizes the **Behavior-Driven Development (BDD)** approach with the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability.
>>>>>>> f473ce653b0a1f9c292c70f11cb9dfd687ad81f0

---

## 🚀 Key Features

- **BDD Approach**: Human-readable test scenarios written in Gherkin (.feature files).
- **Page Object Model (POM)**: Enhances code reusability by separating page actions from test logic.
- **Automated Workflows**:
  - ✅ **Login**: Valid and invalid credential validation.
  - ✅ **Inventory Management**: Adding/removing items from the cart.
  - ✅ **Checkout Flow**: Complete end-to-end purchasing process.
  - ✅ **Logout**: Securely ending sessions.
- **Reporting**: Integration with **Allure Reports** for visually stunning and detailed test results.
- **Global Configuration**: Easily manageable configurations via utility scripts.

---

## 🛠️ Technology Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Programming Language |
| **Selenium WebDriver** | Web Browser Automation |
| **Behave** | BDD Framework (Gherkin syntax) |
| **WebDriver Manager** | Automatic browser driver handling |
| **Allure Behave** | Test reporting and visualization |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.11+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (or any other modern browser)
- [Allure Command-Line](https://docs.qameta.io/allure/#_installing_a_command_line) (for report generation)

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
<<<<<<< HEAD
   git clone https://github.com/Grishma1245/selenium-testing.git
=======
   git clone https://github.com/Grishma1245/Ecommerce-BDD-Selenium
>>>>>>> f473ce653b0a1f9c292c70f11cb9dfd687ad81f0
   cd ecommerce-bdd-selenium
   ```

2. **Set up Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv myenv
   # Windows
   myenv\Scripts\activate
   # macOS/Linux
   source myenv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🏃 Running Tests

### Execute All Tests
Simply run the following command to execute all feature files:
```bash
behave
```

### Execute Specific Features
```bash
behave features/login.feature
```

---

## 📊 Reports (Allure)

This project is integrated with Allure for professional reporting.

1. **Run Tests with Allure Formatter**
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o allure_results/
   ```

2. **Generate and Open Report**
   ```bash
   allure serve allure_results/
   ```

---

## 📁 Project Structure

```text
ecommerce-bdd-selenium/
├── features/               # BDD Feature files (.feature)
│   ├── steps/              # Python step definitions
│   └── environment.py      # Hooks (Before/After scenarios)
├── pages/                  # Page Object Model (POM) classes
├── utils/                  # Utility functions and configurations
├── allure-results/         # Raw test results for Allure
├── .github/                # CI/CD workflows
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Pull requests are the best way to suggest changes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---