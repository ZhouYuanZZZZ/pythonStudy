import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'/Applications/chromedriver'

driver = webdriver.Chrome(executable_path=driver_path)
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
driver.find_element_by_link_text("忘打卡申请").click()


# Find iframe_page
#Frame1 = driver.find_element_by_xpath('//*[@id="tabs-content"]/iframe[1]')

# switch to this frame
# frame2 = driver.find_element_by_tag_name("iframe")
# print(frame2)

#driver.switch_to.frame(Frame1)

# click Forget_to_Punch_Card Application
# driver.find_element_by_link_text("忘打卡申请").click()
#driver.find_element_by_xpath('//*[@id="wf_list_12"]/li[2]/a').click()

print(Frame1.find_e)




