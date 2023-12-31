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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1536, 816)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "id_username").send_keys("Salim")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("1a234567")
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-muted .btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ml-2 > .btn").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("1a234567")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group > .btn").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
