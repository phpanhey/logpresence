from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time

def main():       
    with open('config.json', 'r') as file:
        data = json.load(file)                
        for item in data["items"]:            
            driver = webdriver.Chrome()  
            driver.get(data["url"])        
            input_element=driver.find_element(By.XPATH,"//*[@id='mat-input-0']")
            input_element.send_keys(Keys.CONTROL + "a")
            input_element.send_keys(Keys.DELETE)
            input_element.send_keys(item["date"])       

            mat_select = driver.find_element(By.XPATH,"//*[@id='mat-select-0']")
            mat_select.click()
            # Wait for mat-option elements to become visible
            wait = WebDriverWait(driver, 600)
            all_mat_options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option")))
            all_mat_options[int(item["index"])].click()

            submit = driver.find_element(By.XPATH,"/html/body/app-root/app-user/div/form/section[5]/div/button")
            submit.click()

            time.sleep(2)
            driver.close()


if __name__ == "__main__":
    main()
