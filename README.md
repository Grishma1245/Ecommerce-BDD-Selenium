 HEAD
# 🛒 E-Commerce BDD Test Suite - SauceDemo

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=flat-square&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Behave](https://img.shields.io/badge/Behave-BDD-E34F26?style=flat-square&logo=cucumber&logoColor=white)](https://behave.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

A robust and professional automated testing suite for the [SauceDemo](https://www.saucedemo.com) e-commerce application. This project utilizes the **Behavior-Driven Development (BDD)** approach with the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability.

A robust and professional automated testing suite for the [SauceDemo]https://www.saucedemo.com e-commerce application. This project utilizes the **Behavior-Driven Development (BDD)** approach with the **Page Object Model (POM)** design pattern to ensure maintainability, scalability, and readability 

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


## ⚙️ Installation

   1. **Set up Virtual Environment 
   ```bash
   python -m venv myenv
   # Windows
   myenv\Scripts\activate
   # macOS/Linux
   source myenv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```



## 📁 Project Structure


ecommerce-bdd-selenium/
├── features/               
│   ├── steps/              
│   └── environment.py      
├── pages/                  
├── utils/                  
├── allure-results/         
├── .github/                
├── requirements.txt        
└── README.md               



## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

