# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSupervisorProfileFeatures():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_supervisorProfileFeatures(self):
    self.driver.get("http://127.0.0.1:8000/counter/")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.LINK_TEXT, "Password Reset").click()
    self.driver.find_element(By.ID, "id_old_password").send_keys("1a234567")
    self.driver.find_element(By.ID, "id_new_password1").click()
    self.driver.find_element(By.ID, "id_new_password1").send_keys("1a234567")
    self.driver.find_element(By.ID, "id_new_password2").click()
    self.driver.find_element(By.ID, "id_new_password2").send_keys("1a234567")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-outline-info").click()
    self.driver.find_element(By.LINK_TEXT, "Statistics").click()
    self.driver.find_element(By.LINK_TEXT, "Complaints").click()
    self.driver.find_element(By.NAME, "pdf").click()
    self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    self.driver.find_element(By.ID, "sel1").click()
    dropdown = self.driver.find_element(By.ID, "sel1")
    dropdown.find_element(By.XPATH, "//option[. = 'Hostel']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    self.driver.find_element(By.ID, "menu-toggle").click()
    self.driver.find_element(By.ID, "menu-toggle").click()
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").send_keys("fan")
    self.driver.find_element(By.CSS_SELECTOR, ".my-2").click()
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").send_keys("table")
    self.driver.find_element(By.CSS_SELECTOR, ".my-2").click()
    self.driver.find_element(By.LINK_TEXT, "Solved").click()
    self.driver.find_element(By.CSS_SELECTOR, ".my-2").click()
  