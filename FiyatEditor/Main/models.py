from django.db import models

# Create your models here.

class Sebze(models.Model): # DB Table that contains id(int), type(str), name(str), shown_name(str), price(float)
    id = models.IntegerField(primary_key=True)
    type = models.CharField(default="Herhangi")
    name = models.CharField(max_length=30)
    shown_name = models.CharField(default="test")
    price = models.FloatField(default=1.0)


### This class is necessary to link and handle -> GET, POST request - Database.
### With this class, our database communicates with methods in utils.py

class PriceList: 
    def __init__(self, name,type,yesterday_price,today_price):
        self.name = name
        self.type = type
        self.yesterday_price = yesterday_price # Float
        self.today_price = today_price # Float
    
    
    def filter(input_dict,name): # Filter method basically returns the object that has desired 'name' attribute.
        output_list = []
        for object_list in input_dict.values():
            for object in object_list:
                if name == object.name:
                    output_list.append(object)
        return output_list