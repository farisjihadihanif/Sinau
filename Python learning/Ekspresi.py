# Penerapan Ekspresi pada Python
x = 10
y = 2
result = x - y

print(result)

"""
Output:
8
"""
# Penerepan Ekspresi Biner
# Penggabungan dan Replikasi pada List dengan penjumlahan (+)
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

"""
Output:
[2, 4, 6, 8, 'P', 'Y', 'T', 'H', 'O', 'N']
"""
# Penggabungan dan Replikasi pada List dengan perkalian(*)
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)

"""
Output:
['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']
"""
# Penerapan Ekspresi Unner
a = True
a = not a
print(a)

b = 6
b -= 4
print(b)

c = 6
c += 4
print(c)

d = 10
print(-d)


"""
Output:
False
2
10
-10
"""
# Ekspresi Aritmatika,Relasional,Dan Logika
print(2+2)
print(3>10)
print(True or False)
"""
Output:
4
False
True
"""
# Operator Aritmatika
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

"""
Output:
16
6
55
2
2.2
1
161051
"""
# Operator Relasional dengan tipe integer
x = 5
y = 10
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
"""
Output:
False
True
False
True
False
True
"""
# Operator Relasional dengan tipe string
x = 'Dicoding'
y = 'Indonesia'

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
"""
Output:
False
True
False
True
False
True
"""
# Operator Logika AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)
"""
Output:
True
False
False
False
"""
# Operator Logika OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)


"""
Output:

True
True
True
False
"""
# Operator Logika Not
print(not True)
print(not False)

"""
Output:

False
True
"""
# Operator Assignment
x = 11
x += 5
print(x)


x = 11
x = x + 5
print(x)

"""
Output:
16
16
"""
# AKSI SEKUENSIAL
print("Selamat datang dalam program Python!\n")
print("Silakan masukkan data diri Anda.")
nama = input("Masukkan nama Anda: ")
tahun_lahir = input("Masukkan tahun lahir Anda: ")
umur = 2023 - int(tahun_lahir)
 
print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
print("Terima kasih telah menggunakan program Python!")
 
"""
Output:
Selamat datang dalam program Python!
 
Silakan masukkan data diri Anda:
Masukkan nama Anda: Faris Jihadi
Masukkan tahun lahir Anda: 2005
Selamat datang Faris Jihadi dalam program Python, per 2023 umur Anda adalah 18 tahun.
 
Terima kasih telah menggunakan program Python!
"""
# jika urutan baris diubah, TIDAK mengubah hasil eksekusi
a = 6
b = 9
 
result = a + b
print(result)
 
"""
Output:
15
"""
# Perhatikan bahwa urutan inisialisasi variabel a dan b sekarang diubah
b = 9
a = 6

result = a + b
print(result)

"""
Output:
15
"""
#  instruksi yang mengubah hasil?
a = 6
b = 9
 
print(a**2)
print(b//3)
 
"""
Output:
36
3
"""
# ubah urutan sintaks "print()"
a = 6
b = 9

print(b//3)
print(a**2)

"""
Output:
3
36
"""
# PYTHON INTERPRETER
#  penerapan materi perulangan
for i in range(10):
    print(i)

"""
Output:
0
1
2
3
4
5
6
7
8
9
"""
# Letak indentasi kode blok yang salah
# for i in range(10):
#     print(i)

"""
Output:
IndentationError: expected an indented block
"""
#  case-sensitive
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)

"""
Output:
Dicoding
Indonesia
"""
# One-liner (membangun kode dalam satu baris)
x = 1
y = 2

x, y = y, x    # One-liner

print('Setelah pertukaran: ')
print('x =', x)
print('y =', y)



"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""
# Menukar dua variabel
x = 1
y = 2

temp = x
x = y
y = temp

print("Setelah pertukaran: ")
print("x =", x)
print("y =",  y)

"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""
# CONTROL FLOW
# Percabangan
"""
instruksi berdasarkan "Jika-maka" (if-else). 
"""
ketersediaan = "Daging ayam"

if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
Output:
Ibu membeli dan memasak ayam
"""
# If
score = 100

if score == 100:
    print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""
# If One-liner
score = 100

if score == 100: print("Nilai Anda sempurna!")

"""
Output:
Nilai Anda sempurna!
"""
# Else
tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

"""
Output:
Anda tidak diperbolehkan menaiki roller coaster
"""
# Elif (else if)
nilai = 65

if nilai>=80:
   print("Selamat! Anda mendapat nilai A")
   print("Pertahankan!")
elif nilai>=70:
   print("Hore! Anda mendapat nilai B")
   print("Tingkatkan!")
elif nilai>=60:
   print("Hmm.. Anda mendapat nilai C")
   print("Ayo semangat!")
else:
   print("Waduh, Anda mendapat nilai D")
   print("Yuk belajar lebih giat lagi!")


"""
Output:
Hmm.. Anda mendapat nilai C
Ayo semangat!
"""
# Penambahan operator 'and' atau 'or"
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

"""
Output:
Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik
Perbaiki lagi ya!
"""
# Ternary operators (dalam One-liner)
lulus = True
print("selamat") if lulus else print("perbaiki")

"""
Output:
selamat
"""
# Ternary operators (dalam bentuk blok)
lulus = True
if lulus:
    print("Selamat") 
else:
    print("Perbaiki")

"""
Output:
selamat
"""
# Ternary operators (Tuples)
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)

"""
Output:
Selamat, Anda lulus!
"""
# PERULANGAN
# For
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

"""
Output:
1
2
3
4
5
6
7
8
9
10
"""
# While
counter = 1
while counter <= 5:
    print(counter)
    counter += 1    # Increment

"""
Output:
1
2
3
4
5
"""
# For Bersarang (nested loop)
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

"""
Output:
1,1
1,2
2,1
2,2
"""
# Kontrol Perulangan
# Break
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1


"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""
# Contoh lainnya
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
"""
# Continue (mengabaikan statement yang berada antara continue hingga akhir blok)
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""
# Else setelah for (bersifat pencarian)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

"""
Output:
Angka tidak ditemukan.
"""
# Else setelah while (blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah.)
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")


"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""
# Jika di implementasikan menggunakan break
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

"""
Output:
9
8
"""
# Pass Statement (tidak menampilkan apa pun karena jika kondisi terpenuhi)
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

"""
Output:


"""
# List Comprehension
angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

"""
Output:
[1, 4, 9, 16]

"""
# Implementasi ke one-liner
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

"""
Output:
[1, 4, 9, 16]
"""
# 