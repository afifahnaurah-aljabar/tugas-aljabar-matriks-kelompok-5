import naurah069 # type: ignore

A = [
    [12, 43, 31],
    [40, 15, 66],
    [13, 23, 45]
]

B = [
    [22, 16, 42],
    [77, 35, 25],
    [37, 25, 11]
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