# User Guide 

## C2 UI Checks Automation
### Prerequisites
  Before you begin, ensure you have the following installed on your system:
1. **Python** (version 3.6 or later)
2. **pip** (Python package installer)
3. **GRL_C2_BROWSER_APP**

## Step 1: Install Selenium WebDriver
  Selenium WebDriver is a powerful tool for controlling web browsers through programs and 
performing browser automation.

  Installation: Open your terminal or command prompt and run the following command:
  >> pip install selenium
  Verification: To verify the installation, you can run a simple script to check if Selenium is 
  working:

  1.Create a Python Script:
  Open your preferred text editor or IDE (such as VS Code, PyCharm, or any text editor).

  2.Write the Script:
-------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
driver = webdriver.Chrome
driver.get("https://www.google.com")
print("Page title:", driver.title)
driver.quit() 
print("Selenium is successfully imported and working.")
--------------------------------------------------------------------------------------------------------------------------
  
  3.Save and Run the Script:
  • Save the script with a .py extension, for example, selenium_test.py.
  • Now run selenium_test.py.
  • If Selenium is imported correctly and the WebDriver launches Chrome and accesses 
  Google, you should see output similar to:
--------------------------------------------------------------------------------------------------------------------------
Page title: Google
--------------------------------------------------------------------------------------------------------------------------
Selenium is successfully imported and working.

Make sure you have the appropriate WebDriver for your browser in the directory:
“UI Checks Automation\Resources\chromedriver-win64\chromedriver.exe”.
For example, if you're using Chrome, download the ChromeDriver from here.

## Step 2: Install PyYAML
Open your terminal or command prompt and run the following command:
>> pip install PyYAML
PyYAML is a YAML parser and emitter for Python.

## Step 3: Install Logging
Open your terminal or command prompt and run the following command:
>>pip install logging
Logging is a module for Python that provides a flexible framework for emitting log messages 
from Python programs.

## Step 4: Changing the mode
In the directory “UI Checks Automation\json\setting.json”, update the following fields in the 
YAML File:
1. Mode: If the Tester is "C2", set the mode to "C2". If the Tester is "C2 EPR", set the 
mode to "C2EPR".
2. DynamicIP: Update the IP address as needed. (ex. 192.168.5.17)
3. Static_dynamic: Modify this field based on how the tester is connected to the 
computer. (ex. Static or Dynamic).
