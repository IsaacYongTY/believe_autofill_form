from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('believe_autofill_form.ui', self)

        CHROME_PATH = '/Users/isaacyong/chromedriver'

        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.push_button.clicked.connect(self.action)
        self.exit_button.clicked.connect(self.exit)
        self.show()
        self.open_page_and_login()

    def exit(self):
        self.driver.quit()
        app.quit()

    def open_page_and_login(self):

        f = open('1.txt', 'r')
        content = f.read()

        self.username = content.split(',')[0]
        self.password = content.split(',')[1]

        self.driver.get('https://believebackstage.com/')

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

        facebook_url = self.driver.find_element_by_id('linksFacebook')
        facebook_number = self.driver.find_element_by_id('linksFacebookNumber')

        twitter_url = self.driver.find_element_by_id('linksTwitter')
        twitter_number = self.driver.find_element_by_id('linksTwitterNumber')

        instagram_url = self.driver.find_element_by_id('linksInstagram')
        instagram_number = self.driver.find_element_by_id('linksInstagramNumber')

        songkick_url = self.driver.find_element_by_id('linksSongkick')
        songkick_number = self.driver.find_element_by_id('linksSongkickNumber')

        youtube_url = self.driver.find_element_by_id('linksYoutube')
        youtube_number = self.driver.find_element_by_id('linksYoutubeNumber')

        weibo_url = self.driver.find_element_by_id('linksWeibo')
        weibo_number = self.driver.find_element_by_id('linksWeiboNumber')

        website_url = self.driver.find_element_by_id('linksWebsite')
        website_number = self.driver.find_element_by_id('linksWebsiteNumber')

        facebook_url.clear()
        facebook_number.clear()

        twitter_url.clear()
        twitter_number.clear()

        instagram_url.clear()
        instagram_number.clear()

        songkick_url.clear()
        songkick_number.clear()

        youtube_url.clear()
        youtube_number.clear()

        weibo_url.clear()
        weibo_number.clear()

        website_url.clear()
        website_number.clear()

        facebook_url.send_keys('https://facebook.com/isaacyongmusic')
        facebook_number.send_keys('1950')

        twitter_url.send_keys('https://twitter.com/isaacyongmusic')
        twitter_number.send_keys('30')

        instagram_url.send_keys('https://www.instagram.com/isaacyongmusic/')
        instagram_number.send_keys('1830')

        songkick_url.send_keys('https://www.songkick.com/artists/10139875-isaac-yong')
        #songkick_number.send_keys('1950')

        youtube_url.send_keys('https://youtube.com/c/isaacyongmusic')
        youtube_number.send_keys('5350')

        weibo_url.send_keys('https://weibo.com/5995002939/')
        weibo_number.send_keys('1800')

        website_url.send_keys('https://isaacyong.com')
        #website_number.send_keys('1950')

        save_button = self.driver.find_element_by_id('easyEntryDataSaveButton')

        if self.is_save.isChecked():
            save_button.click()
            print("Saved successfully")

    def action(self):

        # release_number = input('Please enter the release number (e.g. 3720803):')
        self.release_number = self.findChild(QtWidgets.QLineEdit, 'release_number_input').text()

        if self.release_number:
            self.message.setText('')
            self.navigate_to_release(self.release_number)
            self.fill_in_form()

        else:
            self.message.setText('Please input release number')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()


