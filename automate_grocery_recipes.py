from recipe import Recipe
import Food as F.

def updateShoppingList(item, groceries):
    '''start with an empty groceries dictionary and build list of food from Food objects
    that contain individual items of food from recipee.
    '''
    item.parse()
    if not (item.name in groceries):
        groceries[item.name] = item
    else:
        groceries[item.name] = groceries[item.name] + item

recipes = Recipe()
border = "="*11
new_item = ''
grocerys = {}
shopping_list = []
names = recipes.cookbook.keys()
aisle = {'meat': [], 'produce': [], 'misc': [], 'canned': [], 'dairy': [],
         'frozen': [], 'seasonings': [], 'baking': [], }
foodList = []

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

#convert recipe to list of ingredients
for item in shopping_list:
    currentFood = F.Food(item)
    foodList.append(currentFood)
    updateShoppingList(currentFood, grocerys)

#sort list by aisle and print to file
for row in aisle.keys():
    for food in grocerys.values():
        #if aisle equals row
        if food.aisle == row:
            aisle[row].append(food)

#add conversions in here somehow
for row, food in aisle.items():
    if food:
        if row == 'meat':
            file.write(str(row) + '\n')
        else:
            file.write('\n' + row + '\n')
    for i in food:
        print(str(i))
        file.write(str(i)  + '\n')
               
print('open shopping list.txt for list.')
file.close()

if foodList:
    for i in foodList:
        del i
