from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        
        self.browser = webdriver.Chrome(r'.\chromedriver.exe')

    def tearDown(self):

        self.browser.quit()

    def test_buscando_animal(self):
        '''
        Testa se um usuário encontra um animal na pesquisa.
        '''

        # Vini, deseja encontrar um novo animal, para adotar.
        home_page = self.browser.get(self.live_server_url + '/')

        # Ele encontra o Busca Animal e decide usar o site,
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # porque ele vê no menu do site escrito Busca Animal.
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        
        # Ele pesquisa por Leão e clica no botão pesquisar.

        # O site exibe 4 caracteristicas do animal pesquisado.

        # Ele desiste de adotar um leão.
        