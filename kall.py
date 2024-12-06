# Untuk Mengimport Modul
import os #vModul os untuk mengimport path pada suatu file atau script
import sys # Modul sys untuk menyediakan akses ke variabel dan fungsi yang terkait dengan interpreter pada Python
import time # Modul time untuk menyediakan fungsi yang mengontrol waktu.
from pystyle import Colorate, Colors
from colorama import Fore,Back,init,Style # Modul Colorama untuk menambahkan warna pada Python.

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

history = {}  # Menggunakan kamus untuk menyimpan riwayat dengan nomor urut
print(Colorate.Horizontal(Colors.cyan_to_green,"""

██╗  ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██║ ██╔╝██╔══██╗██║     ██║ ██╔╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╔╝ ███████║██║     █████╔╝ ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
██╔═██╗ ██╔══██║██║     ██╔═██╗ ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██╗██║  ██║███████╗██║  ██╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                   
        ╔═════════════════════════════════════════════════╗
        ║                                                 ║
        ║  - 1 |  Cara Menggunakan Kalkulator             ║ 
        ║  - 2 |  Tentang Projek Kalkulator Python        ║
        ║  - 3 |  Kontak Author                           ║
        ║  - 4 |  History                                 ║
        ║  - 5 |  Keluar                                  ║
        ║                                                 ║
        ║  - Kalkulator v.1                               ║
        ║  - Tq Ai and Friends                            ║
        ║                                                 ║  
        ╚═════════════════════════════════════════════════╝

"""))
print(Colorate.Horizontal(Colors.cyan_to_green,"\n[+] Pilih Menu Atau Masukan Bilangan Yang Ingin Dikalkulasikan"))          
while True:
    user_input = input(Colorate.Horizontal(Colors.cyan_to_green, f"\n>>>"))
    
    if user_input.lower() == '4':
        if history:
            for index, item in history.items():
                print(f"{index}. {item}")
            edit_or_delete = input("Ingin edit atau hapus riwayat?\n(edit/hapus/tidak)\n>>> ")
            if edit_or_delete.lower() == 'edit':
                index_to_edit = int(input("Masukkan nomor riwayat yang ingin diedit: "))
                new_expression = input("Masukkan ekspresi baru: ")
                try:
                    new_result = eval(new_expression)
                    history[index_to_edit] = f"{new_expression} = {new_result}"
                    print("Riwayat berhasil diedit.")
                except Exception as e:
                    print(Colorate.Horizontal(Colors.yellow_to_red,"Terjadi kesalahan:", e))
            elif edit_or_delete.lower() == 'hapus':
                index_to_delete = int(input("Masukkan nomor riwayat yang ingin dihapus: "))
                del history[index_to_delete]
                print(Colorate.Horizontal(Colors.cyan_to_green,"Riwayat berhasil dihapus."))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red,"Tidak ada riwayat perhitungan."))
            
    elif user_input.lower() == '1':
        print("╭─「 Cara 」\n│ • Premium\n╰────")
    
    elif user_input.lower() == '2':
        print("Tentang")
    
    elif user_input.lower() == '3':
        print("Kontak")
    
    elif user_input.lower() == '5':
        print(Colorate.Horizontal(Colors.cyan_to_green,"Terima kasih telah menggunakan kalkulator!"))
        break  # Keluar dari loop
            
    else:
        try:
            result = eval(user_input)
            history[len(history) + 1] = f"{user_input} = {result}"
            print("Hasilnya adalah:", result)
        except Exception as e:
            print("Terjadi kesalahan:", e)