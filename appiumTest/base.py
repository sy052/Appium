import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppiumConnection:
    def __init__(self):
        #옵션 설정
        self.options = AppiumOptions()
        self.options.load_capabilities({
            "appium:automationName": "UiAutomator2",
            "appium:automationName": "UiAutomator2",
            "appium:platformName": "Android",
            "appium:deviceName": "emulator-5554",
            "appium:platformVersion": "16",
            "appium:settings[enableMultiWindows]": True,
            "appium:wdaLocalPort": "8100",
            "appium:settings[allowInvisibleElements]": True,
            "appium:connectHardwareKeyboard": True,
        })

    def connection(self):
        try:
            print("Appium 서버 연결 시도중...")
            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=self.options)
            print("Appium 서버 연결 성공!")

        except Exception as e:
            print(f"Appium 서버 연결 실패: {e}")

    def quit(self):
        if self.driver:
            print("드라이버를 종료합니다...")
            self.driver.quit()
            print("드라이버가 종료되었습니다.")
    

