from django.test import LiveServerTestCase , TransactionTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from time import sleep
from RecipeData import *
from VEG_REC.models import Recipe
# for search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import pytest

# imgPathConst = os.path.abspath(os.path.join(os.path.dirname(__file__),'../public/static/RecipeImages','d1.jpg'))
# print(imgPathConst)

class Recipe:
    # constructor
    def __init__(self,name,description,image):
        self.name= name
        self.description = description
        self.image= image

 
class testRecipe(TransactionTestCase):

    def setUp(self):
         self.selenium = webdriver.Chrome()
         return super().setUp()

    def test_title(self):
        selenium = self.selenium

        act_title = selenium.title

        if act_title == "Recipes":
            assert True
            selenium.quit()
        else:
            assert False
        selenium.quit()

        
    def testCreateRecipe(self):
        selenium = self.selenium
        
        selenium.get('http://127.0.0.1:8000/recipes')
        # time.sleep(2)
        recipe_lists=[]
        for name, description, imgPath in zip(recipe_names, recipe_descriptions, recipe_images):
            recipe_lists.append(Recipe(name, description, imgPath))
            

        for i in range(0, len(recipe_lists)):
            Rname=selenium.find_element(by=By.NAME, value="Rname")
            description=selenium.find_element(by=By.NAME, value="description")
            Rimage= selenium.find_element(by=By.NAME, value="Rimage")
            submit=selenium.find_element(by=By.ID, value="submit")

            Rname.send_keys(recipe_lists[i].name)
            description.send_keys(recipe_lists[i].description)
            Rimage.send_keys(recipe_lists[i].image)
            time.sleep(2)
            submit.send_keys(Keys.RETURN)#this clicks the submit button
        

        selenium.quit()


    def testSearch_Validate(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/recipes')
        
        searchInput=selenium.find_element(by=By.NAME, value="search")
        searchBtn=selenium.find_element(by=By.ID, value='search')

        searchInput.send_keys('Cheesy')
        # search improve

        time.sleep(3)
        searchBtn.send_keys(Keys.RETURN)#this clicks the submit button
        time.sleep(5)
        selenium.quit()

# py tests.py
# command: py manage.py test