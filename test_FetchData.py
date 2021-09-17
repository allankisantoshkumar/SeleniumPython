from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

def test_fecttest():
    path="E:\\chromeDriver\\chromedriver_win32 (2)\\chromedriver.exe"
    driver=Chrome(executable_path=path)
    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()

    #fetching title
    #print(driver.title)

    #fetch url of the  page
    #print("page url is "+driver.current_url)

    #complete page html
    #print("******************************")
    #print(driver.page_source)


    #how to ready inner text
    #print(driver.find_element_by_class_name("displayPopup").text)

    #Fetching attribute  value
    #print(driver.find_element_by_xpath("//input[contains(@type,'submit')]").get_attribute("value"))


    #work on dropdowns
    obj=Select(driver.find_element_by_name("sex"))
    obj.select_by_index(1)
    print(obj.first_selected_option.text)

    print("***************")

    list=obj.options

    for i in list:
        print(i.text)

