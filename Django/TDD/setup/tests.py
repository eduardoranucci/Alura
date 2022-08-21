from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        
        self.browser = webdriver.Chrome(r'.\chromedriver.exe')

    def tearDown(self):

        self.browser.quit()

    def test_server(self):
        self.browser.get(self.live_server_url)
