from mixed_fractions import Mixed

class Food():
  """Base class for all food in shopping list."""
  #aisle where food is located in store
  def __init__(self, foodStr):

    '''
    These are my names to locate to
    meat, dairy, baking, misc,
    frozen, produce,canned,
    seasonings
    TODO:
    diced produce can be converted to frozen
    add plural versions in here
    '''

    self.aisles = {}
    self.aisles['beef chuck roast'] = 'meat'
    self.aisles['ground beef'] = 'meat'
    self.aisles['sirloin tip roast'] = 'meat'
    self.aisles['chicken breast'] = 'meat'
    self.aisles['chicken thighs'] = 'meat'
    self.aisles['bone in ham bone steak'] = 'meat'
    self.aisles['pork shoulder'] = 'meat'
    self.aisles['onion'] = 'frozen'
    self.aisles['onions'] = 'frozen'
    #continue plurals below here'
    self.aisles['red onion'] = 'produce'
    self.aisles['red bell pepper'] = 'produce'
    self.aisles['cabbage'] = 'produce'
    self.aisles['carrots'] = 'produce' #frozen
    self.aisles['spinich'] = 'produce'
    self.aisles['zucchini'] = 'produce'
    self.aisles['rainbow peppers'] = 'produce'
    self.aisles['butternut squash'] = 'produce'
    self.aisles['ground turkey'] = 'meat'
    self.aisles['bacon'] = 'meat'
    self.aisles['american cheese'] = 'dairy'
    self.aisles['shredded cheddar cheese'] = 'dairy'
    self.aisles['celery'] = 'produce'
    self.aisles['ground italian sausage'] = 'meat'
    self.aisles['shredded swiss cheese'] = 'dairy'
    self.aisles['diced tomatoes'] = 'canned'
    self.aisles['heavy whipping cream'] = 'dairy'
    self.aisles['egg'] = 'dairy'
    self.aisles['eggplant'] = 'produce'
    self.aisles['orzo'] = 'misc'
    self.aisles['italian sausage'] = 'meat'
    self.aisles['cheddar cheese'] = 'dairy'
    self.aisles['monterey jack cheese'] = 'dairy'
    self.aisles['milk'] = 'dairy'
    self.aisles['tortillas'] = 'misc'
    self.aisles['salsa verde'] = 'misc'
    self.aisles['heavy cream'] = 'dairy'
    self.aisles['freezer bag'] = 'misc'
    self.aisles['frozen bell peppers'] = 'produce'
    self.aisles['parmesean cheese'] = 'misc'
    self.aisles['tomato sauce'] = 'canned'
    self.aisles['extra wide egg noodles'] = 'misc'
    self.aisles['italian bread crumbs'] = 'misc'
    self.aisles['rigatoni'] = 'misc'
    self.aisles['green onions'] = 'produce'
    self.aisles['red potatoes'] = 'produce'
    self.aisles['chili powder'] = 'seasonings'
    self.aisles['salt'] = 'seasonings'
    self.aisles['pepper'] = 'seasonings'
    self.aisles['cumin'] = 'seasonings'
    self.aisles['frozen corn'] = 'frozen'
    self.aisles['cream cheese'] = 'dairy'
    self.aisles['dark red kidney beans'] = 'canned'
    self.aisles['red kidney beans'] = 'canned'
    self.aisles['kidney beans'] = 'canned'
    self.aisles['black beans'] = 'canned'
    self.aisles['pinto beans'] = 'canned'
    self.aisles['penne pasta'] = 'misc'
    self.aisles['butter'] = 'dairy'
    self.aisles['elbow macoroni'] = 'misc'
    self.aisles['evaporated milk'] = 'baking'
    self.aisles['cannellini_beans'] = 'canned'
    self.aisles['green beans'] = 'produce'
    self.aisles['pasta sauce'] = 'misc'
    self.aisles['sour cream'] = 'dairy'
    self.aisles['frozen cheese tortellini'] = 'frozen'
    self.aisles['cornflakes'] = 'misc'
    self.aisles['ritz'] = 'misc'
    self.aisles['apple cider vinegar'] = 'misc'
    self.aisles['corn tortilla'] = 'misc'
    self.aisles['extra virgin olive oil'] = 'misc'
    self.aisles['olive oil'] = 'misc'
    self.aisles['red wine vinegar'] = 'misc'
    self.aisles['paprika'] = 'seasonings'
    self.aisles['garlic powder'] = 'seasonings'
    self.aisles['onion powder'] = 'seasonings'
    self.aisles['Montreal steak seasoning mix'] = 'seasonings'
    self.aisles['garlic'] = 'produce' #1/2 teaspoon = 1 clove garlic
    self.aisles['parsley'] = 'seasonings'
    self.aisles['honey'] = 'misc'
    self.aisles['curry powder'] = 'seasonings'
    self.aisles['disposable or aluminum baking pan(9x13)'] = 'misc'
    self.aisles['bay leaves'] = 'seasonings'
    self.aisles['bay leaf'] = 'seasoninga'
    self.aisles['light brown sugar'] = 'baking'
    self.aisles['worcestershire sauce'] = 'misc'
    self.aisles['lime'] = 'produce'
    self.aisles['dijon mustard'] = 'misc'
    self.aisles['baby spinich'] = 'produce'
    self.aisles['cooking spray'] = 'misc'
    self.aisles['bok choy'] = 'produce'
    self.aisles['basil'] = 'seasonings'
    self.aisles['oregano'] = 'seasonings'
    self.aisles['nutmeg'] = 'seasonings'
    self.aisles['italian seasoning'] = 'seasonings'
    self.aisles['garlic salt'] = 'seasonings'
    self.aisles['dill'] = 'seasonings'
    self.aisles['frozen mixed vegetables'] = 'frozen'
    self.aisles['mild italian sausage links'] = 'meat'
    self.aisles['meatballs'] = 'frozen'
    self.aisles['garam masala'] = 'seasonings'
    self.aisles['jiffy corn Muffin Mix'] = 'baking'
    self.aisles['russet potatoes'] = 'produce'
    self.aisles['frozen broccoli florets'] = 'frozen'
    self.aisles['green bell peppers'] = 'frozen' 
    self.aisles['green pepper'] = 'produce' #green bell peppers that can not be frozen
    self.aisles['crushed red pepper flakes'] = 'seasonings'
    self.aisles['baby spinach'] = 'produce'
    self.aisles['cannellini beans'] = 'canned'
    self.aisles['parmesan cheese'] = 'misc'
    self.aisles['chicken thighs'] = 'meat'
    self.aisles['green bell pepper'] = 'produce'
    self.aisles['diced mild green chilies'] = 'canned'
    self.aisles['ground oregano'] = 'seasonings'
    self.aisles['pork loin'] = 'meat'
    self.aisles['water chestnuts'] = 'canned'
    self.aisles['cornstarch'] = 'misc'
    self.aisles['pineapple chunks in 100% juice'] = 'canned'
    self.aisles['low sodium soy sauce'] = 'seasonings'
    self.aisles['ground ginger'] = 'seasonings'
    self.aisles['top sirloin'] = 'meat'
    self.aisles['rice wine vinegar'] = 'misc'
    self.aisles['sesame seeds'] = 'seasonings'
    self.aisles['seasame oil'] = 'misc'
    self.aisles['dried lentils'] = 'misc'
    self.aisles['garbanzo beans'] = 'canned'
    self.aisles['chicken broth'] = 'misc'
    self.aisles['sweet potato'] = 'produce'
    self.aisles['dry enriched parboiled long grain rice'] = 'misc' #substitute with white or brown rice
    self.aisles['unsweetened coconut milk'] = 'canned'
    self.aisles['green curry paste'] = 'misc'
    self.aisles['bamboo shots'] = 'misc'
    self.aisles['boneless pork ribs'] = 'meat'
    self.aisles['tomato paste'] = 'canned'
    self.aisles['maple syrup'] = 'misc'
    self.aisles['quinoa'] = 'misc'
    self.aisles['stew meat'] = 'meat'
    self.aisles['frozen peas'] = 'frozen'
    self.aisles['jalapeno'] = 'produce'
    self.aisles['vegetable broth'] = 'misc'
    self.aisles['pitted dark sweet cherries'] = 'frozen'
    self.aisles['quartered artichoke hearts'] = 'canned'
    self.aisles['french green lentils'] = 'misc'
    self.aisles['orange'] = 'produce'
    self.aisles['navel orange'] = 'produce'
    self.aisles['lemon'] = 'produce'
    self.aisles['pork roast'] = 'meat'
    self.aisles['frozen sliced peaches'] = 'frozen'
    self.aisles['fennel seeds'] = 'misc'
    self.aisles['mcintosh apples'] = 'produce'
    self.aisles['cinnamon'] = 'seasonings'
    self.aisles['bosc pears'] = 'produce'
    self.aisles['crushed tomatoes'] = 'canned'
    self.aisles['diced green chilies'] = 'canned' #not mild?
    self.aisles['split peas'] = 'misc'
    self.aisles['roma tomato'] = 'produce'
    self.aisles['gallon freezer bag'] = 'misc'
    self.aisles['quart freezer bag'] = 'misc'
    self.aisles['disposable or aluminum baking pan(9x13”)'] = 'misc'
    self.aisles['aluminum foil'] = 'misc'
    self.aisles['all-purpose flour'] = 'baking'
    self.aisles['italian-seasonings breadcrumbs'] = 'misc'
    self.aisles['baby carrots'] = 'produce'
    self.aisles['bone-in chicken thighs'] = 'meat'
    self.aisles['low moisture part-skim mozzarella cheese'] = 'dairy'
    self.aisles['ricotta cheese'] = 'dairy'
    self.aisles['ground chicken'] = 'meat'
    self.aisles['ketchup'] = 'misc'
    self.aisles['baby back ribs'] = 'meat'
    self.aisles['pork tenderloin'] = 'meat'
    self.aisles['diced tomatoes with green chilies'] = 'canned'
    self.aisles['beef chuck shoulder roast'] = 'meat'
    self.aisles['onion flakes'] = 'seasonings'
    self.aisles['celery seed'] = 'sesonings'
    self.aisles['bone-in pork shoulder roast'] = 'meat'
    self.aisles['pork shoulder roast'] = 'meat'
    self.aisles['sugar'] = 'baking'
    self.aisles['hot sauce'] = 'misc'
    self.aisles['distilled white vinegar'] = 'misc'
    self.aisles['french baguette'] = 'misc'
    self.aisles['whole milk'] = 'dairy'
    self.aisles['pure vanilla extract'] = 'baking'
    self.aisles['unsweetened cocoa powder'] = 'baking'
    self.aisles['white vinegar'] = 'misc'
    self.aisles['semi sweet chocolate chips'] = 'baking'
    self.aisles['frozen blueberry'] = 'frozen'
    self.aisles['old-fasioned oats'] = 'misc'
    self.aisles['pineapple'] = 'produce'
    self.aisles['coconut milk'] = 'canned'
    self.aisles['coconut oil'] = 'misc'
    self.aisles['brown rice'] = 'misc'
    self.aisles['wild rice'] = 'misc'
    self.aisles['old fasioned oats'] = 'misc'
    self.aisles['baking powder'] = 'baking'
    self.aisles['canola oil'] = 'misc'
    self.aisles['applesauce'] = 'misc'
    self.aisles['flax seed'] = 'seasonings'
    self.aisles['thyme'] = 'seasonings'
    self.aisles['baking soda'] = 'baking'
    self.aisles['ground clove'] = ''
    self.aisles['disposable or aluminum loaf pan(9x5”)'] = 'misc'
    self.aisles['sweet bell pepper'] = 'produce'
    self.aisles['white mushroom'] = 'produce'
    self.aisles['beef broth'] = 'misc'
    self.aisles['tomato juice'] = 'canned'
    self.aisles['ground mustard'] = 'seasonings'
    self.aisles['dry white wine'] = 'misc'
    self.aisles['capers'] = 'seasonings'
    self.aisles['cranberries'] = 'produce'
    self.aisles['balsamic vinegar'] = 'misc'
    self.aisles['apple juice'] = 'misc'
    self.aisles['bourbon'] = 'misc'
    self.aisles['mayonnaise'] = 'misc'
    self.aisles['sugar snap peas'] = 'produce'
    self.aisles['sirloin tip steak'] = 'meat'
    self.aisles['turmeric'] = 'seasonings'
    self.aisles['bagged coleslaw mix'] = 'produce'
    self.aisles['rosemary'] = 'seasonings'
    self.aisles['cilantro'] = 'produce'
    #self.aisles['Large green pepper'] = 'produce' #check out recipe for japanese beef teriyaki does it need to be large?
    #add more as needed, is large and small a ''unit of measurement'' under units
    self.units = ('oz', 'cup', 'lb', 'teaspoon', 'Tablespoon', 'gallon', 'small', 'large')
    self.other = ('slices', 'box', 'clove',) #add more as seen in recipes
    #not printing correctly, blank
    #ie 1 14.5oz. red pepper
    
    self.foodStr = foodStr
    self.mType = ''
    self.name = ''
    self.aisle = ''
    self.amount = 1

  
  def parse(self):
    
    strList = self.foodStr.split()
    num = ''
    
    for i in strList[:]:
        if strList[0].find('/') >= 0:
            snum = num + ' ' + strList[0]
            strList.pop(0)
        elif strList[0].isdigit():
            num = strList[0]
            strList.pop(0)
            continue
        if not strList[0].isdigit() or strList[0].find('/') == -1:
            break
        
    #if no number is provided assume the number will be 1
    if num == '':
        self.amount = Mixed(1)
    else:
        self.amount = Mixed(num)
    
    for unit in [y for x in [self.units, self.other] for y in x]:
        if strList[0].find(unit) != -1:
            self.mType = strList[0]
            strList.pop(0)

    for i in range(len(strList)):
        if i == len(strList) - 1:
            self.name = self.name + strList[i]
        else:
            self.name = self.name + strList[i] + ' '

    self.aisle = self.aisles[self.name]

  def foodTuple(self):
    return (self.amount, self.mType, self.name, self.aisles[self.name])
  
  
  def __str__(self):
    rep = ''
    if self.amount and self.mType and self.name:
      rep = str(self.amount) +  " "  + self.mType + " " + self.name
    elif not self.amount and self.mType and self.name:
      rep = self.mType + " " + self.name
    elif self.amount and self.name and not self.mType:
      rep = str(self.amount) +  " " + self.name
    elif not self.amount and not self.mType and self.name:
      rep = str(self.name)
    return rep


  def __add__(self, rhs):
    self.amount = self.amount + rhs.amount
    return self
    
  
  def __radd__(self, lhs):
    self.amount = lhs + self.amount
    return self
  
  def __sub__(self, rhs):
    self.amount =  self.amount - rhs
    return self
  
  def __rsub__(self, lhs):
    self.amount =  lhs - self.amount
    return self
  
  def __mul__(self, rhs):
    self.amount = self.amount * rhs
    return self
  
  def __rmul__(self, lhs):
    self.amont =  self.amount * lhs
    return self
  
  def __truediv__(self, rhs):
    self.amount = self.amount / rhs
    return self
  
  def __rtruediv__(self, lhs):
    self.amount =  lhs / self.amount
    return self
  
  '''
  vary for each food item. All Fractions should round up to total number of items needed. 10 oz, 12 oz would be 2 10 oz, etc?
  where and how'''
  def __mod__(self, rhs):
    pass
  #all foods round up to closest container
  #how will I estimate each food to round up


