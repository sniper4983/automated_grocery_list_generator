class Recipe():
    '''Lists of recipes for automate grocery recipes contained in here'''
    def __init__(self):
        
        #1) recipes from new leaf wellness: changed into a list on python.

        #TODO can I get this to work teaspoons ounces have to match grocey list 
        #find a way to convert some produce to frozen
       self.chili_spiced_beef_and_carrots = ["2 lb beef chuck roast", '3 Tablespoon extra virgin olive oil', '2 Tablespoon red wine vinegar', '2 lb carrots', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin', '1/2 teaspoon paprika', '1/2 teaspoon garlic powder', '1/2 teaspoon onion powder', '1 gallon freezer bag',]
        self.monster_cheeseburgers = ['2 lb ground beef', '1 cup onion', '2 1/2 teaspoon Montreal steak seasoning mix',]
        self.tuscan_steak_and_green_peppers = ['2 lb sirloin tip roast', '2 green bell peppers', '2 teaspoon garlic', '1 cup onion', '1 14.5oz diced tomatoes', '2 Tablespoon extra virgin olive oil', '1 Tablespoon italian seasoning', '1 teaspoon salt', '1/2 teaspoon crushed red pepper', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.beef_and_cabbage_soup = ['1 lb ground beef', '1 small cabbage', '1 cup onion', '2 teaspoon garlic',  '4 carrots', '1 14.5oz diced tomatoes', '3 bay leaves', '1 teaspoon salt', '1 teaspoon pepper', '1 gallon freezer bag',] #test this with other carrot recipes, use weight and get frozen
        self.sloppy_joes = ['1 lb ground beef', '1 cup onion', '1 red bell pepper', '1 15oz tomato sauce', '2 Tablespoon light brown sugar', '1 Tablespoon worcestershire sauce', '2 teaspoons chili powder', '1/2 teaspoon garlic powder', '1/2 teaspoon salt', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.chicken_spinach_alfredo = ['1 lb chicken breast', '1 16oz heavy cream', '1 cup parmesean cheese',  '5 oz baby spinach', '2 teaspoon garlic', '1 teaspoon parsley', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.chicken_tikka_masala = ['2 lb chicken breast', '2 15oz tomato sauce', 'teaspoon garlic', '2 Tablespoon honey', '2 Tablespoon curry powder', '1/2 teaspoon onion powder', '1/2 teaspoon salt', '1 8oz heavy cream', '1 gallon freezer bag',]
        self.shredded_chicken_fajitas = ['2 lb chicken breast', '1 red bell pepper', '1 red onion', '1/4 cup extra virgin olive oil', '1 lime', '1 Tablespoon chili powder', '2 teaspoon ground cumin', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.chicken_cordon_bleu_casserole = ['1 8oz extra wide egg noodles', '2 lb chicken breast', '1 lb bone in ham bone steak', '1 8oz shredded swiss cheese', '1 8oz sour cream', '2 Tablespoon dijon mustard', '1/2 pepper', '1 cup italian bread crumbs', '2 Tablespoon butter', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil']
        self.chicken_and_sausage_orzo = ['1 lb italian sausage', '1 lb chicken breast', '2 oz baby spinich', '1 8oz tomato sauce', '1/2 teaspoon salt', '1 Tablespoon parsley', '1 teaspoon garlic powder', '1 teaspoon onion powder', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.italian_sausage_rigatoni = ['1 ground italian sausage' , '2 14.5oz diced tomatoes', '1 15oz tomato sauce', '1 cup onion', '1 red bell pepper', '2 Tablespoon olive oil', '1 teaspoon basil', '1 teaspoon oregano', '1 gallon freezer bag']
        #Garden Vegtable Soup with ground Turkey
        self.gvs_turkey = ['1 ground turkey','1/2 lb carrots', '1 lb zucchini', '1 cup onion', '1 15oz cannellini beans', ' 1 28oz tomato sauce', '1 Tablespoon  extra virgin olive oil', '1 teaspoon garlic', '1 Tablespoon  italian seasoning', '1/2 teaspoon salt', '1/4 teaspoon  pepper', '1 gallon freezer bag',]
        self.tuscan_tortellini_soup = ['1 24oz pasta sauce', '1 15oz cannellini beans', '1 lb carrots', '1 cup onion', '1/2 lb green beans', '5 oz baby spinich', '1 19oz frozen cheese tortellini', '1 gallon freezer bag']
        self.ranch_popcorn_chicken = ['2 lb chicken breast', '1 egg', '1 cup cornflakes', '1 cup parmesan cheese', '1 Tablespoon parsley', '1 teaspoon  garlic salt', '1 teaspoon onion powder', '3/4 teaspoon dill', '1/2 teaspoon pepper', '1 gallon freezer bag'] 
        self.cheesy_chicken_veggie_casserole = ['2 lb chicken breast', '1 16oz frozen mixed vegetables', '1/2 green onions', '8 oz milk', '8 oz sour cream', '1 8oz shredded cheddar','3/4 teaspoon garlic powder', '1/2 pepper', '3 cups ritz', '6 Tablespoon butter', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil']
        self.pulled_pork = ['3 lb pork shoulder', '1 cup onion', '1/4 cup apple cider vinegar', '2 Tablespoon honey', '2 Tablespoon chili powder', '1 teaspoon ground cumin', '1/2 teaspoon garlic powder', '1/2 teaspoon salt', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.sausage_and_peppers =['8 mild italian sausage links', '3 rainbow peppers', '1 cup onion', 'teaspoon garlic', '2 Tablespoons olive oil', '1/2 teaspoon basil', '1/2 teaspoon oregano', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil',]
        self.indian_butter_chicken = ['2 lb chicken thighs', '2 Tablespoon butter', '2 teaspoon onion powder', '2 15oz tomato sauce', '1 16oz heavy whipping cream', '2 Tablespoon garam masala', '2 Tablespoon curry powder', '2 teaspoon garlic', '1 gallon freezer bag',]
        self.creamy_chicken_penne = ['2 lb chicken breast', '1/2 cup parmesan cheese', '2 Tablespoon  olive oil', '1 14.5oz diced tomatoes', '2 teaspoon garlic', '1 16oz heavy cream', '1 teaspoon basil', '5 oz baby spinich', '1 gallon freezer bag',]
        self.salsa_verde_chicken = [ '2 lb chicken breast', '1 15oz black beans', '2 cups frozen corn', '1 16oz salsa verde', '1 gallon freezer bag',]
        self.taco_chili = ['1 lb ground beef', '1 cup onion',  '1 green bell pepper', '1 cup frozen corn', '1 teaspoon honey', '1 15oz tomato sauce', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin', '1/2 teaspoon paprika', '1/2 teaspoon garlic powder', '1/2 teaspoon onion powder', '4 oz shredded cheddar cheese', '1 box jiffy corn Muffin Mix', '1 gallon freezer bag',]
        self.chicken_taco_soup = ['1 lb chicken breast', '1 cup onion', '1 teaspoon garlic', '1 cup frozen corn', '1 28oz diced tomatoes', '1 4oz diced mild green chilies', '1 Tablespoon chili powder', '1 teaspoon pepper', '1/2 teaspoon ground oregano', '1 gallon freezer bag',]
        self.creamy_potato_soup = ['3 lb russet potatoes', '4 celery', '2 onion', '2 teaspoon garlic', '1 8oz frozen broccoli florets', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.japanese_beef_teriyaki = ['2 lb top sirloin', '1 Large green pepper', '1/2 cup low sodium sauce', '1/4 rice wine vinegar', '1/4 cup light brown sugar', '2 teaspoon garlic', '1 teaspoon ginger', '1 Tablespoon cornstarch', '1 teaspoon onion powder', '1/4 cup sesame seads', '1 gallon freezer bag',]
        self.korean_bbq_chicken = ['2 lb chicken thighs', '1 cup onion', '2 teaspoon garlic', '1/4 cup low sodium soy sauce', '1 lemon', '2 Tablespoon light brown sugar', '1 Tablespoon seasame oil', '1/2 teaspoon crushed red pepper flakes', '1 teaspoon ginger', '1 gallon freezer bag',]
        self.lebanese_sweet_potato_lentil_chili = ['1/2 cup dried lentils','1 15oz garbanzo', '1 15oz kidney beans', '2 cups chicken broth', '1 28oz diced tomatoes', '1 lb sweet potato', '2 teaspoon garlic', '1 Tablespoon curry powder', '2 teaspoons chili powder', '5 oz baby spinich', '1 gallon freezer bag',]
        self.singaporean_chicken_rice_stew = ['1 lb chicken breast', '3/4 cup dry enriched parboiled long grain rice', '1 teaspoon ginger', '1 cup onion', '1/2 lb carrots', '2 Tablespoons low sodium soy sauce', '1 Tablespoon sesame oil', '2 teaspoon garlic', '1 gallon freezer bag',]
        self.thai_green_curry_chicken = ['2 lb chicken breast', '2 15oz unsweetened coconut milk', '3 Tablespoons green curry paste', '1 cup onion', '1 Tablespoon low sodium soy sauce', '1 8oz bamboo shots', '1 red bell pepper', '1 8oz green beans', '1 gallon freezer bag',]
        self.bbq_maple_ribs = ['2 lb boneless pork ribs', '1 6oz tomato paste', '1/4 cup maple syrup', '2 Tablespoon apple cider vinegar', '1 Tablespoon chili powder', '2 teaspoon curry powder', '1 teaspoon paprika', '1 teaspoon onion powder', '1 teaspoon garlic powder', '1 teaspoon pepper', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.beef_and_quinoa_stuffed_peppers = ['6 small red bell peppers', '1/2 cup quinoa', '1 lb ground beef', '1 cup onion', '2 teaspoon garlic', '2 Tablespoon italian seasoning', '1 teaspoon salt', '1/2 teaspoon pepper',, '1 15oz tomato sauce', '1 quart freezer bag', '1 gallon freezer bag',]
        self.beef_and_sweet_potato_stew = ['1 1/2 lb stew meat', '1 cup onion', '1/2 lb carrots', '1 lb sweet potato', '1 cup frozen peas', '2 bay leaves', '1 Tablespoon parsley', '1 teaspoon salt', '1 teaspoon pepper', '1 teaspoon garlic powder', '1 teaspoon onion powder', '1 gallon freezer bag',] # add bay to exception list
        self.black_bean_sweet_potato_chili = ['3 15oz black beans', '1 lb sweat potato', '1 28oz diced tomatoes', '1 cup onion', '1 Tablespoon jalapeno,', '1 1/2 teaspoon garlic', '1 Tablespoon chili powder', '1 teaspoon cumin', '1/2 teaspoon pepper', '2 cups vegetable broth', '1 gallon freezer bag',] 
        self.cabbage_rolls_with_wild_rice = ['1 cabbage', '1 lb ground beef', '1 cup wild rice', '1 cup onion', '4 teaspoon italian seasoning', '1 28oz diced tomatoes', '1 15oz tomato sauce', '1 Tablespoon honey', '1/2 teaspoon salt', '1/2 teaspoon pepper', '2 gallon freezer bag',] # only only 6 cabbage leaves needed raise exception when called
        self.cherry_pot_roast_with_sweet_potatoes = ['2 lb beef chuck roast', '1 lb sweet potato', '1 cup onion', '1 12oz pitted dark sweet cherries', '3 Tablespoon extra virgin olive oil', '2 teaspoon garlic', '1 teaspoon thyme', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.chicken_artichoke_marinara = ['1 lb chicken breast', '1 cup onion', '1 red bell pepper', '2 teaspoon garlic', '1 28oz crushed tomatoes', '1 6oz tomato paste', '1 14oz quartered artichoke hearts', '1 Tablespoon honey', '1 Tablespoon basil', '1 teaspoon salt', '1/2 teaspoon crushed red pepper flakes', '1 gallon freezer bag',]
        self.chicken_lentil_curry_chili = ['1 lb chicken breast', ' 1 cup onion', '1 cup frozen peas', '1 cup french green lentils', '1 13.5 unsweetened coconut milk', '2 tablespoom apple cider vinegar', '1 Tablespoon honey', '1 Tablespoon curry powder', '1 Tablespoon gram masala', '1/2 teaspoon salt', '1/4 teaspoon red pepper flakes', '2 cups chicken broth',  '1 gallon freezer bag',]
        self.chicken_and_wild_rice_soup = ['1 lb chicken breast', '1 lb carrots', '1 cup celery', '1 cup onion', '2 teaspoon garlic', '1/4 cup garlic', '1 teaspoon basil', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1/4 teaspoon thyme', '1 gallon freezer bag',]
        self.citrus_chicken = ['2 lb chicken breast', '1 orange', '1 lemon', '1 lime', '2 teaspoon garlic', '1 Tablespoon honey', '1/2 teaspoon thyme', '1/2 teaspoon pepper', '1/2 teaspoon parsley', '1/2 teaspoon basil', '1 gallon freezer bag',]
        self.ginger_peach_pork_roast_with_green_beans = ['2 lb pork roast', '1 16oz frozen sliced peaches', '1 lb green beans', '1 teaspoon ginger', '1 1/2 teaspoon garlic', '1 Tablespoon honey', '1 Tablespoon apple cide vinegar', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.italian_chicken_and_quinoa_soup = ['1 lb chicken breast', '1 28oz diced tomatos', '1 15oz dark red kidney brans', '5 oz baby spinich', '1/4 cup quinoa', '1 Tablespoon italian seasoning', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.italian_meatballs = ['2 lb ground beef', '2 onion', '1/4 cup quinoa', '2 Tablespoon apple cider vinegar', '2 Tablespoon italian seasoning', '2 teaspoon garlic powder', '1 teaspoon paprika', '1 teaspoon fennel seeds', '1 teaspoon pepper', '1/2 teaspoon red pepper flakes', '1 28oz diced tomatoes', '1 150z tomato paste', '1 Tablespoon honey', '1/2 teaspoon salt', '1/2 teaspoon pepper', '3 gallon freezer bag',]        
        self.lemon_chicken_with_baby_spinach = ['2 lb chicken breast', '5 oz baby spinich', '2 teaspoon garlic', '1/4 cup extra virgin olive oil', '1 lemon', '1 Tablespoon parsley', '1 Tablespoon basil', '1/2 teaspoon pepper', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.maple_pork_roast_with_cinnamon_applesauce = ['2 lb pork roast', '2 lb mcintosh apples', '1/2 lemon', '2 Tablespoon maple syrup', '1 teaspoon cinnamon', '1 gallon freezer bag',]
        self.minestrone_soup_w_ground_beef = ['1 lb ground beef', '1 15oz dark red kidney beans', '2 oz baby spinich', '2 cups butternut squash', '2 cups zucchini', '1 cup onion', '1 14.5oz diced tomatoes', '1 Tablespoon italian seasoning', '1 teaspoon salt', '1 teaspoon pepper', '1 gallon freezer bag',]
        self.ratatouille = ['1 lb eggplant', '1/2 teaspoon salt', '1 cup onion', '2 teaspoon garlic', '1 28oz diced tomatoes', '1 15oz cannellini beans', '1 Tablespoon fennel seads', '1 teaspoon basil', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.savory_indian_chickpeas = ['2 15oz garbanzo beans', '1 cup onion', '1/2 lemon', '2 teaspoon garlic', '1 28oz crushed tomatoes', '1 4.25oz diced green chilies', '1 Tablespoon honey', '1 Tablespoon garam masala', '1 Tablespoon curry powder', '1 teaspoon chili powder', '1 gallon freezer bag',]
        self.spagetti_squash_with_marinara_sauce = ['1 28oz crushed tomatoes', '1 14.5 diced tomates', '1 cup onion', '2  teaspoon garlic', '1 Tablespoon honey', '1 Tablespoon italian seasoning', '1/2 teaspoon pepper', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.spiced_butternut_squash = ['2 lb butternut squash', '2 13.5 unsweetened coconut milk', '1 4.25 diced green chilies', '1 cup onion', '1 1/2 teaspoon garlic', '1 Tablespoon  curry powder', '1/2 teaspoon cumin', '1/2 teaspoon pepper', '1/4 teaspoon salt', '1 gallon freezer bag',]
        self.spicy_garlic_lime_chicken = ['2 lb chicken breast', '1/4 cup extra virgin olive oil', '1 lime', '3 teaspoon garlic', '1 cup onion', '1 cup onion', '1 teaspoon crushed red pepper', '1/2 teaspoon pepper', '1/4 teaspoon salt', '', '', '1 gallon freezer bag',]
        self.stuffed_pepper_soup = ['1 lb ground beef', '1/2 cup wild rice', '1 green bell pepper', '1 red bell pepper', '1 cup onion', '1 teaspoon garlic', '1 28oz diced tomatoes', '1 15oz tomato sauce', '2 teaspoons italian seasoning', '1 teaspoon salt', '1 gallon freezer bag',]
        self.sweet_potato_and_pork_burrito_bowl = ['2 lb pork roast', '1 1/2 lb sweet potato', '1 cup onion', '2 red bell pepper', '1 1/2 teaspoon garlic', '2 lime', '1 Tablespoon chili powder', '2 teaspoon cumin', '1/2 teaspoon crushed red pepper', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.sweet_potato_split_pea_soup = ['1 cup split speas', '1 cup onion', '1 1/2 teaspoon garlic', '1/4 cup carrots', '1 lb sweet potato', '2 roma tomato', '1 teaspoon pepper', '1/2 teaspoon thyme', '3 bay leaves', '1 gallon freezer bag',]
        self.sweet_n_spicy_thai_beef = ['2 lb sirloin tip roast', '1 cup onion', '1 13.5oz unsweetened coconut milk', '2 roma tomato', '1 green bell pepper', '1 lime', '1 tabelspoon honey', '1 teaspoon crushed red pepper', '1 teaspoon cumin', '1 teaspoon dried basil', '1 teaspoon ginger', '1 gallon freezer bag',]
        self.bbq_baby_back_ribs = ['3 lb baby back ribs', '1 cup ketchup', '1/4 cup light brown sugar', '2 Tablespoon worcersterhire sauce', '1 Tablespoon chili powder', '1 teaspoon paprika', '1 teaspoon curry powder', '1/2 teaspoon onion powder', '1/2 teaspoon garlic powder', '1/4 teaspoon pepper', '1 gallon freezer bag',]        
        self.classic_pot_roast = ['2 lb beef chuck shoulder roast', '1 lb russet potatoes', '1 lb carrots', '1 cup onion', '1/4 cup onion flakes', '1/4 teaspoon parsley', '1/4 teaspoon onion powder', '1/4 teaspoon celery seed', '1/4 teaspoon paprika', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.grandmas_beef_stew = ['1 lb beef chuck shoulder roast', '1 lb carrots', '2 lb russet potatoes', '1 cup onion', '1 teaspoon garlic', '1 teaspoon thyme', '1 teaspoon rosemary', '1 bay leaf', '1/2 teaspoon salt', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.hamburger_potato_soup = ['1/2 lb carrots', '8 oz russet potatoes', '1 cup onion', '1 28oz diced tomatoes', '1 Tablespoon extra virgin olive oil', '1 teaspoon garlic', '1 Tablespoon italian seasoning', '1/4 teaspoon pepper', '1 lb ground beef', '1 gallon freezer bag',]        
        self.italian_style_pot_roast = ['2 lb beef chuck shoulder roast', '1 cup onion', '1 28oz diced tomatoes', '1 teaspoon garlic', '1/4 cup honey', '2 Tablespoon extra virgin olive oil', '1 teaspoon oregano', '1/2 teaspoon parsley', '1/4 teaspoon pepper', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.orange_ginger_beef_with_soy_glaze = ['2 lb beef chuck shoulder roast', '1 navel orange', '2 tablespoom sugar', '2 Tablespoon apple cider vinegar', '1 Tablespoon low sodium soy sauce', '1 1/2 teaspoon garlic', '1 teaspoon ginger', '1 gallon freezer bag',] #orange ginger shredded beef with soy glaze
        self.spicy_beef_curry_stew = ['1 lb beef chuck shoulder roast', '1 lb carrots', '2 lb russet potatoes', '1 cup onion', '1 teaspoon garlic', '1 28oz diced tomatoes', '3 Tablespoon ginger', '2 Tablespoon curry powder', '1 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.meatball_veggie_soup = ['1 lb small meatballs', '1 24oz pasta sauce', '1 lb carrots', '3 cups green beans', '1 large zucchini', '1 cup onion', '1 gallon freezer bag',] #super simple meatball veggie soup
        self.taco_chili_with_cornbread = ['1 lb ground beef', '1 cup onion', '1 green bell pepper', '1 cup frozen corn', '1 teaspoon honey', '1 15oz tomato paste', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon cumin', '1/2 teaspoon crushed red pepper', '1/2 teaspoon paprika', '1/2 teaspoon garlic powder', '1/2 teaspoon onion powder', '1 gallon freezer bag',] #... topping
        self.coconut_chickpea_curry = ['2 15oz garbanzo beans', '1 cup onion', '1 teaspoon garlic', '1 14.5oz tomato sauce', '1 13.5oz coconut milk', '2 cup frozen peas', '3 Tablespoon honey', '2 Tablespoon curry powder', '1 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.curried_lentils = ['1 cup lentils', '2 cup vegetable broth', '1 13.5oz unsweetened coconut milk', '1 cup onion', '1 1/2 teaspoon garlic', '1/4 cup carrots', '1 Tablespoon curry powder', '1 gallon freezer bag',]
        self.oatmeal_chip_cookies = ['8 Tablespoon butter', '1 egg', '3/4 cup all-purpose flour', '1/2 cup old fasioned oats', '3/4 cup light brown sugar', '1/2 teaspoon baking powder', '1/2 teaspoon pure vanilla extract', '1/4 teaspoon salt', '1 cup semi sweet chocolate chips', '1 gallon freezer bag',]
        self.spiced_carrot_bread = ['1/2 lb carrots', '4 1/3 Tablespoon canola oil', '1/4 cup applesauce', '3 Tablespoon flax seed', '2 teaspoon pure vanilla extract', '4 egg', '3 cup all-purpose flour', '1 2/3 sugar', '2 teaspoon baking powder', '1 teaspoon baking soda', '1 teaspoon cinnamon', '1/2 teaspoon ground clove', '1/4 teaspoon nutmeg', '1 cooking spray', '1 disposable or aluminum loaf pan(9x5”)', 'aluminum foil',]
        self.ground_beef_stroganoff = ['2 lb ground beef', '1 12oz frozen peas', '8oz white mushroom', '1 cup onion', '2 teaspoon garlic', '2 cups sour cream', '2 cups beef broth', '1/4 cup worcestershire sauce', '1 gallon freezer bag',]
        self.monster_burgers = ['2 lb ground beef', '1 cup onion', '2 1/2 teaspoon Montreal steak seasoning mix', '1 gallon freezer bag',]
        self.steak_stir_fry_and_bok_choy_ = ['2 lb sirloin tip steak', '2 red bell pepper', '1 red onion', '1 1/2 lb bok choy', '1 teaspoon ginger', '2 teaspoon garlic', '1/4 cup low sodium soy sauce', '2 Tablespoon olive oil', '1 teaspoon peeper', '1/2 teaspoon salt', '1/2 teaspoon turmeric', '1/2 teaspoon basil', '1 gallon freezer bag',] #1 Tablespoon ginger is 1 teaspoon ground ginger
        self.tex_mex_beef_and_cabbage = ['1 lb ground beef', '8 oz bagged coleslaw mix', '1 15oz black beans', '1 14.5oz diced tomatoes', '1 cup frozen corn', '2 Tablespoon chili powder', '1 tab;espoon paprika', '1 Tablespoon cumin', '1 teaspoon garlic powder', '1 teaspoon onion powder', '1 teaspoon crushed red papper', '1 teaspoon salt', '1 gallon freezer bag',]
        self.artichoke_chicken = ['2 lb chicken', '1 14oz quartered artichoke hearts', '1 14.5oz diced tomatoes', '1 lemon', '1/2 cup dry white wine', '2 teaspoon garlic', '4 Tablespoon butter', '1 Tablespoon capers', '1 Tablespoon cornstarch', '1 gallon freezer bag',]
        self.chicken_enchiladas = ['lb chicken breast', '1 cup onion', '1 15oz tomato sauce', '1 1/2 teaspoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon cumin', '1/2 teaspoon crushed red pepper', '1/2 teaspoon garlic pepper', '1 gallon freezer bag',]
        self.cilantro_lime_chicken = ['2 lb chicken breast', '1/4 cup cilantro', '1 lime', '1/4 teaspoon salt', '1/4 teaspoon pepper', '1/4 teaspoon cumin', '4 Tablespoon butter', '1 gallon freezer bag',]
        self.cranberry_chicken = ['2 lb chicken breast', '1 cup onion', '12 oz cranberries', '1 naval orange', '1 teaspoon garlic', '1/2 cup light brown sugar', '2 Tablespoon balsalmic vinegar', '1/4 cup ketchup', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.honey_bourbon_chicken = ['2 lb chicken breast', '1/2 teaspoon crushed red pepper', '2 1/2 teaspoon garlic', '2 Tablespoon honey', '1/4 cup ketchup', '1/4 cup low sodium soy sauce', '1/4 cup light brown sugar', '1/2 cup apple juice', '1/4 cup bourbon', '3 Tablespoon cornstarch', '1 gallon freezer bag',]
        self.honey_garlic_chicken = ['2 lb chicken breast', '3 teaspoon garlic', '1/2 cup low sodium soy sauce', '1/2 cup honey', '1/4 cup ketchup', '1 Tablespoon dijon mustard', '1 teaspoon paprika', '1 teaspoon crushed red pepper', '3 Tablespoon cornstarch', '1 gallon freezer bag',]
        self.honey_mustard_chicken = ['2 lb chicken breast', '1/4 cup dijon mustard', '1/4 cup honey', '1/4 cup mayonnaise', '1/2 cup chicken broth', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1/2 teaspoon garlic salt', '1/2 teaspoon onion powder', '1 gallon freezer bag',]
        self.orange_chicken = ['2 lb chicken breast', '1 teaspoon garlic', '2 navel orange', '1 tablesoppn low sodium soy sauce', '1/4 cup light brown sugar', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.parmesan_crusted_chicken = ['2 lb chicken breast', '1 egg', '2 Tablespoon milk', '1/4 cup all-purpose flour', '1/2 cup parmesan chhese', '2 teaspoon paprika', '1/2 teaspoon salt', '1/2 teaspoon pepper', '4 Tablespoon butter', '1 gallon freezer bag',]
        self.thai_chicken = ['2 lb chicken breast', '1 cup onion', '1 green bell pepper', '1 13.5oz unsweetened coconut milk', '1 teaspoon crushed red pepper', '1 teaspoon cumin', '1 teaspoon basil', '1 teaspoon salt', '1 teaspoon ginger', '2 lime', '1 gallon freezer bag',]
        self.white_chicken_chili = ['1 lb chicken breast', '1 cup onion', '1 Tablespoon olive oil', '2 cups chicken broth', '16 oz salsa verde', '1 1/2 teaspoon cumin', '2 15oz cannelinni beans', '1 gallon freezer bag',]
        self.zesty_bbq_chicken = ['2 lb chicken breast', '1 cup ketchup', '1/2 cup light brown sugar', '2 Tablespoon apple cider vinegar', '1 teaspoon chili powder', '1 teaspoon onion powder', '1 teaspoon garlic podwer', '1 teaspoon basil', '1 teaspoon oregano', '1/2 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.chicken_and_pepper_stir_fry = ['2 lb chicken breast', '3 sweet bell pepper', '1 cup onion', '1 1/2 teaspoon garlic', '1/2 cup low sodium soy sauce', '1/4 cup rice wine vinegar', '2 Tablespoon light brown sugar', '1 teaspoon ginger', '1 Tablespoon cornstarch', '1 Tablespoon sesame oil', '1 gallon freezer bag',]
        self.chicken_and_sweet_potato_hash = ['2 lb chicken breast', '2 sweet potato', '3 oz baby spinich', '3 teaspoon garlic', '3 Tablespoon olive oil', '2 Tablespoon apple cider vinegar', '1 teaspoon roesemary', '1 teaspoon salt', '1 teaspoon pepper', '1 gallon freezer bag',]
        self.hawaiian_chicken_and_peppers = ['2 lb chicken breast', '1 green bell pepper', '1 red bell pepper', '2 Tablespoon cornstarch', '2 Tablespoon light brown sugar', '2 Tablespoon apple cider vinegar', '2 tablepoon low sodium soy sauce', '2 teaspoon garlic', '1/2 teaspoon ginger', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.honey_garlic_chicken_and_peas = ['2 lb chicken breast', '8 oz sugar snap peas', '1/4 cup carrots', '3 teaspoon garlic', '1/4 cup low sodium soy sauce', '2 Tablespoon seasame sauce', '2 Tablespoon ketchup', '1 teaspoon onion powder', '3/4 teaspoon salt', '1/4 teaspoon pepper', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.tuscan_chicken_tortellini = ['1 lb chicken breast', '3 oz baby spinich', '1 28oz diced tomatoes', '1 15oz tomato sauce', '2 Tablespoon olive oil', '1 Tablespoon basil', '1 Tablespoon oregano', '1 teaspoon onion powder', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.bbq_chicken = ['1 lb chicken breast', '3/4 cup ketchup', '1/4 cup light brown sugar', '3 Tablespoon apple cidar vinegar', '2 Tablespoon dijon mustard', '1 teaspoon paprika', '1/2 teaspoon onion powder', '1/2 teaspoon garlic powder', '1/4 teaspoon pepper', '1 gallon freezer bag',] 
        self.chicken_cheesesteaks = ['1 lb chicken breast', '1 cup onion', '2 red dell pepper', '1 green bell pepper', '1 teaspoon garlic', '1 Tablespoon extra virgin olive oil', '1 Tablespoon honey', '2 teaspoon apple cider vinegar', '1 gallon freezer bag',]
        self.chicken_tortilla_soup = ['1 lb chicken breast', '1 cup onion', '1 red bell pepper', '1 15oz diced tomatoes with green chilies', '1 1/2 cups frozen corn', '1 15oz black beans', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon cumin', '1/2 teaspoon garlic powder', '1 gallon freezer bag',]
        self.honey_dijon_chicken = ['2 lb chicken breast', '1/4 cup honey', '2 tabelspoon dijon mustard', '2 teaspoon pepper', '1/2 teaspoon salt', '1/2 teaspoon thyme', '1 gallon freezer bag',]
        self.lemon_pepper_chicken = ['2 lb chicken breast', '1/4 cup extra virgin olive oil', '1 lemon', '1/2 teaspoon pepper', '1/4 teaspoon salt', '1 gallon freezer bag',]
        self.orange_ginger_chicken = ['2 lb chicken breast', '1 orange', '3 Tablespoon ginger', '2 Tablespoon honey', '2 tab;espoon coconut oil', '1 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.red_pepper_chicken = ['2 lb chicken breast', '1 red bell pepper', '1/4 cup extra virgin olive oil', '2 teaspoon garlic', '1 cup onion', '1 teaspoon crushed red pepper', '1/2 teaspoon pepper', '1/4 teaspoon salt', '1 gallon freezer bag',]
        self.shredded_buffalo_chicken = ['1 lb chicken breast', '1 cup hot sauce', '4 Tablespoon butter', '2 Tablespoon distilled white vinegar', '1 teaspoon paprika', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.roasted_chicken_with_honey_lemon_carrots_and_red_potatoes = ['1 lb baby carrots', '1 lb red potatoes', '2 teaspoon garlic', '1 lemon', '2 Tablespoon honey', '2 Tablespoon olive oil', '1 teaspoon dried rosemary', '1/2 teaspoon pepper', '3 lb bone-in chicken thighs', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil',]
        self.asian_chicken_lettuce_wraps = ['2 lb ground chicken', '1 red bell pepper', '1 cup carrots', '2 teaspoon garlic', '1/4 cup low sodium soy sauce', '1/4 cup ketchup', '1 Tablespoon honey', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.breaded_pork_chops = ['1/4 cup all-purpose flour', '1 egg', '2 Tablespoon milk', '1 teaspoon dijon mustard', '1/2 cup italian-seasoning breadcrumbs', '2 Tablespoon parmesan cheese', '2 teaspoons parsley', '1/4 teaspoon garlic powder', '2 lb pork roast', '', '', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil'] # only have 1 foil in program 
        self.mediterranean_shredded_pork_pita_pockets = ['2 lb pork shoulder roast', '2 Tablespoon extra virgin olive oil', '1 teaspoon garlic', '1 Tablespoon paprika', '1 Tablespoon onion powder', '2 teaspoon oregano', '2 teaspoon basil', '1 teaspoon rosemary', '1/2 teaspoon pepper', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.pear_pork_tenderloin = ['2 lb pork tenderloin', '3 bosc pears', '1 1/2 teaspoon garlic', '1/4 cup apple cider vinegar', '1 Tablespoon honey', '1 teaspoon basil', '1 teaspoon pepper', '1/2 teaspoon salt', '1/2 teaspoon onion powder', '1 gallon freezer bag',]
        self.chinese_sweet_and_sour_pork = ['2 lb pork loin', '1 green bell pepper', '1 8oz can water chestnuts', '2 Tablespoon cornstarch', '1 20oz pineapple chunks in 100% juice', '1/4 light brown sugar', '3 Tablespoon apple cider vinagar', '3 low sodium soy sauce', '2 teaspoon garlic', '1 teaspoon ginger', '1 gallon freezer bag',]
        self.jalapeno_lime_shredded_pork_tacos = ['2 lb bone-in pork shoulder roast', '1 cup onion', '1 jalapeno', '2 limes', '1 Tablespoon honey', '1 teaspoon garlic', '1 teaspoon chili powder', '1/4 teaspoon salt', '1 gallon freezer bag',]
        self.jalepeno_and_bacon = ['1 lb elbow macoroni', '1 8oz monterey jack cheese,', '1 8oz cheddar cheese', '4 Tablespoon butter', '32 oz milk', '16 oz chicken broth', '1 jalepeno', '1/2 cup green onions', '6 slices bacon', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil']
        self.turkey_chili_with_butternut_squash = ['1 lb ground turkey', '2 cups butternut squash', '2 15oz black beans', '1 28 tomato sauce', '1 14.5 diced tomatoes', '1 Tablespoon chili powder', '1 Tablespoon cumin', '1/2 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.turkey_burger_macaroni = ['1 lb ground turkey', '1 cup onion', '1 teaspoon garlic', '4 cup tomato juice', '1 Tablespoon worcestershire sauce', '1 Tablespoon apple cider vinegar', '1 teaspoon pepper', '1 teaspoon ground mustard', '1 gallon freezer bag',]
        self.rice_and_bean_burrito_bowl = ['1 1/2 cup brown rice', '2 Tablespoon olive oil', '1 15oz black beans', '1 10oz diced tomatoes', '1 green bell pepper', '1 cup onion', '1 1/2 teaspoon garlic', '2 cups vegetable broth', '1 teaspoon chili powder', '1 teaspoon cumin', '1 gallon freezer bag',]
        self.black_bean_enchilada_stack = ['4 15oz black beans', '2 10oz diced tomatoes', '1 cup onion', '1 teaspoon garlic salt', '4 teaspoon chili powder', '4 teaspoon cumin', '1/2 teaspoon pepper', '8 corn tortilla', '8 oz cheddar cheese', '1 gallon freezer bag',]
        self.cheesy_eggplant_bake = ['8 oz mozzarella cheese', '1 lb eggplant', '1 15oz ricotta cheese', '1/2 cup parmesan cheese', '2 egg', '1 Tablespoon parsley', '3/4 teaspoon salt', '1/2 teaspoon pepper', '1/2 cup pasta sauce','1 quart freezer bag', '1 gallon freezer bag',]
        self.potato_corn_chowder = ['3 lb red potatoes', '1 cup celery', '1 cup onion', '2 teaspoon garlic', '8 oz frozen corn', '1/2 teaspoon pepper', '1 teaspoon salt', '1 teaspoon rosemary', '1 gallon freezer bag',]
        self.mexican_stuffed_peppers = ['6 red bell pepper', '1 15oz black bean', '1 cup onion', '8 oz frozen corn', '1 lime', '1 Tablespoon honey', '1 Tablespoon chili powder', '2 teaspoon cumin', '1/2 teaspoon garlic salt', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.thai_pineapple_curry = ['1 15oz garbanzo beans', '1 pineapple', '1 lb sweet potato', '1 green bell pepper', '1 cup onion', '1 teaspoon garlic', '1 13.5oz unsweetened coconut milk', '3 Tablespoon curry powder', '1 1/2 teaspoon salt', '1/2 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.three_bean_chili = ['2 15oz red kidney beans', '1 15oz pinto beans', '1 15oz black beans', '1 28oz tomato sauce', '1 14.5oz diced tomatoes', '2 teaspoon garlic', '2 Tablespoon light brown sugar', '1 Tablespoon chili powder', '2 teaspoon cumin', '1/4 teaspoon crushed red pepper', '1 gallon freezer bag',]
        self.zucchini_lasagna = ['1 3/4 lb zucchini', '1/2 cup pasta sauce', '8 oz low moisture part-skim mozzarella cheese', '1 15oz ricotta cheese', '1/2 cup parmesan cheese', '2 egg', '1 Tablespoon parley', '3/4 teaspoon salt', '1/2 teaspoon pepper', '1 disposable or aluminum baking pan(9x13”)', 'aluminum foil',]
        self.minestrone_soup = ['1 28oz diced tomatoes', '1/2 lb carrots', '1 lb green beans', '2 oz baby spinich', '1 cup onion', '2 teaspoon garlic', '1 15oz kidney beans', '1 15oz cannellini beans', '1 teaspoon honey', '2 Tablespoon italion seasoning', '1 bay leaf', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.bread_pudding = ['1/2 french baguette', '16 oz whole milk', '2 egg', '1/2 cup sugar', '1 teaspoon cinnamon', '1 teaspoon pure vanilla extract', '8 Tablespoon butter', '1 gallon freezer bag',]
        self.chocolate_cake = ['2 1/4 all-purpose flour', '1 1/2 cup sugar', '1/4 cup unsweetened cocoa powder', '1/2 teaspoon salt', '1 1/2 teaspoon white vinegar', '1 /12 teaspoon pure vanilla extract', '1/2 o;ive oil', '1 cup semi sweet chocolate chips', '1 gallon freezer bag',]
        self.blueberry_crisp = ['16 oz frozen blueberry', '1 1/2 cup old-fasioned oats', '1 1/2 all-purpose flour', '1 1/2 cup light brown sugar', '1/2 cup butter', '1 lemon', '1 gallon freezer bag',]
        
       self.names = [['chili spiced beef', 'monster cheese burgers', 'tuscan steak and green peppers'],
                      ['beef and cabbage soup', 'sloppy joes', 'chicken spinach alfredo'],
                      ['chicken tikka masala', 'shredded chicken fajitas', 'chicken cordon blue'],
                      ['chicken ans sausage orzo', 'italian susage rigatoni', 'ground turkey soup'],
                      ['tuscan tortellini soup', 'ranch popcorn chicken', 'cheesy chicken veggie caserole'],
                      ['pulled pork', 'sausage and peppers', 'potato corn chowder'],
                      ['jalepno and bacon', 'indian butter chickan', 'creamy chicken penne'],
                      ['salse verde chicken', 'minestrone soup w ground beef', 'cicken tortilla soup'],
                      ['taco chili', 'chicken taco soup', 'creamy potato soup'],
                      ['chinese sweet and sour pork', 'japanese beef teriyaki', 'korean bbq chicken'],
                      ['cilantro lime chicken', 'cranberry chicken', 'honey bourbon chicken'],
                      ['lebanese sweet potato lentil chili', 'singaporean chicken rice stew', 'thai green curry chicken'],
                      ['bbq maple ribs', 'beef and quinoa stuffed peppers', 'beef and sweet potato stew'],
                      ['black bean sweet potato chili', 'cabbage rolls with wild rice', 'cherry pot roast with sweet potatoes'],
                      ['chicken artichoke marinara', 'chicken lentil curry chili', 'chicken and wild rice soup'],
                      ['citrus chicken', 'ginger peach pork roast with green beans', 'italian chicken and quinoa soup'],
                      ['italian meatballs', 'lemon chicken with baby spinach', 'maple pork roast with cinnamon applesauce'],
                      ['ratatouille', 'savory indian chickpeas', 'artichoke chicken'],
                      ['chicken enchiladas', 'honey garlic chicken', 'honey mustard chicken'],
                      ['orange chicken', 'parmesan crusted chicken', 'thai chicken'],
                      ['white chicken chili', 'zesty bbq chicken', 'chicken and pepper stir fry'],
                      ['chicken and sweet potato hash', 'hawaiian chicken and peppers', 'honey garlic chicken and peas'],
                      ['tuscan chicken tortellini', 'bbq chicken', 'chicken cheesesteaks'],
                      ['honey dijon chicken', 'lemon pepper chicken', 'orange ginger chicken'],
                      ['red pepper chicken', 'shredded buffalo chicken', 'roasted chicken with honey lemon carrots and red potatoes'],
                      ['asian chicken lettuce wraps', 'breaded pork chops', 'mediterranean shredded pork pita pockets'],
                      ['pear pork tenderloin', 'chinese sweet and sour pork', 'jalapeno lime shredded pork tacos'],
                      ['turkey chili with butternut squash', 'turkey burger macaroni', 'rice and bean burrito bowl'],
                      ['black bean enchilada stack', 'cheesy eggplant bake', 'mexican stuffed peppers'],
                      ['thai pineapple curry', 'three bean chili', 'zucchini lasagna'],
                      ['spagetti squash with marinara sauce', 'spiced butternut squash soup', 'spicy garlic lime chicken'],
                      ['stuffed pepper soup', 'sweet potato and pork burrito bowl', 'sweet potato split pea soup'],
                      ['sweet n spicy thai beef', 'bbq baby back ribs', 'classic pot roast'],
                      ['grandmas beef stew', 'hamburger potato soup', 'italian style pot roast'], 
                      ['orange ginger shredded beef with soy glaze', 'spicy beef curry stew', 'super simple meatball veggie soup'],
                      ['taco chili with cornbread', 'coconut chickpea curry', 'curried lentils'],
                      ['oatmeal chip cookies', 'spiced carrot bread', 'ground beef stroganoff'],
                      ['monster burgers', 'steak stir fry and bok choy', 'tex mex beef and cabbage'],
                      ['creamy potato soup', 'minestrone soup', 'bread pudding'],
                      ['chocolate cake', 'easy blueberry crisp'],
                     ]

        
    def __str__(self):
        rep = ''
        col_width = max(len(word) for row in self.names for word in row) + 2  # padding
        for row in self.names:
            rep = rep + "".join(word.ljust(col_width) for word in row)
            rep = rep + '\n'
        return rep
