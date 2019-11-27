from recipe import Recipe
import Food
from mixed_fractions import Mixed

def parse(foodStr):
    name = ''
    num = ''
    mType = ''
    strList = foodStr.split()

    for i in strList[:]:
        if strList[0].find('/') >= 0:
            num = num + ' ' + strList[0]
            strList.pop(0)
        elif strList[0].isdigit():
            num = strList[0]
            strList.pop(0)
            continue
        if not strList[0].isdigit() or strList[0].find('/') == -1:
            break
        
    #if no number is provided assume the number will be 1
    if num == '':
        amount = Mixed(1)
    else:
        amount = Mixed(num)
    
    for unit in [y for x in [Food.units, Food.other] for y in x]:
        if strList[0].find(unit) != -1:
            mType = strList[0]
            strList.pop(0)

    for i in range(len(strList)):
        if i == len(strList) - 1:
            name = name + strList[i]
        else:
            name = name + strList[i] + ' '
            
    return (amount, mType, name, grocery.aisles[name])

def updateShoppingList(item, groceries):
    if not (item[2] in groceries):
        groceries[item[2]] = Food.Food(item[0], item[1], item[2], item[3])
        print(grocerys[ingredient_tuple[2]])
    else:
        groceries[item[2]] =  groceries[item[2]] + Food.Food(item[0], item[1], item[2], item[3])
        

recipes = Recipe()
border = "="*11
new_item = ''
grocerys = {}
shopping_list = []
aisle = {'meat': [], 'produce': [], 'misc': [], 'canned': [], 'dairy': [],
         'frozen': [], 'seasonings': [], 'baking': [], }


file = open('shopping list.txt', 'w')

while new_item.upper() != "DONE":
    print("What should we buy from the store?  \n")
    print("Enter 'DONE' to stop adding items. \n'HELP' to see items.")
    print(border + "Remember: Recipes must be entered as a list in the program first"
          + border)
    
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
    elif new_item == 'garden vegetable soup':
        shopping_list.extend(recipes.gvs_turkey)
    elif new_item == 'tuscan tortellini soup':
        shopping_list.extend(recipes.tuscan_tortellini_soup)
    elif new_item == 'white chicken chili':
        shopping_list.extend(recipes.white_chicken_chili)
    elif new_item == 'ranch popcorn chicken':
        shopping_list.extend(recipes.ranch_popcorn_chicken)
    elif new_item == 'cheesy chicken veggie casserole':
        shopping_list.extend(recipes.cheesy_chicken_veggie_casserole)
    elif new_item == 'pulled pork':
        shopping_list.extend(recipes.pulled_pork)
    elif new_item == 'sausage and peppers':
        shopping_list.extend(recipes.sausage_and_peppers)
    elif new_item == 'potato corn chowder':
        shopping_list.extend(recipes.potato_corn_chowder)
    elif new_item == 'jalepeno and bacon':
        shopping_list.extend(recipes.jalepeno_and_bacon)
    elif new_item == 'indian butter chicken':
        shopping_list.extend(recipes.indian_butter_chicken)
    elif new_item == 'salsa verde chicken':
        shopping_list.extend(recipes.salsa_verde_chicken)
    elif new_item == 'chicken tortilla soup':
        shopping_list.extend(recipes.chicken_tortilla_soup)
    elif new_item == 'creamy potato soup':
        shopping_list.extend(recipes.creamy_potato_soup)
    elif new_item == 'chicken taco soup':
        shopping_list.extend(recipes.chicken_taco_soup)
    elif new_item == 'taco chili w cornbread topping':
        shopping_list.extend(recipes.taco_chili)
    elif new_item == 'creamy chicken penne':
        shopping_list.extend(recipes.creamy_chicken_penne)
    elif new_item == 'ministrone_soup_w_ground_beef':
        shopping_list.extend(recipes.ministrone_soup_w_ground_beef)
    elif new_item.upper() == "HELP":
        print(recipes)
    elif new_item.upper() != "DONE":
        print("Your item is invalid, try again. Type HELP to see all items.")


#convert string to food classes
for ingredient in shopping_list:
    (amount, measure, name, aisle)
    ingredient_tuple = parse(ingredient)
    print(ingredient_tuple)
    updateShoppingList(ingredient_tuple, grocerys)
    

#sort list by aisle and print to file
for row in aisle.keys():
    for food in grocerys.values():
        if food.aisle == row:
            aisle[row].append(food)

for row, food in aisle.items():
    if food:
        if row == 'meat':
            file.write(row + '\n')
        else:
            file.write('\n' + row + '\n')
        print(row) #delete prints when done
    for i in food:
        print(i)
        file.write(str(i)  + '\n')
           
print('open shopping list.txt for list.')
file.close()
