from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from PyQt5 import QtWidgets, uic
import sys
import os
import csv

class SocialMedia:
    def __init__(self, name, link, followers):

        name = name.capitalize()

        self.id = f'links{name}'
        self.followers_id = f'links{name}Number'
        self.link = link
        self.followers = followers

    def __str__(self):
        return f'{self.id}, {self.followers_id}, {self.followers}'

    def __repr__(self):
        return str(self)

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        self.relative_path = '.'
        self.directory = self.get_correct_path(self.relative_path)
        uic.loadUi(f'{self.directory}/believe_autofill_form.ui', self)

        CHROME_PATH = '/Users/isaacyong/chromedriver'

        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.executeButton.clicked.connect(self.fill_form)
        self.exitButton.clicked.connect(self.exit)

        self.show()

        self.driver.get('https://believebackstage.com/')

        self.login()

        self.social_media_array = self.generate_latest_stats()

    def get_correct_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')

        return os.path.join(base_path, relative_path)

    def generate_latest_stats(self):

        result_array = []


        with open(f'{self.directory}/social_media_stats.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            next(csv_file, None)
            for row in csv_reader:

                social_media_data = SocialMedia(row[0], row[1], row[2])

                print(social_media_data)
                print(social_media_data.id)
                result_array.append(social_media_data)

        return result_array

    def login(self):

        f = open(f'{self.directory}/1.txt', 'r')
        content = f.read()

        self.username = content.split(',')[0]
        self.password = content.split(',')[1]

        for x in range(2):

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login'))
            )

            print(f'{x} pass')

            login_input = self.driver.find_element_by_id('login')
            password_input = self.driver.find_element_by_id('password')

            login_input.send_keys(self.username)
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)

        self.driver.execute_script("window.open('https://believebackstage.com/catalog/manager', '_blank')")

    def navigate_to_release(self, release_number):

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'menuLabel'))
            )
            self.driver.get(f'https://believebackstage.com/easyentry/promotion/edit/{release_number}')

    def fill_in_form(self):
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.ID, 'linksFacebook'))
        )

        english_textarea_class = self.driver.find_element_by_class_name('inputBehavior-2')
        english_textarea_id = english_textarea_class.get_attribute('id')

        id_number_only = int(english_textarea_id.split('-')[1])

        english_textarea = self.driver.find_element_by_id((f'description-{id_number_only + 2}-easyEntryEditForm'))
        chinese_textarea = self.driver.find_element_by_id(f'description-{id_number_only}-easyEntryEditForm')

        english_textarea.clear()
        chinese_textarea.clear()

        english_textarea.send_keys('Isaac Yong is a singer-songwriter based in Singapore. He draws songwriting inspiration from stories around him, as well as through his personal experience. His voice is described as warm and soothing. Being a content creator, he also releases covers on various platforms, most notably through his style of combining singing with fingerstyle guitar, often playing different parts simultaneously with just one guitar.')
        chinese_textarea.send_keys('杨征宇是来自新加坡的创作歌手。他的创作灵感来源于身边发生故事，也有的是源自于自己生活中的经历和情感。听众形容他”拥有一把温暖、让人觉得舒服的声音“。他也在各大不同的影音平台发行翻唱。他擅长把流行音乐结合指弹吉他，很多时候仅用一把吉他就能够弹唱时同时演奏多个声部。')

        for platform in self.social_media_array:
            self.driver.find_element_by_id(platform.id).clear()
            self.driver.find_element_by_id(platform.followers_id).clear()
            self.driver.find_element_by_id(platform.id).send_keys(platform.link)
            self.driver.find_element_by_id(platform.followers_id).send_keys(platform.followers)

        save_button = self.driver.find_element_by_id('easyEntryDataSaveButton')

        if self.isSave.isChecked():
            save_button.click()
            print("Saved successfully")

    def fill_form(self):

        self.release_number = self.findChild(QtWidgets.QLineEdit, 'releaseNumberInput').text()

        if self.release_number:
            self.message.setText('')
            self.navigate_to_release(self.release_number)
            self.fill_in_form()

        else:
            self.message.setText('Please input release number')

    def exit(self):
        self.driver.quit()
        app.quit()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


