import time
import sys
def write_out(filename,word):
  # The 'a' flag tells Python to keep the file contents
  # and append (add line) at the end of the file.
  myfile = open(filename, 'a')

  # Add the line
  myfile.write(word+"\n")

  # Close the file
  myfile.close()

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#for Repl
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')





driver = webdriver.Chrome(options=chrome_options)



#PATH of your executable
#driver = webdriver.Chrome()
driver.get('https://www.mudah.my/Pembantu+am-88630910.htm')
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"__next"))
    )

    #__next > div.mw13.mw4 > div.sc-htoDjs.ktvtLN > div.sc-dnqmqq.dgFJPO > div:nth-child(3)

    #link=main.find_element_by_link_text("Marketing manager / senior marketing")
    
    #link.click()
    

except Exception as e: # work on python 3.x
  print("exception"+ str(e))
  driver.quit()



finally:
  print("The 'try except' is finished")
  #driver.quit()

