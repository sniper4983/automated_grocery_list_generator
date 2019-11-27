aisles = {}
'''
These are my names to locate to
meat, dairy, baking, misc,
frozen, produce,canned, seasonings
'''
aisles['beef chuck roast'] = 'meat'
aisles['ground beef'] = 'meat'
aisles['sliced & fat trimmed boneless sirloin tip roast'] = 'meat'
aisles['chicken breast'] = 'meat'
aisles['chicken theighs'] = 'meat'
aisles['bone in ham bone steak'] = 'meat'
aisles['pork shoulder'] = 'meat'
aisles['onion'] = 'produce'
aisles['red onion'] = 'produce'
aisles['red bell pepper'] = 'produce'
aisles['small cabbage'] = 'produce'
aisles['carrots'] = 'produce'
aisles['spinich'] = 'produce'
aisles['zucchini'] = 'produce'
aisles['rainbow peppers'] = 'produce'
aisles['butternut squash'] = 'produce'
aisles['ground turkey'] = 'meat'
aisles['bacon'] = 'meat'
aisles['american cheese'] = 'dairy'
aisles['shredded cheddar cheese'] = 'dairy'
aisles['celery'] = 'produce'
aisles['ground italian sausage'] = 'meat'
aisles['shredded swiss cheese'] = 'dairy'
aisles['diced tomatoes'] = 'canned'
aisles['heavy whipping cream'] = 'dairy'
aisles['egg'] = 'dairy'
aisles['orzo'] = 'misc'
aisles['italian sausage'] = 'meat'
aisles['shredded cheddar'] = 'dairy'
aisles['shredded monterey jack cheese,'] = 'dairy'
aisles['milk'] = 'dairy'
aisles['tortillas'] = 'misc'
aisles['salsa verde'] = 'misc'
aisles['heavy cream'] = 'dairy'
aisles['freezer bag'] = 'misc'
aisles['frozen bell peppers'] = 'produce'
aisles['parmesean cheese'] = 'misc'
aisles['tomato sauce'] = 'canned'
aisles['extra wide egg noodles'] = 'misc'
aisles['italian bread crumbs'] = 'misc'
aisles['rigatoni'] = 'misc'
aisles['green onions'] = 'produce'
aisles['red potatoes'] = 'produce'
aisles['chili powder'] = 'seasonings'
aisles['salt'] = 'seasonings'
aisles['pepper'] = 'seasonings'
aisles['ground cumin'] = 'seasonings'
aisles['frozen corn'] = 'frozen'
aisles['cream cheese'] = 'dairy'
aisles['dark red kidney beans'] = 'canned'
aisles['black beans'] = 'canned'
aisles['penne pasta'] = 'misc'
aisles['butter'] = 'dairy'
aisles['jalepeno'] = 'produce'
aisles['elbow macoroni'] = 'misc'
aisles['evaporated milk'] = 'baking'
aisles['cannellini_beans'] = 'canned'
aisles['green beans'] = 'produce'
aisles['pasta sauce'] = 'misc'
aisles['sour cream'] = 'dairy'
aisles['frozen cheese tortellini'] = 'frozen'
aisles['cornflakes'] = 'misc'
aisles['ritz'] = 'misc'
aisles['apple cider vinegar'] = 'misc'
aisles['extra virgin olive oil'] = 'misc'
aisles['olive oil'] = 'misc'
aisles['red wine vinegar'] = 'misc'
aisles['paprika'] = 'seasonings'
aisles['garlic powder'] = 'seasonings'
aisles['onion powder'] = 'seasonings'
aisles['Montreal steak seasoning mix'] = ''
aisles['garlic'] = 'produce'
aisles['parsley'] = 'seasonings'
aisles['honey'] = 'misc'
aisles['curry powder'] = 'seasonings'
aisles['disposable or aluminum baking pan(9x13)'] = 'misc'
aisles['bay leaves'] = 'seasonings'
aisles['light brown sugar'] = 'baking'
aisles['worcestershire sauce'] = 'misc'
aisles['lime'] = 'produce'
aisles['dijon mustard'] = 'misc'
aisles['baby spinich'] = 'produce'
aisles['basil'] = 'seasonings'
aisles['oregano'] = 'seasonings'
aisles['italian seasoning'] = 'seasonings'
aisles['garlic salt'] = 'seasonings'
aisles['dill'] = 'seasonings'
aisles['frozen mixed vegetables'] = 'frozen'
aisles['mild italian sausage links'] = 'meat'
aisles['garam masala'] = 'seasonings'
aisles['jiffy corn Muffin Mix'] = 'baking'
aisles['russet potatoes'] = 'produce'
aisles['frozen broccoli florets'] = 'frozen'
aisles['green bell peppers'] = 'produce'
aisles['crushed red pepper'] = 'seasonings'
aisles['baby spinach'] = 'produce'
aisles['cannellini beans'] = 'canned'
aisles['parmesan cheese'] = 'misc'
aisles['chicken thighs'] = 'meat'
aisles['green bell pepper'] = 'produce'
aisles['diced mild green chilies'] = 'canned'
aisles['ground oregano'] = 'seasonings'


units = ('oz', 'cup', 'lb', 'teaspoon', 'Tablespoon', 'gallon',)
other = ('slices', 'box', 'clove',) 

class Food():
  """Base class for all food in shopping list."""
  #aisle general location in store
  def __init__(self, amount=0, mType='', name='', aisle =''):
    self.aisle = aisle
    #amount already already parsed unless nothing passed, will ever be default?
    self.amount = amount 
    self.mType = mType
    self.name = name;
    #ie 1 14.5oz. red pepper  
   
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
