#Cree una clase de User que:
#Tenga un atributo de date_of_birth.
#Tenga un property de age.
#Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date
from functools import wraps


class User:
   def __init__(self, date_of_birth):
      self.date_of_birth = date_of_birth

   @property
   def age(self):
      today = date.today()
      age = today.year - self.date_of_birth.year

      if (
         (today.month, today.day)
         <
         (self.date_of_birth.month, self.date_of_birth.day)
      ):
         age -= 1

      return age
   

def validate_user(func):

   @wraps(func)
   def wrapper(user, *args, **kwargs):

      if user.age < 18:
         raise Exception(
            f'El usuario tiene {user.age} años y es menor de edad'
         )
      
      return func(user, *args, **kwargs)
   
   return wrapper


@validate_user
def purchase_beer(user):
   print("Compra permitida")


adult = User(date(2015, 1, 11))
try:
   purchase_beer(adult)

except Exception as e:
   print(f'Compra no permitida {e}')