class Makanan:

    
    def isEmpty(self,kalori):
        kalori == 0
        return self.kalori == kalori
    
        # def get_jenisKelamin(self):
    #     return self.nama
    
    # def set_jenisKelamin(self,jenisKelamin):
    #     self.jenisKelamin = jenisKelamin
    


print ('Pilih Jenis Kelamin:')
print('1. Pria') 
print ('2. Wanita')    
jenisKelamin = input('Pilihan Anda : ')
print ('Pilih Menu: ')
print ('1. Makan')
print ('2. Buang')
print ('3. Riwayat Makanan')
print ('4. Keluar')
print ('Kalori saat ini: 0 kal')
pilih = input('Pilihan Anda : ')
nama = input('Masukkan nama : ')
kalori = input('Masukkan kalori : ')

hitung = Makanan()

while True:
    print ('Pilih Menu: ')
    print ('1. Makan')
    print ('2. Buang')
    print ('3. Riwayat Makanan')
    print ('4. Keluar')
    print (f'Kalori saat ini: {hitung.get_kalori()} kal')
    pilih = input('Pilihan Anda : ')
    
    

