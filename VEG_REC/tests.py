import allure
from allure_commons.types import AttachmentType
from django.conf import settings
import os
from pathlib import Path
import django

BASE_DIR = Path(__file__).resolve().parent.parent

settings.configure(

    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'home',  # Your custom apps
        'VEG_REC',
    ],
    ROOT_URLCONF='core.urls',
    WSGI_APPLICATION='core.wsgi.application',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            # 'NAME': 'testdb.sqlite3',  # Use a separate test database
        }
        # 'test': {
        #                 'ENGINE': 'django.db.backends.sqlite3',
        #                 'NAME': BASE_DIR / 'testdb.sqlite3'}
    }
)
django.setup()
# applications not registered SOLVED

from django.test import LiveServerTestCase, TransactionTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from time import sleep
from RecipeData import *
from VEG_REC.models import Recipe

from django.db import transaction

# for search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
from pathlib import Path
# imgPathConst = os.path.abspath(os.path.join(os.path.dirname(__file__),'../public/static/RecipeImages','d1.jpg'))
# print(imgPathConst)
import django
from django.conf import settings


# Replace 'your_project' with the actual name of your Django project

class Recipe1:
    # constructor
    def __init__(self,name,description,image):
        self.name= name
        self.description = description
        self.image= image
        
class testRecipe(LiveServerTestCase):
    # testCase ----isOptimal---no
    #liveServerTestCase and TransactinTestCase ---- will automatically rollback the database without teardown function
    def setUp(self):
        self.selenium = webdriver.Chrome()
        return super().setUp()


    # teardown without handling the exception
    # def tearDown(self):
    #     # Delete the created Recipe objects
    #     # Recipe.objects.all().delete()
    #     toPrint= Recipe.objects.all()
    #     # .filter(Rname__icontains="test")
    #     toPrint.delete()
    #     print(toPrint)
    #     self.selenium.quit()
    #     super().tearDown()
    def tearDown(self):
        # 1. Filter for test recipes (adjust filtering as needed):
        recipesToDelete = Recipe.objects.all().filter(Rname__icontains="test").delete()
        # print(type(recipesToDelete))

        # 2. Check number of recipes targeted (optional):
        # numberOfRecipesToDelete = recipesToDelete.count()
        # print(f"Number of recipes to delete: {numberOfRecipesToDelete}")

        # 3. Verify before deletion (optional):
        # print("Recipes to delete:", recipesToDelete.values())

        # 4. Delete with explicit commit to ensure execution:
        # with transaction.atomic():
        #     recipesToDelete.delete()

        # 5. Additional asynchronous task handling if needed:
        # ... (trigger tasks, check completion)

        super().tearDown()
        self.selenium.quit()
 
    def testCreateRecipe(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/recipes')
        # time.sleep(2)
        recipe_lists=[]
        for name, description, imgPath in zip(recipe_names, recipe_descriptions, recipe_images):
            recipe_lists.append(Recipe1(name, description, imgPath))


        for i in range(0, len(recipe_lists)-3):
            Rname=selenium.find_element(by=By.NAME, value="Rname")
            description=selenium.find_element(by=By.NAME, value="description")
            Rimage= selenium.find_element(by=By.NAME, value="Rimage")
            submit=selenium.find_element(by=By.ID, value="submit")

            Rname.send_keys("test:" + recipe_lists[i].name)
            description.send_keys(recipe_lists[i].description)
            Rimage.send_keys(recipe_lists[i].image)
            time.sleep(2)
            submit.send_keys(Keys.RETURN)#this clicks the submit button
        # time.sleep(2)
        Recipe.objects.all().filter(Rname__icontains="test").delete()
        selenium.quit()

    # @allure.severity(allure.severity_level.CRITICAL)
    # def testLogin(self):
    #     selenium = self.selenium
    #     selenium.get('http://127.0.0.1:8000/login')
    #
    #     Username = selenium.find_element(by=By.NAME, value="username")
    #     Password = selenium.find_element(by=By.NAME, value="password")
    #     Submitbtn = selenium.find_element(by=By.NAME, value="submit")
    #
    #     Username.send_keys("shashank1")
    #     Password.send_keys("hello")
    #     time.sleep(2)
    #     Submitbtn.send_keys(Keys.RETURN)
    #     time.sleep(3)
    #     allure.attach(selenium.get_screenshot_as_png(), name='TestLogin', attachment_type=AttachmentType.PNG)
    #     selenium.quit()
    # def test_title(self):
    #     selenium = self.selenium
    #     selenium.get('http://127.0.0.1:8000/recipes')
    #
    #     time.sleep(5)
    #     act_title = selenium.title
    #     # print(act_title)
    #     if act_title == "Recipes":
    #         assert True
    #
    #         selenium.quit()
    #     else:
    #         assert False
    #     selenium.quit()
    #
    # def test_Search_Validate(self):
    #     selenium = self.selenium
    #     selenium.get('http://127.0.0.1:8000/recipes')
    #
    #     searchInput = selenium.find_element(by=By.NAME, value="search")
    #     searchBtn = selenium.find_element(by=By.ID, value='search')
    #
    #     searchInput.send_keys('Cheesy')
    #     # search improve
    #
    #     time.sleep(3)
    #     searchBtn.send_keys(Keys.RETURN)  # this clicks the submit button
    #     time.sleep(5)
    #     selenium.quit()


    #
    # def tearDown(self):
    #     try:
    #         Recipe.objects.all().delete()
    #         transaction.on_commit(lambda: None)  # Explicitly commit the transaction
    #     except AttributeError as e:
    #         print(f"AttributeError: {e}")
    #     self.selenium.quit()
    #     super().tearDown()

    # def tearDown(self):
    #     # Delete the created Recipe objects
    #     try:
    #         Recipe.objects.all().delete()
    #     except AttributeError as e:
    #         print(f"AttributeError: {e}")
    #     self.selenium.quit()
    #     super().tearDown()



# py tests.py
# command: py manage.py test