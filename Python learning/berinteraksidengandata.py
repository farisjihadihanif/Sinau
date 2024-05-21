# Deklarasi dan Inialisasi (tapi dalam Python tidak perlu Deklarasi cukup Inialisasi saja.)
# Penerapan losely typed
age = 17
salary = 5000000.0

print(type(age))
print(type(salary))

"""
Output:
<class ‘int’>
<class ‘float’>
"""
# penerapan dynamic typing
x = 6
print(type(x))

x = "6"
print(type(x))



"""
Output:
<class ‘int’>
<class ‘str’>
"""
# type data numbers
x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""
# contoh type data yang bersifat imutable
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""
# Boolean
x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""
# string
x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""
# string dengan menggunakan tiga single/double quote
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""
# Indexing dari string yaitu setiap variable dimulai dan dibaca dari nol
x = 'Dicoding'
print(x[0])

""" 
Output:
D
"""
# String pada Python bersifat immutable, sehingga  Anda tidak dapat mengubah substring di dalamnya.
# x = 'Dicoding'
# x[0] = 'F'

# """ 
# Output:
# TypeError: 'str' object does not support item assignment
# """
# substring dengan menggunakan metode indexing dan slicing.
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""
# Formatted String
name = "Faris Jihadi Hanif Lubis."
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Faris Jihadi Hanif Lubis.
"""
# %-formatting
name = "Faris Jihadi Hanif Lubis."
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Faris Jihadi Hanif Lubis.
"""
# str.format()
name = "Faris Jihadi Hanif Lubis."
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Faris Jihadi Hanif Lubis.
"""
# nilai yang diawali dengan kurung siku “[]” akan dianggap sebagai data bertipe list
x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output: 
<class ‘list’>
"""
# Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0
x = [1, 'Dicoding', True, 1.0]

print(x[2])

""" 
Output:
True
"""
# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""
# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya
# Beberapa cara untuk melakukan indexing sebagai berikut
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


"""
Output:
laptop
mouse
microphone
keyboard
"""
#  konsep slicing merujuk pada pengambilan data berdasarkan indeks dari rentang tertentu
# sequence[start:stop:step]
x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya
x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""
# indexing dan slicing pada tuple sama seperti list
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

""" 
Output:
program
(5, 'program', (1+3j))
"""
# Tuple bersifat immutable yang artinya tidak dapat diubah
""""
x = (5, 'program', 1+3j)
x[1] = 'Dicoding'
"""

"""
Output:
'tuple' object does not support item assignment
"""
# Set tidak bisa melakukan indeksing
"""
x = {1,2,7,2,3,13,3}
print(x[0])
"""

"""
Output:
'set' object is not subscriptable
"""
# Data yang ada dalam Set tidak dapat di Duplikat
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""
# Union dan Intersection dalam Set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""
# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }

print(type(x))

"""
Output:
<class 'dict'>
"""
# Dictionary juga tidak bisa memakai indexing
"""
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }

print(x[0])
""" 
"""
Output:
KeyError: 0
"""
# Data dictionary bisa diambil dengan memanggil key-nya
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }

print(x ['name'])

""" 
Output:
Faris Jihadi Hanif Lubis.
"""
# Menambahkan data Dicationary
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

