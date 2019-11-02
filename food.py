from mixed import Mixed
#from decimal import Decimal

ailes = {}
ailes['beef chuck roast'] = 'meat'
ailes['ground beef'] = 'meat'
ailes['sliced & fat trimmed boneless sirloin tip roast'] = 'meat'
ailes['chicken breast'] = 'meat'
ailes['chicken theighs'] = 'meat'
ailes['bone in ham bone steak'] = 'meat'
ailes['pork shoulder'] = 'meat'
ailes['baby carrots'] = 'produce'
ailes['onion'] = 'produce'
ailes['red bell pepper'] = 'produce'
ailes['small cabbage'] = 'produce'
ailes['carrots'] = 'produce'
ailes['spinich'] = 'produce'
ailes['zucchini'] = 'produce'
ailes['rainbow_peppers'] = 'produce'
ailes['butternut squash'] = 'produce'
ailes['ground turkey'] = 'meat'
ailes['bacon'] = 'meat'
ailes['american cheese'] = 'cheese'
ailes['cheddar cheese'] = 'cheese'
ailes['celery'] = 'produce'
ailes['ground italian sausage'] = 'meat'
ailes['swiss cheese'] = 'cheese'
ailes['diced tomatoes'] = 'canned'
ailes['heavy whipping cream'] = 'dairy'
ailes['egg'] = 'eggs'
ailes['orzo'] = 'pasta'
ailes['italian sausage'] = 'meat'
ailes['shredded cheddar'] = 'cheese'
ailes['monterey jack cheese,'] = 'cheese'
ailes['milk'] = 'dairy'
ailes['tortillas'] = 'mexican'
ailes['salsa verde'] = 'mexican'
ailes['heavy cream'] = 'dairy'
ailes['freezer bag'] = 'housewares'
ailes['frozen bell peppers'] = 'frozen'
ailes['parmesean cheese'] = 'italian'
ailes['tomato sauce'] = 'canned'
ailes['extra wide egg noodles'] = 'italian'
ailes['italian bread crumbs'] = 'italian'
ailes['rigatoni'] = 'italian'
ailes['green onions'] = 'produce'
ailes['red potatoes'] = 'produce'
ailes['chili powder'] = 'spices'
ailes['salt'] = 'spices'
ailes['ground cumin'] = 'spices'
ailes['frozen corn'] = 'frozen'
ailes['cream cheese'] = 'dairy' #?location
ailes['dark red kidney beans'] = 'canned'
ailes['black beans'] = 'canned'
ailes['penne pasta'] = 'italian'
ailes['butter'] = 'dairy'
ailes['jalepeno'] = 'produce'
ailes['elbow macoroni'] = 'italian'
ailes['evaporated milk'] = 'baking'
ailes['cannellini_beans'] = 'canned'
ailes['green beans'] = 'canned' #fresh?
ailes['pasta_sauce'] = 'pasta'
ailes['sour cream'] = 'dairy'
ailes['frozen cheese tortellini'] = 'frozen'
ailes['cornflakes'] = 'cereal'
ailes['ritz'] = 'crackers'



#continue editing all foods to meet correct ailse
class Food():
  """Base class for all food in shopping list."""
  #aisle where food is located in store
  
  def __init__(self, amount=0, name='', aisle =''):
    self.aisle = aisle
    self.amount = Mixed(amount)
    self.name = name;
    #ie 14.5 oz. can  
   
  def __str__(self):
    if not name:
      return amount
    else:
      return amount +  " " + name
    
  def __add__(self, rhs):
    return self.amount + rhs
  
  def __radd__(self, lhs):
    return lhs + self.amount
  
  def __sub__(self, rhs):
    return self.amount - rhs
  
  def __rsub__(self, lhs):
    return lhs - self.amount
  
  def __mul__(self, rhs):
    return self.amount * rhs
  
  def __rmul__(self, lhs):
    return self.amount * lhs
  
  def __truediv__(self, rhs):
    return self.amount / rhs
  
  def __rtruediv__(self, lhs):
    return lhs / self.amount
  
  '''
  vary for each food item. All Fractions should round up to total number of items needed. 10 oz, 12 oz would be 2 10 oz, etc?
  where and how'''
  def __mod__(self, rhs):
    pass

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
  def __init__(self, amount=1, unitOfMeasure='Lb'):
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
  
class HamSteak(Food):
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

class AmericanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='slice'):
    Super().__init__(amount, unitOfMeasure)
    self.food = 'American cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class HeavyCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Milk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'milk'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class HeavyWhippingCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'heavy whipping cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ParmeseanCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'parmesean cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Butter(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'butter'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class EvaporatedMilk(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'evaporated milk'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CreamCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cream cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class SourCream(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'sour cream'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class MontereyJackCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'monterey jack cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CheddarCheese(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cheddar cheese'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class ShreddedCheddar(Food): #same as above 
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'shredded cheddar'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
#Veggies
class Babycarrots(Food):
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


class Onion(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'onion'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Spinach(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'spinach'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class FrozenBellPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen bell peppers'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenOnions(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'green onions'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class DicedTomatoes(Food):
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

class RedBellPepper(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red bell pepper'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
#needed?
class RainbowPeppers(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rainbow peppers'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  #fix below
class ButternutSquash(Food):
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

class DarkRedKidneyBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'dark red kidney beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class GreenBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'grean beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class RedPotatoes(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'red potatoes'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class Celery(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'celery'
    self.aisle = ailes[self.food]
    #play with this one stalks change to bunches or pounds
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class CannelliniBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cannellini beans('
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class BlackBeans(Food):
  def __init__(self, amount=1, unitOfMeasure='Lb'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'black beans'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    

class SalsaVerde(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'salsa verde'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class TomatoSauce(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'tomato Sauce'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class ExtraWideEggNoodles(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'extra wide egg noodles'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class ItalianBreadCrumbs(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'italian bread crumbs'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
 
class Orzo(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'orzo'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Rigatoni(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'rigatoni'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food

class PastaSauce(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'pasta sauce'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class FrozenCheeseTortellini(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'frozen cheese tortellini'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Cornflakes(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'cornflakes'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Egg(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'egg'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
    
class Ritz(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ritz'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class Jalapeno(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'jalapeno'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class ElbowMacoroni(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'elbow macoroni'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class PennePasta(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'penne pasta'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class ChiliPowder(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'chili powder'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class Salt(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'salt'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GroundCumin(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'ground cumin'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class GarlicPowder(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'garlic powder'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class LowSodiumChickenBroth(Food):
  def __init__(self, amount=1, unitOfMeasure='stalk'):
    Super().__init__(unitOfMeasure, amount)
    self.food = 'low-sodium chicken broth'
    self.aisle = ailes[self.food]
    
  def __str__(self):
    return Super.__str__() + " " + self.food
  
class CornTortilla(Food):
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
