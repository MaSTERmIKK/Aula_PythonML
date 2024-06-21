# 1. Chiedere un numero positivo usando un ciclo while
n = int(input("Inserisci un numero intero positivo: "))
while n <= 0:
    n = int(input("Inserisci un numero intero positivo: "))

# 2. Calcolare la somma dei numeri pari da 1 a n
somma_pari = 0
for i in range(2, n+1, 2):
    somma_pari += i
print(f"La somma dei numeri pari da 1 a {n} è: {somma_pari}")

# 3. Stampare tutti i numeri dispari da 1 a n
print(f"Numeri dispari da 1 a {n}:")
for i in range(1, n+1, 2):
    print(i)

# 4. Determinare se n è un numero primo
is_prime = True
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
else:
    is_prime = False

if is_prime:
    print(f"Il numero {n} è un numero primo.")
else:
    print(f"Il numero {n} non è un numero primo.")
