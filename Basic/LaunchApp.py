import base64
import os
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

desired_cap ={
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "2cd4481c",
    "app": "E:\\Apium\\nopstationCart_4.40.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(25)

# Start Video Recording
driver.start_recording_screen()

el1 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnAccept")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Placeholder\"])[6]")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/tvSelectedAttr")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RadioGroup/android.widget.RadioButton[2]")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/tvDone")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnPlus")
el6.click()
el7 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnAddToCart")
el7.click()

el1 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/counterIcon")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnCheckOut")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnGuestCheckout")
el3.click()
el4 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etFirstName")
el4.send_keys("Naruto")
el5 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etLastName")
el5.send_keys("Uzumaki")
el6 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etEmail")
el6.send_keys("abc@demo.com")
el7 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/countrySpinner")
el7.click()
el8 = driver.find_element(by=AppiumBy.XPATH,
                          value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
el8.click()
el9 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/stateSpinner")
el9.click()
el10 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]")
el10.click()
el11 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etCompanyName")
el11.send_keys("abc")
el12 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etCity")
el12.send_keys("DDD")
el13 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress")
el13.send_keys("asd 234")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(530, 2123)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(583, 764)
actions.w3c_actions.pointer_action.release()
actions.perform()

el13.click()
el14 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etStreetAddress2")
el14.send_keys("aaa")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(550, 1409)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(575, 776)
actions.w3c_actions.pointer_action.release()
actions.perform()

el15 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/etZipCode")
el15.send_keys("2020")
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(542, 1413)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(612, 645)
actions.w3c_actions.pointer_action.release()
actions.perform()

el16 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
el16.click()
el17 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[4]")
el17.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(661, 2131)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(698, 698)
actions.w3c_actions.pointer_action.release()
actions.perform()

el18 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
el18.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(522, 2086)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(583, 821)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(538, 2094)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(591, 723)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(443, 2094)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(505, 698)
actions.w3c_actions.pointer_action.release()
actions.perform()

el19 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/com.bs.ecommerce.customViews.RadioGridGroupforReyMaterial/android.widget.RelativeLayout[4]")
el19.click()
el19.click()
el20 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout[2]/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
el20.click()
el21 = driver.find_element(by=AppiumBy.XPATH,
                           value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
el21.click()
el22 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/btnContinue")
el22.click()
el23 = driver.find_element(by=AppiumBy.ID, value="com.nopstation.nopcommerce.nopstationcart:id/md_button_positive")
el23.click()

#Stop Recordinh
video_data = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = os.path.join("E:/Apium/bsProject/Screenshot/", video_name+".mp4")

with open(filepath,"wb") as vd:
    vd.write(base64.b64decode(video_data))

