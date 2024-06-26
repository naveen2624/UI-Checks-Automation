import json
import time
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import logging
import os
import inspect
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

def read_file(path):
    with open(path, "r") as rf:
        values = json.load(rf)
    return values

Xpath = read_file('json/Xpath.json')
setting = read_file('json/setting.json')

ElementXpath = Xpath['Xpath']
Element=setting['Mode']

def get_exe_yaml():
    exe_yaml_dict()
    messages_dict = exe_yaml_dict()
    return messages_dict

def exe_yaml_dict():
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = current_path + "\\Resource\\resources.yaml"
    print(file_path)
    yaml_dict = {}
    if os.path.exists(file_path):
        with open(file_path, "r") as resource_yaml_fh:
            yaml_dict = yaml.safe_load(resource_yaml_fh)
    else:
        err_msg = "Specified file {} does not exist ".format(file_path)
        raise Exception(err_msg)
    return yaml_dict

def yaml_msg(value):
    config = get_exe_yaml()
    message = config[value]
    return message


def tc1_check_readme_file():
    logging.info("*************** TC-1 ***************")
    logging.info("Check the ReadMe File is present")
    # directory_path = r"C:\GRL\USBPD-C2-Browser-App"
    # Set the path to the directory
    if Element == "C2":
        directory_path = r"C:\GRL\USBPD-C2-Browser-App"
    else:
        directory_path = r"C:\GRL\USBPD-C2-Browser-App"

    # Check if the ReadMe file exists in the directory
    readme_path = os.path.join(directory_path, "ReadMe.txt")

    try:
        if os.path.exists(readme_path):
            logging.info(f"The ReadMe file was found in the directory at: {readme_path}")
        else:
            raise FileNotFoundError(f"The ReadMe file was not found in the directory at: {directory_path}")
    except FileNotFoundError as e:
        logging.error(f"An error occurred: {str(e)}")


def tc2_check_release_file():
    logging.info("*************** TC-2 ***************")
    logging.info("Check the Release Notes File is present")

    # Set the path to the directory
    if Element == "C2":
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\Firmware_Files\C2"
        release_notes_path = os.path.join(directory_path, "ReleaseNotes.txt")
    else:
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\Firmware_Files\C2 EPR"
        release_notes_path = os.path.join(directory_path, "ReleaseNotes.txt")

    try:
        if os.path.exists(release_notes_path):
            logging.info(f"The Release Notes was found in the directory at: {release_notes_path}")
        else:
            raise FileNotFoundError(f"The Release Notes was not found in the directory at: {directory_path}")
    except FileNotFoundError as e:
        logging.error(f"An error occurred: {str(e)}")
        

def tc3_check_eload_file():
    logging.info("*************** TC-3 ***************")
    logging.info("Check the Eload File is present")
    if Element=="C2":
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\EloadFWupdate" 
        pps_eload_path = os.path.join(directory_path, "ELOADFW_PORT1.cpp.bin")       
    else:
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\C2EPR_FWupdate"
        pps_eload_path = os.path.join(directory_path, "_Eload.txt")
        
    try:
        if os.path.exists(pps_eload_path):
            logging.info(f"Eload File was found in the directory at: {pps_eload_path}")
        else:
            raise FileNotFoundError(f"Eload file is not found in the directory at: {directory_path}")
    except FileNotFoundError as e:
        logging.error(f"An error occurred: {str(e)}")
      
        

def tc4_check_firmware_file():
    logging.info("*************** TC-4 ***************")
    logging.info("Check all the Firmware Files are present")
    
    if Element=="C2":
        # Set the path to the directory
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\Firmware_Files\C2"
    else:
        directory_path = r"C:\GRL\USBPD-C2-Browser-App\Firmware_Files\C2 EPR"
    # List of files to check
    files_to_check = ["BOOT.BIN", "image.ub", "start.sh"]

    try:
        missing_files = []

        # Check if each file exists in the directory
        for file_name in files_to_check:
            file_path = os.path.join(directory_path, file_name)
            if not os.path.exists(file_path):
                missing_files.append(file_name)

        # Print missing files
        if missing_files:
            logging.info("The following files are missing:")
            for file_name in missing_files:
                logging.error(file_name)
        else:
            logging.info(f"All files are present{files_to_check}.")
    except FileNotFoundError as e:
        logging.error(f"An error occurred: {str(e)}")
        
