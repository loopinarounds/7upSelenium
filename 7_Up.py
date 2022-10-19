from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import ProxyType, Proxy
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

if __name__ == '__main__':

#How to add options to a Chrome Browser... (ie. Headless + No-Images)

    option = webdriver.ChromeOptions()
    chrome_prefs = {}
    option.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

    # option.add_argument("--headless")

    ## Use CTRL + / to comment blocks of code...

    # Proxy data...
    # proxy_ip = '104.45.128.122:80'
    # proxy = Proxy()
    # proxy.proxy_type = ProxyType.MANUAL
    # proxy.http_proxy = proxy_ip
    # proxy.ssl_proxy = proxy_ip
    #
    # # linking proxy and setting up driver
    # capabilities = webdriver.DesiredCapabilities.CHROME
    # proxy.add_to_capabilities(capabilities)

    # Setting up browser...
    s = Service("C:\Program Files (x86)\chromedriver.exe")

    # web = webdriver.Chrome(service=s,options=option,desired_capabilities=capabilities) # For proxy use, we add desired capabilities.
    web = webdriver.Chrome(service=s,options=option)

    # Website Link...
    web.get("https://7up.co.uk/moments")

    WebDriverWait(web,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="truste-consent-button"]'))).click()

    # Switching to an iframe... (Find label of iframe)
    web.switch_to.frame("iframe")

    fname = web.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("George")
    lname = web.find_element(By.XPATH,'//*[@id="lastName"]').send_keys("Lopez")
    email = web.find_element(By.XPATH,'//*[@id="email"]').send_keys("pmygl6@nottingham.ac.uk")
    c_email = web.find_element(By.XPATH,'//*[@id="emailConfirm"]').send_keys("pmygl6@nottingham.ac.uk")
    phone = web.find_element(By.XPATH,'//*[@id="telephoneNumber"]').send_keys("07421237853")


    WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ajaxForm"]/div/div[6]'))).click()
    WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.searchResult [data-text = "Aberdeenshire"]'))).click()

    dropdown1 = Select(web.find_element(By.ID,'store'))
    dropdown1.select_by_visible_text('Tesco')

    WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ajaxForm"]/div/div[8]/div[1]/div/a'))).click()
    WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ajaxForm"]/div/div[9]/div[1]/div/a'))).click()

    # Good for avoiding interception...
    web.execute_script("arguments[0].click();", WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajaxForm"]/div/div[12]/button'))))

    try:
        WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH,'// *[ @ id = "content"] / div[1] / p')))
        result = web.find_element(By.XPATH,'// *[ @ id = "content"] / div[1] / p')
        print(result.text)
        web.close()
    except:
        try:
            WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/h2')))
            ans = web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/h2').text
            print(ans)
            web.switch_to.default_content()
            web.close()
        except:
            print('Winner!')

