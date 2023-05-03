# capstone_satu

PENJELASAN SINGKAT
Halo, Saya Musa disini saya akan memberikan penjelasan singkat dari program yang saya buat, saya membuat program ini menggunakan pythonb. program yang saya buat ini adalah menu sederhana terkait data mahasiswa pada suatu kampus, disini saya membagi menu-menu tersebut menjadi 5, pertama untuk menampilkan data mahasiswa, kedua untuk input data mahasiswa, ketiga untuk update data, keempat untuk delete data, dan kelima adalah quit agar program berhenti bekerja.

FLOW PROGRAM
1.Ketika kita melakukan run terhadap code program akan mulai bekerja, program menu akan menampilkan 5 pilihan(show,input,update,delete,quit)
2.Jika kita memilih menu pertama maka program akan menampilkan seluruh data mahasiswa yang ada dikampus tersebut berupa Nama,NIM,Jurusan,Nama Orang tua,GPA.
3.Jika kita memilih menu kedua maka program akan meminta kita untuk melakukan input data mahasiswa, adapun disini akan banyak validasi-validasi yang saya buat seperti
- ketika memasukan input nama, nama tidak boleh kurang dari 4 dan lebih dari 30 karakter
- ketika memasukan input nama, nama harus berupa huruf tidak boleh angka
- Nama yang di-input akan automatis dirubah menjadi kapital
- ketika memasukan inputan NIM, NIM harus berawalan dengan "B0"
- NIM yang di-input harus sebanyak 8 karakter
- ketika memasukan input Nama Orang tua, nama tidak boleh kurang dari 4 dan lebih dari 30 karakter
- ketika memasukan input Nama Orang tua, nama harus berupa huruf tidak boleh angka
- Nama Orang tua yang di-input akan automatis dirubah menjadi kapital
- ketika memasukan GPA memiliki range dari [0 - 4.0], tidak bisa kurang atau lebih dari range tersebut
4. Setelah kita mengisi seluruh inputan dengan benar maka program akan menyimpan data tersebut, sehingga jika kita melakukan Show data, data yang baru saja kita input sudah tersimpan
5. Jika kita memilih menu ketiga maka program akan kembali menawarkan pilihan kepada kita, Cari berdasarkan NIM/Cari berdasarkan Nama, ini saya buat untuk memudahkan admin sehingga jika ingin melakukan update, admin hanya perlu melakukan inputan nama/nim dari mahasiswa tersebut dan program langsung mengenali mahasiswa mana yang akan dirubah datanya
6.Jika kita memilih menu keempat ini adalah menu untuk menghapus data spesifik, yang nantinya bisa kita direct melalui NIM/Nama
7.Jika kita memilih menu kelima maka program berhenti bekerja/berjalan.
