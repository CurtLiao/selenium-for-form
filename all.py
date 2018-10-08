
# coding: utf-8

# In[16]:


from selenium import webdriver
from scrapy.selector import Selector
import random
import time

def myfun():
    time.sleep(1)
    #page1
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div > content > span').click()



    girlboy = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div','#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div']
    age = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
	       '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(7) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    ageplay = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
              '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			  '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			  '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			  '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			  '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			  '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(7) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    job = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
	       '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(7) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(8) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(9) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(10) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(11) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    isMarried = [
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
			'#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    money = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
	         '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    edu = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
	       '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
		   '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
	]
    time.sleep(2)
    #page 2
    driver.find_element_by_css_selector(random.choice(girlboy)).click()
    driver.find_element_by_css_selector(random.choice(age)).click()
    driver.find_element_by_css_selector(random.choice(ageplay)).click()
    driver.find_element_by_css_selector(random.choice(job)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    #page3
    driver.find_element_by_css_selector(random.choice(money)).click()
    driver.find_element_by_css_selector(random.choice(edu)).click()
    driver.find_element_by_css_selector(random.choice(isMarried)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()


    times = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
            ]
    price = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
             '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'  
            ]
    #page4
    driver.find_element_by_css_selector(random.choice(times)).click()
    driver.find_element_by_css_selector(random.choice(price)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(2)
    #page5
    p51 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p52 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    p53 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
          ]
    p54 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
          ]
    p55 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
          ]
    p56 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    driver.find_element_by_css_selector(random.choice(p51)).click()
    driver.find_element_by_css_selector(random.choice(p52)).click()
    driver.find_element_by_css_selector(random.choice(p53)).click()
    driver.find_element_by_css_selector(random.choice(p54)).click()
    driver.find_element_by_css_selector(random.choice(p55)).click()
    driver.find_element_by_css_selector(random.choice(p56)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(2)
    #page6
    p61 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div' ,
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]

    p62 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',  ]

    p63 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]


    p64 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]

    p65 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]

    p66 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]
    driver.find_element_by_css_selector(random.choice(p61)).click()
    driver.find_element_by_css_selector(random.choice(p62)).click()
    driver.find_element_by_css_selector(random.choice(p63)).click()
    driver.find_element_by_css_selector(random.choice(p64)).click()
    driver.find_element_by_css_selector(random.choice(p65)).click()
    driver.find_element_by_css_selector(random.choice(p66)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
    #page7
    p71 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p72 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p73 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p74 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p75 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p76 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p77 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]

    driver.find_element_by_css_selector(random.choice(p71)).click()
    driver.find_element_by_css_selector(random.choice(p72)).click()
    driver.find_element_by_css_selector(random.choice(p73)).click()
    driver.find_element_by_css_selector(random.choice(p74)).click()
    driver.find_element_by_css_selector(random.choice(p75)).click()
    driver.find_element_by_css_selector(random.choice(p76)).click()
    driver.find_element_by_css_selector(random.choice(p77)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
	#page8
    p81 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',  
    ]


    p82 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]

    p83 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]


    p84 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]

    p85 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',]

    p86 =['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
          '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
    ]
    driver.find_element_by_css_selector(random.choice(p81)).click()
    driver.find_element_by_css_selector(random.choice(p82)).click()
    driver.find_element_by_css_selector(random.choice(p83)).click()
    driver.find_element_by_css_selector(random.choice(p84)).click()
    driver.find_element_by_css_selector(random.choice(p85)).click()
    driver.find_element_by_css_selector(random.choice(p86)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
    #page9

    p91 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p92 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p93 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p94 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    driver.find_element_by_css_selector(random.choice(p91)).click()
    driver.find_element_by_css_selector(random.choice(p92)).click()
    driver.find_element_by_css_selector(random.choice(p93)).click()
    driver.find_element_by_css_selector(random.choice(p94)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
    #page10
    p101 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p102 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer'
        ]
    p103 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p104 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    driver.find_element_by_css_selector(random.choice(p101)).click()
    driver.find_element_by_css_selector(random.choice(p102)).click()
    driver.find_element_by_css_selector(random.choice(p103)).click()
    driver.find_element_by_css_selector(random.choice(p104)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
    #page11
    p111 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    p112 = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
            '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div',
           '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div.quantumWizTogglePaperradioRadioContainer > div'
        ]
    driver.find_element_by_css_selector(random.choice(p111)).click()
    driver.find_element_by_css_selector(random.choice(p112)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    time.sleep(1)
    #last
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div.quantumWizButtonEl.quantumWizButtonPaperbuttonEl.quantumWizButtonPaperbuttonFlat.quantumWizButtonPaperbuttonDark.quantumWizButtonPaperbutton2El2.freebirdFormviewerViewNavigationSubmitButton > content > span').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/div[3]/a').click()
    text = '%s %d %s' % ('剩下 ', timsss - (i+1), ' 次')
    print(text)
    time.sleep(1)
    
# In[17]:
'''
timsss = 200
chrome_path = "D:\chromedriver.exe"
url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform'
driver = webdriver.Chrome(chrome_path) #chromedriver         
driver.get(url)
'''
while True:
    timsss = 200
    chrome_path = "D:\chromedriver.exe"
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform'
    driver = webdriver.Chrome(chrome_path) #chromedriver         
    driver.get(url)
    try:
        for i in range(timsss):
            myfun()
    except:
        chrome_path = "D:\chromedriver.exe"
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform'
        driver = webdriver.Chrome(chrome_path) #chromedriver         
        driver.get(url)
        for i in range(timsss):
            myfun()
    print("洪毓謙小朋友 做完囉><")
    driver.quit()
   

