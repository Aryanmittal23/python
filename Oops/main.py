class car:
    color = None
class motorCycle:
    color = None
def  changeColor(car,color):
    car.color = color
    

car1=car()    
car2=car()    
car3=car()    
car4=car()   

bike1 = motorCycle()

changeColor(car1,'red')
changeColor(car2,'green')
changeColor(car3,'blue')
changeColor(car4,'yellow')
changeColor(bike1,'white')

print(car1.color)
print(car2.color)
print(car3.color)
print(car4.color)
print(bike1.color)
