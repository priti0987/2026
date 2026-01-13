from lxml.etree import XPath
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import *
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
now = datetime.now()

# Format the time into a readable string (HH:MM:SS)
start_time = now.strftime("%H:%M:%S")

# Print the current time
print("Current Time =", start_time)

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.accept_insecure_certs = True

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
wait = WebDriverWait(driver, 30)


#Set up the Chrome browser using WebDriver Manager (auto handles driver setup)
# driver = webdriver.Chrome()
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
# #Open a website
# driver.get(url)
# def click(xpathOfElement):
#     element = wait.until(EC.element_to_be_clickable((By.XPATH, xpathOfElement)))
#     # element = driver.find_element(By.XPATH,'//*[@class="btn btn-xs btn-status-dispense"]')
#     driver.execute_script("arguments[0].scrollIntoView((true));", element)
#     element.click()
#     # driver.find_element(By.XPAT
#     # H,xpathOfElement).click()
#     time.sleep(1)
def enterData(xpathOfElement,data):
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpathOfElement)))
        time.sleep(1)
        element.send_keys(data)
    except:
        raise Exception(f"Click failed for xpath: {xpathOfElement}")


#*****************************
def click(xpath):
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(1)
    except Exception as e:
        raise Exception(f"Click failed for xpath: {xpath}")

# # driver.get("https://sos-288.dev.dmerocket.com/Patient/2574/")
driver.get("https://staging.dmerocket.com/Patient/")

#Optional: Maximize the browser window
driver.maximize_window()
time.sleep(2)

driver.find_element(By.NAME,"username").send_keys("priti.b@hashroot.com")
driver.find_element(By.NAME,"password").send_keys("R0cketT3st!")
click("//button[@type='submit']")

click('//*[@id="rocket-modal-btn-cancel"]')
time.sleep(2)
#click on search button
enterData('//*[@id="PatientSearchQuery_MRN"]','MRNQA5418')
click('//*[@class="btn btn-primary btn-xs"]')
#Click on 1st item [row]
click('(//*[@id="patient-search-results"]/tr)[1]')

#open draft order
# draftLink = driver.find_element(By.XPATH,'(//*[text()="Draft"])[1]')

# driver.execute_script("arguments[0].scrollIntoView((true));", draftLink)
#Click on dispense
#    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn-xs btn-status-dispense"]')))
    # element = driver.fin
    # element = driver.find_element(By.XPATH,'//*[@class="btn btn-xs btn-status-dispense"]')
#    driver.execute_script("arguments[0].scrollIntoView((true));", element)
#    time.sleep(1)
#    element.click()
#    time.sleep(1)
    #//*[@name="DateOfService"]
#    click('//*[@class="form-control datepicker valid"]')
#    enterData('//*[@class="form-control datepicker valid"]','01052026')
#    click('//*[@id="rocket-modal-btn-submit"]')

for i in range(15):
    print("............... i =" ,i)
    if i>0:
        # print("scrollup...")
        driver.execute_script("window.scrollTo({top: 0, behavior: 'instant'});")
        time.sleep(1)

    element_createnewOrderele = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn-add btn-xs"]'))
    )
    element_createnewOrderele.click()
    time.sleep(2)
    click('//*[@id="ClientLocationId"]')
    click('(//*[contains(text(),"Hilton Head Island")])[2]')
    click('//*[@id="OrderingProviderId"]')
    click('//option[contains(text(),"Devin Dukes")]')
    click('//*[@id="FitterAccountId"]')
    click('//option[contains(text(),"Akshay Gundigara")]')
    click('//*[@id="FitterAccountId"]')
    click('//*[contains(text(),"Save and Add Products")]')
    enterData('//*[@id="SearchProduct"]','SKU_X')
    click('//*[@id="search-products-button"]')
    click('//*[@id="product-row-7301"]')
    time.sleep(1)
    quantity  = driver.find_element(By.XPATH,'//*[contains(@id,"CartQuantity_")]')
    driver.execute_script("arguments[0].scrollIntoView((true));", quantity)
    time.sleep(1)
    quantity.clear()
    quantity.send_keys('2')
    click('//*[@id="product-details"]')

    enterData('//*[@id="ChargeOut_1"]','1')
    enterData('//*[@id="Allowable_1"]','1')
    enterData('//*[@id="PatientResponsibility_1"]','1')
    enterData('//*[@id="PatientPayment_1"]','1')
    click('(//*[@class="form-check-input responseRadio"])[1]')
    click('//*[@id="nextBtn"]')
    time.sleep(5)
    # #scroll to dispense button
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    # driver.execute_script("window.scrollBy(0, 2000);")

    dispenseButton = driver.find_element(By.XPATH,'//*[@class="btn btn-xs btn-status-dispense"]')
    # driver.execute_script("arguments[0].scrollIntoView((true));", dispenseButton)
    driver.execute_script("window.scrollBy(0, 900);")

    driver.execute_script("""
    arguments[0].scrollIntoView({
        behavior: 'instant',
        block: 'center'
    });
    """, dispenseButton)

    dispenseButton.click()
#    click('//*[@class="btn btn-xs btn-status-dispense"]')
    time.sleep(4)
    datepickerdis = driver.find_element(By.XPATH,'//*[@class="form-control datepicker"]')
    # print(datepickerdis)
    # datepickerdis.click()
    datepickerdis.clear()
    datepickerdis.send_keys('01052026')
    click('//*[@id="rocket-modal-btn-submit"]')
    time.sleep(4)

now = datetime.now()

# Format the time into a readable string (HH:MM:SS)
end_time = now.strftime("%H:%M:%S")

# Print the current time
print("Current Time =", end_time)