"""
Output:
{'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""
# Menghapus Data Dictiionary
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }
del x['isMarried']

print(x)

"""
Output:
{'name': 'Faris Jihadi Hanif Lubis.', 'age': 20}
"""
# Mengubah Data Dictionary
x = { 'name': 'Faris Jihadi Hanif Lubis.', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"

print(x)

"""
Output:
{'name': 'Dicoding', 'age': 20, 'isMarried': False}
"""
# Konversi Integer ke Float
print(float(5))

"""
Output:
5.0
"""
# Konversi Float Ke Integer
print(int(5.6))
print(int(-5.6)) 

""" 
Output:
5
-5
"""
# Konversi dari-dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""
# Perlu Anda perhatikan bahwa konversi dari-dan-ke string akan melalui pengujian dan dipastikan validitasnya. 
# Jika pengujian dan validitasnya gagal, error akan dihasilkan.
"""
print(int("1p"))
"""

"""
Output:
ValueError: invalid literal for int() with base 10: '1p
"""
# Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""
# Konversi ke Dictionary
print(dict([[1,2],[3,4]]))

"""
Output:
{1:2, 3:4}
"""
# Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.
print(dict([(3,26),(4,44)]))

"""
Output:
{3:26, 4:44}
"""
# UPPER Dalam python
kata = 'dicoding'
kata = kata.upper()
print(kata)

"""
Output:
DICODING
"""
# lower Dalam python
kata = 'DICODING'
kata = kata.lower()
print(kata)

"""
Output:
dicoding
"""
# Capitalize Dalam python
kata = 'dicoding'
kata = kata.capitalize()
print(kata)

"""
Output:
DICODING
"""
# Metode rstrip() menghapus whitespace pada sebelah kanan atau akhir string
print("Dicoding          ".rstrip())

"""
Output:
Dicoding
"""
# Kebalikan dari rstrip(), lstrip() bertugas untuk menghapus whitespace pada sebelah kiri atau awal string
print("           Dicoding".lstrip())

"""
Output:
Dicoding
"""
# strip() Metode ini bertugas untuk menghapus whitespace pada bagian awal dan akhir string. 
print("     Dicoding      ".strip())
"""
Output:
Dicoding
"""
# Menghapus Selain Whitespace
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

"""
Output:
Dicoding
"""
# startswith() bertujuan untuk menemukan suatu kata pada awal string
# Operasi ini mengembalikan nilai True, pada string "Dicoding Indonesia" diawali dengan string "Dicoding"
print('Dicoding Indonesia'.startswith('Indonesia'))

"""
Output:
True
"""
# endswith() bertujun untuk menemukan suatu kata pada akhir string / kebalikannya startwith()
print('Dicoding Indonesia'.endswith('Dicoding'))

"""
Output:
False 
Terjadi False karena input dari endswith yang di masukkan adalah awal kata yaitu startswith()
"""
# Memisah dan Menggabung String
print(' '.join(['Dicoding','Indonesia', '!']))

"""
Output:
Dicoding Indonesia !
Single quotes pada kode bermaksud agar Anda menentukan delimiter pada setiap kata/nilai yang ingin Anda gabungkan. 
Pada kode di atas, delimiter-nya adalah whitespace atau spasi.
"""
# Contoh delimiter lain / Dengan Input
print(' 123 '.join(['Faris Jihadi', 'Hanif Lubis.', 'Is My Name', '!']))
"""
Output:
Faris Jihadi 123 Hanif Lubis. 123 Is My Name 123 !
"""
# split() bertujuan untuk memisahkan kata/substring berdasarkan delimiter
print('Dicoding Indonesia!'.split())
"""
Output:
['Dicoding', 'Indonesia', '!']
"""
# menggunakan delimiter newline (\n) untuk memisahkan setiap baris .split('\n')
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""
# replace() mengubah suatu kata pada string
string = "Ayo Belajar Coding Di Dicoding!"
print(string.replace("Coding", "Pemrograman"))
"""
Output:
Ayo Belajar Pemrograman Di Dicoding!
"""
# isupper() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kapital (uppercase) 
# Sebaliknya, jika ada satu huruf saja yang kecil/tidak uppercase, nilai False akan dikembalikan
kata = 'DICODING'
print(kata.isupper())
"""
Output:
True
"""
# islower() akan mengembalikan nilai True jika semua huruf dalam string adalah huruf kecil (lowercase) 
# Sebaliknya, jika ada satu huruf saja yang besar/tidak lowercase, nilai False akan dikembalikan
kata = 'dicoding'
print(kata.islower())
"""
Output:
True
"""
# isalpha() Metode ini mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet
# Jika ada satu huruf lain yang bukan alfabet, seperti angka, nilai False akan dikembalikan
kata = 'farisjihadihanif'
print(kata.isalpha())
"""
Output:
True
"""
# isalnum() mengembalikan nilai True jika karakter dalam string adalah alfanumerik, 
#  yaitu hanya huruf atau hanya angka atau berisi keduanya. Jika tidak, nilai False akan dikembalikan.
kata = "farisjihadihanif695"
print(kata.isalnum())
"""
Output:
True
"""
# isdecimal() akan mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik.
# Jika tidak, nilai False akan dikembalikan.
angka = '12345678910'
print(angka.isdecimal())
"""
Output:
True
"""
# isspace() akan mengembalikan nilai True jika string hanya
# berisi whitespace, seperti spasi, tab, newline, atau karakter whitespace lainnya.
print('     '.isspace())
"""
Output:
True
"""
# istitle() mengembalikan nilai True jika string berisi huruf kapital pada setiap kata pertamanya. 
# Jika tidak, nilai False dikembalikan.
kata = ' Faris Jihadi Hanif Lubis.'
print(kata.istitle())
"""
Output:
True
"""
# zfill() bertujuan untuk menambahkan nilai nol (0) di depan sebuah string 
teks = 'Coding'
print(teks.zfill(5))
"""
Output:
0Coding
"""
# rjust() berguna untuk merapikan pencetakan teks, dengan membuata nya menjadi rata kanan
print('Dicoding'.rjust(20))

"""
Output:
            Dicoding

