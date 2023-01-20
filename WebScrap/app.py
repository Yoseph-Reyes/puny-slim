from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def webs(url): 
    
    # configure webdriver
    operadriver = "chromedriver.exe"
    options = Options()
    options.binary_location = 'chromedriver.exe'
    options.headless = True  # hide GUI
    
    #options.add_argument("start-maximized")  # ensure window is full-screen

    ...
    # configure chrome browser to not load images and javascript
    chrome_options = webdriver.ChromeOptions()

    ...

    driver = webdriver.Chrome(operadriver, options=options, chrome_options=chrome_options )
    #                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    WebDriverWait(driver, timeout=10)
    driver.minimize_window()
    driver.maximize_window()
    
    driver.get(url)

    pb = driver.find_elements(By.XPATH, ".//*")
    lista = list()
    x = 0
   
    for p in pb:
        if str(p.tag_name) == 'input' or str(p.tag_name) == 'select' or str(p.tag_name) == 'textarea' or str(p.tag_name) == 'button' :
            x+=1
            #print (x)
            
            lista.append([x,p.tag_name,p.get_attribute('type'),p.get_attribute('id'),str(p.get_attribute('class')).split(" ")])
            if x > 100:
                break
            if lista == None:
                lista.appen("no hay formularios en la pagina")
        else:
            continue

    driver.quit()
    print (lista)   
    return lista