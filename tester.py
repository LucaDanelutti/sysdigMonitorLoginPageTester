import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "http://app.sysdigcloud.com/"
TRANSITION_TIMEOUT = 10

# Super class that handles setup and teardown
class SysdigMonitorTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, TRANSITION_TIMEOUT)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# Checks the page title
class Title(SysdigMonitorTestCase):
    def test_title(self):
        driver = self.driver
        driver.get(URL)
        self.assertIn("Sysdig Monitor", driver.title)

# Checks if the browser is redirected to a secure connection
class HttpsRedirect(SysdigMonitorTestCase):
    def test_https_redirect(self):
        driver = self.driver
        driver.get(URL)
        self.assertIn("https", driver.current_url)

# Checks if the login form works as expected
class Login(SysdigMonitorTestCase):
    def test_failed_login(self):
        driver = self.driver
        wait = self.wait
        driver.get(URL + "#/login")
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-login")))
        
        username_box = driver.find_element(By.NAME, "username")
        self.assertEqual("", username_box.text)
        username_box.send_keys("a@a.com")

        password_box = driver.find_element(By.NAME, "password")
        self.assertEqual("", password_box.text)
        password_box.send_keys("a")
        
        log_in_button = driver.find_element(By.CLASS_NAME, "simple-btn--login")
        log_in_button.click()

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "login__error-display")))

        error_box = driver.find_element(By.CLASS_NAME, "login__error-display")
        self.assertIn("Credentials are not valid", error_box.text)

    def test_wrong_username_format(self):
        driver = self.driver
        wait = self.wait
        # TODO

    def test_empty_username(self):
        driver = self.driver
        wait = self.wait
        # TODO

    def test_empty_password(self):
        driver = self.driver
        wait = self.wait
        # TODO

# Checks if the "Forgot your passowrd?" link works
class ForgotPasswordLink(SysdigMonitorTestCase):
    def test(self):
        driver = self.driver
        wait = self.wait
        driver.get(URL + "#/login")
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-login")))
        
        forgot_password = driver.find_element(By.CLASS_NAME, "login__link")
        forgot_password.click()

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-forgot-password")))
        self.assertIn("forgotPassword", driver.current_url)

# Checks if the "Changed your mind? Login!" link works
class LoginLink(SysdigMonitorTestCase):
    def test(self):
        driver = self.driver
        wait = self.wait
        driver.get(URL + "#/forgotPassword")
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-forgot-password")))
        
        login = driver.find_element(By.CLASS_NAME, "login__link")
        login.click()

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-login")))
        self.assertIn("login", driver.current_url)

# Checks if the region selector works
# Default one is us_east (app.sysdigcloud.com)
class SwitchRegion(SysdigMonitorTestCase):
    # Checks whether pressing a region option works (see test_switch_region_eu1, test_switch_region_us_east, test_switch_region_us_west, test_switch_region_ap)
    def switch_region(self, region_element, region_name):
        driver = self.driver
        wait = self.wait
        driver.get(URL)
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-authentication-form")))
        
        dropdown_menu = driver.find_element(By.CLASS_NAME, "reactsel__dropdown-indicator")
        dropdown_menu.click()

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "reactsel__menu-list")))
        region = driver.find_element(By.XPATH, region_element)
        region.click()
        self.assertIn(region_name, driver.current_url)

    def test_switch_region_eu1(self):
        self.switch_region("/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[1]", "eu1.app.sysdig.com")

    def test_switch_region_us_east(self):
        self.switch_region("/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[2]", "app.sysdigcloud.com")

    def test_switch_region_us_west(self):
        self.switch_region("/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[3]", "us2.app.sysdig.com")

    def test_switch_region_ap(self):
        self.switch_region("/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[4]", "app.au1.sysdig.com")

    # Checks the default region
    def test_default(self):
        driver = self.driver
        wait = self.wait
        driver.get(URL)
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-authentication-form")))
        
        self.assertIn("app.sysdigcloud.com", driver.current_url)

    # Checks whether the current region menù option is selected
    def test_us_east_is_selected(self):
        driver = self.driver
        wait = self.wait
        driver.get(URL)
        
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "block-authentication-form")))
        
        dropdown_menu = driver.find_element(By.CLASS_NAME, "reactsel__dropdown-indicator")
        dropdown_menu.click()

        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "reactsel__menu-list")))
        region = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[2]")
        self.assertIn("reactsel__option--is-selected", region.get_attribute("class"))
        

if __name__ == "__main__":
    # Run all the tests
    unittest.main()