#Dry and liquid Measure Equivalents: nested list in food or recipe
'''
Turn into dictionary

Volume (Liquid) 
American Standard      American Standard             Metric
 (Cups & Quarts )           (Ounces)           (Milliliters & Liters)
   2 tbsp                   1 fl. oz.               30 ml
   1/4 cup                  2 fl. oz.               60 ml
   1/2 cup                  4 fl. oz.               125 ml
   1 cup                    8 fl. oz.               250 ml
   1 1/2 cups               12 fl. oz.              375 ml
   2 cups or 1 pint         16 fl. oz.              500 ml
   4 cups or 1 quart        32 fl. oz.              1000 ml or 1 liter
   1 gallon                 128 fl. oz.             4 liters
 

Dry Measure Equivalents
 	 	 	 
 3 teaspoons	 1 tablespoon	 1/2 ounce	 14.3 grams
 2 tablespoons	1/8 cup	 1 ounce	 28.3 grams
 4 tablespoons	 1/4 cup	 2 ounces	 56.7 grams
 5 1/3 tablespoons	 1/3 cup	 2.6 ounces	 75.6 grams
 8 tablespoons	 1/2 cup	 4 ounces	 113.4 grams
 12 tablespoons	 3/4 cup	 6 ounces	 .375 pound
 32 tablespoons	 2 cups	 16 ounces	 1 pound
'''
