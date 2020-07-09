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
    
    for unit in [y for x in [grocery.units, grocery.other] for y in x]:
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
        groceries[item[2]] = grocery.Food(item[0], item[1], item[2], item[3])
    else:
        groceries[item[2]] =  groceries[item[2]] + grocery.Food(item[0], item[1], item[2], item[3])
        

recipes = Recipe()
border = "="*11
new_item = ''
grocerys = {}
shopping_list = []
names = recipes.cookbook.keys()
aisle = {'meat': [], 'produce': [], 'misc': [], 'canned': [], 'dairy': [],
         'frozen': [], 'seasonings': [], 'baking': [], }

file = open('shopping list.txt', 'w')

while new_item.upper() != "DONE":
    print("What should we buy from the store?  \n")
    print("Enter 'DONE' to stop adding items. \n'HELP' to see items.")
    print(border + "Remember: Enter all recipes before saying DONE."
          + border)
    
    new_item = input("Enter a Recipe: ")

    while new_item.upper() != 'DONE':

        if new_item.lower() in names:
            shopping_list.extend(recipes.cookbook[new_item.lower()])     
        elif new_item.upper() == "HELP":
            print(recipes)
        elif new_item.upper() != "DONE":
            print("Your item is invalid, try again. Type HELP to see all items.")
        new_item = input("Enter a Recipe: ")

#convert string to food classes
for ingredient in shopping_list:
    #(amount, measure, name, aisle)
    ingredient_tuple = parse(ingredient)
    updateShoppingList(ingredient_tuple, grocerys)
        
#sort list by aisle and print to file
for row in aisle.keys():
    for food in grocerys.values():
        if food.aisle == row:
            aisle[row].append(food)


#add conversions in here somehow

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
