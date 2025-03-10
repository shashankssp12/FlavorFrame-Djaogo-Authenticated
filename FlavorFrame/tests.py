from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from FlavorFrame.models import Recipe

class RecipeTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()

    # def tearDown(self):
    #     Recipe.objects.filter(Rname__icontains="test").delete()
    #     self.selenium.quit()

    def test_create_recipe(self):
        self.selenium.get(self.live_server_url + "/recipes")

        recipe_data = [
            {"name": "Test Recipe 1", "desc": "Delicious", "image": "/media/RecipeImages/img1.jpg"},
            {"name": "Test Recipe 2", "desc": "Yummy", "image": "/media/RecipeImages/img1.jpg"}
        ]

        for data in recipe_data:
            self.selenium.find_element(By.NAME, "Rname").send_keys("test:" + data["name"])
            self.selenium.find_element(By.NAME, "description").send_keys(data["desc"])
            self.selenium.find_element(By.NAME, "Rimage").send_keys(data["image"])
            self.selenium.find_element(By.ID, "submit").send_keys(Keys.RETURN)
            time.sleep(1)

        assert Recipe.objects.filter(Rname__icontains="test").exists()
