import re
from recipe import Recipe
import Food

def cleanPrint(aList, Dict=False):
    """Prints inside of a list or dictionary. List is the Default print."""
    count = len(aList)
    counterDict = {}
    
    if Dict:    
        for item in aList:
            if item not in counterDict.keys():
                counterDict[item] = 1
            else:
                counterDict[item] = counterDict[item] + 1

        count = len(counterDict)
        for key, value in counterDict.items():
            if count == 1:
                print(key + ": " + str(value))
            else:
                print(key + ": " + str(value) + ",")
                count = count - 1
    else:
        for item in aList:
            if count == 1:
                print(item)
            else:
                print(item + ",")
                count = count - 1
                
    return counterDict

def firstTimeEntry(food, dict):
    return not (food in dict)

def processNumber(numList):
    whole = 0
    num = 0
    den = 1
    
    if len(numList) > 1:
        whole = int(numList[0])
        numList = numList[1].split('/')
        num = numList[0]
        den = numList[1]
        return Mixed(whole, num, den)
    elif numList[0].find('/') == -1:
        return int(numList[0])
    else:
        numList = numList[0].split('/')
        num = numList[0]
        den = numList[1]
        return Mixed(0, num, den)

def parse(foodStr):
    fractionList = []
    name = ''
    strList = re.split("\s", foodStr)

    while (strList[0].isdigit() or strList[0].find('/')):
        fractionList.append(strList[0])
        strList.pop(0)
        if strList[0].isdigit() or strList[0].find('/') == -1:
            break
    number = processNumber(fractionList)

    
    mType = strList[0]
    strList.pop(0)

    for i in range(len(strList)):
        if i == len(strList) - 1:
            name = name + strList[i]
        else:
            name = name + strList[i] + ' '

    return (number, mType, name)

recipes = Recipe()
border = "="*11
counterDict = {}
new_item = ''
grocerys = {}
shopping_list = []
food_list = []
store_list = []

#these are the store aisles that will be used to eventually sort grocery list
#or ask user to define aisles
aisles = [['produce'],['meat', 'cheese', 'lunch meat',], ['dairy', 'eggs', 'juice', 'pies', 'yogurt', 'butter'],
          ['frozen vegetables'], ['housewares'], ['cereal', 'coffee/tea'], ['baking', 'spices', 'PBJ'],
          ['boxed dinner', 'canned meat', 'pasta/sauce'], ['soup', 'mexican', 'asian'], 
          ['condiments', 'canned fruits/veggies & juice'], ['cookies & crackers'], ['candy, snacks, & chips'], ['bread'],
         ['ice']]

