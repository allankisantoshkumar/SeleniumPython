from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import pytest

@pytest.fixture()
def  env_setUp():
    global driver
    path = "E:\\chromeDriver\\chromedriver_win32 (2)\\chromedriver.exe"

    driver = Chrome(executable_path=path)

    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield
    driver.close()


def test_verify_registration(env_setUp):

    #enter data into text box
    driver.find_element_by_name("fld_username").send_keys("cherryallanki")
    driver.find_element_by_name("fld_email").send_keys("allanki@gmail.com")
    driver.find_element_by_name("fld_password").send_keys("cherry")
    driver.find_element_by_name("fld_cpassword").send_keys("abc")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("deetya")
    driver.find_element_by_xpath("//input[@value='home']").click()

    wait = WebDriverWait(driver, 10)
    wait.until(ec.text_to_be_present_in_element((By.NAME,'country'),'India'))
    #work on dropdowns
    obj=Select(driver.find_element_by_name("country"))
    obj.select_by_visible_text("India")

    #select country  from drop down
    wait.until(ec.text_to_be_present_in_element((By.NAME, 'state'), 'Goa'))
    obj = Select(driver.find_element_by_name("state"))
    obj.select_by_visible_text("Goa")

    driver.find_element_by_xpath("//input[@name='terms']").click()

    driver.find_element_by_xpath("//input[@value='Sign up']").click()
