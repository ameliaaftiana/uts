# class node:
#     def __init__(self, element, n):
#         self._element = element
#         self._next = n

class stack:
    def __init__(self):
        self.head=None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def top (self):
        return self.head._element
    
    def pop (self,kalori):
        a = self.head._element
        self.head = self.head._next
        self.kalori -= kalori
        return a
    
    def printAll(self):
        elements = []
        bantu = self.head
        while bantu:
            elements.append(bantu._element)
            bantu = bantu._next
        while elements:
            print (elements.pop(), end='')
        print()
    
class Makanan:
    def __init__(self,nama,kalori,jenis,pilih):
        self.nama = nama
        self.jenis = jenis
        self.kalori = kalori
        self._size = 0
        self.pilih = pilih
    
    def get_nama(self):
        return self.nama
    
    def set_nama(self,nama):
        self.nama = nama
    
    def get_kalori(self):
        return self.kalori
    
    def set_kalori(self,kalori):
        self.kalori = kalori
    
    def setpilih(self,pilih):
        self.pilih = pilih
        
    def setpilih(self,kalori):
        self.kalori = kalori
    
    def setjenis(self,jenis):
        self.jenis = jenis
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self,nama,kalori):
        # nama = node(None)
        # if not self.isEmpty():
        #     self.hapus(i)
        #     if self.pilih == 3:
        #         self.printAll()
        #         return
        # if self.isEmpty():
        #     self.head = nama
        # if self.jenis == 1 and self.kalori < 2000:
        self.head = nama
        self.kalori += kalori
        # if self.jenis == 2 and self.kalori < 1500:
        #     self.head = nama
        #     self.kalori += kalori
        # else:
        #     nama.next = self.head
        #     self.head = nama
            

    


print ('Pilih Jenis Kelamin:')
print('1. Pria') 
print ('2. Wanita')    
jenis = input('Pilihan Anda : ')

print ('Pilih Menu: ')
print ('1. Makan')
print ('2. Buang')
print ('3. Riwayat Makanan')
print ('4. Keluar')
print ('Kalori saat ini: 0 kal')
pilih = int(input('Pilihan Anda : '))
if pilih == 1:
    nama = input('Masukkan nama : ')
    kalori = int(input('Masukkan kalori : '))
    tes = Makanan(nama,kalori,jenis,pilih)
    tes.push(nama,kalori)
if pilih == 2:
    map(nama,kalori) == input(f'Makanan dibuang : {nama (kalori)}')
    tes = Makanan(nama,kalori,jenis,pilih)
if pilih == 3:
    tes.printAll()


        
jek = [1,2,3]

while pilih in jek:
    print ('Pilih Menu: ')
    print ('1. Makan')
    print ('2. Buang')
    print ('3. Riwayat Makanan')
    print ('4. Keluar')
    print ('Kalori saat ini: 0 kal')
    pilih = int(input('Pilihan Anda : '))
    if pilih == 1:
        nama = input('Masukkan nama : ')
        kalori = int(input('Masukkan kalori : '))
        tes = Makanan(nama,kalori,jenis,pilih)
        tes.push(nama,kalori)
    print(f'Data ')
    if pilih == 2:
        map(nama,kalori) == input(f'Makanan dibuang : {nama (kalori)}')
    if pilih == 3:
        tes.printAll()


        
            