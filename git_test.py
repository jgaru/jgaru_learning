from time import sleep
import pyautogui as pg
a = "This"
b = ' is'
c= ' a'
d = ' test.'
print(a+b+c+d)

print('this is a change from the second PC')

abc= "This is a test"
for i in abc:
    print(i,end=" ")
    sleep(0.1)

counter = 0
while counter <=2:
    pg.moveTo(500,500,0.5)
    pg.moveTo(750,500,0.5)
    pg.moveTo(750,750,0.5)
    pg.moveTo(500,750,0.5)
    counter +=1
    print(counter)