from appium import webdriver
import time
desired_caps=dict()
#平台名字 ，大小写无所谓
desired_caps['platformName']='Android'
#平台版本 5.4.3可以写5.4,5
desired_caps['platformVersion']='5.0'
#设备名，随便写，但是不能为空
desired_caps['deviceName']='192.168.162.101:5555'
#包名
desired_caps['appPackage']='com.android.settings'
#界面名
desired_caps['appActivity']='.Settings'
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(5)
driver.quit()