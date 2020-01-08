import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC

driver_path_mac = r'/Applications/chromedriver'
driver_path_win = r'C:\develop\chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path_win)
driver.get("http://ics.chinasoftinc.com")
driver.maximize_window()


driver.find_element_by_name("userName").send_keys("185423")

pwdbox = driver.find_element_by_id("password")
ActionChains(driver).click(pwdbox).perform()

driver.find_element_by_id("password").send_keys("zj@19881126")

driver.find_element_by_class_name("button").click()

time.sleep(2)

driver.find_element_by_link_text("新OA(开放区)").click()
time.sleep(2)

# mouse move to "workflow"
current_window1 = driver.current_window_handle
print("current_window1")
# driver.switch_to.window(current_window1)

# Find window
window_all = driver.window_handles
print(window_all)
driver.switch_to.window(window_all[1])

# Mouse move to "Work Flow"
workflow = driver.find_element_by_link_text("工作流程")
ActionChains(driver).move_to_element(workflow).perform()

# Click New Work
driver.find_element_by_link_text("新建工作").click()


frame1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//iframe[@src="/system/core/workflow/flowrun/createNewWork_HuaWei.jsp"]')))

# switch to this frame
driver.switch_to.frame(frame1)


element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "忘打卡申请"))
    )

element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "其他类人事证明申请"))
    )

ActionChains(driver).move_to_element(element2).perform()

element1.click()






