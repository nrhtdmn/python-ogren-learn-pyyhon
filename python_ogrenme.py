import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QLineEdit,
    QMessageBox,
    QTextEdit,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import io
import contextlib


class PythonOgrenmeAraci(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.gorevleriYukle()
        self.gorevGoster()

    def initUI(self):
        self.setWindowTitle("Python Öğrenme Aracı")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.gorev_etiketi = QLabel("", self)
        self.gorev_etiketi.setAlignment(Qt.AlignCenter)
        self.gorev_etiketi.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.gorev_etiketi)

        self.kod_girdisi = QTextEdit(self)
        self.kod_girdisi.setFont(QFont("Courier", 12))
        self.layout.addWidget(self.kod_girdisi)

        self.buton_layout = QHBoxLayout()

        self.kontrol_butonu = QPushButton("Kontrol Et", self)
        self.kontrol_butonu.setFixedSize(150, 40)
        self.kontrol_butonu.setStyleSheet("font-size: 18px;")
        self.kontrol_butonu.clicked.connect(self.koduKontrolEt)
        self.buton_layout.addWidget(self.kontrol_butonu, alignment=Qt.AlignCenter)

        self.sonraki_buton = QPushButton("Sonraki Görev", self)
        self.sonraki_buton.setFixedSize(150, 40)
        self.sonraki_buton.setStyleSheet("font-size: 18px;")
        self.sonraki_buton.clicked.connect(self.sonrakiGorev)
        self.buton_layout.addWidget(self.sonraki_buton, alignment=Qt.AlignCenter)

        self.layout.addLayout(self.buton_layout)

        self.central_widget.setLayout(self.layout)

        self.show()

    def gorevleriYukle(self):

        self.gorevler = [
            {
                "soru": "1. Görev: 'Merhaba, Dünya!' yazdırın.",
                "kontrol": "print('Merhaba, Dünya!')",
            },
            {
                "soru": "2. Görev: 2 ile 3'ü toplayın ve sonucu yazdırın.",
                "kontrol": "print(2 + 3)",
            },
            {
                "soru": "3. Görev: 10 ile 20'yi çarpın ve sonucu yazdırın.",
                "kontrol": "print(10 * 20)",
            },
            {
                "soru": "4. Görev: 100'ü 5'e bölün ve sonucu yazdırın.",
                "kontrol": "print(100 / 5)",
            },
            {
                "soru": "5. Görev: 15'i 4'e bölün ve tam sayı kısmını yazdırın.",
                "kontrol": "print(15 // 4)",
            },
            {
                "soru": "6. Görev: 5'in 3. kuvvetini hesaplayın ve sonucu yazdırın.",
                "kontrol": "print(5 ** 3)",
            },
            {
                "soru": "7. Görev: 'Python' ve 'Öğreniyorum' kelimelerini birleştirerek yazdırın.",
                "kontrol": "print('Python' + ' Öğreniyorum')",
            },
            {
                "soru": "8. Görev: 'Python' kelimesini 5 kez tekrar ederek yazdırın.",
                "kontrol": "print('Python' * 5)",
            },
            {
                "soru": "9. Görev: 25 sayısının karekökünü hesaplayın ve sonucu yazdırın.",
                "kontrol": "import math\nprint(math.sqrt(25))",
            },
            {
                "soru": "10. Görev: 50 ile 75 arasındaki rastgele bir sayıyı yazdırın.",
                "kontrol": "import random\nprint(random.randint(50, 75))",
            },
            {
                "soru": "11. Görev: Kullanıcıdan adını alıp 'Merhaba, [ad]' şeklinde yazdırın.",
                "kontrol": "ad = input('Adınız: ')\nprint(f'Merhaba, {ad}')",
            },
            {
                "soru": "12. Görev: Kullanıcıdan iki sayı alıp toplayarak sonucu yazdırın.",
                "kontrol": "sayi1 = int(input('Birinci sayı: '))\nsayi2 = int(input('İkinci sayı: '))\nprint(sayi1 + sayi2)",
            },
            {
                "soru": "13. Görev: Kullanıcıdan bir sayı alıp, sayının tek veya çift olduğunu yazdırın.",
                "kontrol": "sayi = int(input('Sayı: '))\nif sayi % 2 == 0:\n    print('Çift')\nelse:\n    print('Tek')",
            },
            {
                "soru": "14. Görev: 0'dan 9'a kadar olan sayıları yazdırın.",
                "kontrol": "for i in range(10):\n    print(i)",
            },
            {
                "soru": "15. Görev: 1'den 10'a kadar olan sayıların toplamını yazdırın.",
                "kontrol": "print(sum(range(1, 11)))",
            },
            {
                "soru": "16. Görev: 5 ile 15 arasındaki sayıları içeren bir liste oluşturun ve yazdırın.",
                "kontrol": "liste = list(range(5, 16))\nprint(liste)",
            },
            {
                "soru": "17. Görev: [1, 2, 3, 4, 5] listesindeki her elemanın karesini alıp yeni bir liste oluşturun.",
                "kontrol": "liste = [1, 2, 3, 4, 5]\nkaresi = [x**2 for x in liste]\nprint(karesi)",
            },
            {
                "soru": "18. Görev: [3, 6, 9, 12, 15] listesindeki çift sayıları yazdırın.",
                "kontrol": "liste = [3, 6, 9, 12, 15]\nfor x in liste:\n    if x % 2 == 0:\n        print(x)",
            },
            {
                "soru": "19. Görev: Kullanıcıdan aldığı yaşa göre reşit olup olmadığını yazdırın. (18 yaş ve üstü reşit kabul edilir).",
                "kontrol": "yas = int(input('Yaşınız: '))\nif yas >= 18:\n    print('Reşit')\nelse:\n    print('Reşit Değil')",
            },
            {
                "soru": "20. Görev: Kullanıcıdan bir kelime alıp kelimenin uzunluğunu yazdırın.",
                "kontrol": "kelime = input('Bir kelime: ')\nprint(len(kelime))",
            },
            {
                "soru": "21. Görev: 'hello' kelimesinin tüm harflerini büyük harfe çevirin ve yazdırın.",
                "kontrol": "print('hello'.upper())",
            },
            {
                "soru": "22. Görev: 'WORLD' kelimesinin tüm harflerini küçük harfe çevirin ve yazdırın.",
                "kontrol": "print('WORLD'.lower())",
            },
            {
                "soru": "23. Görev: '  Python  ' kelimesinin başındaki ve sonundaki boşlukları kaldırın ve yazdırın.",
                "kontrol": "print('  Python  '.strip())",
            },
            {
                "soru": "24. Görev: 'Python' kelimesinin ilk 3 harfini yazdırın.",
                "kontrol": "print('Python'[:3])",
            },
            {
                "soru": "25. Görev: 'Python' kelimesinin son 3 harfini yazdırın.",
                "kontrol": "print('Python'[-3:])",
            },
            {
                "soru": "26. Görev: Kullanıcıdan aldığı iki sayının en büyüğünü yazdırın.",
                "kontrol": "sayi1 = int(input('Birinci sayı: '))\nsayi2 = int(input('İkinci sayı: '))\nprint(max(sayi1, sayi2))",
            },
            {
                "soru": "27. Görev: Kullanıcıdan aldığı üç sayının ortalamasını hesaplayıp yazdırın.",
                "kontrol": "sayi1 = int(input('Birinci sayı: '))\nsayi2 = int(input('İkinci sayı: '))\nsayi3 = int(input('Üçüncü sayı: '))\nprint((sayi1 + sayi2 + sayi3) / 3)",
            },
            {
                "soru": "28. Görev: Bir listeyi ters çevirip yazdırın. [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]",
                "kontrol": "liste = [1, 2, 3, 4, 5]\nliste.reverse()\nprint(liste)",
            },
            {
                "soru": "29. Görev: Bir listedeki en büyük sayıyı bulun ve yazdırın. [10, 20, 30, 40, 50]",
                "kontrol": "liste = [10, 20, 30, 40, 50]\nprint(max(liste))",
            },
            {
                "soru": "30. Görev: Bir listedeki en küçük sayıyı bulun ve yazdırın. [10, 20, 30, 40, 50]",
                "kontrol": "liste = [10, 20, 30, 40, 50]\nprint(min(liste))",
            },
            {
                "soru": "31. Görev: 5 faktöriyel (5!) hesaplayın ve sonucu yazdırın.",
                "kontrol": "import math\nprint(math.factorial(5))",
            },
            {
                "soru": "32. Görev: 3.14159 sayısını en yakın tam sayıya yuvarlayın ve sonucu yazdırın.",
                "kontrol": "print(round(3.14159))",
            },
            {
                "soru": "33. Görev: 5.6789 sayısını 2 ondalık basamağa yuvarlayın ve sonucu yazdırın.",
                "kontrol": "print(round(5.6789, 2))",
            },
            {
                "soru": "34. Görev: Kullanıcıdan aldığı kelimenin tersini yazdırın.",
                "kontrol": "kelime = input('Bir kelime: ')\nprint(kelime[::-1])",
            },
            {
                "soru": "35. Görev: Kullanıcıdan aldığı sayının negatif olup olmadığını kontrol edip sonucu yazdırın.",
                "kontrol": "sayi = int(input('Sayı: '))\nif sayi < 0:\n    print('Negatif')\nelse:\n    print('Negatif Değil')",
            },
            {
                "soru": "36. Görev: Kullanıcıdan aldığı kelimenin sadece ilk harfini büyük yapıp yazdırın.",
                "kontrol": "kelime = input('Bir kelime: ')\nprint(kelime.capitalize())",
            },
            {
                "soru": "37. Görev: Kullanıcıdan aldığı cümledeki kelimelerin ilk harflerini büyük yapıp yazdırın.",
                "kontrol": "cumle = input('Bir cümle: ')\nprint(cumle.title())",
            },
            {
                "soru": "38. Görev: Bir listede aranan bir elemanın olup olmadığını kontrol edin. [1, 2, 3, 4, 5], aranan: 3",
                "kontrol": "liste = [1, 2, 3, 4, 5]\narama = 3\nprint(arama in liste)",
            },
            {
                "soru": "39. Görev: Bir listede bir elemanın kaç kez geçtiğini bulun. [1, 2, 2, 3, 3, 3], aranan: 2",
                "kontrol": "liste = [1, 2, 2, 3, 3, 3]\narama = 2\nprint(liste.count(arama))",
            },
            {
                "soru": "40. Görev: Bir listeyi sıralayın ve yazdırın. [5, 2, 9, 1, 5, 6]",
                "kontrol": "liste = [5, 2, 9, 1, 5, 6]\nliste.sort()\nprint(liste)",
            },
            {
                "soru": "41. Görev: Bir listede her elemanın karesini alıp yeni bir liste oluşturun. [1, 2, 3, 4, 5]",
                "kontrol": "liste = [1, 2, 3, 4, 5]\nkaresi = [x**2 for x in liste]\nprint(karesi)",
            },
            {
                "soru": "42. Görev: Kullanıcıdan aldığı iki sayıyı karşılaştırın ve büyük olanı yazdırın.",
                "kontrol": "sayi1 = int(input('Birinci sayı: '))\nsayi2 = int(input('İkinci sayı: '))\nprint(max(sayi1, sayi2))",
            },
            {
                "soru": "43. Görev: Bir sözlük oluşturun ve bir anahtar-değer çifti ekleyin. {'ad': 'Ahmet'}",
                "kontrol": "sozluk = {'ad': 'Ahmet'}\nprint(sozluk)",
            },
            {
                "soru": "44. Görev: Bir sözlükte bir anahtarın olup olmadığını kontrol edin. {'ad': 'Ahmet'}, anahtar: 'ad'",
                "kontrol": "sozluk = {'ad': 'Ahmet'}\nprint('ad' in sozluk)",
            },
            {
                "soru": "45. Görev: Bir sözlükte bir anahtarın değerini yazdırın. {'ad': 'Ahmet'}, anahtar: 'ad'",
                "kontrol": "sozluk = {'ad': 'Ahmet'}\nprint(sozluk['ad'])",
            },
            {
                "soru": "46. Görev: Bir sözlükte bir anahtar-değer çiftini silin. {'ad': 'Ahmet'}, silinecek: 'ad'",
                "kontrol": "sozluk = {'ad': 'Ahmet'}\ndel sozluk['ad']\nprint(sozluk)",
            },
            {
                "soru": "47. Görev: Bir demet oluşturun ve elemanlarını yazdırın. (1, 2, 3, 4, 5)",
                "kontrol": "demet = (1, 2, 3, 4, 5)\nprint(demet)",
            },
            {
                "soru": "48. Görev: Bir demetin bir elemanını yazdırın. (1, 2, 3, 4, 5), eleman: 3",
                "kontrol": "demet = (1, 2, 3, 4, 5)\nprint(demet[2])",
            },
            {
                "soru": "49. Görev: Bir demetin uzunluğunu yazdırın. (1, 2, 3, 4, 5)",
                "kontrol": "demet = (1, 2, 3, 4, 5)\nprint(len(demet))",
            },
            {
                "soru": "50. Görev: Bir kümeyi yazdırın. {1, 2, 3, 4, 5}",
                "kontrol": "kume = {1, 2, 3, 4, 5}\nprint(kume)",
            },
            {
                "soru": "51. Görev: Bir kümeye eleman ekleyin ve yazdırın. {1, 2, 3, 4, 5}, eklenen: 6",
                "kontrol": "kume = {1, 2, 3, 4, 5}\nkume.add(6)\nprint(kume)",
            },
            {
                "soru": "52. Görev: Bir kümeden eleman çıkarın ve yazdırın. {1, 2, 3, 4, 5}, çıkarılan: 3",
                "kontrol": "kume = {1, 2, 3, 4, 5}\nkume.remove(3)\nprint(kume)",
            },
            {
                "soru": "53. Görev: Bir listeyi kümeye dönüştürün ve yazdırın. [1, 2, 2, 3, 4, 4, 5]",
                "kontrol": "liste = [1, 2, 2, 3, 4, 4, 5]\nkume = set(liste)\nprint(kume)",
            },
            {
                "soru": "54. Görev: Bir fonksiyon tanımlayın ve çağırın. def selamla(): 'Merhaba!'",
                "kontrol": "def selamla():\n    print('Merhaba!')\nselamla()",
            },
            {
                "soru": "55. Görev: Parametre alan bir fonksiyon tanımlayın ve çağırın. def selamla(ad): 'Merhaba, [ad]!'",
                "kontrol": "def selamla(ad):\n    print(f'Merhaba, {ad}!')\nselamla('Ahmet')",
            },
            {
                "soru": "56. Görev: Geriye değer döndüren bir fonksiyon tanımlayın ve sonucu yazdırın. def topla(a, b): return a + b",
                "kontrol": "def topla(a, b):\n    return a + b\nprint(topla(2, 3))",
            },
            {
                "soru": "57. Görev: Bir listeyi parametre olarak alan ve toplamını döndüren bir fonksiyon yazın.",
                "kontrol": "def liste_toplami(liste):\n    return sum(liste)\nprint(liste_toplami([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "58. Görev: Bir sözlükteki tüm anahtarları yazdıran bir fonksiyon yazın.",
                "kontrol": "def anahtarlar(sozluk):\n    for anahtar in sozluk.keys():\n        print(anahtar)\nanahtarlar({'ad': 'Ahmet', 'yas': 30})",
            },
            {
                "soru": "59. Görev: Bir sözlükteki tüm değerleri yazdıran bir fonksiyon yazın.",
                "kontrol": "def degerler(sozluk):\n    for deger in sozluk.values():\n        print(deger)\ndegerler({'ad': 'Ahmet', 'yas': 30})",
            },
            {
                "soru": "60. Görev: Bir sözlükteki anahtar-değer çiftlerini yazdıran bir fonksiyon yazın.",
                "kontrol": "def ciftler(sozluk):\n    for anahtar, deger in sozluk.items():\n        print(f'{anahtar}: {deger}')\nciftler({'ad': 'Ahmet', 'yas': 30})",
            },
            {
                "soru": "61. Görev: Bir dosya oluşturun ve içine 'Merhaba, Dünya!' yazın.",
                "kontrol": "with open('merhaba.txt', 'w') as dosya:\n    dosya.write('Merhaba, Dünya!')",
            },
            {
                "soru": "62. Görev: Bir dosya oluşturun ve içine kullanıcıdan aldığı metni yazın.",
                "kontrol": "metin = input('Bir metin: ')\nwith open('metin.txt', 'w') as dosya:\n    dosya.write(metin)",
            },
            {
                "soru": "63. Görev: Bir dosyadan metni okuyun ve yazdırın.",
                "kontrol": "with open('metin.txt', 'r') as dosya:\n    print(dosya.read())",
            },
            {
                "soru": "64. Görev: Bir dosyaya ekleme yapın. (Dosyada mevcut olan metne ekleyin)",
                "kontrol": "with open('metin.txt', 'a') as dosya:\n    dosya.write('\\nEklenen metin')",
            },
            {
                "soru": "65. Görev: Kullanıcıdan aldığı metni bir dosyaya ekleyin.",
                "kontrol": "metin = input('Bir metin: ')\nwith open('metin.txt', 'a') as dosya:\n    dosya.write(f'\\n{metin}')",
            },
            {
                "soru": "66. Görev: Bir listeyi bir dosyaya yazın. ['Python', 'Java', 'C++']",
                "kontrol": "liste = ['Python', 'Java', 'C++']\nwith open('diller.txt', 'w') as dosya:\n    for dil in liste:\n        dosya.write(dil + '\\n')",
            },
            {
                "soru": "67. Görev: Bir dosyadan liste okuyun ve yazdırın. (Her satır bir liste elemanı olacak)",
                "kontrol": "with open('diller.txt', 'r') as dosya:\n    liste = dosya.read().splitlines()\nprint(liste)",
            },
            {
                "soru": "68. Görev: Kullanıcıdan aldığı metni bir listeye ekleyip yazdırın.",
                "kontrol": "liste = []\nmetin = input('Bir metin: ')\nliste.append(metin)\nprint(liste)",
            },
            {
                "soru": "69. Görev: Bir metin dosyasını satır satır okuyup yazdırın.",
                "kontrol": "with open('metin.txt', 'r') as dosya:\n    for satir in dosya:\n        print(satir.strip())",
            },
            {
                "soru": "70. Görev: Bir sayının asal olup olmadığını kontrol eden bir fonksiyon yazın.",
                "kontrol": "def asal_mi(sayi):\n    if sayi <= 1:\n        return False\n    for i in range(2, sayi):\n        if sayi % i == 0:\n            return False\n    return True\nprint(asal_mi(17))",
            },
            {
                "soru": "71. Görev: Bir metindeki tüm kelimeleri ters çeviren bir fonksiyon yazın.",
                "kontrol": "def kelimeleri_ters_cevir(metin):\n    kelimeler = metin.split()\n    ters = [kelime[::-1] for kelime in kelimeler]\n    return ' '.join(ters)\nprint(kelimeleri_ters_cevir('Merhaba Dünya'))",
            },
            {
                "soru": "72. Görev: Bir listedeki çift sayıları filtreleyen bir fonksiyon yazın.",
                "kontrol": "def ciftleri_filtrele(liste):\n    return [x for x in liste if x % 2 == 0]\nprint(ciftleri_filtrele([1, 2, 3, 4, 5, 6]))",
            },
            {
                "soru": "73. Görev: Bir listedeki tek sayıları filtreleyen bir fonksiyon yazın.",
                "kontrol": "def tekleri_filtrele(liste):\n    return [x for x in liste if x % 2 != 0]\nprint(tekleri_filtrele([1, 2, 3, 4, 5, 6]))",
            },
            {
                "soru": "74. Görev: Bir listedeki pozitif sayıları filtreleyen bir fonksiyon yazın.",
                "kontrol": "def pozitifleri_filtrele(liste):\n    return [x for x in liste if x > 0]\nprint(pozitifleri_filtrele([-1, 2, -3, 4, 5]))",
            },
            {
                "soru": "75. Görev: Bir listedeki negatif sayıları filtreleyen bir fonksiyon yazın.",
                "kontrol": "def negatifleri_filtrele(liste):\n    return [x for x in liste if x < 0]\nprint(negatifleri_filtrele([-1, 2, -3, 4, 5]))",
            },
            {
                "soru": "76. Görev: Bir listeyi çift ve tek sayılara ayıran bir fonksiyon yazın.",
                "kontrol": "def cift_ve_tek(liste):\n    ciftler = [x for x in liste if x % 2 == 0]\n    tekler = [x for x in liste if x % 2 != 0]\n    return ciftler, tekler\nprint(cift_ve_tek([1, 2, 3, 4, 5, 6]))",
            },
            {
                "soru": "77. Görev: Bir listedeki elemanları ters sırayla döndüren bir fonksiyon yazın.",
                "kontrol": "def ters_cevir(liste):\n    return liste[::-1]\nprint(ters_cevir([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "78. Görev: Bir metindeki sesli harfleri sayan bir fonksiyon yazın.",
                "kontrol": "def sesli_harf_sayisi(metin):\n    sesli_harfler = 'aeiouAEIOU'\n    return sum(1 for harf in metin if harf in sesli_harfler)\nprint(sesli_harf_sayisi('Merhaba Dünya'))",
            },
            {
                "soru": "79. Görev: Bir metindeki sessiz harfleri sayan bir fonksiyon yazın.",
                "kontrol": "def sessiz_harf_sayisi(metin):\n    sesli_harfler = 'aeiouAEIOU'\n    return sum(1 for harf in metin if harf.isalpha() and harf not in sesli_harfler)\nprint(sessiz_harf_sayisi('Merhaba Dünya'))",
            },
            {
                "soru": "80. Görev: Bir metindeki kelimeleri alfabetik sıraya göre sıralayan bir fonksiyon yazın.",
                "kontrol": "def alfabetik_sirala(metin):\n    kelimeler = metin.split()\n    kelimeler.sort()\n    return ' '.join(kelimeler)\nprint(alfabetik_sirala('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "81. Görev: Bir metindeki cümleleri ters sırayla yazdıran bir fonksiyon yazın.",
                "kontrol": "def cumleleri_ters_cevir(metin):\n    cumleler = metin.split('. ')\n    cumleler = [cumle.strip() for cumle in cumleler]\n    return '. '.join(cumleler[::-1])\nprint(cumleleri_ters_cevir('Python öğrenmek çok eğlenceli. Python çok güçlü bir dil.'))",
            },
            {
                "soru": "82. Görev: Bir listedeki en büyük ve en küçük sayıyı bulan bir fonksiyon yazın.",
                "kontrol": "def en_buyuk_ve_en_kucuk(liste):\n    return max(liste), min(liste)\nprint(en_buyuk_ve_en_kucuk([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "83. Görev: Bir listeyi küçükten büyüğe sıralayan bir fonksiyon yazın.",
                "kontrol": "def kucukten_buyuge(liste):\n    liste.sort()\n    return liste\nprint(kucukten_buyuge([5, 3, 2, 4, 1]))",
            },
            {
                "soru": "84. Görev: Bir listeyi büyükten küçüğe sıralayan bir fonksiyon yazın.",
                "kontrol": "def buyukten_kucuge(liste):\n    liste.sort(reverse=True)\n    return liste\nprint(buyukten_kucuge([5, 3, 2, 4, 1]))",
            },
            {
                "soru": "85. Görev: Bir sayının faktöriyelini hesaplayan bir fonksiyon yazın.",
                "kontrol": "def faktoriyel(sayi):\n    if sayi == 0:\n        return 1\n    else:\n        return sayi * faktoriyel(sayi-1)\nprint(faktoriyel(5))",
            },
            {
                "soru": "86. Görev: Bir listenin elemanlarını toplayan bir fonksiyon yazın.",
                "kontrol": "def liste_toplami(liste):\n    return sum(liste)\nprint(liste_toplami([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "87. Görev: Bir listenin ortalamasını hesaplayan bir fonksiyon yazın.",
                "kontrol": "def liste_ortalamasi(liste):\n    return sum(liste) / len(liste)\nprint(liste_ortalamasi([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "88. Görev: Bir listenin medyanını hesaplayan bir fonksiyon yazın.",
                "kontrol": "def liste_medyani(liste):\n    liste.sort()\n    n = len(liste)\n    if n % 2 == 0:\n        medyan = (liste[n//2 - 1] + liste[n//2]) / 2\n    else:\n        medyan = liste[n//2]\n    return medyan\nprint(liste_medyani([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "89. Görev: Bir metindeki kelimeleri sayan bir fonksiyon yazın.",
                "kontrol": "def kelime_sayisi(metin):\n    kelimeler = metin.split()\n    return len(kelimeler)\nprint(kelime_sayisi('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "90. Görev: Bir listedeki en uzun kelimeyi bulan bir fonksiyon yazın.",
                "kontrol": "def en_uzun_kelime(liste):\n    return max(liste, key=len)\nprint(en_uzun_kelime(['Python', 'öğrenmek', 'çok', 'eğlenceli']))",
            },
            {
                "soru": "91. Görev: Bir listedeki en kısa kelimeyi bulan bir fonksiyon yazın.",
                "kontrol": "def en_kisa_kelime(liste):\n    return min(liste, key=len)\nprint(en_kisa_kelime(['Python', 'öğrenmek', 'çok', 'eğlenceli']))",
            },
            {
                "soru": "92. Görev: Bir metindeki en sık geçen kelimeyi bulan bir fonksiyon yazın.",
                "kontrol": "def en_sik_kelime(metin):\n    kelimeler = metin.split()\n    kelime_sayilari = {kelime: kelimeler.count(kelime) for kelime in kelimeler}\n    return max(kelime_sayilari, key=kelime_sayilari.get)\nprint(en_sik_kelime('Python öğrenmek çok eğlenceli. Python çok güçlü bir dil.'))",
            },
            {
                "soru": "93. Görev: Bir metindeki en uzun kelimeyi bulan bir fonksiyon yazın.",
                "kontrol": "def en_uzun_kelime(metin):\n    kelimeler = metin.split()\n    return max(kelimeler, key=len)\nprint(en_uzun_kelime('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "94. Görev: Bir metindeki en kısa kelimeyi bulan bir fonksiyon yazın.",
                "kontrol": "def en_kisa_kelime(metin):\n    kelimeler = metin.split()\n    return min(kelimeler, key=len)\nprint(en_kisa_kelime('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "95. Görev: Bir metindeki tüm kelimeleri büyük harfle yazdıran bir fonksiyon yazın.",
                "kontrol": "def buyuk_harfler(metin):\n    kelimeler = metin.split()\n    buyukler = [kelime.upper() for kelime in kelimeler]\n    return ' '.join(buyukler)\nprint(buyuk_harfler('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "96. Görev: Bir metindeki tüm kelimeleri küçük harfle yazdıran bir fonksiyon yazın.",
                "kontrol": "def kucuk_harfler(metin):\n    kelimeler = metin.split()\n    kucukler = [kelime.lower() for kelime in kelimeler]\n    return ' '.join(kucukler)\nprint(kucuk_harfler('Python öğrenmek çok eğlenceli'))",
            },
            {
                "soru": "97. Görev: Bir listedeki tüm elemanları çift olan bir liste döndüren bir fonksiyon yazın.",
                "kontrol": "def hepsi_cift_mi(liste):\n    return all(x % 2 == 0 for x in liste)\nprint(hepsi_cift_mi([2, 4, 6, 8]))",
            },
            {
                "soru": "98. Görev: Bir listedeki tüm elemanları tek olan bir liste döndüren bir fonksiyon yazın.",
                "kontrol": "def hepsi_tek_mi(liste):\n    return all(x % 2 != 0 for x in liste)\nprint(hepsi_tek_mi([1, 3, 5, 7]))",
            },
            {
                "soru": "99. Görev: Bir listedeki tüm elemanları pozitif olan bir liste döndüren bir fonksiyon yazın.",
                "kontrol": "def hepsi_pozitif_mi(liste):\n    return all(x > 0 for x in liste)\nprint(hepsi_pozitif_mi([1, 2, 3, 4, 5]))",
            },
            {
                "soru": "100. Görev: Bir listedeki tüm elemanları negatif olan bir liste döndüren bir fonksiyon yazın.",
                "kontrol": "def hepsi_negatif_mi(liste):\n    return all(x < 0 for x in liste)\nprint(hepsi_negatif_mi([-1, -2, -3, -4, -5]))",
            },
        ]

        self.gorev_index = 0

    def gorevGoster(self):
        self.gorev_etiketi.setText(self.gorevler[self.gorev_index]["soru"])
        self.kod_girdisi.clear()

    def koduKontrolEt(self):
        kullanici_kodu = self.kod_girdisi.toPlainText()
        dogru_kod = self.gorevler[self.gorev_index]["kontrol"]

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        try:
            exec(kullanici_kodu)
            kullanici_sonucu = new_stdout.getvalue().strip()
        except Exception as e:
            kullanici_sonucu = str(e)

        sys.stdout = old_stdout

        with contextlib.redirect_stdout(io.StringIO()) as f:
            try:
                exec(dogru_kod)
                dogru_sonuc = f.getvalue().strip()
            except Exception as e:
                dogru_sonuc = str(e)

        if kullanici_sonucu == dogru_sonuc:
            QMessageBox.information(self, "Doğru", "Tebrikler! Doğru cevap.")
        else:
            QMessageBox.warning(
                self,
                "Yanlış",
                f"Yanlış cevap.\nBeklenen: {dogru_sonuc}\nAldığınız: {kullanici_sonucu}",
            )

    def sonrakiGorev(self):
        if self.gorev_index < len(self.gorevler) - 1:
            self.gorev_index += 1
            self.gorevGoster()
        else:
            QMessageBox.information(self, "Bitti", "Tüm görevleri tamamladınız!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    python_ogrenme_araci = PythonOgrenmeAraci()
    sys.exit(app.exec_())
