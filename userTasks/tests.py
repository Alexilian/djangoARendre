import re
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.chrome.options import Options

class FunctionnalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.options = Options()
        # cls.options.add_argument('--headless')
        cls.browser = webdriver.Chrome(executable_path='D:\chromedriver\chromedriver.exe', options=cls.options)
        cls.browser.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        super().tearDownClass()

    def test_add_user(self):
        """Test d'ajout d'un utilisateur"""

        self.browser.get("http://127.0.0.1:8000/userTasks/addUser/")

        name = self.browser.find_element(By.ID, "id_name")
        surname = self.browser.find_element(By.ID, "id_surname")

        name.send_keys("Jonas")
        surname.send_keys("Doucet")

        self.browser.find_element(By.ID, "submit").click()

    # Vérifier la création de l'utilisateur

        self.browser.get("http://127.0.0.1:8000/userTasks/users/")

        nom = self.browser.find_element(By.CSS_SELECTOR, "tbody:last-child > tr > td:first-child")

        self.assertIn('Jonas', nom.text)
        self.fail("L'utilisateur Jonas a bien ete cree !")


    def test_supp_user(self):
        """Test de suppression d'un utilisateur"""

        self.browser.get("http://127.0.0.1:8000/userTasks/users/")

        self.browser.find_element(By.CSS_SELECTOR, "td:last-child > a:first-child > button").click()

        nom = self.browser.find_element(By.CSS_SELECTOR, "tbody:last-child > tr > td:first-child")

        self.assertNotEqual('Jonas', nom)

    def test_add_task(self):
        """Test d'ajout d'une tache"""

        self.browser.get("http://127.0.0.1:8000/userTasks/addTask/")

        name = self.browser.find_element(By.ID, "id_name")
        description = self.browser.find_element(By.ID, "id_description")
        due_date = self.browser.find_element(By.ID, "id_due_date")
        schedule_date = self.browser.find_element(By.ID, "id_schedule_date")
        user = self.browser.find_element(By.ID, "id_user")
        closed = self.browser.find_element(By.ID, "id_closed")

        name.send_keys("TacheTest")
        description.send_keys("Un test")
        due_date.send_keys("2022-10-08")
        schedule_date.send_keys("2022-10-08")
        user.send_keys("1")
        closed.send_keys("False")

        self.browser.find_element(By.ID, "submit").click()

    