def buat_matriks(data):
    return data 

def tampilkan_matriks(m):
    for baris in m:
        print(baris)

def buat_matriks(data):
    return data

def tampilkan_matriks(m):
    for baris in m:
        print(baris)

def tambah_matriks(A, B):
    # Menghitung baris dan kolom
    baris = len(A)
    kolom = len(A[0])
    
    # Inisialisasi matriks hasil dengan nol
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] + B[i][j]
    return hasil

def kurang_matriks(A, B):
    baris = len(A)
    kolom = len(A[0])
    
    hasil = [[0 for _ in range(kolom)] for _ in range(baris)]
    
    for i in range(baris):
        for j in range(kolom):
            hasil[i][j] = A[i][j] - B[i][j]
    return hasil

import naurah069

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

B = [[10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]]


print("Matriks A:")
naurah069.tampilkan_matriks(A)

print("Matriks B:")
naurah069.tampilkan_matriks(B)

print("Hasil Penjumlahan:")
naurah069.tampilkan_matriks(naurah069.tambah_matriks(A, B))

print("Hasil Pengurangan:")
naurah069.tampilkan_matriks(naurah069.kurang_matriks(A, B))
