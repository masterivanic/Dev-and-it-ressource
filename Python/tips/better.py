"""
 Here i will show you
 better way to implement python
 code
"""

from typing import Protocol


"""
  Use protocol to define the interface
  required by your function/method instead of using
  real objects.

  This way, your function/method defines what it
  needs.

  Useful when you've large configuration objects,
  and you need only a small part of them. Learn more 
  on PEP544
"""
#-------------------- bad way -----------------------

class ApplicationConfig:
    DEBUG = False
    SECRET_KEY = 'your_secret_key'
    EMAIL_API_KEY = 'your_email_api_key'


def send_email(config:ApplicationConfig):
    print(f"i send my mail here: {config.EMAIL_API_KEY}")


#-------------------- better way -----------------------
class EmailConfig(Protocol):
    EMAIL_API_KEY : str

def send_email(config:EmailConfig):
    print(f"i send my mail here: {config.EMAIL_API_KEY}")

#---------------------------------------------------------------------------

from enum import Enum
from dataclasses import dataclass
from uuid import UUID

class OrderStatus(str, Enum):
    PLACED = "PLACED"
    CANCELED = "CANCELED"
    FULFILED = "FULFILED"

#-------------------- bad way -----------------------

"""
 Avoid setting attribuets of your objects 
 outside of the constructor. Instead, implement method
 that map to real-word concepts.

 Why?
 To ensure attributes exist and are easily
 discovereable. Also to encapsulate knowledge
 in single place 👇
"""

@dataclass
class Order:
    status : OrderStatus

class CancelOrder:
    def __init__(self,order_repository) -> None:
        self.order_repository = order_repository

    def execute(self, order_id:UUID):
        order = self.order_repository.get_by_id(order_id)
        order.status = OrderStatus.CANCELED
        self.order_repository.save(order)

#-------------------- better way -----------------------

class Order:
    def __init__(self, status:OrderStatus) -> None:
        self._status = status
    
    def cancel(self):
        self._status = OrderStatus.CANCELED
    
class CancelOrder:
    def __init__(self, order_repository) -> None:
        self.order_repository = order_repository
    
    def execute(self, order_id:UUID):
        order:Order = self.order_repository.get_by_id(order_id)
        order.cancel()
        self.order_repository.save(order)

        

    
        


        

