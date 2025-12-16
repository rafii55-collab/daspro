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
 pilih_fitur = input('> masukan fitur yang kamu inginkan: '.title())

 if pilih_fitur=='1':
    while True:
     print("""
._________________________________.
|        < Bangun Ruang >         |
|=================================|
| > PILIH SALAH SATU BANGUN RUANG |
|=================================|
|1.| Kubus        |5.| bola       |
|2.| Balok        |  |            |
|3.| Tabung       |  |            |
|4.| Kerucut      |  |            | 
|__|______________|__|____________|
           """)
     nama = input('> Masukan Nomor Bangun Ruang Yang di Inginkan: ') #type data disini sama di bagian if harus sama
     print(' ')

     if nama=='1': #kubus
         print('='*74)
         print('| {:^70} | '.format('Kubus'))
         print('='*74)
         r = float(input('> Masukan Panjang Rusuk : '))
         print('='*74)
         luas = 6 * (r * r)
         print('| {:<1} {:<54.2f} |'.format('Luas Kubus   = ',luas))
         vol = r * r * r
         print('| {:<1} {:<54.2f} |'.format('Volume Kubus = ',vol))
         print('='*74)

     elif nama=='2': # balok
         print('='*74)
         print('| {:^70} | '.format('Balok'))
         print('='*74)
         l = float(input('> Masukan Lebar   : '))
         t = float(input('> Masukan Tinggi  : '))
         p = float(input('> Masukan Panjang : '))
         print('='*74)
         luas = 2 * (p*l + p*t + l*t)
         print('| {:<1} {:<54.2f} |'.format('Luas Balok   = ',luas))
         vol = p * l * t
         print('| {:<1} {:<54.2f} |'.format('Volume Balok = ',vol))
         print('='*74)

     elif nama=='3': # tabung
         print('='*74)
         print('| {:^70} | '.format('Tabung'))
         print('='*74)
         r = float(input('> Masukan Jari-jari   : '))
         t = float(input('> Masukan Tinggi      : '))
         print('='*74)
         luas = 2 * 22/7 * r * (r + t)
         print('| {:<1} {:<53.2f} |'.format('Luas Tabung   = ',luas))
         vol = 22/7 * r * r * t
         print('| {:<1} {:<53.2f} |'.format('Volume Tabung = ',vol))
         print('='*74)

     elif nama=='4': # Kerucut
         print('='*74)
         print('| {:^70} | '.format('Kerucut'))
         print('='*74)
         r = float(input('> Masukan Jari-jari        : '))
         t = float(input('> Masukan Tinggi           : '))
         s = float(input('> Masukan Sisi-sisi Miring : '))
         print('='*74)
         luas = 22/7 * r * (r + s)
         print('| {:<1} {:<52.2f} |'.format('Luas Kerucut   = ',luas))
         vol = 1/3 * 22/7 * r * r * t
         print('| {:<1} {:<52.2f} |'.format('Volume Kerucut = ',vol))
         print('='*74)
         
     elif nama=='5': # bola
         print('='*74)
         print('| {:^70} | '.format('Bola'))
         print('='*74)
         r = float(input('> Masukan Jari-jari : '))
         t = float(input('> Masukan Tinggi    : '))
         print('='*74)
         luas = 4 * 22/7 * r * r
         print('| {:<1} {:<55.2f} |'.format('Luas bola   = ',luas))
         vol = 4/3 * 22/7 * r * r * r
         print('| {:<1} {:<55.2f} |'.format('Volume Bola = ',vol))
         print('='*74)
         
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
| > PILIH SALAH SATU BANGUN DATAR       |
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
         print('='*74)
         print('| {:^70} | '.format('Persegi'))
         print('='*74)
         sisi = float(input('> Masukan Sisi: '))
         print('='*74)
         luas = sisi * sisi
         print('| {:<1} {:<50.2f} |'.format('Luas Persegi     = ',luas))
         keliling = 4 * sisi
         print('| {:<1} {:<50.2f} |'.format('Keliling Persegi = ',keliling))
         print('='*74)
    
      elif nama=='2': #persegi panjang
         print('='*74)
         print('| {:^70} | '.format('Persegi Panjang'))
         print('='*74)
         panjang = float(input('> Masukan Panjang : '))
         lebar   = float(input('> Masukan Lebar   : '))
         print('='*74)
         luas = panjang * lebar
         print('| {:<1} {:<42.2f} |'.format('Luas Persegi Panjang     = ',luas))
         keliling = 2 * (panjang + lebar)
         print('| {:<1} {:<42.2f} |'.format('Keliling Persegi Panjang = ',keliling))
         print('='*74)

      elif nama=='3': #segitiga
         print('> Segitiga')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         lk = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling\n= '))
         print(' ')
         if lk==1:
             print('='*74)
             print('| {:^70} | '.format('Luas Segitiga'))
             print('='*74)
             alas = float(input('> Masukan Alas   : '))
             tinggi = float(input('> Masukan Tinggi : '))
             print('='*74)
             luas = 1/2 * alas * tinggi
             print('| {:<1} {:<53.2f} |'.format('Luas Segitiga = ',luas))
             print('='*74)
         elif lk==2:
             print('='*74)
             print('| {:^70} | '.format('Keliling Segitiga'))
             print('='*74)
             sisi = float(input('> Masukan Sisi : '))
             print('='*74)
             keliling = 3 * sisi
             print('| {:<1} {:<49.2f} |'.format('Keliling Segitiga = ',keliling))
             print('='*74)
         else:
             print('MASUKAN ANGKA YANG SESUAI')
        
      elif nama=='4': #jajar genjang
         print('> Jajar Genjang')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('='*74)
             print('| {:^70} | '.format('Luas Jajar Genjang'))
             print('='*74)
             alas = float(input('> Masukan Alas   : '))
             tinggi = float(input('> Masukan Tinggi : '))
             print('='*74)
             luas = alas * tinggi
             print('| {:<1} {:<48.2f} |'.format('Luas Jajar Genjang = ',luas))
             print('='*74)
         elif opsi==2:
             print('='*74)
             print('| {:^70} | '.format('Keliling Jajar Genjang'))
             print('='*74)
             sisi1 = float(input('> Masukan Sisi lurus 1  : ')) 
             sisi2 = float(input('> Masukan Sisi lurus 2  : '))
             sisi3 = float(input('> Masukan Sisi miring 1 : '))
             sisi4 = float(input('> Masukan Sisi miring 2 : '))
             print('='*74)
             keliling = sisi1+sisi2+sisi3+sisi4
             print('| {:<1} {:<44.2f} |'.format('Keliling Jajar Genjang = ',keliling))
             print('='*74)
         else:
             print('MASUKAN ANGKA YANG SESUAI')
             continue

      elif nama=='5': #trapesium
         print('> Trapesium')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('='*74)
             print('| {:^70} | '.format('Luas Trapesium'))
             print('='*74)
             sb = float(input('> Masukan Sisi Sisi Bawah : '))
             sa = float(input('> Masukan Sisi Sisi Atas  : '))
             t =  float(input('> Masukan Sisi tinggi     : '))
             print('='*74)
             luas = 1/2 * (sa + sb) * t
             print('| {:<1} {:<52.2f} |'.format('Luas Trapesium = ',luas))
             print('='*74)
         elif opsi==2:
             print('='*74)
             print('| {:^70} | '.format('Keliling Trapesium'))
             print('='*74)
             s1 = float(input('> Masukan Sisi Sisi 1 : '))
             s2 = float(input('> Masukan Sisi Sisi 2 : '))
             s3 = float(input('> Masukan Sisi Sisi 3 : '))
             s4 = float(input('> Masukan Sisi Sisi 4 : '))
             print('='*74)
             keliling = s1 + s2 + s3 +s4
             print('| {:<1} {:<48.2f} |'.format('Keliling Trapesium = ',keliling))
             print('='*74)
         else:
             print('MASUKAN ANGKA YANG SESUAI')
             continue

      elif nama=='6': #belah ketupat
         print('> Belah Ketupat')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('='*74)
             print('| {:^70} | '.format('Luas Belas Ketupat'))
             print('='*74)
             d1 = float(input('> Masukan Diagonal 1 : '))
             d2 = float(input('> Masukan Diagonal 2 : '))
             print('='*74)
             luas = 1/2 * d1 * d2
             print('| {:<1} {:<48.2f} |'.format('Luas Belah Ketupat = ',luas))
             print('='*74)
         elif opsi==2:
             print('='*74)
             print('| {:^70} | '.format('Keliling Belah Ketupat'))
             print('='*74)
             sisi = float(input('> Masukan Sisi : '))
             print('='*74)
             keliling = 4 * sisi
             print('| {:<1} {:<44.2f} |'.format('Keliling Belah Ketupat = ',keliling))
             print('='*74)
         else:
             print('MASUKAN ANGKA YANG SESUAI')
             continue

      elif nama=='7': #layang layang
         print('> Layang-layang')
         print("MANA YANG INGIN KAMU CARI:\n1. Luas\n2. keliling")
         opsi = int(input('Masukan 1 Jika Ingin Luas, 2 Jika Ingin Keliling.\n= '))
         print(' ')
         if opsi==1:
             print('='*74)
             print('| {:^70} | '.format('Luas Layang-layang'))
             print('='*74)
             d1 = float(input('> Masukan Diagonal 1 : '))
             d2 = float(input('> Masukan Diagonal 2 : '))
             print('='*74)
             luas = 1/2 * d1 * d2
             print('| {:<1} {:<48.2f} |'.format('Luas Layang-layang = ',luas))
             print('='*74)
         elif opsi==2:
             print('='*74)
             print('| {:^70} | '.format('Keliling Layang-layang'))
             print('='*74)
             sisia = float(input('> Masukan Sisi Atas  : '))
             sisib = float(input('> Masukan Sisi Bawah : '))
             print('='*74)
             keliling = 2 * (sisia + sisib)
             print('| {:<1} {:<44.2f} |'.format('Keliling Layang-layang = ',keliling))
             print('='*74)
         else:
             print('MASUKAN ANGKA YANG SESUAI')
             continue

      elif nama=="8": #lingkaran
         print('='*74)
         print('| {:^70} | '.format('Lingkaran'))
         print('='*74)
         r = float(input('> Masukan Jari-jari : '))
         luas = (22/7) * r**2
         print('='*74)
         print('| {:<1} {:<52.2f} |'.format('Luas Lingkaran = ',luas))
         kel = 2 * (22/7) * r
         print('| {:<1} {:<48.2f} |'.format('Keliling Lingkaran = ',kel))
         print('='*74)
      else:
         print('MASUKAN ANGKA YANG SESUAI')
         continue
         
      print(' ')
      syarat = int(input('Apakah Kamu Masih Ingin Lanjut di Bangun Datar? \nKetik: \n1. Lanjut\n2. Tidak\nMasukan Angka: '))
      print('')
      if syarat==1:
           continue
      elif syarat==2:
           break
      else:
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
         print('='*44)
         if bil >= 1:
             for i in range(2,bil):
                 if(bil % i)==0:
                     print('| {:<1} {:<37} |'.format(bil,'bukan bilangan prima'))
                     break
                 elif bil==1:
                     print('| {:<1} {:<37} |'.format('1','bukan bilangan prima'))
                     break
                 else:
                     print('| {:<1} {:<38} |'.format(bil,'adalah bilangan prima'))
                     break

         else:
             print('| {:<1} {:<38} |'.format(bil,'bukan bilangan prima'))
         print('='*44)
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
            print('='*74)
            print('| {:^70} | '.format('Skala'))
            print('='*74)
            jp = float(input('> Masukan Jarak Pada Peta (cm) : '))
            js = float(input('> Masukan Jarak Sebenarnya (km): '))
            jpk = js * 100000
            skala = jpk/js
            print('='*74)
            print('| {:<1} {:<43} |'.format('Skala Pada Peta Adalah 1 :',(int(skala))))
            print('='*74)
            
            
        elif nama=='2':
            print('='*74)
            print('| {:^70} | '.format('Jarak Sebenarnya'))
            print('='*74)
            jp    = float(input('> Masukan Jarak Pada Peta (cm)           : '))
            skala = float(input('> Masukan Skala (contoh 100 untuk 1:100) : '))
            js = jp * skala
            print('='*74)
            print('| {:<1} {:<1} {:<45} |'.format('Jarak Sebenarnya :',js, 'cm'))
            print('| {:<1} {:<1} {:<43} |'.format('Jika Dalam km    :',js/100000, 'km'))
            print('='*74)
            
        elif nama=='3':
            print('='*74)
            print('| {:^70} | '.format('Jarak Pada Peta'))
            print('='*74)
            js    = float(input('> Masukan Jarak Sebenarnya (km)         : '))
            skala = float(input('> Masukan Skala (contoh 100 untuk 1:100): '))
            jsk = js * 100000
            jp = jsk / skala
            print('='*74)
            print('| {:<1} {:<1} {:<47} |'.format('Jarak Pada Peta :',jp,'cm'))
            print('='*74)

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