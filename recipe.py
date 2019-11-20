class Recipe():
    '''Lists of recipes for automate grocery recipes contained in here'''
    def __init__(self):
        
        #1) recipes from new leaf wellness: changed into a list on python.
                #these recipes are incomplte

        #condence lists to say total amount of itesm, not split up as is now
        self.chili_spiced_beef_and_carrots = ["2 lb beef chuck roast", '2 lb baby carrots','1 gallon freezer bag',]
        self.monster_cheese_burgers = ['1 lb ground beef', 'american cheese']
        self.tuscan_steak_and_green_peppers = ['1 lb sliced & fat trimmed boneless sirloin tip roast', '1 frozen bell peppers','1 onion', '1 14.5oz DICED tomatoes', '1 gallon freezer bag',]
        self.beef_and_cabbage_soup = ['1  small cabage', '1 onion', 'x carrots', '1 14.5oz diced tomatoes', '1 gallon freezer bag',]
        self.sloppy_joes = ['1 onion','1 red bell pepper', '1 15oz tomato sauce', '1 gallon freezer bag',]
        self.chicken_spinach_alfredo = ['1 heavy cream', '1 heavy cream', '1 parmesean cheese',  '1 spinach', '1 gallon freezer bag',]
        self.chicken_tikka_masala = ['1 15oz tomato sauce','1 15oz tomato sauce','1 heavy cream', '1 gallon freezer bag',]
        self.shredded_chicken_fajitas = ['1 red bell pepper', '1 gallon freezer bag',]
        self.chicken_cordon_bleu_casserole = ['1 extra wide egg noodles','1 bone in ham bone steak', '1 swiss cheese', '1 sour cream', '1 italian bread crumbs', '1 gallon freezer bag',]
        self.chicken_and_sausage_orzo = ['1 italian_sausage', '1 8oz tomato sauce', '1 orzo','1 gallon freezer bag',]
        self.italian_sausage_rigatoni = ['1 ground italian sausage' , '1 14.5oz diced tomatoes','1 14.5oz diced tomatoes', '1 onion', '4.5 cups rigatoni', '1 gallon freezer bag']
        self.gvb_soup_turkey = ['1 ground turkey','1 carrots', '1 zucchini',]
        self.tuscaan_torellini_soup = ['1 24oz pasta sauce', '1 cannellini beans', '1 carrot', '1 onion', '1 green beans', '1 frozen cheese tortellini', '1 gallon freezer bag']
        self.ranch_popcorn_chicken = ['1 egg', '1 cornflakes',]
        self.cheesy_chicken_veggie_casserole = ['1 green onions', '1 milk', '1 shredded cheddar', '1 ritz', '1 gallon freezer bag',]
        self.pulled_pork = ['1 lb pork shoulder','1 lb pork shoulder' '1 onion', '1 gallon freezer bag',]
        self.suasage_and_peppers =['1 lb italian sausage', '1 rainbow peppers','1 rainbow peppers', '1 rainbow peppers', '1 onion', '1 gallon freezer bag',]
        self.potato_corn_chowder = ['1 red potatoes', '1 red potatoes', '1 red potatoes', '1 celery','1 evaporated milk', '1 gallon freezer bag',]
        self.jalepeno_and_bacon = ['1 elbow macoroni', '1 monterey jack cheese,', '1 cheddar cheese', '1 jalepeno', '1 onions', '1 bacon', '1 gallon freezer bag',]
        self.indian_butter_chicken = ['1 lb chicken thighs', '1 lb chicken thighs', '1 butter,' '1 15oz tomato sauce', '1 15oz tomato sauce', '1 heavy whipping cream', '1 heavy whipping cream', '1 gallon freezer bag',]
        self.creamy_chicken_penne = ['1 lb chicken breast', '1 lb chicken breast', '1 parmesan cheese', '1 14.5oz DICED tomatoes', '1 heavy cream', '1 heavy cream', '1 penne pasta', '1 gallon freezer bag',]
        self.salsa_verde_chicken = [ '1 lb chicken breast', '1 black beans', '1 frozen corn', '1 cream cheese', '1 salsa verde',]
        self.ministrone_soup_w_ground_beef = [ '1 dark red kidney beans', '1 spinach', '1 butternut squash', '1 zucchini', '1 onion', '1 gallon freezer bag',]
        self.chicken_tortilla_soup = ['1 onion', '1 red bell pepper', '1 14.5oz diced tomatoes', '1.5 cups frozen corn', '1 black beans', '1 tablespoon chili powder', '1/2 teaspoon salt', '1/2 teaspoon ground cumin','1/2 teaspoon garlic powder','4 cups low-sodium chicken broth*','4 corn tortillas*',]

    def __str__(self):
        rep = 'Options are: chili spiced beef and carrots, \nmonster cheese burgers, \ntuscan steak and green peppers, \nbeef and cabbage soup, \nsloppy joes, chicken spinach alfredo'
        rep += ', \nchicken tikka masala, \nshredded chicken fajitas, \nchicken cordon bleu casserole, \nchicken and sausage orzo, \nitalian sausage rigatoni, \ngvb soup turkey, \ntuscaan torellini soup, \nwhite chicken chili'
        rep += ', \nranch popcorn chicken, \ncheesy chicken veggie casserole, \npulled pork, \nsuasage and peppers, \npotato corn chowder, \njalepeno and bacon, \nindian butter chicken, \ncreamy chicken penne, \nsalsa verde chicken'
        rep += ', \nministrone soup w ground beef\nchicken tortilla soup'
        return rep
    
    '''
     self.meats = ['ground_beef','beef chuck shouulder', '1_Lb__chicken_breast','ground_turkey', 'ham', 'sliced _&_fat_trimmed_boneless_sirloin_tip_roast',]
        self.vegtables =['green bell peppers', 'frozen_bell_peppers', ]
        self.suggested_sides = ['potatoes','rice','broccoli', 'brussel sprouts',]

       
        self.chili_spiced_beef_and_carrots = ["1_Lb_beef_chuck_roast", "1_Lb_beef_chuck_roast", '1_lb_baby_carrots', '1_lb_baby_carrots','freezer_bag',]
        self.monster_cheese_burgers = ['1_Lb_ground_beef','1_Lb_ground_beef' , 'American_cheese']
        self.tuscan_steak_and_green_peppers = ['1_Lb_sliced _&_fat_trimmed_boneless_sirloin_tip_roast', 'frozen_bell_peppers','onion', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
        self.beef_and_cabbage_soup = ['1_Lb_ground_beef', 'small cabage', 'onion', 'carrots', '14.5_oz_DICED_tomatoes', 'freezer_bag',]
        self.sloppy_joes = ['1_Lb_ground_beef','onion','red_bell_pepper', '15_OZ. tomato_SAUCE', 'freezer_bag',]
        self.chicken_spinach_alfredo = ['1_Lb_1_Lb__chicken_breast', 'heavy_cream', 'heavy_cream', 'parmesean_cheese',  'spinach', 'freezer_bag',]
        self.chicken_tikka_masala = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', '15_OZ. tomato_SAUCE','15_OZ. tomato_SAUCE','heavy_cream', 'freezer_bag',]
        self.shredded_chicken_fajitas = ['1_Lb_1_Lb__chicken_breast', '1_Lb_1_Lb__chicken_breast', 'red_bell_pepper', 'freezer_bag',]
        self.chicken_cordon_bleu_casserole = ['extra_wide_egg_noodles', '1_Lb__chicken_breast', '1_Lb__chicken_breast','bone_in_ham_bone_steak', 'swiss_cheese', 'sour_cream', 'italian_bread_crumbs', 'freezer_bag',]
        self.chicken_and_sausage_orzo = ['italian_sausage', '1_Lb__chicken_breast', '8oz._tomatoe_SAUCE', 'orzo','freezer_bag', ]
        self.italian_sausage_rigatoni = ['ground_italian_sausage' , '14.5_oz_DICED_tomatoes','14.5_oz_DICED_tomatoes', 'onion', '4.5_cups_rigatoni', 'freezer_bag']
        self.gvb_soup_turkey = ['ground_turkey','carrots', 'zucchini',]
        self.tuscaan_torellini_soup = ['24oz_pasta_sauce', 'cannellini_beans', 'carrot', 'onion', 'green beans', 'frozen cheese tortellini', 'freezer_bag',]
        self.white_chicken_chili = ['1_Lb__chicken_breast', 'onion', 'salsa verde', 'cannellini_beans', 'cannellini_beans', 'freezer_bag', ]
        self.ranch_popcorn_chicken = [ 'egg','1_Lb__chicken_breast', '1_Lb__chicken_breast', 'cornflakes' ]
        self.cheesy_chicken_veggie_casserole = ['1_Lb__chicken_breast', '1_Lb__chicken_breast','green_onions', 'milk', 'shredded_cheddar', 'ritz', 'freezer_bag', ]
        self.pulled_pork = ['1_Lb_pork shoulder','1_Lb_pork_shoulder' 'onion', 'freezer_bag', ]
        self.suasage_and_peppers =[ '1_Lb_italian_sausage', 'rainbow_peppers','rainbow_peppers', 'rainbow_peppers', 'onion', 'freezer_bag',  ]
        self.potatoe_corn_chowder = ['red_potatoes', 'red_potatoes', 'red_potatoes', 'celery','evaporated_milk', 'freezer_bag', ]
        self.jalepeno_and_bacon = ['elbow_macoroni', 'monterey_jack_cheese,', 'cheddar_cheese', 'jalepeno', 'onions', 'bacon', 'freezer_bag', ]
        self.indian_butter_chicken = ['1_Lb_chicken_thighs', '1_Lb_chicken_thighs', 'butter,' '15oz_tomatoes_SAUCE', '15oz_tomatoes_SAUCE', 'heavy_whipping_cream', 'heavy_whipping_cream', 'freezer_bag', ]
        self.creamy_chicken_penne = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'parmesan cheese', '14.5_oz_DICED_tomatoes', 'heavy_cream', 'heavy_cream', 'penne pasta', 'freezer_bag',]
        self.salsa_verde_chicken = ['1_Lb__chicken_breast', '1_Lb__chicken_breast', 'black_beans', 'frozen_corn', 'cream_cheese', 'salsa_verde', ]
        self.ministrone_soup_w_ground_beef = ['1_Lb_ground_beef', 'dark_red_kidney_beans', 'spinach', 'butternut_squash', 'zucchini', 'onion', 'freezer_bag', ]
        self.chicken_tortilla_soup = chicken_tortilla_soup = [ '1_Lb__chicken_breast', 'onion', 'red_bell_pepper', '14.5_oz_DICED_tomatoes', '1.5 cups frozen corn', 'black_beans', '1TB Chili Powder', '1/2 tsp salt', '1/2 TEASPOON GROUND CUMIN','1/2 TEASPOON GARLIC POWDER', '4 CUPS LOW-SODIUM CHICKEN BROTH *NOT NEEDED UNTIL DAY OF COOKING','4 CORN TORTILLAS--SLICED *NOT NEEDED UNTIL DAY OF SERVING',
'''
