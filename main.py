from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
username = ""
password = ""
def launchBrower(username, password):

    chrome_driver_path = "C:/Users/linyi/chromedriver"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3426410897&f_AL=true&keywords=software%20engineer&refresh=true")

    sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
    sign_in_button.click()

    email_field = driver.find_element(By.ID,"username")
    email_field.send_keys( username )
    password_field = driver.find_element(By.ID,"password")
    password_field.send_keys( password)
    password_field.send_keys(Keys.ENTER)
    print("login success")
 
    all_listings = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

   
    print("all listings::::::::", all_listings)
    # all_listings = driver.find_elements(By.XPATH, "//ul[@class='jobs-search__results-list']/li")
    clickables = 0
    unclickables = 0
    counter = 0
    print("Number of listings found:", len(all_listings))
    for listing in all_listings:
        actions = ActionChains(driver)
        actions.move_to_element(listing).click().perform()
        # print(listing)
        # counter+=1
        # print(counter)
        # if listing.is_enabled() and listing.is_displayed():
        #     print("Clickable listing found:", listing.text)
        #     # clickables += 1
        #     # listing.click()
        #     # time.sleep(5)
        #     # driver.back()
        # else:
        #     # unclickables += 1
        #     print("Non-clickable listing found:", listing.text)
    
    # print("Total clickable listings:", clickables)
    # print("Total non-clickable listings:", unclickables)
    # for listing in all_listings:
    #     job_title = driver.find_element(By.CLASS_NAME, "topcard__title").text
    #     company_name = driver.find_element(By.CLASS_NAME, "topcard__org-name-link").text
    #     location = driver.find_element(By.CLASS_NAME, "topcard__flavor").text
    #     job_description = driver.find_element(By.CLASS_NAME, "show-more-less-html__markup").get_attribute("innerHTML")

    #     # Print the details
    #     print("Job title:", job_title)
    #     print("Company name:", company_name)
    #     print("Location:", location)
    #     print("Job description:", job_description)
    #     # print("called")
    #     # listing.click()
    #     # print(listing)
    #     # time.sleep(2)

    print(all_listings)
    while True:
        pass

launchBrower(username, password)