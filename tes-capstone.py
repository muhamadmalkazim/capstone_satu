import string

mahasiswa = [
    ['Muhamad','Teknik Informatika','20121455','Ramdani', 3.95],
    ['Ali','Sistem Informasi','20121667','Rozi', 3.77],
    ['Dodi','Psikologi','20121898','Farhan', 3.88]
]


def showMahasiswa():
    while True:
        print(f'''
1. Show All Data
2. Show data By NIM
3. Kembali ke Menu Utama''')
        menu_pilih_show = input('Pilih Menu (1/2/3): ')

        if menu_pilih_show == '1':
            print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format('NIM', 'NAMA', 'JURUSAN', 'NAMA WALI', 'GPA'))
            for i in range(len(mahasiswa)):
                print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format(mahasiswa[i][2], mahasiswa[i][0], mahasiswa[i][1], mahasiswa[i][3], mahasiswa[i][4]))
        elif menu_pilih_show == '2':
            nim = input('Masukan NIM: ')
            for i in range(len(mahasiswa)):
                if nim == mahasiswa[i][2]:
                    print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format('NIM', 'NAMA', 'JURUSAN', 'NAMA WALI', 'GPA'))
                    print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format(mahasiswa[i][2], mahasiswa[i][0], mahasiswa[i][1], mahasiswa[i][3], mahasiswa[i][4]))
                    break
            else:
                print('Data tidak ditemukan')
                break
        elif menu_pilih_show == '3':
            return
        else:
            print('Pilihan tidak tersedia')

        

def inputMahasiswa():
    nama = input('Masukkan Nama[4-30]: ')
    while not (nama.replace(" ", "").isalpha() and 4 <= len(nama) <= 30):
        print('Nama harus terdiri dari 4-30 karakter dan hanya berisi huruf')
        nama = input('Masukkan Nama[4-30]: ')

    jurusan = input('Masukkan Jurusan: ')
    while not (jurusan.replace(" ", "").isalpha() and 4 <= len(jurusan) <= 40):
        print('Jurusan harus terdiri dari 4-40 karakter dan hanya berisi huruf')
        jurusan = input('Masukkan Jurusan: ')

    nim = input('Masukkan NIM: ')
    while len(nim) != 8 or not nim.startswith('20') or not nim[2:].isdigit():
        print('NIM harus terdiri dari 8 karakter dan diawali dengan "20"')
        nim = input('Masukkan NIM: ')
        nim = str(nim)

    nama_orang_tua = input('Masukkan Nama Orang Tua[4-30]: ')
    while not (nama_orang_tua.replace(" ", "").isalpha() and 4 <= len(nama_orang_tua) <= 30):
        print('Nama Orang Tua harus terdiri dari 4-30 karakter dan hanya berisi huruf')
        nama_orang_tua = input('Masukkan Nama Orang Tua[4-30]: ')

    gpa = input('Masukkan GPA[0.00-4.00]: ')
    while True:
        if not gpa.replace('.', '', 1).isdigit() or float(gpa) < 0 or float(gpa) > 4:
            print('GPA harus berupa angka di antara 0.00-4.00')
            gpa = input('Masukkan GPA[0.00-4.00]: ')
        else:
            break
        gpa = float(gpa)

    mahasiswa.append([nama, jurusan, nim, nama_orang_tua, gpa])
    showMahasiswa()


def updateMahasiswa():
    nim = input("Masukkan NIM mahasiswa yang ingin diupdate: ")
    for i in range(len(mahasiswa)):
        if nim == mahasiswa[i][2]:
            while True:
                print('''
                1. Nama
                2. Jurusan
                3. Nama Wali
                4. GPA
                5. Kembali ke Menu Utama
                ''')
                menu_pilih_update = input('Pilih Menu (1/2/3/4/5): ')

                if menu_pilih_update == '1':
                    mahasiswa[i][0] = input("Masukkan nama baru: ")
                    print("Data berhasil diupdate")
                elif menu_pilih_update == '2':
                    mahasiswa[i][1] = input("Masukkan jurusan baru: ")
                    print("Data berhasil diupdate")
                elif menu_pilih_update == '3':
                    mahasiswa[i][3] = input("Masukkan nama wali baru: ")
                    print("Data berhasil diupdate")
                elif menu_pilih_update == '4':
                    mahasiswa[i][4] = input("Masukkan GPA baru: ")
                    print("Data berhasil diupdate")
                elif menu_pilih_update == '5':
                    return
                else:
                    print('Pilihan tidak tersedia')
            break
    else:
        print('Data tidak ditemukan')



def deleteMahasiswa():
    nim = input('Masukkan NIM Mahasiswa yang akan dihapus: ')
    for i in range(len(mahasiswa)):
        if nim == mahasiswa[i][2]:
            del mahasiswa[i]
            print('Data berhasil dihapus')
            return
    else:
        print('Data tidak ditemukan')



    

def menu():
    print(f'''

"MAHASISWA"
{'-' * 150}
1.Show Mahasiswa Data
2.Input Mahasiswa Data
3.Update Mahasiswa Data
4.Delete Mahasiswa Data
5.Exit
{'-' * 150}
    ''')

while True:
    menu()
    menu_input = input('Pilih Menu: ')
    if menu_input == '1':
        showMahasiswa()
    elif menu_input == '2':
        menu()
        inputMahasiswa()
    elif menu_input == '3':
        menu()
        updateMahasiswa()
    elif menu_input == '4':
        menu()
        deleteMahasiswa()
    elif menu_input.lower() == 'quit':
        break
    else:
        print("Invalid input, please try again")






    
