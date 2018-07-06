import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import json

def main():


  binary = FirefoxBinary("C:/Program Files/Firefox/firefox.exe")
  #driver = webdriver.Firefox(firefox_binary=binary)
  driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:/Users/gavva_000/Desktop/VAG Company/Боты/Telegram Bot/BotYandexTaxopark/geckodriver.exe')
  driver.maximize_window()
  driver.implicitly_wait(20)
  # Переходим по ссылке.
  # client_id - идентификатор созданного нами приложения
  # scope - права доступа
  driver.get("https://passport.yandex.ru/auth?retpath=https%3A%2F%2Flk.taximeter.yandex.ru%2F")
  login = ''
  password = ''

  user_input = driver.find_element_by_name("login")
  user_input.send_keys(login)
  password_input = driver.find_element_by_name("passwd")
  password_input.send_keys(password)

  submit = driver.find_element_by_class_name("passport-Button")
  submit.click()
  driver.implicitly_wait(20)
  continue_link = driver.find_element_by_link_text('Заказы')
  continue_link.click()
  driver.implicitly_wait(20)
  table = driver.find_element_by_id("table1")
  #table = driver.find_element_by_xpath("//table1/.datagrid-body/.datagrid-content/table/tbody")


if __name__ == '__main__':
  main()