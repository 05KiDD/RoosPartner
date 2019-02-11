from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/KiDD/PycharmProjects/untitled5/venv/Scripts/chromedriver.exe")

driver.implicitly_wait(30)
driver.maximize_window()


driver.get("https://mos.ru/")
a = len(driver.find_elements_by_class_name("today__item"))
if a >= 6:
    print(True)
else:
    print(False)
driver.find_element_by_class_name("today__item").click()
 #driver.document.readyState.interective
driver.find_element_by_class_name("news-app")

driver.close()
driver.quit()