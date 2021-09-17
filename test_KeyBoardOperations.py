from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  time

def test_keyboard():
    path="E:\\chromeDriver\\chromedriver_win32 (2)\\chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()

    #enter data into text box
    driver.find_element_by_name("fld_username").send_keys("cherryallanki")
    act=ActionChains(driver)
    #act.send_keys(Keys.TAB).perform()
    act.key_down(Keys.CONTROL).send_keys('a').perform()
    act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
    time.sleep(10)
    driver.close()
    driver.quit()