while new_item.upper() != "DONE":
    print("What should we buy from the store?  \n")
    print("Enter 'DONE' to stop adding items. \n'HELP' to see items.")
    print(border + "Remember: Recipes must be entered as a list in the program first"
          + border)
    
    #asks for new items
    new_item = input("Enter a Recipe ")
    
    if new_item == 'monster cheese burgers':
        shopping_list.extend(recipes.monster_cheese_burgers)
    elif new_item == 'chili spiced beef and carrots':
        shopping_list.extend(recipes.chili_spiced_beef_and_carrots)
    elif new_item == 'tuscan steak and green peppers':
        shopping_list.extend(recipes.tuscan_steak_and_green_peppers)
    elif new_item == 'beef and cabbage soup':
        shopping_list.extend(recipes.beef_and_cabbage_soup)
    elif new_item == 'sloppy joes':
        shopping_list.extend(recipes.sloppy_joes)
    elif new_item == 'chicken spinach alfredo':
        shopping_list.extend(recipes.chicken_spinach_alfredo)
    elif new_item == 'chicken tikka masala':
        shopping_list.extend(recipes.chicken_tikka_masala)
    elif new_item == 'shredded chicken fajitas':
        shopping_list.extend(recipes.shredded_chicken_fajitas)
    elif new_item == 'chicken cordon bleu casserole':
        shopping_list.extend(recipes.chicken_cordon_bleu_casserole)
    elif new_item == 'chicken and sausage orzo':
        shopping_list.extend(recipes.chicken_and_sausage_orzo)
    elif new_item == 'italian sausage rigatoni':
        shopping_list.extend(recipes.italian_sausage_rigatoni)
    elif new_item == 'gvb soup turkey':
        shopping_list.extend(recipes.gvb_soup_turkey)
    elif new_item == 'tuscaan torellini soup':
        shopping_list.extend(recipes.tuscaan_torellini_soup)
    elif new_item == 'white chicken chili':
        shopping_list.extend(recipes.white_chicken_chili)
    elif new_item == 'ranch popcorn chicken':
        shopping_list.extend(recipes.ranch_popcorn_chicken)
    elif new_item == 'cheesy chicken veggie casserole':
        shopping_list.extend(recipes.cheesy_chicken_veggie_casserole)
    elif new_item == 'pulled pork':
        shopping_list.extend(recipes.pulled_pork)
    elif new_item == 'suasage and peppers':
        shopping_list.extend(recipes.suasage_and_peppers)
    elif new_item == 'potatoe corn chowder':
        shopping_list.extend(recipes.potatoe_corn_chowder)
    elif new_item == 'jalepeno and bacon':
        shopping_list.extend(recipes.jalepeno_and_bacon)
    elif new_item == 'indian butter chicken':
        shopping_list.extend(recipes.indian_butter_chicken)
    elif new_item == 'salsa verde chicken':
        shopping_list.extend(recipes.salsa_verde_chicken)
    elif new_item == 'chicken tortilla soup':
        shopping_list.extend(recipes.chicken_tortilla_soup)
    elif new_item.upper() == "HELP":
        print(recipes)
    elif new_item.upper() != "DONE":
        print("Your item is invalid, try again. Type HELP to see all items.")

'''
Shorter need to find to add aisle
for ingredient in shopping_list:
     new_item = parse(ingredient)
    if not(new_item[1] in groceries):
        groceries[new_item[1]] = Food(new_item[0][0], new_item[0][1])
        #how do I add aisle, aisle dictionary
    elif new_item[1] == ”chicken breast“:
 '''       

