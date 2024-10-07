# Untuk Mengimport Modul
import os,sys,time
from colorama import Fore,Back,init

# Mendefinisikan autoketik adalah print kalimat yang seperti diketik
def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

# Warna
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

# Rumus Sederhana
def penjumlahan(a, b):
  return a + b

def pengurangan(a, b):
  return a - b

def perkalian(a, b):
  return a * b

def pembagian(a, b):
  return a / b
  
# Teks Pada Awal Kode Saat Di Run
os.system("clear") # Untuk Menghapus Semua Elemen Dari Suatu Set, Sehingga Menghasilkan Set Yang Kosong
autoketik(f"{W}[{R}•{W}] {kuning}Loading...")
time.sleep(1) # Untuk menjeda sebentar
autoketik(f"{W}[{R}•{W}] {biru}Script By Marpel")
time.sleep(1)
os.system("clear")
autoketik(f"""
{abu}-----------------------------------------
{Y}K {W}A {R}L {G}K {Y}U {ungu}L {biru}A {Y}T {W}O {R}R  {Y}S {W}E {R}D {G}E {Y}R {ungu}H {biru}A {Y}N {W}A\n{Y}P {W}Y {R}T {G}H {Y}O {ungu}N\n{putih}[{R}•{putih}] {biru}Author {putih}: Marvell\n{putih}[{R}•{putih}] {biru}Github {putih}: MarvellAlvin\n{putih}[{R}•{putih}] {biru}Instagram {putih}: marpell_xyz\n{abu}-----------------------------------------
""") # Judul dan Deskripsi. \n adalah seperti enter

while True:
    print(f"""{abu}-----------------------------------------\n{W}[{R}• {kuning}•{hijau}•{W}] M E N U {W}[{R}• {kuning}•{hijau}•{W}]\n{W}[{ungu}1{W}] {kuning}Penjumlahan\n{W}[{ungu}2{W}] {kuning}Pengurangan\n{W}[{ungu}3{W}] {kuning}Perkalian\n{W}[{ungu}4{W}] {kuning}Pembagian\n{W}[{ungu}5{W}] {kuning}Keluar{W}""") # Menu Kalkulator

    inp_no = input("Masukkan Nomor (1, 2, 3, 4, 5): ") # Menginput Nomor Untuk Memilih Menu

    if inp_no == "1": # Penjumlahan
        a = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka Pertama {W}: "))
        b = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka kedua {W}: "))
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Penjumlahan {putih}: {penjumlahan(a, b)}""")
    elif inp_no == "2": # Pengurangan
        a = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka Pertama {W}: "))
        b = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka kedua {W}: "))
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Pengurangan {putih}: {pengurangan(a, b)}""")
    elif inp_no == "3": # Perkalian
        a = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka Pertama {W}: "))
        b = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka kedua {W}: "))
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Perkalian {putih}: {perkalian(a, b)}""")
    elif inp_no == "4": # Pembagian
        a = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka Pertama {W}: "))
        b = int(input(f"{W}[{R}•{W}] {biru}Masukan Angka kedua {W}: "))
        autoketik(f"""{W}[{R}•{W}] {biru}Hasil Pembagian {putih}: {pembagian(a, b)}""")
    elif inp_no == "5": # Keluar Pada Menu
      break
