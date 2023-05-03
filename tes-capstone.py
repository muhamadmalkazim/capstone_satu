import string


# MENU SHOW MAHASISWA TAMBAHIN KEMBALI KE MENU UTAMA
# MENU 1 DAN 2 HILANG KETIKA KEMBALI KE MENU UTAMA

mahasiswa = [
    ['Muhamad','Teknik Informatika','B0121455','Ramdani', 3.95],
    ['Ali','Sistem Informasi','B0121667','Rozi', 3.77],
    ['Dodi','Psikologi','B0121898','Farhan', 3.88]
]

def showMahasiswa():
    print('''
    1. Tampilkan Semua Data
    2. Tampilkan Data Melali NIM
    ''')
    while True:
        try:
            menu_pilih_show = int(input('Pilih Menu: '))
            break
        except ValueError:
            print('Input harus berupa angka')
    if menu_pilih_show == 1:
        print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format('NIM', 'NAMA', 'JURUSAN', 'NAMA WALI', 'GPA'))
        for i in range(len(mahasiswa)):
            print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format(mahasiswa[i][2], mahasiswa[i][0], mahasiswa[i][1], mahasiswa[i][3], mahasiswa[i][4]))
    elif menu_pilih_show == 2:
        nim = input('Masukan NIM: ')
        for i in range(len(mahasiswa)):
            if nim == mahasiswa[i][2]:
                print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format('NIM', 'NAMA', 'JURUSAN', 'NAMA WALI', 'GPA'))
                print('{:<10} | {:<30} | {:<30} | {:<30} | {}'.format(mahasiswa[i][2], mahasiswa[i][0], mahasiswa[i][1], mahasiswa[i][3], mahasiswa[i][4]))
                break
        else:
            print('Data tidak ditemukan')
    else:
        print('Pilihan tidak tersedia')




def inputMahasiswa():
    nama = input('Masukkan Nama[4-30]: ')
    while not (nama.isalpha() and 4 <= len(nama) <= 30):
        print('Nama harus terdiri dari 4-30 karakter dan hanya berisi huruf')
        nama = input('Masukkan Nama[4-30]: ')

    jurusan = input('Masukkan Jurusan: ')
    nim = input('Masukkan NIM: ')
    while not (nim.startswith('B0') and len(nim) != 8):
        print('NIM harus diawali dengan "B0" dan terdiri dari 8 karakter')
        nim = input('Masukkan NIM: ')

    nama_orang_tua = input('Masukkan Nama Orang Tua[4-30]: ')
    while not (nama_orang_tua.isalpha() and 4 <= len(nama_orang_tua) <= 30):
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

   


def updateDataMahasiswa():
    print('''

1.Update Jurusan
2.Update GPA

    ''')

    pilih_update = int(input('Masukan Nomor: '))
    if pilih_update == 1:
        nim = input('Masukan NIM: ')
        for i in range(len(mahasiswa)):
            if nim in mahasiswa[i] :
                jurusan_baru = input('Masukan Jurusan Baru: ')
                mahasiswa[i][1] = jurusan_baru
    elif pilih_update == 2:
        nim = input('Masukan NIM: ')
        for i in range(len(mahasiswa)):
            if nim in mahasiswa[i]:
                gpa_baru = input('Masukan GPA Baru: ')
                mahasiswa[i][4] = gpa_baru
    showMahasiswa()


def deleteDataMahasiswa():
    nim = input('Masukan NIM: ')
    for i in range(len(mahasiswa)):
        if nim in mahasiswa[i]:
            del mahasiswa[i]
            break
    
    showMahasiswa()


    

def menu():
    print(f'''

"EMPLOYEES"
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
        inputMahasiswa()
    elif menu_input == '3':
        updateDataMahasiswa()
    elif menu_input == '4':
        deleteDataMahasiswa()
    elif menu_input.lower() == 'quit':
        break
    else:
        print("Invalid input, please try again")






    
