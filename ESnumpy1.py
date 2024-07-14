import numpy as np

# Creazione di un array 1D
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Slicing: selezione di un sottoarray (elementi da 3 a 7)
sub_arr = arr[3:8]
print("Sottoarray con slicing:", sub_arr)  # Output: [40 50 60 70 80]

# Modifica degli elementi del sottoarray (slicing modifica anche l'array originale)
sub_arr[:] = sub_arr[:] + 5
print("Array originale dopo modifica del sottoarray:", arr)  # Output: [10 20 30 45 55 65 75 85 90 100]

# Creazione di un array 2D
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing: selezione di un sottoarray 2D (prime due righe e colonne da 1 a 3)
sub_arr_2d = arr_2d[:2, 1:3]
print("Sottoarray 2D con slicing:\n", sub_arr_2d)  # Output: [[2 3]
                                                    #          [6 7]]

# Fancy indexing: selezione di elementi specifici (elementi agli indici [0, 2], [1, 1], [2, 3])
selected_elements = arr_2d[[0, 1, 2], [2, 1, 3]]
print("Elementi selezionati con fancy indexing:", selected_elements)  # Output: [3 6 12]

# Fancy indexing: selezione di righe specifiche (riga 0 e 2) e tutte le colonne
selected_rows = arr_2d[[0, 2], :]
print("Righe selezionate con fancy indexing:\n", selected_rows)  # Output: [[ 1  2  3  4]
                                                                 #          [ 9 10 11 12]]

# Fancy indexing: selezione di colonne specifiche (colonna 1 e 3) e tutte le righe
selected_cols = arr_2d[:, [1, 3]]
print("Colonne selezionate con fancy indexing:\n", selected_cols)  # Output: [[ 2  4]
                                                                   #          [ 6  8]
                                                                   #          [10 12]]
