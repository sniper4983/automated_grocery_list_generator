aisles = {}
aisles['beef chuck roast'] = 'meat'
aisles['ground beef'] = 'meat'
aisles['sliced & fat trimmed boneless sirloin tip roast'] = 'meat'
aisles['chicken breast'] = 'meat'
aisles['chicken theighs'] = 'meat'
aisles['bone in ham bone steak'] = 'meat'
aisles['pork shoulder'] = 'meat'
aisles['baby carrots'] = 'produce'
aisles['onion'] = 'produce'
aisles['red bell pepper'] = 'produce'
aisles['small cabbage'] = 'produce'
aisles['carrots'] = 'produce'
aisles['spinich'] = 'produce'
aisles['zucchini'] = 'produce'
aisles['rainbow peppers'] = 'produce'
aisles['butternut squash'] = 'produce'
aisles['ground turkey'] = 'meat'
aisles['bacon'] = 'meat'
aisles['american cheese'] = 'cheese'
aisles['cheddar cheese'] = 'cheese'
aisles['celery'] = 'produce'
aisles['ground italian sausage'] = 'meat'
aisles['swiss cheese'] = 'cheese'
aisles['diced tomatoes'] = 'canned'
aisles['heavy whipping cream'] = 'dairy'
aisles['egg'] = 'eggs'
aisles['orzo'] = 'pasta'
aisles['italian sausage'] = 'meat'
aisles['shredded cheddar'] = 'cheese'
aisles['monterey jack cheese,'] = 'cheese'
aisles['milk'] = 'dairy'
aisles['tortillas'] = 'mexican'
aisles['salsa verde'] = 'mexican'
aisles['heavy cream'] = 'dairy'
aisles['freezer bag'] = 'housewares'
aisles['frozen bell peppers'] = 'frozen'
aisles['parmesean cheese'] = 'pasta'
aisles['tomato sauce'] = 'canned'
aisles['extra wide egg noodles'] = 'pasta'
aisles['italian bread crumbs'] = 'pasta'
aisles['rigatoni'] = 'pasta'
aisles['green onions'] = 'produce'
aisles['red potatoes'] = 'produce'
aisles['chili powder'] = 'spices'
aisles['salt'] = 'spices'
aisles['ground cumin'] = 'spices'
aisles['frozen corn'] = 'frozen'
aisles['cream cheese'] = 'dairy'
aisles['dark red kidney beans'] = 'canned'
aisles['black beans'] = 'canned'
aisles['penne pasta'] = 'pasta'
aisles['butter'] = 'dairy'
aisles['jalepeno'] = 'produce'
aisles['elbow macoroni'] = 'pasta'
aisles['evaporated milk'] = 'baking'
aisles['cannellini_beans'] = 'canned'
aisles['green beans'] = 'canned'
aisles['pasta sauce'] = 'pasta'
aisles['sour cream'] = ''
aisles['frozen cheese tortellini'] = 'frozen'
aisles['cornflakes'] = 'cereal'
aisles['ritz'] = 'crackers'

#add more as needed
units = ('oz', 'cup', 'lb', 'teaspoon', 'Tablespoon', 'gallon',)

#not printing correctly, blank
class Food():
  """Base class for all food in shopping list."""
  #aisle where food is located in store
  def __init__(self, amount=0, mType='', name='', aisle =''):
    self.aisle = aisle
    #amount already already parsed unless nothing passed, will ever be default?
    self.amount = amount 
    self.mType = mType
    self.name = name;
    #roundUp = Estimate()
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
class Estimate():
  pass

'''
#---foods need to be modified, unit of measure or name clean up all ailes so it matches main file and dictionary---
#meats
class ChickenBreast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chicken breast'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BeefChuckRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'beef chuck roast'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  
class GroundBeef(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground beef'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GroundItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground italian sausage'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ItalianSausage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'italian sausage'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class PorkShoulder(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'pork shoulder'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Bacon(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'): #look up
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bacon'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GroundTurkey(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'ground turkey'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HamSteak(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'bone in ham bone steak'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ChickenThighs(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'chicken thighs'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SerloinTipRoast(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'sliced & fat trimmed boneless sirloin tip roast'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

  #Dairy

class AmericanCheese(Food): #change to packages at ending for everything non lb.
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HeavyCream(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Milk(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class HeavyWhippingCream(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ParmeseanCheese(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'parmesean cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Butter(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butter'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class EvaporatedMilk(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'evaporated milk'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CreamCheese(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cream cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SourCream(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'sour cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class MontereyJackCheese(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'monterey jack cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CheddarCheese(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cheddar cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ShreddedCheddar(Food): #same as above? #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'shredded cheddar'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
#Veggies
class Babycarrots(Food): #look up mixup to bag
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'baby carrots'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Carrots(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'carrots'
    self.aisle = ailes[self.food]
   
  def __str__(self):
    return Super.__str__() + " " + self.food


class Onion(Food): #look up frozen onions
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'onion'
    #what to become frozen onions
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Spinach(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'spinach'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenBellPeppers(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen bell peppers'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenOnions(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'green onions'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DicedTomatoes(Food): #look up if works
  def __init__(self, amount=1, unitOfMeasure='14.5 oz'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'diced tomatoes'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Zucchini(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'zucchini'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SmallCabbage(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'small cabbage'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedBellPepper(Food): #look up if blank
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red bell pepper'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
#needed?
class RainbowPeppers(Food): #same as red peppers
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rainbow peppers'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class ButternutSquash(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butternut squash'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenCorn(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen corn'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DarkRedKidneyBeans(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'dark red kidney beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenBeans(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'grean beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedPotatoes(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red potatoes'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = ailes[self.food]
    #play with this one stalks change to bunches or pounds
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CannelliniBeans(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cannellini beans('
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BlackBeans(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'black beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    

class SalsaVerde(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'salsa verde'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class TomatoSauce(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'tomato Sauce'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class ExtraWideEggNoodles(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'extra wide egg noodles'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class ItalianBreadCrumbs(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'italian bread crumbs'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
 
class Orzo(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'orzo'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Rigatoni(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rigatoni'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class PastaSauce(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'pasta sauce'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class FrozenCheeseTortellini(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen cheese tortellini'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Cornflakes(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cornflakes'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Egg(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'egg'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Ritz(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ritz'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class Jalapeno(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'jalapeno'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class ElbowMacoroni(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'elbow macoroni'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class PennePasta(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'penne pasta'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class ChiliPowder(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chili powder'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class Salt(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'salt'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GroundCumin(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ground cumin'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GarlicPowder(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'garlic powder'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class LowSodiumChickenBroth(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'low-sodium chicken broth'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class CornTortilla(Food): #look up
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'corn tortilla'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

#Non-food items
class FreezerBag(Food): 
  def __init__(self, amount=1):
    Super().__init__(amount)
    self.food = 'freezer bag'
    self.category = ailes[self.food]
               
  def __str__(self):
    return Super.__str__() + " " + self.food
  
'''
