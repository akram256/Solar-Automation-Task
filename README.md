# Solar-Automation-Task
Interview Quesion


Project Structure
mobile_e2e/:
Contains automated end-to-end tests for mobile platforms using Appium and related frameworks. These tests validate the functionality of the WikiApp on mobile devices.

page_objects/:
Houses the Page Object Model (POM) classes for the web juice app. Each class encapsulates the locators and methods for a specific page or feature, promoting code reusability and maintainability.

web_e2e/:
Includes the main test cases for both web. These tests interact with the page_objects to perform validations and assertions.

utilities/:
Contains helper utilities such as custom loggers, environment configurations, or reusable methods that support test execution.

Exploratory Testings for the basic functions...:
A document outlining exploratory testing approaches and scenarios for assessing the core functionalities of the WikiApp.

Test Plan.pdf:
A detailed test plan document specifying the testing objectives, scope, strategies, and execution timeline.

WikiApp Exploration Testing.pdf:
A comprehensive report on the exploratory testing results and insights.

requirements.txt:
A file listing all Python dependencies required to run the tests.

Getting Started
Follow the steps below to set up and run the tests:

Prerequisites
Python 3.8 or above
pip (Python package installer)
Node.js (for Appium)
Google Chrome (for web tests)
Android/iOS Simulator or Device (for mobile tests)
JDK 8 or later (for Appium)

Installation
Clone the repository:
git clone <repository_url>
cd <repository_folder>

Set up a Python virtual environment:
python3 -m venv venv
source venv/bin/activate  # Linux/Mac

Install dependencies:
pip install -r requirements.txt
Install Appium globally (for mobile tests):
npm install -g appium

Download the appropriate WebDriver (e.g., ChromeDriver) using webdriver-manager:
pip install webdriver-manager

How to Run the Tests
Web Tests
Start the WebDriver:

Ensure the browser and WebDriver versions match.
chromedriver --port=9515

Run the test suite:

pytest tests/ --browser chrome
Mobile Tests

Start Appium:

appium
Connect your mobile device or simulator.

Run mobile tests:
pytest mobile_e2e/

View Test Reports
Use pytest-html for generating reports:

pytest --html=report.html --self-contained-html
Open report.html in a browser to review the results.

Contact
For any queries or contributions, contact Akram Mukasa at [mukasaakram55@gmail.com].