def initialize_browser(driver_setup):
    try:
        driver_setup.get(Xpath['URL'])
        driver_setup.maximize_window()
        logging.info("The browser has been successfully opened, and the page has landed on the connection setup page.")
    except WebDriverException as e:
        logging.error(f"The attempt to open the browser failed: {str(e)}")
        raise



def tc5_open_browser(driver_setup):
    logging.info("*************** TC-5 ***************")
    logging.info("Check the Browser is opens")
    
    
    try:
        initialize_browser(driver_setup)
        # Add additional steps if needed after browser initialization
    except Exception as e:
        logging.error(f"{str(e)}")



def tc6_browser_tab_title(driver_setup):
    logging.info("*************** TC-6 ***************")
    logging.info("Browser Tab Title")
    time.sleep(4)
    try:
        actual_title = BrowserTitle(driver_setup)
        
        expected_title = yaml_msg("TITLE")
        

        if actual_title == expected_title:
            logging.info(f"The browser title in the UI tab is: {actual_title}")
        else:
            logging.critical(
                f"The browser title in the UI tab Value is Mismatched. Actual Value: {actual_title}, Expected Value: {expected_title}")
            
        time.sleep(5)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

def BrowserTitle(driver_setup):
    act_title = driver_setup.title
    return act_title


def tc7_scannetwork_enablestate(driver_setup):
    logging.info("*************** TC-7 ***************")
    logging.info("Check that the Scan Network Button is present and whether it's clickable or not")


    try:
        # Use the WebDriver to find the button element
        button_elements = driver_setup.find_elements(By.XPATH, ElementXpath['scanbutton'])
        # Check if the button is available
        if button_elements:
            logging.info("The Scan Network button is visible on the UI.")
            # Select the first button element from the list (assuming there's only one)
            button_element = button_elements[0]
            
            # Check if the button is clickable
            if button_element.is_displayed() and button_element.is_enabled():
                logging.info("The Scan Network button is clickable.")
            else:
                logging.critical("The Scan Network button is not clickable at the moment.")
        else:
            logging.critical("The Scan Network button is not visible on the UI.")
            
    except NoSuchElementException as e:
        logging.error(f"Element not found: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        logging.info(ElementXpath['scanbutton'])



def tc8_scanNetworkstate(driver_setup):
    logging.info("*************** TC-8 ***************")
    logging.info("Check that after clicking the Scan network button, the loading icon is visible, and the connect button should be disabled, and vice versa")
    
    input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])
    # Click on the input element to focus it
    input_element.click()
    time.sleep(3)
    # Select all text in the input field and delete it
    input_element.send_keys(Keys.CONTROL + "a")  # Select all text
    input_element.send_keys(Keys.DELETE)  # Delete the selected text
    # Enter the new IP 
    in_valid = "192.168.255.1"
    input_element.send_keys(in_valid)
    time.sleep(3)
    button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
    button_element.click()
    time.sleep(5)
    try:
        pass_or_fail = "Pass"
        # Find the "Scan Network" and "Connect" buttons
        scan_button = driver_setup.find_element(By.XPATH,  ElementXpath['scanbutton'])
        connect_button = driver_setup.find_element(By.XPATH, ElementXpath['connect_button'])

        # Click the "Scan Network" button
        scan_button.click()

        # Define a wait for the loading icon to appear
        wait = WebDriverWait(driver_setup, 40)  # Adjust the timeout as needed

        # Wait for the loading icon to appear
        try:
            loading_icon = wait.until(EC.visibility_of_element_located((By.XPATH, ElementXpath['loading_icon'])))
            
            # Check if the "Connect" button is disabled
            if not connect_button.is_enabled():
                logging.info("'Connect' button is disabled as expected")
                pass
            else:
                logging.error("Error: 'Connect' button is not disabled as expected.")
            
        except Exception as e:
            logging.error("Loading icon did not appear within the specified time or is not visible.")
        # Wait for the loading icon to disappear
        try:
            wait.until_not(EC.visibility_of_element_located((By.XPATH, ElementXpath['loading_icon'])))
            logging.info("Loading icon has disappeared")
            
            # Check if the "Connect" button is enabled
            if connect_button.is_enabled():
                logging.info("'Connect' button is enabled as expected.")
                pass
            else:
                logging.error("Error: 'Connect' button is not enabled as expected.")

        except Exception as e:
            logging.error("Loading icon did not disappear within the specified time or is still visible.")

    except Exception as e:
        # If OpenBrowser raises an exception, it's a fail
        logging.error(f" The Scan Network button not visible on the UI: {str(e)}")




