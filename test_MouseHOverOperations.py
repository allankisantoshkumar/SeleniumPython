from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_mouse():
    path="E:\\chromeDriver\\chromedriver_win32 (2)\\chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com")
    driver.maximize_window()

    act=ActionChains(driver)
    #time.sleep(3)
    #act.click().perform()
    #time.sleep(10)
    #act.context_click().perform()

    #clickOperation
    #act.click(driver.find_element_by_xpath("//*[text()='Login']")).perform()


    #contxtclick(rightclick)
    #act.context_click().perform()
    #act.context_click(driver.find_element_by_xpath("//*[text()='Login']")).perform()

    #double  click
    #act.double_click(driver.find_element_by_xpath("//*[text()='Login']")).perform()

    #mouse over event
    act.move_to_element(driver.find_element_by_xpath("//*[contains(@title,'TUTORIAL')]")).perform()
    act.move_to_element(driver.find_element_by_xpath("//*[contains(@title,'MANUAL TESTING')]")).perform()

