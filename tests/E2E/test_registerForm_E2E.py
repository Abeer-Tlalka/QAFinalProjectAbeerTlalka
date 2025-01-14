# # Generated by Selenium IDE
# import pytest
# import time
# import json
# import faker
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.support import expected_conditions as EC


# class TestRegisterForm():
#   def setup_method(self, method):
#     self.driver = webdriver.Chrome()
#     self.driver.get("http://localhost:8000/")
#     self.driver.maximize_window()
#     # self.driver.set_window_size(1296, 687)
#     self.vars = {}
  
#   def teardown_method(self, method):
#     self.driver.quit()
  
#   def test_registerWithTokenUser(self):
    
#     self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     self.driver.find_element(By.LINK_TEXT, "Register").click()
#     self.driver.find_element(By.ID, "name").send_keys("user")
#     self.driver.find_element(By.ID, "email").send_keys("marklee@gmail.com")
#     self.driver.find_element(By.ID, "password").send_keys("123123")
#     self.driver.find_element(By.ID, "passwordConfirm").send_keys("123123")
    
#     register_button = self.driver.find_element(By.CSS_SELECTOR, ".mt-3")

#     # Scroll to the element to make sure it's in view
#     self.driver.execute_script("arguments[0].scrollIntoView();", register_button)

#     # Wait until the button is clickable
#     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(register_button))

#     # Use ActionChains to click on the element if it's not clickable directly
#     ActionChains(self.driver).move_to_element(register_button).click().perform()

#     # Wait for the error message to appear
#     WebDriverWait(self.driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".fade"))
#     )

#     # Assert the error message
#     assert self.driver.find_element(By.CSS_SELECTOR, ".fade").text == "User with this email is already registered"
  
  
  
  
#   def test_registerFormPasswordDoesNotMatch(self):
    
#     self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     self.driver.find_element(By.LINK_TEXT, "Register").click()
#     self.driver.find_element(By.ID, "name").send_keys("user")
#     self.driver.find_element(By.ID, "email").send_keys("user@gmail.com")
#     self.driver.find_element(By.ID, "password").send_keys("1234")
#     self.driver.find_element(By.ID, "passwordConfirm").send_keys("123")

#     # Scroll to the register button and ensure it's clickable
#     register_button = self.driver.find_element(By.CSS_SELECTOR, ".mt-3")
#     self.driver.execute_script("arguments[0].scrollIntoView();", register_button)
    
#     # Wait until the button is clickable
#     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(register_button))

#     # Use ActionChains to click the register button
#     ActionChains(self.driver).move_to_element(register_button).click().perform()

#     # Wait for the error message to appear
#     WebDriverWait(self.driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".fade"))
#     )

#     # Assert the error message for mismatched passwords
#     assert self.driver.find_element(By.CSS_SELECTOR, ".fade").text == "Passwords do not match"
  
  
#   #In this function I will use the faker library to generate random data
#   def test_registerCorrectly(self):
    
#     fake = faker.Faker()
#     name=fake.name()

#     self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     self.driver.find_element(By.LINK_TEXT, "Register").click()
#     self.driver.find_element(By.ID, "name").send_keys(name)
#     self.driver.find_element(By.ID, "email").send_keys(fake.email())
#     self.driver.find_element(By.ID, "password").send_keys("123123")
#     self.driver.find_element(By.ID, "passwordConfirm").send_keys("123123")

#     # Scroll to the register button and ensure it's clickable
#     register_button = self.driver.find_element(By.CSS_SELECTOR, ".mt-3")
#     self.driver.execute_script("arguments[0].scrollIntoView();", register_button)

#     # Wait until the button is clickable
#     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(register_button))

#     # Use ActionChains to click the register button
#     ActionChains(self.driver).move_to_element(register_button).click().perform()

#     # Wait for the username to appear after successful registration
#     WebDriverWait(self.driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "username"))
#     )

#     # Assert that the registered username matches the fake generated name
#     assert self.driver.find_element(By.ID, "username").text == name.upper()
    
  
#   def test_registerWithEmptyFill(self):
#       time.sleep(2)
#       self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#       time.sleep(2)
#       self.driver.find_element(By.LINK_TEXT, "Register").click()
#       self.driver.find_element(By.ID, "name").send_keys("")
#       self.driver.find_element(By.ID, "email").send_keys("")
#       self.driver.find_element(By.ID, "password").send_keys("")
#       self.driver.find_element(By.ID, "passwordConfirm").send_keys("")
#       self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()

#        # Wait for the form to be submitted and validation to occur
#       WebDriverWait(self.driver, 10).until(
#           EC.visibility_of_element_located((By.ID, "name"))  # Wait until the form reappears (or use another suitable condition)
#       )

#       # Check that the fields are still showing the required error
#       name_error = self.driver.find_element(By.ID, "name").get_attribute("validationMessage")
#       assert name_error == "Please fill out this field."