def tc9_devicedetails(driver_setup):
    logging.info("*************** TC-9 ***************")
    logging.info("Please ensure that the device details keys are correctly present on the connection setup page")
    pass_or_fail = "Pass"
    remark = ""
    method_name = inspect.currentframe().f_code.co_name
    
    try:
        if setting['Mode']=="C2":
            elements_to_check = {
                'Tester_status': 'expected_tester_status',
                'Serial_Number': 'expected_serial_number',
                'Firmware_version': 'expected_firmware_version',
                'Tester_IP_Address_Information': 'expected_tester_ip_address',
                'Last_calibration_date': 'expected_last_calibration_date',
                'Next_calibration_date': 'expected_next_calibration_date',
                'Test_cable_calibration_status': 'expected_test_cable_calibration_status',
                'C2_tester_calibration': 'expected_C2_tester_calibration'
            }
        else:
            elements_to_check = {
                'Tester_status': 'expected_tester_status',
                'Serial_Number': 'expected_serial_number',
                'Firmware_version': 'expected_firmware_version',
                'Tester_IP_Address_Information': 'expected_tester_ip_address',
                'Last_calibration_date': 'expected_last_calibration_date',
                'Next_calibration_date': 'expected_next_calibration_date',
                'Test_cable_calibration_status': 'expected_test_cable_calibration_status',
                'C2-EPR_Tester_Calibration': 'expected_C2_EPR_tester_calibration'
            }
        logging.info("Expected Values : Browser Values")

        for element_locator, expected_value_key in elements_to_check.items():
            element = driver_setup.find_element(By.XPATH, ElementXpath[element_locator])
            actual_value = element.text
            
            # Log the values with logger information
            logging.info(f"{element_locator.replace('_', ' ').title()}: {actual_value}")

            # Add assert statements to check the values
            assert actual_value == yaml_msg(expected_value_key), f"{element_locator.replace('_', ' ').title()} mismatch: Expected '{yaml_msg(expected_value_key)}', but got '{actual_value}'"

    except Exception as e:
        logging.error(f"An exception occurred: {str(e)}")
        raise e




def tc10_addressText(driver_setup):
    logging.info("*************** TC-10 ***************")
    logging.info("Verify the address Text")

    pass_or_fail = "Pass"
    remark = ""

    try:
        time.sleep(2)
        # Find the element by its CSS selector
        element = driver_setup.find_element(By.XPATH, ElementXpath['AddressText'])

        # Get the text content of the element
        element_text = element.text

        if Element == 'C2':
            desired_text = yaml_msg('IP_Address_Title_C2')
        else:
            # Get the desired text based on the Element variable
            desired_text_key = "IP_Address_Title_C2_EPR"
            desired_text = yaml_msg(desired_text_key)

        # Check if the desired text is present in the element's text
        if desired_text == element_text:
            logging.info(f"Desired text '{desired_text}' is present.")
        else:
            logging.error(f"Desired text '{desired_text}' is not present.")

    except NoSuchElementException as e:
        logging.error(f"Element not found: {str(e)}")

    except Exception as e:
        pass_or_fail = "Fail"
        remark = f"An unexpected error occurred: {str(e)}"
        logging.error(f"An unexpected error occurred: {str(e)}")




