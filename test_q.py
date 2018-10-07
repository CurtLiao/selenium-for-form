
# coding: utf-8

# In[16]:


from selenium import webdriver
from scrapy.selector import Selector
import random


# In[17]:


for i in range(20):
    chrome_path = "C:\chromedriver.exe"
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform'
    driver = webdriver.Chrome(chrome_path) #chromedriver         
    driver.get(url)

    #page1
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div > content > span').click()



    girlboy = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div','#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div']
    age = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div','#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div']


    #page 2
    driver.find_element_by_css_selector(random.choice(girlboy)).click()
    driver.find_element_by_css_selector(random.choice(age)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()

    #page3
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
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

    #last
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div.quantumWizButtonEl.quantumWizButtonPaperbuttonEl.quantumWizButtonPaperbuttonFlat.quantumWizButtonPaperbuttonDark.quantumWizButtonPaperbutton2El2.freebirdFormviewerViewNavigationSubmitButton > content > span').click()
    driver.quit()


# In[2]:


'''
p91 = ['',
       '',
        '',
       '',
       ''
    ]
driver.find_element_by_css_selector('').click()
driver.find_element_by_css_selector(random.choice(p56)).click()
# coding: utf-8

# In[37]:





# In[216]:

for i in range(50):
    chrome_path = "D:\chromedriver.exe"
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSe6Hpm6j-h_QHtjzDd-s7iEWr-3vPoBGEJyXdckjcfWAq4Lpg/viewform?c=0&w=1'
    driver = webdriver.Chrome(chrome_path) #chromedriver         
    driver.get(url)


    # In[217]:


    driver.find_element_by_css_selector('div.quantumWizTogglePaperradioOffRadio.exportOuterCircle').click()
    driver.find_element_by_css_selector('span.quantumWizButtonPaperbuttonLabel.exportLabel').click()


    # In[218]:


    boygirl = ['#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl.isCheckedNext > div.quantumWizTogglePaperradioRadioContainer > div','div.quantumWizTogglePaperradioOffRadio.exportOuterCircle'] #男女
    age = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    playage = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    career = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(6) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(7) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]



    # In[219]:


    #page1
    driver.find_element_by_css_selector(random.choice(age)).click()
    driver.find_element_by_css_selector(random.choice(playage)).click()
    driver.find_element_by_css_selector(random.choice(career)).click()


    # In[220]:


    #girl
    driver.find_element_by_css_selector('div.quantumWizTogglePaperradioOffRadio.exportOuterCircle').click()#男女會有問題 放在最後選


    # In[221]:


    #change page
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()#換第二頁


    # In[222]:


    pay = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]

    edu = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]


    # In[223]:


    #page2
    driver.find_element_by_css_selector(random.choice(pay)).click()
    driver.find_element_by_css_selector(random.choice(edu)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div').click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()#換第三頁


    # In[224]:



    freq = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    since = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(3) > div:nth-child(4) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox'
    ]
    price = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'

    ]
    attr = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(3) > div:nth-child(1) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(3) > div:nth-child(6) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox' 
    ]

    attrplay = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(3) > div:nth-child(1) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(3) > div:nth-child(3) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(3) > div:nth-child(4) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox'
    ]


    # In[225]:


    #page3
    driver.find_element_by_css_selector(random.choice(freq)).click()
    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(3) > div:nth-child(4) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox').click()
    driver.find_element_by_css_selector(random.choice(price)).click()
    driver.find_element_by_css_selector(random.choice(attr)).click()
    driver.find_element_by_css_selector(random.choice(attrplay)).click()


    # In[226]:

    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()
    #driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()#換第四頁


    # In[227]:


    #page 4
    ser = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div > label > div > div.quantumWizTogglePapercheckboxEl.docssharedWizToggleLabeledControl.freebirdThemedCheckbox.freebirdThemedCheckboxDarkerDisabled.freebirdFormviewerViewItemsCheckboxControl > div.quantumWizTogglePapercheckboxInnerBox.exportInnerBox' 
    ]
    timge = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    timho = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(5) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]

    prod = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    app = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    video = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]


    # In[228]:


    #page 4
    driver.find_element_by_css_selector(random.choice(ser)).click()
    driver.find_element_by_css_selector(random.choice(timge)).click()
    driver.find_element_by_css_selector(random.choice(timho)).click()
    driver.find_element_by_css_selector(random.choice(prod)).click()
    driver.find_element_by_css_selector(random.choice(app)).click()
    driver.find_element_by_css_selector(random.choice(video)).click()


    # In[229]:


    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()#換第四頁


    # In[230]:


    #page 5
    stress = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(2) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'

    ]
    wantgo = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(3) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    moremoney = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(4) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]
    highhand = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(5) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]

    watch = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(6) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]

    enviro = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(3) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(7) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div'
    ]

    shop = [
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(1) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(2) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div',
        '#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewItemList > div:nth-child(8) > div:nth-child(2) > div > content > div > label:nth-child(4) > div > div.quantumWizTogglePaperradioEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled.freebirdFormviewerViewItemsRadioControl > div.quantumWizTogglePaperradioRadioContainer > div' 
    ]


    # In[231]:


    driver.find_element_by_css_selector(random.choice(stress)).click()
    driver.find_element_by_css_selector(random.choice(wantgo)).click()
    driver.find_element_by_css_selector(random.choice(moremoney)).click()
    driver.find_element_by_css_selector(random.choice(highhand)).click()
    driver.find_element_by_css_selector(random.choice(watch)).click()
    driver.find_element_by_css_selector(random.choice(enviro)).click()
    driver.find_element_by_css_selector(random.choice(shop)).click()


    # In[232]:


    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div:nth-child(2) > content > span').click()#換第四頁


    # In[233]:


    driver.find_element_by_css_selector('#mG61Hd > div > div.freebirdFormviewerViewFormContent > div.freebirdFormviewerViewNavigationNavControls > div > div > div.quantumWizButtonPaperbuttonEl.quantumWizButtonPaperbuttonFlat.quantumWizButtonPaperbuttonDark.quantumWizButtonPaperbutton2El2.freebirdFormviewerViewNavigationSubmitButton > content > span').click()


    # In[234]:


    driver.quit()
'''

