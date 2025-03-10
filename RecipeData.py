import os

 
recipe_names = [
    "Pasta with Creamy Tomato Sauce",
    "Pan-Seared Salmon with Lemon Herb Butter",
    "Cheesy Baked Chicken Enchiladas",
    "Steak Fajitas with Sizzling Peppers and Onions",
    "Garlicky Shrimp Scampi with Linguine"
    ]
recipe_descriptions = [
    "Pasta tossed in a rich and velvety tomato sauce, studded with fresh basil and Parmesan cheese.",
    "Tender salmon fillets with a crispy skin, drizzled with a vibrant lemon herb butter.",
    "Comforting cheesy chicken enchiladas, baked to perfection with a mouthwatering sauce.",
    "Sizzling steak strips and colorful peppers and onions, served with warm tortillas and your favorite toppings.",
    "Juicy shrimp tossed in a garlicky, buttery, and lemony sauce, served over a bed of linguine."
    ]
recipe_images=[]
        # r is used for identifying RAW string--Does not ignore backlashes

for i in range(1,3):
    imgPathConst = os.path.abspath(os.path.join(os.path.dirname(__file__),'./media/RecipeImages',f"d{i}.jpg"))
    recipe_images.append(imgPathConst)

    # os.path.dirname(__file__): This gets the directory path of the current script file.

def RecipeName():
     return recipe_names

def RecipeDescription():
    return recipe_descriptions


def RecipeImage():
     return recipe_images

if __name__== "__main__":
     RecipeName()
     RecipeDescription()
     RecipeImage()
     
# this conditional block executes only when the current script is run as the main program
#  in python every script and module has a built-in variable named _ _name_ _ 