def tc11_defaultIp(driver_setup):
    logging.info("*************** TC-11 ***************")
    
    logging.info("Clicking the scan network, verify default IP is present in the C2 IP Address input box and connect")
    check = setting["tester_connected"]
    check1 = setting["static_dynamic"]
    if check == True:
        if check1 == "Static":
            try:
                ip = 'DefaultIP'
                elements = driver_setup.find_elements(By.CSS_SELECTOR, ElementXpath['Ipdropdown'])
                element_req = None
                for element in elements:
                    ip_element = element.find_element(By.TAG_NAME,ElementXpath['option'])
                    ip_address = ip_element.get_attribute('value')
                    Defaultip = yaml_msg("Defaultip")
                    if ip_address == Defaultip:
                        element_req = element
                logging.info(f"The Default IP is :{Defaultip}")
                if element_req is not None:  # Check if element_req is assigned
                    time.sleep(2)
                    element_req.click()   
                connected = False
                while not connected:
                    try:
                        # Try to find the image element using the provided XPath
                        element = driver_setup.find_element(By.XPATH, ElementXpath["connection_status"])
                        connection_status = element.text
                        # If the Tester status is connected
                        if connection_status=="Connected":
                            connected = True
                            logging.info("Tester is connected with Default IP")

                    except Exception as e:
                        try:
                            # If the image is not found, try to click the button
                            button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
                            button_element.click()
                            #print("Clicked the connection setup button")
                            time.sleep(7)
                            # You can add additional logic here if needed after clicking the button
                            
                        except Exception as e:
                            # If both the image and button are not found, print a message and wait before trying again
                            logging.info("c2 is not connected, retrying...")
                            time.sleep(5)  # Adjust the sleep duration as needed

            except Exception as e:
                # If OpenBrowser raises an exception, it's a fail
                logging.error(f"DefaultIp failed with error: {str(e)}")
            # Get the calling method's name using inspect
        else:
            logging.info("Tester is not connected with Default IP so the test is get skipped")
            
    else:
        logging.info("Tester is not connected so the test is get skipped")



def tc12_dynamicIp(driver_setup):
    logging.info("*************** TC-12 ***************")
    logging.info("Verify Connection with Dynamic IP and Verify the Tester Status")
    remark = ""
    try:
        check = setting["tester_connected"]
        check1 = setting["static_dynamic"]
        if check == True:
            if check1 == "Dynamic":
                # Find the input element using its class name
                input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])

                # Click on the input element to focus it
                # input_element.click()

                # Select all text in the input field and delete it
                # input_element.clear()

                # Enter the new IP
                in_valid = setting["DynamicIP"]
                input_element.send_keys(Keys.CONTROL + "a")  # Select all text
                input_element.send_keys(Keys.DELETE)  # Delete the selected text
                time.sleep(5)
                input_element.send_keys(in_valid)
                # # Click the connection setup button
                button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
                button_element.click()

                connected = False
                while not connected:
                    try:
                        #Check for the Tester status 
                        element = driver_setup.find_element(By.XPATH, ElementXpath["connection_status"])
                        connection_status = element.text
                        # If the Tester status is connected
                        if connection_status=="Connected":
                            logging.info(f"Tester is connected with Dynamic IP '{in_valid}'")
                            break


                    except NoSuchElementException:
                        try:
                            # If the Tester status is not connected, try to click the button
                            button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
                            button_element.click()
                            time.sleep(15)
                        except NoSuchElementException:
                            # If both the image and button are not found, print a message and wait before trying again
                            remark = "c2 is not connected, retrying..."
                            logging.info(remark)
                            time.sleep(5)  # Adjust the sleep duration as needed

                time.sleep(5)
                # TesterStatus(driver_setup, ip)
                time.sleep(5)
                # pass_or_fail, remark = check_license(driver_setup)
            
            else:
                logging.info("Tester is not connected with Dynamic IP so the test is get skipped")

        else:
            logging.info("Tester is not connected, so the test is skipped")

    except Exception as e:
        remark = f"An unexpected error occurred: {str(e)}"
        logging.error(remark)




