# Untuk Mengimport Modul
import os,sys,time # Modul os untuk mengimport path pada suatu file atau script, Modul sys untuk menyediakan akses ke variabel dan fungsi yang terkait dengan interpreter pada Python, Modul time untuk menyediakan fungsi untuk mengontrol waktu.
from colorama import Fore,Back,init # Modul Colorama untuk menambahkan warna pada Python.

def autoketik(s): # Fungsi pada string (s) sebagai input dan secara bertahap mencetak karakter-karakter dalam string tersebut ke terminal dengan penundaan waktu tertentu. Ini menciptakan efek "auto-typing".
    for c in s + "\n": # Fungsi ini mengiterasi setiap karakter dalam string s ditambah dengan karakter newline (\n) untuk pindah ke baris baru.
        sys.stdout.write(c) # Setiap karakter ditulis ke output standar.
        sys.stdout.flush() # Memastikan tampilan segera.
        time.sleep(0.008) # Fungsi ini digunakan untuk menunda eksekusi selama 0.008 detik. Menciptakan efek "ketikan" yang lambat dan terlihat nyata.

# Warna
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

# Warna kode ANSI escape sequence
hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

# Teks Pada Awal Kode Saat Di Run
os.system("clear") # Untuk Menghapus Semua Elemen Dari Suatu Set, Sehingga Menghasilkan Set Yang Kosong
autoketik(f"{W}[{R}•{W}] {kuning}Loading...") # Fungsi yang telah didefinisikan sebelumnya untuk menampilkan teks secara bertahap, memberikan efek "mengetik".
time.sleep(1) # Fungsi ini membuat program berhenti selama 1 detik sebelum menampilkan pesan berikutnya, memberikan efek jeda.
autoketik(f"{W}[{R}•{W}] {G}Jangan Lupa Follow {biru}marpell.xyz") # f-string yang digunakan untuk membuat format teks dengan warna yang berbeda. variabel W, R, G, biru, dll, berisi kode warna untuk terminal.
url_instagram = "https://www.instagram.com/marpell.xyz" # Variabel yang menyimpan URL Instagram.
os.system(f"xdg-open {url_instagram}") # Fungsi ini digunakan untuk menjalankan perintah sistem dan perintah untuk membuka URL menggunakan aplikasi default. xdg-open adalah perintah umum di sistem operasi berbasis Unix.
time.sleep(10)
autoketik(f"{W}[{R}•{W}] {kuning}Terimakasih {ungu}>_<{G}")
time.sleep(2)
os.system("clear") # Fungsi yang dasarnya mengirim oerintah clear untuk membersihkan layar, menghapus semua teks, dan memindahkan kursor ke sudut kiri atas.
print("""
 _  __     _ _          _       _             
| |/ /    | | |        | |     | |            
| ' / __ _| | | ___   _| | __ _| |_ ___  _ __ 
|  < / _` | | |/ / | | | |/ _` | __/ _ \| '__|
| . \ (_| | |   <| |_| | | (_| | || (_) | |   
|_|\_\__,_|_|_|\_\\__,__|_|\__,_|\__\___/|_|   
""") # ASCII ART bentuk seni digital yang menggunakan karakter ASCII untuk membentuk gambar atau teks.
autoketik(f"""
{putih}[{R}•{putih}] {ungu}Author {putih}: Marvell\n{putih}[{R}•{putih}] {ungu}Github {putih}: MarvellAlvin\n{putih}[{R}•{putih}] {ungu}Instagram {putih}: marpell.xyz
""") # Judul dan Deskripsi

while True:
    print(f"""{abu}-----------------------------------------\n{W}[{R}• {kuning}•{hijau}•{W}] M E N U {W}[{R}• {kuning}•{hijau}•{W}]\n{W}[{G}1{W}] {biru}Penjumlahan\n{W}[{G}2{W}] {biru}Pengurangan\n{W}[{G}3{W}] {biru}Perkalian\n{W}[{G}4{W}] {biru}Pembagian\n{W}[{G}5{W}] {biru}Keluar{W}""") # Menu Kalkulator

    inp_no = input("Masukkan Nomor (1, 2, 3, 4, 5): ") # Menginput Nomor Untuk Memilih Menu

    if inp_no == "1": # Penjumlahan
        bilangan_string = input("Masukkan bilangan (pisahkan dengan spasi): ")
        bilangan_list = bilangan_string.split()  # Membagi string menjadi list
        bilangan = [int(x) for x in bilangan_list]
        penjumlahan = sum(bilangan)
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Penjumlahan {putih}: {penjumlahan}""")
    elif inp_no == "2": # Pengurangan
        angka_input = input("Masukkan bilangan (pisahkan dengan spasi): ")
        list_angka = angka_input.split()
        list_angka = [int(angka) for angka in list_angka]
        pengurangan = list_angka[0]
        for angka in list_angka[1:]:
            pengurangan -= angka
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Pengurangan {putih}: {pengurangan}""")
    elif inp_no == "3": # Perkalian
        angka_input = input("Masukkan bilangan (pisahkan dengan spasi): ")
        list_angka = angka_input.split()
        list_angka = [int(angka) for angka in list_angka]
        perkalian = list_angka[0]
        for angka in list_angka[1:]:
            perkalian *= angka
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Perkalian {putih}: {perkalian}""")
    elif inp_no == "4": # Pembagian
        angka_input = input("Masukkan bilangan (pisahkan dengan spasi): ")
        list_angka = angka_input.split()
        list_angka = [int(angka) for angka in list_angka]
        pembagian = list_angka[0]
        for angka in list_angka[1:]:
            pembagian /= angka
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Pembagian {putih}: {pembagian}""")
    elif inp_no == "5": # Keluar Pada Menu
        time.sleep(1)
        autoketik(f"""{W}[{kuning}•{W}] {kuning}Terimakasih telah menggunakan kalkulator ini {ungu}>_<""")
        break
    else:
        time.sleep(0.5)
        autoketik(f"""{W}[{R}•{W}] {R}Pilihan tidak valid!""")
        time.sleep(1)
        autoketik(f"""{W}[{kuning}•{W}] {kuning}Kembali ke menu {R}. {Y}. {G}.""")
        time.sleep(1)