#convert string to food classes
for ingredient in shopping_list:
    ingredient_Tuple = parse(ingredient)
   
    if ingredient_Tuple[1] == 'chicken breast':
        if firstTimeEntry('chicken breast'):
            groceries['chicken breast'] = ChickenBreast(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries['chicken breast'] =  groceries['chicken breast'] + ChickenBreast(ingredient_Tuple[0], ingredient_Tuple[1])
   elif ingredient_Tuple[1] == 'beef chuck roast':
    pass

'''  
class BeefChuckRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'beef chuck roast'
    self.aisle = 'meat'
 
class GroundBeef(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground beef'
    self.aisle = 'meat'
 
class GroundItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground italian sausage'
    self.aisle = 'meat'
 
class ItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'italian sausage'
    self.aisle = 'meat'
 
class PorkShoulder(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'pork shoulder'
    self.aisle = 'meat'
 
class Bacon(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bacon'
    self.aisle = 'meat'
 
class GroundTurkey(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground turkey'
    self.aisle = 'meat'

class HamSteak(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bone in ham bone steak'
    self.aisle = 'meat'
  
class ChickenThighs(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'chicken thighs'
    self.aisle = 'meat'
  
class SerloinTipRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'sliced & fat trimmed boneless sirloin tip roast'
    self.aisle = 'meat'
 
  #Dairy

class AmericanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
    self.aisle = 'dairy'
  
class HeavyCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
    self.aisle = 'dairy'
   
class Milk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
    self.aisle = 'dairy'
 
class HeavyWhippingCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
    self.aisle = 'dairy'

class ParmeseanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'parmesean cheese'
    self.aisle = 'dairy'

class Butter(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butter'
    self.aisle = 'dairy'
  
class EvaporatedMilk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'evaporated milk'
    self.aisle = 'dairy'
  
class CreamCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cream cheese'
    self.aisle = 'dairy'
 
class SourCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'sour cream'
    self.aisle = 'dairy'
 
class MontereyJackCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'monterey jack cheese'
    self.aisle = 'dairy'
 
class CheddarCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cheddar cheese'
    self.aisle = 'dairy'
 
class ShreddedCheddar(Food): #same as above 
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'shredded cheddar'
    self.aisle = 'dairy'
 
#Veggies
class baby carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'baby carrots'
    self.aisle = 'veggie'

class Carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'carrots'
    self.aisle = 'veggie'

class Onion(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'onion'
    self.aisle = 'veggie'
 
class Spinach(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'spinach'
    self.aisle = 'veggie'
 
class FrozenBellPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen bell peppers'
    self.aisle = 'veggie'
  
class GreenOnions(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'green onions'
    self.aisle = 'veggie'
    
class DicedTomatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='14.5 oz'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'diced tomatoes'
    self.aisle = 'veggie' #can
 
class Zucchini(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'zucchini'
    self.aisle = 'veggie'
    
class SmallCabbage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'small cabbage'
    self.aisle = 'veggie'
  
class RedBellPepper(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red bell pepper'
    self.aisle = 'veggie'
  
class RainbowPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rainbow peppers'
    self.aisle = 'veggie'
  
  class ButternutSquash(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butternut squash'
    self.aisle = 'veggie'
   
class FrozenCorn(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen corn'
    self.aisle = 'veggie'
 
 class DarkRedKidneyBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'dark red kidney beans'
    self.aisle = 'veggie'

class GreenBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'grean beans'
    self.aisle = 'veggie'
  
class RedPotatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red potatoes'
    self.aisle = 'veggie'
 
 class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = 'veggie'
    #play with this one stalks change to bunches or pounds
 
class CannelliniBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cannellini beans('
    self.aisle = 'veggie'

class BlackBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'black beans'
    self.aisle = 'veggie'

class SalsaVerde(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'salsa verde'
    self.aisle = ''

class TomatoSauce(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'tomato Sauce'
    self.aisle = ''
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class ExtraWideEggNoodles(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'extra wide egg noodles'
    self.aisle = 'veggie'

class ItalianBreadCrumbs(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'italian bread crumbs'
    self.aisle = 'veggie'

class Orzo(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'orzo'
    self.aisle = 'pasta'
 
class Rigatoni(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rigatoni'
    self.aisle = 'veggie'

class PastaSauce(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'pasta sauce'
    self.aisle = 'veggie'
  
class FrozenCheeseTortellini(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen cheese tortellini'
    self.aisle = 'veggie'
    
class Cornflakes(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cornflakes'
    self.aisle = 'veggie'
    
class Egg(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'egg'
    self.aisle = 'veggie'
    
class Ritz(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ritz'
    self.aisle = 'veggie'
  
class Jalapeno(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'jalapeno'
    self.aisle = 'veggie'
  
class ElbowMacoroni(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'elbow macoroni'
    self.aisle = 'veggie'
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class PennePasta(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'penne pasta'
    self.aisle = 'veggie'
  
class ChiliPowder(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chili powder'
    self.aisle = 'veggie'
  
class Salt(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ritz'
    self.aisle = 'veggie'
  
class GroundCumin(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ground cumin'
    self.aisle = 'veggie'

  
class GarlicPowder(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'garlic powder'
    self.aisle = 'veggie'
  
class LowSodiumChickenBroth(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'low-sodium chicken broth'
    self.aisle = 'veggie'
    
  
class CornTortilla(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'corn tortilla'
    self.aisle = 'veggie'


#Non-food items
class FreezerBag(Food):
'''

'''use dictionary here foodlist
   d[parse[1]] = class(parse[0][0],
Parse[0][1]). Add if included'''
    #add tons of if statements
for food in d.keys():
    pass#d[food].aisle
 # == aisle up above enter in list?
#complete list of obj ingredients store list
#Sort this list based on aisle        
#for item in shopping_list:
#    print(item)

#counter = cleanPrint(shopping_list, True)
#print("\nAlso Stock your Pantry with these items:\n")
#cleanPrint(recipes.always_keep_stocked)

#Count all of the ingredients after adding them up.
'''
total = 0
for recipe in counter.keys():
    total = total + counter[recipe]
    print( recipe + " " + str(counter[recipe]))
print('* items are not needed until day of cooking.')

print("There are " + str(total) + " ingredients to buy. Not including pantry items.")
#print("There are " + str(len(counter.keys())) + " ingredients to buy. Not including pantry items.")
'''
