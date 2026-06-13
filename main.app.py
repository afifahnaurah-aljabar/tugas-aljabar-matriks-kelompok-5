import naurah069

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matriks A")
naurah069.tampilkan(A)

print("\nMatriks B")
naurah069.tampilkan(B)

print("\nPenjumlahan")
naurah069.tampilkan(naurah069.tambah_matriks(A, B))

print("\nPengurangan")
naurah069.tampilkan(naurah069.kurang_matriks(A, B))

print("\nPerkalian")
naurah069.tampilkan(naurah069.kali_matriks(A, B))

print("\nTranspose A")
naurah069.tampilkan(naurah069.transpose_matriks(A))

C = [
    [2, 1],
    [5, 3]
]

print("\nDeterminan C")
print(naurah069.determinan(C))

print("\nInvers C")
naurah069.tampilkan(naurah069.invers_matriks(C))