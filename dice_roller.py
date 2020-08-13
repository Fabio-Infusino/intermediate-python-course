def main():
  print('Lancia il dado')

if __name__== "__main__":
  main()

#importiamo la funzione casuale
import random

#creiamo una simulazione del lancio di dadi dove verrà simulata e addizionata la scelta di due numeri casuali.
import random
dice_rolls  =  int (input('Quanti dadi vorresti tirate?')) #faccciamo scegliere al nostro utente quanti dadi vuole lanciare
dice_size = int (input('Quante facce ha il tuo dado?')) #facciamo scegliere al nostro utente quante facce deve avere il dado
dice_sum  =  0
for i in range (0, dice_rolls):
    roll = random.randint (1, dice_size)
    dice_sum += roll
    if roll == 1:
        print (f'Hai tirato un {roll}! Risultato critico') #diremo che è un risultato critico quando esce il numero 1
    elif roll == dice_size:
        print (f'Hai tirato un {roll}! Ottimo risultato!') #quando il riusltato è il numero maggiore possibile scriveremo ottimo risultato
    else:
        print (f'Hai tirato un {roll}')
    print(f'Hai tirato un totale di {dice_sum}')
