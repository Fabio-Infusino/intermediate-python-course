def main():
  print('Lancia il dado')

if __name__== "__main__":
  main()

#importiamo la funzione casuale
import random

#creiamo una simulazione del lancio di due dadi dove verrà simulata e addizionata la scelta di due numeri casuali compresi tra 1 e 6
dice_rolls = 2
dice_sum = 0
for i in range (0, dice_rolls):
    roll = random.randint (1, 6)
    dice_sum += roll
    if roll == 1:
        print (f'Hai tirato un {roll}! Risultato critico')
    elif roll == 6:
        print (f'Hai tirato un {roll}! Ottimo risultato!')
    else:
        print (f'Hai tirato un {roll}')
    print(f'Hai tirato un totale di {dice_sum}')
