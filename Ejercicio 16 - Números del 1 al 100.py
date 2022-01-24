print("Cree un programa que sea capaz de escribir los números del 1 al 100.\n"+
"Si un número es múltiplo de 3, se escribe “mare” en su lugar. \n"+
"Si el número es múltiplo de 5, se escribe 'igua'.\n"+
"*Si el número es múltiplo de ambos se escribe 'mareigua'.")
import time as t 
t.sleep(2)
for i in range(1,100,1):
    if i%3==0:
        print('mare')
    elif i%5==0:
        print('igua')
    elif i%3==0 and i%5==0:
        print('mareigua')

        