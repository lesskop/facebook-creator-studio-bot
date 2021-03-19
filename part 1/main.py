import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from data import *


class CreatorStudioBot:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'')
        self.username = username
        self.password = password

    def close_browser(self):
        print("Closing browser.")
        self.driver.close()
        self.driver.quit()

    def xpath_exists(self, xpath):
        driver = self.driver

        try:
            driver.find_element_by_xpath(xpath)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def login(self):
        driver = self.driver
        driver.get(link)

        driver.find_element_by_id('media_manager_chrome_bar_instagram_icon').click()
        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div'
        ).click()
        time.sleep(3)

        # username input
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_name('username').send_keys(username)
        time.sleep(1)

        # password input
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(2)

        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/form/div/div[3]/button'
        ).click()
        time.sleep(3)

        if self.xpath_exists('/html/body/div[1]/section/main/div/div/div/section/div/div[2]'):
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div/div/button'
            ).click()
            time.sleep(3)

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)


bot = CreatorStudioBot()
bot.login()
# bot.close_browser()
