# Kuis Tipe Data
"""
TODO:
Buatlah variabel firstName, lastName, age, isMarried dengan ketentuan:
- firstName: isi dengan nama depan Anda bertipe data string.
- lastName: isi dengan nama belakang Anda bertipe data string.
- age: isi dengan umur Anda bertipe data integer.
- isMarried: isi dengan status pernikahan Anda bertipe data boolean.

Catatan:
- Value variabel harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""

# TODO: Silakan buat kode Anda di bawah ini.
firstName= "Faris Jihadi "
lastName= "Hanif Lubis"
age= 18
isMarried= False
print(firstName+lastName, age, isMarried)
"""
Output:
Faris Jihadi Hanif Lubis 18 False
"""

# kuis Dictionary
"""
TODO:
Buatlah variabel dictionary dengan nama "data_diri",
variabel tersebut berisi identitas diri Anda berdasarkan ketentuan berikut.
- Memiliki key bernama "firstName":
    - Isi value dengan nama depan Anda, pastikan bertipe data string.
- Memiliki key bernama "lastName":
    - Isi value dengan nama terakhir Anda, pastikan bertipe data string.
- Memiliki key bernama "age":
    - Isi value dengan umur Anda, pastikan bertipe data integer.
- Memiliki key bernama "isMarried":
    - Isi value dengan status pernikahan Anda, pastikan bertipe data boolean.

Catatan:
- Value pada dictionary harus berupa nilai sesungguhnya (literal) seperti string, 
  bilangan bulat (integer), dan boolean (benar atau salah).
"""


# TODO: Silakan buat kode Anda di bawah ini.
data_diri ={"firstName": 'Faris Jihadi', "lastName": 'Hanif Lubis', "age": 18, "isMarried": False}
print(data_diri)
"""
Output:
{'firstName': 'Faris Jihadi', 'lastName': 'Hanif Lubis', 'age': 18, 'isMarried': False}
"""

# Kuis Operasi List
"""
TODO:
Diberikan sebuah variabel berisi nilai list dengan nama "var_list". 
Berdasarkan list tersebut, cari hal-hal berikut ini:
- Panjang list tersebut dan simpan dengan nama variabel "panjang".
- Nilai maksimal list tersebut dan simpan dengan nama variabel "maksimal".
- Nilai minimal list tersebut dan simpan dengan nama variabel "minimal".
- Berapa banyak angka 605132 dalam list tersebut dan simpan dalam variabel bernama "banyak"

Tips:
- Anda bisa menggunakan berbagai kode yang ada di materi operasi, 
  tidak diperbolehkan memasukan nilai secara langsung.
"""

# Jangan ubah kode ini
var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
235780, 857943, 605132, 125094, 620493, 913250
]

# TODO: Buat kode Anda di bawah ini
panjang = len(var_list)
maksimal = max(var_list)
minimal = min(var_list)
banyak = var_list.count(605132)
print(f"panjang = {panjang},\n maksimal = {maksimal},\n minimal = {minimal},\n banyak = {banyak}")
"""
Output:
panjang = 96,
maksimal = 985026,
minimal = 109237,
banyak = 8
"""
# Kuis Berinteraksi dengan Data
print(dict([['name','Dicoding'],['age',17]]))

data = ['dress', 'red']
apparel, color = data
print(apparel)
print(color)

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

name = 'Dicoding Indonesia'
print(f"Hello, saya belajar coding di {name}")

# x = 'Dicoding'
# x[0] = 'F'
print(x)
# KUIS EKSPRESI
"""
TODO:
Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
- Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
- Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
- Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
  dan simpan dalam variabel bernama "total_harga".

Tips:
- Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
"""
# Jangan ubah kode ini
dico = 750000

# TODO: Silakan buat kode Anda di bawah ini.
dico = 750000
discount = dico * 0.1
total_harga = dico - discount
print(total_harga)
"""
Output:
675000.0
"""