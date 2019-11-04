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
#assign aisle here
for ingredient in shopping_list:
    #(amount, measure, name)
    ingredient_Tuple = parse(ingredient)
   
    if ingredient_Tuple[2] == 'chicken breast':
        if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ChickenBreast(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ChickenBreast(ingredient_Tuple[0], ingredient_Tuple[1])
   elif ingredient_Tuple[2] == 'beef chuck roast':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = BeefChuckRoast(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + BeefChuckRoast(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'ground beef':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GroundBeef(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GroundBeef(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'ground italian sausage':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GroundItalianSausage(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GroundItalianSausage(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'italian sausage':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ItalianSausage(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ItalianSausage(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'pork shoulder':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = PorkShoulder(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + PorkShoulder(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'bacon':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Bacon(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Bacon(ingredient_Tuple[0], ingredient_Tuple[1])
  elif ingredient_Tuple[2] == 'ground turkey':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GroundTurkey(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GroundTurkey(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'bone in ham bone steak':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = HamSteak(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + HamSteak(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'chicken thighs':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ChickenThighs(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ChickenThighs(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'sliced & fat trimmed boneless sirloin tip roast':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = SerloinTipRoast(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + SerloinTipRoast(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'american cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = AmericanCheese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + AmericanCheese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'heavy cream':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = HeavyCream(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + HeavyCream(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'milk':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Milk(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Milk(ingredient_Tuple[0], ingredient_Tuple[1])
elif ingredient_Tuple[2] == 'heavy whipping cream':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = HeavyWhippingCream(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + HeavyWhippingCream(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'parmsean cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ParmseanCheese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ParmseanCheese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'butter':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Butter(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Butter(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'evaporated milk':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = EvaporatedMik(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + EvaporatedMilk(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'cream cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = CreamCheese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + CreamCheese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'sour cream':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = (ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + (ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'monterey jack cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = MontereyJackChhese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + MonterEyJackChhese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'cheddar cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = CheedarCheese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + CheedarCheese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'shredded cheddar cheese':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ShreddedCheddarCheese(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ShreddedCheddarCheese(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'baby carrots':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = BabyCarrots(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + BabyCarrots(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'carrot': #fix for plural
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Carrots(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Carrots(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'onion':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Onion(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Onion(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'spinach':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Spinach(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Spinach(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'frozen bell peppers':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = FrozenBellPeppers(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + FrozenBellPeppers(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'green onions':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GreenOnions(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GreenOnions(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'diced tomatoes':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = DicedTomatoes(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + (ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'zucchini':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Zucchini(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Zucchini(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'small cabbage':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = SmallCabbage(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + SmallCabbage(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'red bell pepper':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = RedBellPepper(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + RedBellPepper(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'rainbow peppers':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = RainbowPeppers(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + RainbowPeppers(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'butternut squash':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ButternutSquash(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ButternutSquash(ingredient_Tuple[0], ingredient_Tuple[1])
elif ingredient_Tuple[2] == 'celery':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Celery(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Celery(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'dark red kidney beans':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = DarkRedKidneyBeans(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + DarkRedKidneyBeans(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'frozen corn':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = FrozenCorn(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + FrozenCorn(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'green beans':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GreenBeans(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GreenBeans(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'red potatoes':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = RedPotatoes(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + RedPotatoes(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'cannellini beans':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = CannelliniBeansingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + CannelliniBeans(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'black beans':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = (ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + BlackBeans(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'salsa verde':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = SalsaVerde(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + SalsaVerde(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'tomato sauce':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = TomatoSauce(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + TomatoSauce(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'extra wide egg noddles':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ExtraWideEggNoodles(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ExtraWideEggNoodles(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'rigatoni':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Rigatoni(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Rigatoni(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'orzo':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Orzo(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Orzo(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'italian bread crumbs':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ItalianBreadCrumbs(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ItalianBreadCrumbs(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'pasta sauce':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = PastaSauce(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + PastaSauce(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'frozen cheese tortellini':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = FrozenCheeseTortellini(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + FrozenCheeseTortellini(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'cornflakes':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Cornflakes(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Cornflakes(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'egg':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Egg(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Egg(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'ritz':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Ritz(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Ritz(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'jalapeno':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Jalapeno(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Jalapeno(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'elbow macaroni':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ElbowMacaroni(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ElbowMacaroni(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'penne pasta':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = PennePasta(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + PennePasta(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'salt':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = Salt(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + Salt(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'ground cumin':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GroundCumin(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GroundCumin(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'chili powder':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = ChiliPowder(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + ChiliPowder(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'low-sodium chicken broth':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = LowSodiumChickenBroth(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + LowSodiumChickenBroth(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'garlic powder':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = GarlicPowder(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + GarlicPowder(ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'corn tortilla':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = (ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + (ingredient_Tuple[0], ingredient_Tuple[1])
 elif ingredient_Tuple[2] == 'freezer bag':
    if not (food in groceries)
            groceries[ingredient_Tuple[2]] = FreezerBag(ingredient_Tuple[0], ingredient_Tuple[1])
        else:
            groceries[ingredient_Tuple[2]] =  groceries[ingredient_Tuple[2]] + FreezerBag

for food in d.keys():
    pass
#d[food].aisle
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
