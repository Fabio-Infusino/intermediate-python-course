def main():
  print('Lancia il dado')

if __name__== "__main__":
  main()

#importiamo la funzione casuale
import random

#roll sarà una scelta casuale dei numeri da 1 a 6
roll = random.randint(1,6)

#stampiamo il valore di roll
print(f'Hai fatto {roll}!')
