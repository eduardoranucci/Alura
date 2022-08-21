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
        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')  
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: Leão')      

        # Ele pesquisa por Leão e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        resultado = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(resultado), 3)

        # Ele desiste de adotar um leão.
        