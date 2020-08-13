def main():
  print('Lancia il dado')

if __name__== "__main__":
  main()

#importiamo la funzione casuale
import random

#creiamo una simulazione del lancio di due dadi dove verrà simulata e addizionata la scelta di due numeri casuali compresi tra 1 e 6
dice_rolls = 2
dice_sum = 0
for i in range(0,dice_rolls):
  roll = random.randint(1,6)
  dice_sum += roll
  print(f'Hai fatto {roll}')
print(f'Hai fatto un totale di {dice_sum}')
