# 🪙 Smart Currency Converter

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

A lightweight, real-time command-line Currency Converter built with Python. It fetches live, dynamic exchange rates globally using the ExchangeRate-API to deliver precise currency conversions instantly based on USD as the base currency.

---

## ✨ Features

* 🔄 **Live Exchange Rates**: Fetches real-time financial data directly from a third-party REST API.
* 🌍 **Dynamic Input**: Supports major global currency codes (e.g., PKR, INR, EUR, GBP).
* 🔠 **Case Insensitive**: Automatically normalizes user input to handle both lowercase and uppercase inputs.
* ⚙️ **Robust Flow**: Validates API response status codes before parsing JSON payloads.

---

## 📸 Screenshots

### CLI Execution Preview

![Application Screenshot](./assets/screenshot.png)

> **Note**: If you are running it locally, the terminal output will look like this:
```text
write your currency: PKR
write amount: 100
27850.0
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8 or higher installed on your machine. You will also need to install the HTTP library for Python.

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory**:
   ```bash
   cd smart-currency-converter
   ```
3. **Install dependencies**:
   ```bash
   pip install requests
   ```

### Running the Application
Execute the script via your terminal or command prompt:
```bash
python main.py
```

---

## 🛠️ Tech Stack & Concepts Used

* **Language**: Python 3
* **Libraries**: `requests` (for handling HTTP GET requests)
* **API Integration**: REST API interaction with JSON response parsing
* **Data Handling**: Manipulating nested dictionaries to extract key-value pairs dynamically

---

## 🤝 Contributing

Contributions are welcome! If you want to improve this project:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🔗 Connect With Me

If you have any questions, feedback, or want to discuss DevOps and programming, feel free to reach out:

* 📺 **YouTube**: [CodeGhar001](https://youtube.com) — Subscribe for tech tutorials and insights!
* 📸 **Instagram**: [@saqibrashid.devops](https://instagram.com) — Drop a DM for collaborations or queries!
