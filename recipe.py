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
        
    def __str__(self):
        #tabular format, this list is too long (name\t\tname\t\tname\n)
        rep = 'Options are: chili spiced beef and carrots, \nmonster cheese burgers, \ntuscan steak and green peppers, \nbeef and cabbage soup, \nsloppy joes, chicken spinach alfredo'
        rep += ', \nchicken tikka masala, \nshredded chicken fajitas, \nchicken cordon bleu casserole, \nchicken and sausage orzo, \nitalian sausage rigatoni, \ngarden vegetable soup, \ntuscaan torellini soup, \nwhite chicken chili'
        rep += ', \nranch popcorn chicken, \ncheesy chicken veggie casserole, \npulled pork, \nsuasage and peppers, \npotato corn chowder, \njalepeno and bacon, \nindian butter chicken, \ncreamy chicken penne, \nsalsa verde chicken'
        rep += ', \nministrone soup w ground beef\nchicken tortilla soup,\nchicken taco soup,\ntaco chili w cornbread topping\ncreamy potato soup'
        return rep