"""
# rjust() juga bisa di input dengan sebuah data
print('Dicoding'.rjust(20, '!'))

"""
Output:
!!!!!!!!!!!!Dicoding
"""
# ljust() kebalikan dari rjust() yaitu membuat teks menjadi rata kiri
print('Dicoding'.ljust(20))
"""
Output:
Dicoding
"""
# center() menjadikan teks rata tengah
print('Dicoding'.center(10, '-'))

"""
Output:
-Dicoding-

"""
# String Literals
print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")


"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash
"""
Di atas Adalah Macam-Macam sintax-nya
"""
# Rawstring
print(r'Dicoding\tIndonesia')

"""
Output:
Dicoding\tIndonesia

"""
# Perhatikan bahwa escape character (\t) ikut tercetak pada teks tersebut. 
# Hal ini karena raw string akan mencetak string sesuai dengan apa pun input atau teks yang diberikan.

# len() bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.
# List

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)
print(len(contoh_list))

"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""
# Konversi List menjadi Set

contoh_list = set([1, 3, 3, 5, 5, 5, 7, 7, 9])

print(contoh_list)
print(len(contoh_list))

"""
Output:
{1, 3, 5, 7, 9}
5
"""
# len() dengan String
# Perhatikan bahwa karakter space dihitung sebagai karakter string
contoh_list = "Belajar Python"

print(contoh_list)
print(len(contoh_list))

"""
Output:
Belajar Python
14
"""
# min() dan max()
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))

"""
Output:
5
96
"""
# count() digunakan untuk mengetahui berapa kali suatu objek muncul dalam list
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))

"""
Output:
3
"""
# count() juga bisa untuk menghitung string 
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))


"""
Output:
6
# """
# Operator in dan not in akan mengembalikan nilai boolean True atau False
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

"""
Output:
True
False
False
True

"""
# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

"""
Output:
['shirt', 'white', 'L']
"""
# Dalam kode di atas, Anda mengakses indeks pertama pada variabel "data" yang merupakan list, lalu menyimpannya pada variabel baru bernama "apparel". 
# Lalu, berlaku seterusnya, Anda mengakses indeks kedua serta ketiga dan menyimpannya pada variabel baru, masing-masing bernama "color" dan "size".

# sort() untuk mengurutkan angka atau urutan huruf
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
 ['helikopter', 'mobil', 'motor', 'pesawat']
"""
# Membalikkan urutan pada sort()
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

"""
Output:
 ['pesawat', 'motor', 'mobil', 'helikopter']

"""
# Sort() Akan error Apabila terdapat string dan integer secara bersamaan
"""
urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
urutan.sort()

print(urutan)
"""

"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""
# sort menggunakan  ASCII sehingga uppercase akan lebih dahulu dibandingkan lowercase
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)

"""
Output:
['Pesawat', 'helikopter', 'mobil', 'motor']
"""
# keyword "str.lower" pada sort(). Jadi, sort() akan menganggap semua objek menggunakan huruf kecil
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort(key=str.lower)
print(kendaraan)
"""
Output:
['helikopter', 'mobil', 'motor', 'Pesawat']
"""
# Kelar juga,yee baru juga satu.