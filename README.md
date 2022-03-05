# Todoist test
> Automated BDD test of tasks management app https://todoist.com/app/ created using Behave.

#### Technologies
```
* Python 3.8.10
* Selenium 
```

#### Environment
```
Chrome 98.0.4758.80 
Ubuntu 20.04.3
```

#### Setup
Installing dependencies:
```
pip install -r requirements.txt
```

Getting ChromeDriver:
1. Download the correct version of ChromeDriver from: https://chromedriver.chromium.org/downloads
2. Unzip the file and move it to usr/local/bin
```
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin
```

#### Test overview
Feature 1: Login
```
Scenario 1: Login with valid credentials
Scenario 2: Login with invalid credentials
```
Feature 2: Managing tasks
```
Scenario 1: Add task
Scenario 2: Edit task
Scenario 3: Delete task
```
