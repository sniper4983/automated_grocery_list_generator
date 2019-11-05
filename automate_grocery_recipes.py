import re
from recipe import Recipe
import Food
#import fractions

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

#will not work for 'red bell pepper'
def parse(foodStr):
    acceptMeasure []
    #checkre '/doz' as well as list
    fractionList = []
    name = ''
    num = None
    strList = re.split("\s", foodStr)
#[1,red,bell,pepper]
#dont make red measurement
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

def updateShoppingList(item, groceries):
    if not (item[2] in groceries)
        groceries[item[2]] = Food(item[0], item[1], item[2])
    else:
        groceries[item[2]] =  groceries[item[2]] + Food(item[0], item[1], item[2])

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
#assign aisle here, if user selects aisles to print list in
for ingredient in shopping_list:
    #(amount, measure, name)
    ingredient_Tuple = parse(ingredient)
    updateShoppingList(ingredient_tuple, groceries)
    #one list seperated by keys value is itsfood class
 
#sort list by aisle  
for row in Food.aisles:
    print(row)
    for food in groceries.values():#if food.aisle
        if food.aisle == row:
            print(food)
        
#create seperate file?

#Count all of the ingredients after adding them up.
'''
for item in store_list:
    #add another for loop
    print(item)
