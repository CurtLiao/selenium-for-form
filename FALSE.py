
# coding: utf-8

# In[16]:


from selenium import webdriver
from scrapy.selector import Selector
import random
import time


# In[17]:
timsss = 100
chrome_path = "C:\chromedriver.exe"
url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform'
driver = webdriver.Chrome(chrome_path) #chromedriver         
driver.get(url)
for i in range(timsss):
    
    time.sleep(1)
    #page1
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div > content > span').click()

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div/div/div[2]/content/span').click()
    time.sleep(1)
    driver.find_element_by_css_selector('body > div > div.freebirdFormviewerViewCenteredContent > div.freebirdFormviewerViewFormCard.exportFormCard > div.freebirdFormviewerViewResponseConfirmContentContainer > div.freebirdFormviewerViewResponseLinksContainer > a').click()
    
    text = '%s %d %s' % ('剩下 ', timsss - (i+1), ' 次')
    print(text)
    time.sleep(1)
print("yoyo 心平氣和 yoyo check it out yo><")
driver.quit()

