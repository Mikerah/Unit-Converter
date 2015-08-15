
class Unit:

    def __init__(self, name, symbol, magnitude, measure):
        self.name = name
        self.symbol = symbol
        self.magnitude = magnitude
        self.measure = measure
        
    def __str__(self):
        return "%s: %d %s" % (self.name,self.magnitude,self.symbol)
        
    def __add__(self, measure):
        self.magnitude = self.magnitude + measure.magnitude
        return self.magnitude

class Kilometer(Unit):
        
    def convert_to(self, unit, magnitude):
        
        if unit.lower() == "metre" or unit.lower() == "meter":
            return magnitude * 1000
            
        if unit.lower() == "feet":
            return magnitude * 3280.8
            
        if unit.lower() == "inches":
            return magnitude * 39370
        
class Meter(Unit):
 
    def convert_to(self, unit, magnitude):
        if unit.lower() == "kilometre" or unit.lower() == "kilometer":
            return magnitude / 1000
            
        if unit.lower() == "feet":
            return magnitude * 3.2808
            
        if unit.lower() == "inches":
            return magnitude * 39.370
        
class Feet(Unit):
       
    def convert_to(self, unit):
        if unit.lower() == "kilometre" or unit.lower() == "kilometer":
            return magnitude / 3280.8
        if unit.lower() == "metre" or unit.lower() == "meter":
            return magnitude / 3.2808
        if unit.lower() == "inches":
            return magnitude * 12        
        
class Inch(Unit):

    def convert_to(self, unit):
        if unit.lower() == "kilometre" or unit.lower() == "kilometer":
            return magnitude / 39370
        if unit.lower() == "metre" or unit.lower() == "meter":
            return magnitude / 39.370
        if unit.lower() == "feet":
            return magnitude / 12        
        
        
class Litre(Unit):  
        
    def convert_to(self, unit, magnitude):
        if unit.lower() == "millilitre" or unit.lower() == "millileter":
            return magnitude / 0.001
        if unit.lower() == "fluid ounce":
            return magnitude * 33.814
        
class Millilitre(Unit):
     
    def convert_to(self, unit, magnitude):
        if unit.lower() == "litre" or unit.lower() == "liter":
            return magnitude * 0.001
        if unit.lower() == "fluid ounce":
            return magnitude * 0.033814
        
class FluidOunce(Unit):
     
    def convert_to(self, unit,magnitude):
        if unit.lower() == "litre" or unit.lower() == "liter":
            return magnitude / 33.814
        if unit.lower() == "millilitre" or unit.lower == "milliliter":
            return magntiude / 0.033814
        
class Kilogram(Unit):
     
    def convert_to(self, unit,magntiude):
        if unit.lower() == "pounds":
            magnitude * 2.2046
        
class Pound(Unit):
      
    def convert_to(self, unit,magnitude):
        if unit.lower() == "kilogram":
            magnitude / 2.2046
       