print ("Selamat Datang di Program Daftar Belanja")

item_1 = str(input("Masukkan item 1: "))
item_2 = str(input("Masukkan item 2: "))
item_3 = str(input("Masukkan item 3: "))
item_4 = str(input("Masukkan item 4: "))
item_5 = str(input("Masukkan item 5: "))
item_6 = str(input("Masukkan item 6: "))
item_7 = str(input("Masukkan item 7: "))
item_8 = str(input("Masukkan item 8: "))
item_9 = str(input("Masukkan item 9: "))
item_10 = str(input("Masukkan item 10: "))

daftar_Belanja = [item_1, item_2, item_3, item_4, item_5]
print (daftar_Belanja)

while True:
    try:
        print ("Pilih program yang diinginkan:")
        jawab = str(input('Opsi 1: Tambah Item\nOpsi 2: Hapus item\nOpsi 3: Exit\n'))
        jawab_lower = jawab.lower()

        if jawab_lower in ['1', 'Tambah Item', 'Tambah', 'tambah item', 'tambah']:
                tambah = str(input("Masukkan item yang ingin ditambahkan: "))
                daftar_Belanja.append(tambah)
                print(daftar_Belanja)
                print('Apakah anda ingin menambah/menghapus item lagi?')
                if str(input('Opsi 1: Iya\nOpsi 2: Tidak (Exit)\n')) in ['1', 'Iya', 'iya']:
                    continue
                else:
                    print('Terima kasih telah menggunakan program ini')
                    break
        
        elif jawab_lower in ['2', 'Hapus Item', 'Hapus', 'hapus item', 'hapus']:
                hapus = str(input("Masukkan item yang ingin dihapus: "))
                daftar_Belanja.remove(hapus)
                print(daftar_Belanja)
                print('Apakah anda ingin menambah/menghapus item lagi?')
                if str(input('Opsi 1: Iya\nOpsi 2: Tidak (Exit)\n')) in ['1', 'Iya', 'iya']:
                    continue
                else:
                    print('Terima kasih telah menggunakan program ini')
                    break
        
        elif jawab_lower in ['3', 'Exit', 'exit']:
            print('Terima kasih telah menggunakan program ini')
            break
                
        else:
            print('Inputan salah, coba kembali input dengan benar')
            continue
        
    except ValueError:
        print('Inputan salah, coba kembali input dengan benar')