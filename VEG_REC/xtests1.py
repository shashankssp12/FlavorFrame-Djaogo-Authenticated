from django.test import LiveServerTestCase , TransactionTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
# discover what it does
from time import sleep
from RecipeData import *
from VEG_REC.models import Recipe
# for search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import pytest

# imgPathConst = os.path.abspath(os.path.join(os.path.dirname(__file__),'../public/static/RecipeImages','d1.jpg'))
# print(imgPathConst)

# Create your tests here.
 
class Recipe:
    # constructor
    def __init__(self,name,description,image):
        self.name= name
        self.description = description
        self.image= image

 
class testRecipe(TransactionTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.implicitly_wait(3)  # Adjust wait time as needed

    def tearDown(self):
        self.selenium.quit()

    def testCreateRecipe(self):
        self.selenium.get('http://127.0.0.1:8000/recipes')
        # time.sleep(2)
        recipe_lists=[]
        for name, description, imgPath in zip(recipe_names, recipe_descriptions, recipe_images):
            recipe_lists.append(Recipe(name, description, imgPath))
            

        # imgPathConst = r"C:\Users\shash\Downloads\img.jpg"
        # r is used for identifying RAW string--Does not ignore backlashes
        # recipe_images=[]

           
        # can also use loop
        for i in range(0, len(recipe_lists)):
            Rname=self.selenium.find_element(by=By.NAME, value="Rname")
            description=self.selenium.find_element(by=By.NAME, value="description")
            Rimage= self.selenium.find_element(by=By.NAME, value="Rimage")
            submit=self.selenium.find_element(by=By.ID, value="submit")
            Rname.send_keys(recipe_lists[i].name)
            description.send_keys(recipe_lists[i].description)
            Rimage.send_keys(recipe_lists[i].image)
            time.sleep(2)
            submit.send_keys(Keys.RETURN)#this clicks the submit button


    # def tearDown(self):
    #     self.selenium.quit()
    #     testDel= Recipe.objects.all()
    #     testDel.delete()
    #     super().tearDown()  # Rolls back database transactions
        
    # def testSearch_Validate(self):
    #     driver= webdriver.Chrome()    
    #     driver.get('http://127.0.0.1:8000/recipes')
        
    #     searchInput=driver.find_element(by=By.NAME, value="search")
    #     searchBtn=driver.find_element(by=By.ID, value='search')

    #     searchInput.send_keys('Cheesy')
    #     # search improve

    #     time.sleep(3)
    #     searchBtn.send_keys(Keys.RETURN)#this clicks the submit button
    #     time.sleep(5)
    #     driver.quit()

# py tests.py
# command: py manage.py test