def tc13_invalidIP(driver_setup):
    logging.info("*************** TC-13 ***************")
    logging.info("Pass Invalid IP Address and Verify the Tester Status")
    driver_setup.refresh()

    try:
        remark = ""

        # Find the input element using its class name
        input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])

        # # Click on the input element to focus it
        input_element.click()

        # # Select all text in the input field and delete it
        input_element.clear()
        
        # Enter the new IP "1.1.1"
        in_valid = yaml_msg("invalid")
        input_element.send_keys(Keys.CONTROL + "a")  # Select all text
        input_element.send_keys(Keys.DELETE)  # Delete the selected text
        time.sleep(2)
        input_element.send_keys(in_valid)
        logging.info(f"Entered invalid IP: {in_valid}")

        time.sleep(2)
        # Click the connection setup button
        driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton']).click()
        time.sleep(3)
        element = driver_setup.find_element(By.XPATH, ElementXpath["connection_status"])
        connection_status = element.text
        # If the Tester status is connected
        if connection_status!="Connected":
            connected = True
            logging.info("Tester is not connected")


        # Additional wait if needed
        time.sleep(3)


    except Exception as e:
        # If OpenBrowser raises an exception, it's a fail
        remark = str(e)
        logging.error(f"InvalidIP failed with error: {remark}")



def tc14_unreachableIP(driver_setup):
    logging.info("*************** TC-14 ***************")
    logging.info("Pass Unreachable IP Address and Verify the Tester Status")
    
    try:
        remark = ""

        # Find the input element using its class name
        input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])

        # Click on the input element to focus it
        input_element.click()

        # Select all text in the input field and delete it
        input_element.clear()

        # Enter the new IP "192.168.255.2"
        un_reach = yaml_msg("unreach")
        input_element.send_keys(Keys.CONTROL + "a")  # Select all text
        input_element.send_keys(Keys.DELETE)  # Delete the selected text
        time.sleep(2)
        input_element.send_keys(un_reach)
        logging.info(f"Entered unreachable IP: {un_reach}")

        # Click the connection setup button
        driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton']).click()
        time.sleep(3)
        element = driver_setup.find_element(By.XPATH, ElementXpath["connection_status"])
        connection_status = element.text
        # Wait for the connection off image to appear
        if connection_status !="Connected":
            logging.info("Tester is not connected")

        # Additional wait if needed
        time.sleep(3)


    except Exception as e:
        # If OpenBrowser raises an exception, it's a fail
        remark = str(e)
        logging.error(f"UnreachableIP failed with error: {remark}")
        

def tc15_ImageCompare(driver_setup): 
    logging.info("*************** TC-15 ***************")
    logging.info("Verify the Setup Diagram")

    try:
        driver_setup.find_element(By.XPATH, ElementXpath['SetupDiagram_button']).click()
        time.sleep(5)
        image_element = driver_setup.find_element(By.XPATH, ElementXpath['SetupDiagram_image'])
        if image_element.is_displayed():
            logging.info("Setup Diagram is Displayed")
            time.sleep(5)
            driver_setup.find_element(By.XPATH, ElementXpath['imageok']).click()
        else:
            logging.error("Setup Diagram is not Displayed")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        

