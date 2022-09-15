from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep as tt
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from inbotlist import ppl_to_be_followed


url = "https://www.instagram.com/"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument( "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/jarvis/mycod/chromedriver")
driver = webdriver.Chrome(executable_path="/Users/jarvis/mycod/chromedriver")
print("getting url....")
driver.get(url)
print("url grabbed and loaded !!")
def er(num):
    print(f"something went wrong..... ERROR CODE {num}")

def login_info():
    login_det = ['naman122334','pass1']
    login_det1 = ['nimonimo2324','pass2']
    wait = WebDriverWait(driver,10)
            #################################  ERROR CODE 1  #################################
    try:
        print("logging in ......")
        fill_id = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'f0n8F ')))
        select_all = driver.find_elements(By.CLASS_NAME, "f0n8F ")
        select_all[0].click()
        select_all[0].send_keys(login_det1[0])
    except Exception as error1:
        print(error1)
        er(1) 
            #################################  ERROR CODE 2  #################################
    try:
        fill_id = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'f0n8F ')))
        select_all = driver.find_elements(By.CLASS_NAME, "f0n8F ")
        select_all[1].click()
        select_all[1].send_keys(login_det1[1])
        print("details filled..")

    except Exception as error2:
        print(error2)
        er(2) 
            #################################  ERROR CODE 3  #################################
    try:
        clik_submit = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
        clik_submit.submit()
        print("logged in !!")

    except Exception as error3:
        print(error3)
        er(3) 

def dialog_go():
    wait = WebDriverWait(driver,10)
            #################################  ERROR CODE 4  #################################
    try:
        print("getting rid of dialog boxes 1 and 2")

        if wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='Not now']" ))):
            find_dialog = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Not now']" )))
            find_dialog.click()
            print("dialog box 1 gone !!")
        else:
            pass     
        find_dialog = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='Not Now']" )))
        find_dialog.click()
        print("dialog box 2 gone !!")
    except Exception as error4:
        print(error4)
        er(4) 

def search_follow(ids):
    
    wait = WebDriverWait(driver,10)
    for id1 in ids:
        print(f"trying to search and follow {id1} ")
            #################################  ERROR CODE 5  #################################
        try:
            search_id = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
            search_id.send_keys(id1)
            tt(3)
            search_id.send_keys(Keys.ENTER)
            tt(3)
            search_id.send_keys(Keys.ENTER)
        except Exception as error5:
            print(error5)
            er(5) 

                #################################  ERROR CODE 6  #################################
        try:
            # scrolldown=driver.execute_script("window.scrollTo(0, 4000);")
            # scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
            # # match=False
            # # while(match==False):
            # #     last_count = scrolldown
            # #     tt(3)
            # #     scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
            # # if last_count==scrolldown:
            # #     match=True      
            tt(5)
            follow1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button' )))
            follow = driver.find_elements(By.CSS_SELECTOR,"button")
            follow[1].click()
            tt(2)
            
            
        except Exception as error6:
            print(error6)
            er(6) 

def search_like_most_recent_post(ids):
    wait = WebDriverWait(driver,10)
    for id1 in ids:
        print(f"trying to search and like most recent post of {id1} ")
                #################################  ERROR CODE 7  #################################
        try:
            search_id = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
            search_id.send_keys(id1)
            tt(3)
            search_id.send_keys(Keys.ENTER)
            tt(2)
            search_id.send_keys(Keys.ENTER)
        except Exception as error7:
            print(error7)
            er(7) 
    
                #################################  ERROR CODE 8  #################################
        try:
            follow1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button' )))
            follow1.send_keys(Keys.PAGE_DOWN)
            tt(1)
            find_pic = driver.find_elements(By.TAG_NAME, "div[class='v1Nh3 kIKUG _bz0w']")
            find_pic[0].click()
            tt(1)
            like_pic = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")))
            like_pic.click()
            tt(1)
            close_pic = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[1]/button")))
            close_pic.click()
        except Exception as error8:
            print(error8)
            er(8) 



login_info()
dialog_go()
search_follow(ppl_to_be_followed)
list_of = ["to_be_followed"]
search_like_most_recent_post(list_of)
driver.quit()
print("work done !!!")

