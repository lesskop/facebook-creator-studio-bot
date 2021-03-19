from time import sleep
import random
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from data import *


def get_last_date():
    now = datetime.now()

    year_now = int(now.strftime("%Y"))

    month_now = int(now.strftime("%m"))

    day_now = int(now.strftime("%d"))

    count_days = 0

    for month in range(month_now, month_now + 4):

        if year_now % 4 == 0:
            feb = 29
        else:
            feb = 28

        days_in_month = {1: 31, 2: feb, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if month % 12 == 0:
            m = 12
        else:
            m = month % 12

        if count_days == 75:
            break

        for day in range(day_now, days_in_month[m] + 1):

            count_days += 1

            if count_days == 75:
                last_date = f'{day}.{m}.{year_now}'
                break

            if day == days_in_month[m]:
                day_now = 1
                if month % 12 == 0:
                    year_now += 1

    return last_date


def tag_randomizer(tag_list):
    text = ''
    used_tags = []

    # post can contain <= 30 tags
    for tag in range(29):
        random_tag = random.choice(tag_list)
        text += f'#{random_tag} '
        used_tags.append(random_tag)
        tag_list.remove(random_tag)

    tag_list += used_tags

    return text


def text_randomizer(tag_list):
    text = f"""Tag cat lovers 🐱
Follow @catzz_of_ig to be featured 😉
Don't miss new posts! Turn on notifications! ✔️

#cattzofig {tag_randomizer(tag_list)}"""

    return text


class CreatorStudioBot:

    def __init__(self):

        # write path to your geckodriver.exe in executable path
        self.driver = webdriver.Firefox(executable_path=r'')

        # set username and password in file data.py
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
        sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div'
        ).click()
        sleep(4)

        # switch active browser window
        driver.switch_to.window(driver.window_handles[1])

        # username input
        driver.find_element_by_name('username').send_keys(username)
        sleep(1)

        # password input
        driver.find_element_by_name('password').send_keys(password)
        sleep(2)

        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/form/div/div[3]/button'
        ).click()
        sleep(5)

        if self.xpath_exists('/html/body/div[1]/section/main/div/div/div/section/div/div[2]'):
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/div/div/div/button'
            ).click()
            sleep(3)

        driver.switch_to.window(driver.window_handles[0])
        sleep(3)

    def create_new_post(self):
        print('Creating new post...')
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div/div[1]'
        ).click()
        sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/strong'
        ).click()
        sleep(4)

    def upload_content(self, path):
        print('Uploading content:', path.split('\\')[-1])
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[5]/div/div/div/span'
        ).click()
        sleep(1)

        driver.find_element_by_css_selector("input[type=file]").send_keys(path)
        sleep(2)

    def add_text(self, text):
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div'
        ).send_keys(text)
        sleep(2)

    def add_random_text(self):
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[2]/div'
        ).send_keys(text_randomizer(tags))
        sleep(2)

    def add_location(self, location):
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[3]/span/label/input'
        ).send_keys(location)
        sleep(2)

    def add_random_location(self):
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div[3]/span/label/input'
        ).send_keys(random.choice(locations))
        sleep(2)

    def schedule(self, day, month, year, hour, minutes):
        date = f'{day}.{month}.{year}'
        print('Scheduling content for a date:', date)
        driver = self.driver

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/div[2]/div/button'
        ).click()
        sleep(1)

        div = 'div[9]'

        if self.xpath_exists('/html/body/div[6]/div/div/div/div/div[2]/div/div/span'):
            div = 'div[6]'

        # schedule radio button
        driver.find_element_by_xpath(
            f'/html/body/{div}/div/div/div/div/div[2]/div/div/span'
        ).click()
        sleep(1)

        # date
        driver.find_element_by_xpath(
            f'/html/body/{div}/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/span/div/span/label/input'
        ).send_keys(date)
        sleep(1)

        # hour
        driver.find_element_by_xpath(
            f'/html/body/{div}/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/input'
        ).send_keys(hour)
        sleep(1)

        # minutes
        driver.find_element_by_xpath(
            f'/html/body/{div}/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/input'
        ).send_keys(minutes)
        sleep(1)

        # submit
        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/div[2]/button'
        ).click()

    def schedule_random_content_from_date(self, day, month, year, hour, minutes):
        driver = self.driver

        day_now = day
        month_now = month
        year_now = year

        date = datetime.now().strftime('%d.%m.%Y')

        for month in range(month_now, month_now + 4):

            if year_now % 4 == 0:
                feb = 29
            else:
                feb = 28

            days_in_month = {1: 31, 2: feb, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

            if month % 12 == 0:
                m = 12
            else:
                m = month % 12

            if date == get_last_date():
                break

            for day in range(day_now, days_in_month[m] + 1):

                date = f'{day}.{m}.{year_now}'

                self.create_new_post()
                self.upload_content(random.choice(cats_content))
                self.add_random_text()
                self.add_random_location()
                self.schedule(day, m, year_now, hour, minutes)

                sleep(5)
                driver.refresh()
                sleep(5)

                if date == get_last_date():
                    break

                if day == days_in_month[m]:
                    day_now = 1
                    if month % 12 == 0:
                        year_now += 1


bot = CreatorStudioBot()
bot.login()
bot.schedule_random_content_from_date(20, 3, 2021, 20, 00)
# bot.close_browser()
