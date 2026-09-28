python 
import math

class Circle:
  def__init_(self, radius: float):
    if radius <= 0:
      raise ValueError("Радиус должен быть положительным")
    self.radius = radius

def are(self) -> float:
  return math.pi * (self.radius ** 2)
