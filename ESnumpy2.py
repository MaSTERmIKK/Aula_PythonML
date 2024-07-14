import numpy as np

# Creazione di un array 1D di numeri pari da 0 a 18
arr = np.arange(0, 20, 2)
print("Array originale:", arr)  # Output: [ 0  2  4  6  8 10 12 14 16 18]

# Slicing: selezione degli ultimi 5 elementi dell'array
sub_arr = arr[-5:]
print("Ultimi 5 elementi con slicing:", sub_arr)  # Output: [10 12 14 16 18]

# Modifica degli elementi selezionati tramite slicing
sub_arr[:] = sub_arr[:] * 2
print("Array originale dopo la modifica degli ultimi 5 elementi:", arr)  # Output: [ 0  2  4  6  8 20 24 28 32 36]

# Creazione di un array 2D di numeri da 1 a 12
arr_2d = np.arange(1, 13).reshape(3, 4)
print("Array 2D originale:\n", arr_2d)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

# Slicing: selezione di un sottoarray 2D (ultime due righe e ultime due colonne)
sub_arr_2d = arr_2d[1:, 2:]
print("Sottoarray 2D con slicing:\n", sub_arr_2d)
# Output:
# [[ 7  8]
#  [11 12]]

# Fancy indexing: selezione degli elementi agli indici [0, 1], [1, 0], [2, 3]
selected_elements = arr_2d[[0, 1, 2], [1, 0, 3]]
print("Elementi selezionati con fancy indexing:", selected_elements)  # Output: [ 2  5 12]

# Fancy indexing: selezione di righe specifiche (riga 0 e 2) e colonne specifiche (colonna 1 e 3)
selected_rows_cols = arr_2d[[0, 2], :][:, [1, 3]]
print("Righe e colonne selezionate con fancy indexing:\n", selected_rows_cols)
# Output:
# [[ 2  4]
#  [10 12]]
