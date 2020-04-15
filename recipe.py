class Recipe():
    '''Lists of recipes for automate grocery recipes contained in here'''
    def __init__(self):
        
        #1) recipes from new leaf wellness: changed into a list on python.

        #TODO can I get this to work teaspoons ounces have to match grocey list 
        #find a way to convert some produce to frozen
        self.chili_spiced_beef_and_carrots = ["2 lb beef chuck roast", '3 Tablespoon extra virgin olive oil', '2 Tablespoon red wine vinegar', '2 lb carrots', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin', '1/2 teaspoon paprika', '1/2 teaspoon garlic powder', '1/2 teaspoon onion powder', '1 gallon freezer bag',]
        self.monster_cheese_burgers = ['2 lb ground beef', '4 slices american cheese', '1 onion', '2 1/2 teaspoon Montreal steak seasoning mix',]
        self.tuscan_steak_and_green_peppers = ['2 lb sliced & fat trimmed boneless sirloin tip roast', '2 green bell peppers', '4 cloves garlic', '1 onion', '1 14.5oz diced tomatoes', '2 Tablespoon extra virgin olive oil', '1 Tablespoon italian seasoning', '1 teaspoon salt', '1/2 teaspoon crushed red pepper', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.beef_and_cabbage_soup = ['1 lb ground beef', '1 small cabbage', '1 onion', '4 cloves garlic',  '4 carrots', '1 14.5oz diced tomatoes', '3 bay leaves', '1 teaspoon salt', '1 teaspoon pepper', '1 gallon freezer bag',] #test this with other carrot recipes
        self.sloppy_joes = ['1 lb ground beef', '1 onion', '1 red bell pepper', '1 15oz tomato sauce', '2 Tablespoon light brown sugar', '1 Tablespoon worcestershire sauce', '2 teaspoons chili powder', '1/2 teaspoon garlic powder', '1/2 teaspoon salt', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.chicken_spinach_alfredo = ['1 lb chicken breast', '1 16oz heavy cream', '1 cup parmesean cheese',  '5 oz baby spinach', '4 cloves garlic', '1 teaspoon parsley', '1/2 teaspoon salt', '1/2 teaspoon pepper', '1 gallon freezer bag',]
        self.chicken_tikka_masala = ['2 lb chicken breast', '2 15oz tomato sauce', '2 cloves garlic', '2 Tablespoon honey', '2 Tablespoon curry powder', '1/2 teaspoon onion powder', '1/2 teaspoon salt', '1 8oz heavy cream', '1 gallon freezer bag',]
        self.shredded_chicken_fajitas = ['2 lb chicken breast', '1 red bell pepper', '1 red onion', '1/4 cup extra virgin olive oil', '1 lime', '1 Tablespoon chili powder', '2 teaspoon ground cumin', '1/2 teaspoon salt', '1 gallon freezer bag',]
        self.chicken_cordon_bleu_casserole = ['1 8oz extra wide egg noodles', '2 lb chicken breast', '1 lb bone in ham bone steak', '1 8oz shredded swiss cheese', '1 8oz sour cream', '2 Tablespoon dijon mustard', '1/2 pepper', '1 cup italian bread crumbs', '2 Tablespoon butter', '1 disposable or aluminum baking pan(9x13)',]
        self.chicken_and_sausage_orzo = ['1 lb italian sausage', '1 lb chicken breast', '2 oz baby spinich', '1 8oz tomato sauce', '1/2 teaspoon salt', '1 Tablespoon parsley', '1 teaspoon garlic powder', '1 teaspoon onion powder', '1/2 teaspoon pepper', '1 cup orzo', '1 gallon freezer bag',]
        self.italian_sausage_rigatoni = ['1 ground italian sausage' , '2 14.5oz diced tomatoes', '1 15oz tomato sauce', '1 onion', '1 red bell pepper', '2 Tablespoon olive oil', '1 teaspoon basil', '1 teaspoon oregano', '4 1/2 cups rigatoni', '1 gallon freezer bag']
        self.gvs_turkey = ['1 ground turkey','1/2 lb carrots', '1 lb zucchini', '1 onion', '1 15oz cannellini beans', ' 1 28oz tomato sauce', '1 Tablespoon  extra virgin olive oil', '2 cloves garlic', '1 Tablespoon  italian seasoning', '1/2 teaspoon salt', '1/4 teaspoon  pepper',]
        self.tuscan_tortellini_soup = ['1 24oz pasta sauce', '1 15oz cannellini beans', '1 lb carrots', '1 onion', '1/2 lb green beans', '5 oz baby spinich', '1 19oz frozen cheese tortellini', '1 gallon freezer bag']
        self.ranch_popcorn_chicken = ['2 lb chicken breast', '1 egg', '1 cup cornflakes', '1 cup parmesan cheese', '1 Tablespoon parsley', '1 teaspoon  garlic salt', '1 teaspoon onion powder', '3/4 teaspoon dill', '1/2 teaspoon pepper', '4 Tablespoons butter', '1 gallon freezer bag'] 
        self.cheesy_chicken_veggie_casserole = ['2 lb chicken breast', '1 16oz frozen mixed vegetables', '1/2 green onions', '8 oz milk', '8 oz sour cream', '1 8oz shredded cheddar','3/4 teaspoon garlic powder', '1/2 pepper', '3 cups ritz', '6 Tablespoon butter', '1 disposable or aluminum baking pan(9x13)',]
        self.pulled_pork = ['3 lb pork shoulder', '1 onion', '1/4 cup apple cider vinegar', '2 Tablespoon honey', '2 Tablespoon chili powder', '1 teaspoon ground cumin', '1/2 teaspoon garlic powder', '1/2 teaspoon salt', '1/4 teaspoon pepper', '1 gallon freezer bag',]
        self.sausage_and_peppers =['8 mild italian sausage links', '3 rainbow peppers', '1 onion', '4 cloves garlic', '2 Tablespoons olive oil', '1/2 teaspoon basil', '1/2 teaspoon oregano', '1 disposable or aluminum baking pan(9x13)',]
        self.potato_corn_chowder = ['1 red potatoes', '1 red potatoes', '1 red potatoes', '1 celery', '1 evaporated milk', '1 gallon freezer bag',] #find recipe
        self.jalepeno_and_bacon = ['1 lb elbow macoroni', '1 8oz shredded monterey jack cheese,', '1 8oz shredded cheddar cheese', '4 Tablespoon butter', '32 oz milk', '1 jalepeno', '1/2 cup green onions', '6 slices bacon', '1 disposable or aluminum baking pan(9x13)',] #come back to
        self.indian_butter_chicken = ['2 lb chicken thighs', '2 Tablespoon butter', '2 teaspoon onion powder', '2 15oz tomato sauce', '1 16oz heavy whipping cream', '2 Tablespoon garam masala', '2 Tablespoon curry powder', '4 cloves garlic', '1 gallon freezer bag',]
        self.creamy_chicken_penne = ['2 lb chicken breast', '1/2 cup parmesan cheese', '2 Tablespoon  olive oil', '1 14.5oz diced tomatoes', '4 cloves garlic', '1 16oz heavy cream', '1 teaspoon basil', '5 oz baby spinich', '3 cups penne pasta', '1 gallon freezer bag',]
        self.salsa_verde_chicken = [ '2 lb chicken breast', '1 15oz black beans', '2 cups frozen corn', '1 cream cheese', '1 16oz salsa verde',]
        self.ministrone_soup_w_ground_beef = [ '1 28oz diced tomatoes', '1/2 lb carrots', '3 cups green beans', '2 oz baby spinich', '1 onion', '4 cloves garlic',  '1 15oz dark red kidney beans', '1 butternut squash', '1 zucchini', '1 onion', '1 gallon freezer bag',] #find recipe
        self.chicken_tortilla_soup = ['1 onion', '1 red bell pepper', '1 14.5oz diced tomatoes', '1 1/2 cups frozen corn', '1 black beans', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin','1/2 teaspoon garlic powder',]#test this with other chicken broths to see output $find recipe
        self.taco_chili = ['1 lb ground beef', '1 onion',  '1 green bell pepper', '1 cup frozen corn', '1 teaspoon honey', '1 15oz tomato sauce', '1 Tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin', '1/2 teaspoon paprika', '1/2 teaspoon garlic powder', '1/2 teaspoon onion powder', '4 oz shredded cheddar cheese', '1 box jiffy corn Muffin Mix', '1 gallon freezer bag',]
        self.chicken_taco_soup = ['1 lb chicken breast', '1 onion', '2 cloves garlic', '1 cup frozen corn', '1 28oz diced tomatoes', '1 4oz diced mild green chilies', '1 Tablespoon chili powder', '1 teaspoon pepper', '1/2 teaspoon ground oregano', '1 gallon freezer bag',]
        self.creamy_potato_soup = ['3 lb russet potatoes', '4 celery', '2 onion', '4 cloves garlic', '1 8oz frozen broccoli florets', '1/2 teaspoon pepper', '1 12oz evaporated milk',]
        
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
