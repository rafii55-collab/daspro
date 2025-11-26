while True: 
 print("""
````````````` < selamat datang > ```````````````
.______________________________________________.
|       fitur penghitungan yang tersedia       |
|==============================================|
|1.| Perhitungan bangun ruang                  |
|2.| Perhitungan bangun datar                  |
|3.| menentukan suatu bilang prima             |
|4.| skala dan perbandingan                    |
|__|___________________________________________|
          """.title())
 print('')
 pilih_fitur = input('masukan fitur yang kamu inginkan: '.title())

 if pilih_fitur=='1':
    while True:
     print("""
._________________________________.
|        < Bangun Ruang >         |
|=================================|
| > PILIH SALAH SATU BANGUN RUANG |
|=================================|
|1.| Kubus        |5.| bola       |
|2.| Balok        |6.|            |
|3.| Tabung       |7.|            |
|4.| Kerucut      |  |            | 
|__|______________|__|____________|
           """)
     nama = input('> Masukan Nomor Bangun Ruang Yang di Inginkan: ') #type data disini sama di bagian if harus sama
     print(' ')

     if nama=='1': #kubus
         print('> Kubus')
         print('='*70)
         r = float(input('Masukan Panjang Rusuk : '))
         print('='*70)
         luas = 6 * (r * r)
         print('Luas Kubus   = ',luas)
         vol = r * r * r
         print('Volume Kubus = ',vol)
         print('='*70)

     elif nama=='2': # balok
         print('> Balok')
         print('='*70)
         l = float(input('Masukan Lebar   : '))
         t = float(input('Masukan Tinggi  : '))
         p = float(input('Masukan Panjang : '))
         print('='*70)
         luas = 2 * (p*l + p*t + l*t)
         print('Luas Balok   = ',luas)
         vol = p * l * t
         print('Volume Balok = ',vol)
         print('='*70)

     elif nama=='3': # tabung
         print('> Tabung')
         print('='*70)
         r = float(input('Masukan Jari-jari   : '))
         t = float(input('Masukan Tinggi      : '))
         print('='*70)
         luas = 2 * 22/7 * r * (r + t)
         print('Luas Tabung     = ',luas)
         vol = 22/7 * r * r * t
         print('Volume Tabung   = ',vol)
         print('='*70)

     elif nama=='4': # Kerucut
         print('> Kerucut')
         print('='*70)
         r = float(input('Masukan Jari-jari        : '))
         t = float(input('Masukan Tinggi           : '))
         s = float(input('Masukan Sisi-sisi Miring : '))
         print('='*70)
         luas = 22/7 * r * (r + s)
         print('Luas Kerucut     = ',luas)
         vol = 1/3 * 22/7 * r * r * t
         print('Volume Kerucut   = ',vol)
         print('='*70)
         
     elif nama=='5': # bola
         print('> Bola')
         print('='*70)
         r = float(input('Masukan Jari-jari        : '))
         t = float(input('Masukan Tinggi           : '))
         print('='*70)
         luas = 4 * 22/7 * r * r
         print('Luas Bola     = ',luas)
         vol = 4/3 * 22/7 * r * r * r
         print('Volume Bola   = ',vol)
         print('='*70)
         
    
     print(' ')

     syarat = int(input('Apakah Kamu Masih Ingin Lanjut di Bangun Ruang? \nKetik: \n1. Lanjut\n2. Tidak\nMasukan Angka: '))
     print('')
     if syarat==1:
        continue
     elif syarat==2:
        break
     else:
      print(' ')
      print('MASUKAN ANGKA YANG SESUAI')
      print(' ')


             

 elif pilih_fitur=='2': #bangun datar
    while True:
      print("""
._______________________________________.
|           < Bangun Datar >            |
|=======================================|
| > PILIH SALAH SATU BANGUN RUANG       |
|=======================================|
|1.| Persegi         |5.| Trapesium     |
|2.| Persegi Panjang |6.| Belah Ketupat |
|3.| Segitiga        |7.| Layang-layang |
|4.| Jajar Genjang   |8.| Lingkarang    | 
|__|_________________|__|_______________|
           """)
      nama = input('> Masukan Nomor Bangun Datar Yang di Inginkan: ')
      print(' ')

      if nama=='1': #persegi
         print('> Persegi')
         print('='*70)
         sisi = float(input('Masukan Sisi: '))
         print('='*70)
         luas = sisi * sisi
         print('Luas Persegi (Sisi x Sisi)  = ', luas)
         keliling = 4 * sisi
         print('Keliling Persegi (4 x Sisi) = ', keliling)
         print('='*70)
    
      elif nama=='2': #persegi panjang
         print('> Persegi Panjang')
         print('='*70)
         panjang = float(input('Masukan Panjang : '))
         lebar   = float(input('Masukan Lebar   : '))
         print('='*70)
         luas = panjang * lebar
         print('Luas Persegi Panjang (P x L) = ', luas)
         keliling = 2 * (panjang + lebar)
         print('Keliling Persegi Panjang (P + L) = ', keliling)
         print('='*70)

      elif nama=='3': #segitiga
         print('> Segitiga')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         lk = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling\n= '))
         print(' ')
         if lk==1:
             print('> Luas Segitiga')
             print('='*70)
             alas = float(input('Masukan Alas   : '))
             tinggi = float(input('Masukan Tinggi : '))
             print('='*70)
             luas = 1/2 * alas * tinggi
             print('Luas Segitiga (1/2 x Alas x Tinggi) = ', luas)
             print('='*70)
         elif lk==2:
             print('> Keliling Segitiga')
             print('='*70)
             sisi = float(input('Masukan Sisi : '))
             print('='*70)
             keliling = 3 * sisi
             print('Keliling Segitiga (3 x Sisi) = ',keliling )
             print('='*70)
         else:
             print('MASUKAN ANGKA YANG SESUAI')

        
      elif nama=='4': #jajar genjang
         print('> Jajar Genjang')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('> Luas Jajar Genjang')
             print('='*70)
             alas = float(input('Masukan Alas   : '))
             tinggi = float(input('Masukan Tinggi : '))
             print('='*70)
             luas = alas * tinggi
             print('Luas Jajar genjang (Alas x Tinggi) = ',luas)
             print('='*70)
         elif opsi==2:
             print('> Keliling Jajar Genjang')
             print('='*70)
             sisi1 = float(input('Masukan Sisi lurus 1  : ')) 
             sisi2 = float(input('Masukan Sisi lurus 2  : '))
             sisi3 = float(input('Masukan Sisi miring 1 : '))
             sisi4 = float(input('Masukan Sisi miring 2 : '))
             print('='*70)
             keliling = sisi1+sisi2+sisi3+sisi4
             print('Keliling Jajar Genjang (2 x Miring + 2 x Lurus) = ',keliling)
             print('='*70)
         else:
             print('MASUKAN ANGKA YANG SESUAI')

      elif nama=='5': #trapesium
         print('> Trapesium')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('> Luas Trapesium')
             print('='*70)
             sb = float(input('Masukan Sisi Sisi Bawah : '))
             sa = float(input('Masukan Sisi Sisi Atas  : '))
             t =  float(input('Masukan Sisi tinggi     : '))
             print('='*70)
             luas = 1/2 * (sa + sb) * t
             print('Luas Trapesium (1/2 x (sisi atas + sisi bawah) x tinggi) = ', luas)
             print('='*70)
         elif opsi==2:
             print('> Keliling Trapesium')
             print('='*70)
             s1 = float(input('Masukan Sisi Sisi 1 : '))
             s2 = float(input('Masukan Sisi Sisi 2 : '))
             s3 = float(input('Masukan Sisi Sisi 3 : '))
             s4 = float(input('Masukan Sisi Sisi 4 : '))
             print('='*70)
             keliling = s1 + s2 + s3 +s4
             print('Keliling Trapesium (sisi + sisi + sisi + sisi) = ', keliling)
             print('='*70)
         else:
             print('MASUKAN ANGKA YANG SESUAI')

      elif nama=='6': #belah ketupat
         print('> Belah Ketupat')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('> Luas Belah Ketupat')
             print('='*70)
             d1 = float(input('Masukan Diagonal 1 : '))
             d2 = float(input('Masukan Diagonal 2 : '))
             print('='*70)
             luas = 1/2 * d1 * d2
             print('Luas Belah Ketupat (1/2 x Diagonal 1 x Diagonal 2) =', luas)
             print('='*70)
         elif opsi==2:
             print('> Keliling Belah Ketupat')
             print('='*70)
             sisi = float(input('Masukan Sisi : '))
             print('='*70)
             keliling = 4 * sisi
             print('Keliling Belah ketupat (4 x Sisi) = ', keliling)
             print('='*70)
         else:
             print('MASUKAN ANGKA YANG SESUAI')

      elif nama=='7': #layang layang
         print('> Layang-layang')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('> Luas Layang-layang')
             print('='*70)
             d1 = float(input('Masukan Diagonal 1 : '))
             d2 = float(input('Masukan Diagonal 2 : '))
             print('='*70)
             luas = 1/2 * d1 * d2
             print('Luas Layang-layang (1/2 x Diagonal 1 x Diagonal 2) = ', luas)
             print('='*70)
         elif opsi==2:
             print('> Keliling Layang-layang')
             print('='*70)
             sisia = float(input('Masukan Sisi Atas  : '))
             sisib = float(input('Masukan Sisi Bawah : '))
             print('='*70)
             keliling = 2 * (sisia + sisib)
             print('Keliling Layang-layang (4 x (Sisi + Sisi) = ', keliling)
             print('='*70)
         else:
             print('MASUKAN ANGKA YANG SESUAI')

      elif nama=="8": #lingkaran
         print('> Lingkaran')
         print('='*70)
         r = float(input('Masukan Jari-jari : '))
         luas = (22/7) * r**2
         print('='*70)
         print('Luas Lingkaran (Phi x r x r)      = ', luas)
         kel = 2 * (22/7) * r
         print('='*70)
         print('Keliling Lingkarang (2 x Phi x r) = ', kel)
         print('='*70)
         
      else:
         print('MASUKAN ANGKA YANG SESUAI')
         
      print(' ')
      syarat = int(input('Apakah Kamu Masih Ingin Lanjut di Bangun Datar? \nKetik: \n1. Lanjut\n2. Tidak\nMasukan Angka: '))
      print('')
      if syarat==1:
           continue
      elif syarat==2:
           break
      else:
          print(' ')
          print('MASUKAN ANGKA YANG SESUAI')
          print(' ')

 elif pilih_fitur=='3': # bilangan prima 
     while True:
         print("""
.___________________________________________.
|            < Bilangan Prima >             |
|===========================================|
|  > Bilangan prima adalah bilangan bulat   |
|  lebih dari 1 yang hanya habis di Bagi    | 
|  oleh 1 dan bilangan itu sendiri.         |
|___________________________________________|
           """)
         bil = int(input('> masukan bilangan yang ingin di cari: '.title()))
         print('='*70)
         if bil >= 1:
             for i in range(2,bil):
                 if(bil % i)==0:
                     print(f'{bil} bukan bilangan prima'.title())
                     break
                 elif bil==1:
                     print('1 bukan bilangan prima'.title())
                 else:
                     print(f'{bil} adalah bilangan prima'.title())
                     break

         else:
             print(f'{bil} bukan bilangan prima'.title())
         print('='*70)
         print('')
         syarat = int(input('Apakah Kamu Masih Ingin Lanjut Mencari Bilangan Prima? \nKetik: \n1. Lanjut\n2. Tidak\nMasukan Angka: '))
         print('')
         if syarat==1:
           continue
         elif syarat==2:
           break
         
 elif pilih_fitur=='4': # skala dan perbandingan
     while True:
        print("""
.____________________________.
| < Skala dan Perbandingan > |
|============================|
|1.| Skala                   |
|2.| Jarak Sebenarnya        |
|3.| Jarak Pada Peta         | 
|__|_________________________|
           """)
        nama = input('> masukan pilihan (1/2/3): ')
        print('')

        if nama=='1':
            print('> Skala')
            print('='*70)
            print('jarak pada peta diketahui dalam satuan:\n1. Kilometer\n2. centimeter '.title())
            diket = input('Masukan (1/2): ')
            print('='*70)
            if diket=='1':
                jp = float(input('Masukan Jarak Pada Peta (km) : '))
                js = float(input('Masukan Jarak Sebenarnya (cm): '))
                jpk = jp * 100000
                skala = jpk/js
                print('='*70)
                print(f'Skala Peta Adalah 1 : {int(skala)}')
            elif diket=='2':
                jp = float(input('Masukan Jarak Pada Peta (cm) : '))
                js = float(input('Masukan Jarak Sebenarnya (cm): '))
                skala = jp/js
                print('='*70)
                print(f'Skala Peta Adalah 1 : {int(skala)}')
            else:
                print('pilihan tidak sesuai'.upper)
            print('='*70)
            
        elif nama=='2':
            print('> Jarak Sebenarnya')
            print('='*70)
            jp    = float(input('Masukan Jarak Pada Peta (cm)          : '))
            skala = float(input('Masukan Skala (contoh 100 untuk 1:100): '))
            js = jp * skala
            print('='*70)
            print(f'Jarak Sebenarnya : {js} cm')
            print(f'dalam km         : {js/100000:.2f} km')
            print('='*70)
            
        elif nama=='3':
            print('> Jarak Pada Peta')
            print('='*70)
            js    = float(input('Masukan Jarak Sebenarnya (cm)         : '))
            skala = float(input('Masukan Skala (contoh 100 untuk 1:100): '))
            jp = js / skala
            print('='*70)
            print(f'Jarak Pada Peta : {jp} cm')
            print('='*70)

        else:
            print('pilihan tidak sesuai'.upper)

        print('')
        syarat = int(input('Apakah Kamu Masih Ingin Lanjut di Skala dan Perbandingan? \nKetik: \n1. Lanjut\n2. Tidak\nMasukan Angka: '))
        print('')
        if syarat==1:
             continue
        elif syarat==2:
             break
        else:
            print(' ')
            print('MASUKAN ANGKA YANG SESUAI')

 syarat = int(input('Apakah Kamu Masih Ingin Lanjut Menghitung? \nKetik: \n1. ya\n2. tidak\nMasukan Angka: '))
 print('')
 if syarat==1:
    print(' ')
    continue
 elif syarat==2:
    print('TERIMAKASIHHH')
    break