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
        shopping_list.extend(recipes.monster_cheeseburgers)
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
    elif new_item == 'jalepeno and bacon': #mac and cheese
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
    elif new_item == 'minestrone_soup_w_ground_beef':
        shopping_list.extend(recipes.ministrone_soup_w_ground_beef)
    elif new_item == 'japanese beef teriyaki':
        shopping_list.extend(recipes.japanese_beef_teriyaki)
    elif new_item == 'korean bbq chicken':
        shopping_list.extend(recipes.korean_bbq_chicken)
    elif new_item == 'lebanese sweet potato lentil chili':
        shopping_list.extend(recipes.lebanese_sweet_potato_lentil_chili)
    elif new_item == 'singaporean chicken rice stew':
        shopping_list.extend(recipes.singaporean_chicken_rice_stew)
    elif new_item == 'thai green curry chicken':
        shopping_list.extend(recipes.thai_green_curry_chicken)
    elif new_item == 'bbq maple ribs':
        shopping_list.extend(recipes.bbq_maple_ribs)
    elif new_item == 'beef and quinoa stuffed peppers':
        shopping_list.extend(recipes.beef_and_quinoa_stuffed_peppers)
    elif new_item == 'beef and sweet potato stew':
        shopping_list.extend(recipes.beef_and_sweet_potato_stew)
    elif new_item == 'black bean sweet potato chili':
        shopping_list.extend(recipes.black_bean_sweet_potato_chili)
    elif new_item == 'cabbage rolls with wild rice':
        print('cabbage rolls with wild rice only need six cabbage leaves.')
        shopping_list.extend(recipes.cabbage_rolls_with_wild_rice)
    elif new_item == 'cherry pot roast with sweet potatoes':
        shopping_list.extend(recipes.cherry_pot_roast_with_sweet_potatoes)
    elif new_item == 'chicken artichoke marinara':
        shopping_list.extend(recipes.chicken_artichoke_marinara)
    elif new_item == 'chicken lentil curry chili':
        shopping_list.extend(recipes.chicken_lentil_curry_chili)
    elif new_item == 'chicken and wild rice soup':
        shopping_list.extend(recipes.chicken_and_wild_rice_soup)
    elif new_item == 'citrus chicken':
        shopping_list.extend(recipes.citrus_chicken)
    elif new_item == 'ginger peach pork roast with green beans':
        shopping_list.extend(recipes.ginger_peach_pork_roast_with_green_beans)
    elif new_item == 'italian chicken and quinoa soup':
        shopping_list.extend(recipes.italian_chicken_and_quinoa_soup)
    elif new_item == 'italian meatballs':
        shopping_list.extend(recipes.italian_meatballs)
    elif new_item == 'lemon chicken with baby spinach':
        shopping_list.extend(recipes.lemon_chicken_with_baby_spinach)
    elif new_item == 'maple pork roast with cinnamon applesauce':
        shopping_list.extend(recipes.maple_pork_roast_with_cinnamon_applesauce)
    elif new_item == 'ratatouille':
        shopping_list.extend(recipes.ratatouille)
    elif new_item == 'savory indian chickpeas':
        shopping_list.extend(recipes.savory_indian_chickpeas)
    elif new_item == 'spagetti squash with marinara sauce':
        shopping_list.extend(recipes.spagetti_squash_with_marinara_sauce)
    elif new_item == 'spiced butternut squash soup':
        shopping_list.extend(recipes.spiced_butternut_squash)
    elif new_item == 'spicy garlic lime chicken':
        shopping_list.extend(recipes.spicy_garlic_lime_chicken)
    elif new_item == 'stuffed pepper soup':
        shopping_list.extend(recipes.stuffed_pepper_soup)
    elif new_item == 'sweet potato and pork burrito bowl':
        shopping_list.extend(recipes.sweet_potato_and_pork_burrito_bowl)
    elif new_item == 'sweet potato split pea soup':
        shopping_list.extend(recipes.sweet_potato_split_pea_soup)
    elif new_item == 'sweet n spicy thai beef':
        shopping_list.extend(recipes.sweet_n_spicy_thai_beef)
    elif new_item == 'bbq baby back ribs':
        shopping_list.extend(recipes.bbq_baby_back_ribs)
    elif new_item == 'classic pot roast':
        shopping_list.extend(recipes.classic_pot_roast)
    elif new_item == 'grandmas beef stew':
        shopping_list.extend(recipes.grandmas_beef_stew)
    elif new_item == 'hamburger potato soup':
        shopping_list.extend(recipes.hamburger_potato_soup)
    elif new_item == 'italian style pot roast':
        shopping_list.extend(recipes.italian_style_pot_roast)
    elif new_item == 'orange ginger beef with soy glaze':
        shopping_list.extend(recipes.orange_ginger_beef_with_soy_glaze)
    elif new_item == 'spicy beef curry stew':
        shopping_list.extend(recipes.spicy_beef_curry_stew)
    elif new_item == 'meatball veggie soup':
        shopping_list.extend(recipes.meatball_veggie_soup)
    elif new_item == 'coconut chickpea curry':
        shopping_list.extend(recipes.coconut_chickpea_curry)
    elif new_item == 'curried lentils':
        shopping_list.extend(recipes.curried_lentils)
    elif new_item == 'oatmeal chip cookies':
        shopping_list.extend(recipes.oatmeal_chip_cookies)
    elif new_item == 'spiced carrot bread':
        shopping_list.extend(recipes.spiced_carrot_bread)
    elif new_item == 'ground beef stroganoff':
        shopping_list.extend(recipes.ground_beef_stroganoff)
    elif new_item == 'monster burgers':
        shopping_list.extend(recipes.monster_burgers.)
    elif new_item == 'steak stir fry and bok choy':
        shopping_list.extend(recipes.steak_stir_fry_and_bok_choy)
    elif new_item == 'tex mex beef and cabbage':
        shopping_list.extend(recipes.tex_mex_beef_and_cabbage)
    elif new_item == 'artichoke chicken':
        shopping_list.extend(recipes.artichoke_chicken)
    elif new_item == 'chicken enchiladas':
        shopping_list.extend(recipes.chicken_enchiladas)
    elif new_item == 'cilantro lime chicken':
        shopping_list.extend(recipes.cilantro_lime_chicken)
    elif new_item == 'cranberry chicken':
        shopping_list.extend(recipes.cranberry_chicken)
    elif new_item == 'honey bourbon chicken':
        shopping_list.extend(recipes.honey_bourbon_chicken)
    elif new_item == 'honey garlic chicken':
        shopping_list.extend(recipes.honey_garlic_chicken)
    elif new_item == 'honey mustard chicken':
        shopping_list.extend(recipes.honey_mustard_chicken)
   elif new_item == 'orange chicken':
        shopping_list.extend(recipes.orange_chicken)
    elif new_item == 'parmesan crusted chicken':
        shopping_list.extend(recipes.parmesan_crusted_chicken)
    elif new_item == 'thai chicken':
        shopping_list.extend(recipes.thai_chicken)
    elif new_item == 'white chicken chili':
        shopping_list.extend(recipes.white_chicken_chili)
    elif new_item == 'zesty bbq chicken':
        shopping_list.extend(recipes.zesty_bbq_chicken)
    elif new_item == 'chicken and pepper stir fry':
        shopping_list.extend(recipes.chicken_and_pepper_stir_fry)
    elif new_item == 'chicken and sweet potato hash':
        shopping_list.extend(recipes.chicken_and_sweet_potato_hash)
    elif new_item == 'hawaiian chicken and peppers':
        shopping_list.extend(recipes.hawaiian_chicken_and_peppers)
    elif new_item == 'honey garlic chicken and peas':
        shopping_list.extend(recipes.honey_garlic_chicken_and_peas)
    elif new_item == 'tuscan chicken tortellini':
        shopping_list.extend(recipes.tuscan_chicken_tortellini)
    elif new_item == 'bbq chicken':
        shopping_list.extend(recipes.bbq_chicken)
    elif new_item == 'chicken cheesesteaks':
        shopping_list.extend(recipes.chicken_cheesesteaks)
    elif new_item == 'honey dijon chicken':
        shopping_list.extend(recipes.honey_dijon_chicken)
    elif new_item == 'lemon pepper chicken':
        shopping_list.extend(recipes.lemon_pepper_chicken)
    elif new_item == 'orange ginger chicken':
        shopping_list.extend(recipes.orange_ginger_chicken)
    elif new_item == 'red pepper chicken':
        shopping_list.extend(recipes.red_pepper_chicken)
    elif new_item == 'shredded buffalo chicken':
        shopping_list.extend(recipes.shredded_buffalo_chicken)
    elif new_item == 'roasted chicken with honey lemon carrots and red potatoes':
        shopping_list.extend(recipes.roasted_chicken_with_honey_lemon_carrots_and_red_potatoes)
    elif new_item == 'asian chicken lettuce wraps':
        shopping_list.extend(recipes.asian_chicken_lettuce_wraps)
    elif new_item == 'breaded pork chops':
        shopping_list.extend(recipes.breaded_pork_chops)
    elif new_item == 'mediterranean shredded pork pita pockets':
        shopping_list.extend(recipes.mediterranean_shredded_pork_pita_pockets)
    elif new_item == 'pear_pork_tenderloin':
        shopping_list.extend(recipes.pear_pork_tenderloin)
    elif new_item == 'chinese sweet and sour pork':
        shopping_list.extend(recipes.chinese_sweet_and_sour_pork)
    elif new_item == 'jalapeno lime shredded pork tacos':
        shopping_list.extend(recipes.jalapeno_lime_shredded_pork_tacos)
    elif new_item == 'turkey chili with butternut squash':
        shopping_list.extend(recipes.turkey_chili_with_butternut_squash)
    elif new_item == 'turkey burger macaroni':
        shopping_list.extend(recipes.turkey_burger_macaroni)
    elif new_item == 'rice and bean burrito bowl':
        shopping_list.extend(recipes.rice_and_bean_burrito_bowl)
    elif new_item == 'cheesy eggplant bake':
        shopping_list.extend(recipes.cheesy_eggplant_bake)
    elif new_item == 'black bean enchilada stack':
        shopping_list.extend(recipes.black_bean_enchilada_stack)
    elif new_item == 'mexican stuffed peppers':
        shopping_list.extend(recipes.mexican_stuffed_peppers)
    elif new_item == 'thai pineapple curry':
        shopping_list.extend(recipes.thai_pineapple_curry)
    elif new_item == 'three bean chili':
        shopping_list.extend(recipes.three_bean_chili)
    elif new_item == 'zucchini lasagna':
        shopping_list.extend(recipes.zucchini_lasagna)
    elif new_item == 'minestrone soup':
        shopping_list.extend(recipes.minestrone_soup)
    elif new_item == 'bread pudding':
        shopping_list.extend(recipes.bread_pudding)
    elif new_item == 'chocolate cake':
        shopping_list.extend(recipes.chocolate_cake)
    elif new_item == 'blueberry crisp':#clean up strings
        shopping_list.extend(recipes.blueberry_crisp)
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