def tc16_sw_hw_details(driver_setup):
    logging.info("*************** TC-16 ***************")
    logging.info("Please ensure that the software and hardware details keys are correctly present on the connection setup page")
    driver_setup.refresh()
    input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])

    # Enter the new IP
    in_valid = setting["DynamicIP"]
    input_element.send_keys(Keys.CONTROL + "a")  # Select all text
    input_element.send_keys(Keys.DELETE)  # Delete the selected text
    time.sleep(2)
    input_element.send_keys(in_valid)
    ## Click the connection setup button
    button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
    button_element.click()
    time.sleep(2)
    try:
        elements_to_check =['Tester.IP.Address.Information','Serial.Number','Firmware.Version']
        time.sleep(2)
        for element_locator in elements_to_check:
            
            element = driver_setup.find_element(By.XPATH, ElementXpath[element_locator])
            actual_value = element.text
            
            # Log the values with logger information
            logging.info(f"{element_locator.replace('.', ' ').title()}: {actual_value}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

    
    
def tc17_updatefirmwarebutton(driver_setup):
    logging.info("*************** TC-17 ***************")
    logging.info("Check that the Firmware Update Button is present and whether it's clickable or not")
    driver_setup.refresh()
    try:
        # Use the WebDriver to find the button element
        button_elements = driver_setup.find_elements(By.XPATH, ElementXpath['FW_updatebutton'])
        # Check if the button is available
        if button_elements:
            logging.info("The Firmware Update button is visible on the UI.")
            # Select the first button element from the list (assuming there's only one)
            button_element = button_elements[0]
            
            # Check if the button is clickable
            if button_element.is_displayed() and button_element.is_enabled():
                logging.info("The Firmware Update button is clickable.")
            else:
                logging.critical("The Firmware Update button is not clickable at the moment.")
        else:
            logging.critical("The Firmware Update button is not visible on the UI.")
            
    except NoSuchElementException as e:
        logging.error(f"Element not found: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        logging.info(ElementXpath['FW_updatebutton'])
    
    
    
def tc18_updatefirmware(driver_setup):
    logging.info("*************** TC-18 ***************")
    logging.info("Check that the Firmware Update Button is clicked and the Tester is Restarted")
    input_element = driver_setup.find_element(By.CLASS_NAME, ElementXpath['Iptextbox'])
    # Click on the input element to focus it
    input_element.click()
    time.sleep(3)
    # Select all text in the input field and delete it
    input_element.send_keys(Keys.CONTROL + "a")  # Select all text
    input_element.send_keys(Keys.DELETE)  # Delete the selected text
    # Enter the new IP 
    in_valid = setting["DynamicIP"]
    input_element.send_keys(in_valid)
    time.sleep(3)
    button_element = driver_setup.find_element(By.XPATH, ElementXpath['Connectbutton'])
    button_element.click()
    time.sleep(5)
    try:
        driver_setup.find_element(By.XPATH, ElementXpath['FW_updatebutton']).click()
        time.sleep(8)
        image_element = driver_setup.find_element(By.XPATH, ElementXpath['FW_updatediagram'])
        if image_element.is_displayed():
            logging.info("Firmware Update Setup Diagram is Displayed")
            time.sleep(5)
            driver_setup.find_element(By.XPATH, ElementXpath['imageok']).click()
            time.sleep(30)
            try:
                element=driver_setup.find_element(By.XPATH, ElementXpath['FWupdate_status'])
                update_status=element.text
                expected_update_status= yaml_msg("successful_fwupdate")
                expected_update_unsuccesful_status= yaml_msg("Unsuccessful_fwupdate")
                if update_status==expected_update_status:
                    logging.info("Tester Updated Successfully and Restarted")
                elif update_status==expected_update_unsuccesful_status:
                    logging.error("Tester Update was Unsuccessfull. Please ensure that the USB cable for firmware update is connected and power cycle the C2 controller and retry.")
                else:
                    logging.error(f"Firmware Update was Unsuccessful: {update_status}")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {str(e)}")
                
        else:
            logging.error("Firmware Update Setup Diagram is not Displayed")
        
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    