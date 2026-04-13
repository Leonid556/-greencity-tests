import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_tc004_search_event(self):
        self.driver.get('https://www.greencity.cx.ua/#/greenCity/events')
        
        search_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search-input")))
        search_input.clear()
        search_input.send_keys("Eco-picnic\ue007")
        
        event_titles = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-title")))
        
        for title in event_titles:
            self.assertIn("Eco-picnic", title.text)

    def test_tc005_filter_by_location(self):
        self.driver.get('https://www.greencity.cx.ua/#/greenCity/events')
        
        location_dropdown = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".location-dropdown")))
        location_dropdown.click()
        
        kyiv_checkbox = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Kyiv')]")))
        kyiv_checkbox.click()
        
        event_locations = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-location")))
        
        for location in event_locations:
            self.assertIn("Kyiv", location.text)

    def test_tc006_join_event(self):
        self.driver.get('https://www.greencity.cx.ua/#/greenCity')
        
        sign_in_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-in-link")))
        sign_in_btn.click()
        
        email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "email")))
        email_input.send_keys("my_email@example.com")
        
        pass_input = self.driver.find_element(By.ID, "password")
        pass_input.send_keys("myPassword123!\ue007")
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-profile-icon")))
        
        self.driver.get('https://www.greencity.cx.ua/#/greenCity/events/1') 
        
        join_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Join event')]")))
        join_btn.click()
        
        notification = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".snack-bar-success")))
        self.assertTrue(notification.is_displayed())
        
        cancel_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Cancel join')]")))
        self.assertTrue(cancel_btn.is_displayed())

if __name__ == "__main__":
    unittest.main()