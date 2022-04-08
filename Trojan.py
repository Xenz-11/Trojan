#bin/python
import os
import sys
import time


def auto(Z):
        for e in Z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.01)

def nanya():
    nanya = raw_input("KIRIM VIRUS LAGI? [Y/T] ")
    if nanya == "y" or nanya == "Y":
        menu()
    elif nanya == "t" or nanya == "T":
        auto("Bye bye :)")
        time.sleep(2)
        sys.exit()
    elif nanya == "" or nanya == " ":
        auto("JANGAN SAMPAI KOSONG STAH!")
        time.sleep(1)
        nanya()
    else:
        auto("Masukan Input Dengan Benar!")
        time.sleep(1)
        nanya()

def menu():
    os.system("clear")

    logo = """
          SC TROJAN BUAT KIRIM VIRUS
+===================================+
[+] Author : Xenz-11
[+] Github : github.com/Xenz-11
[+] Wa     : 6283138613993
+===================================+"""
    print (logo)
    nomor = raw_input("masukan nomer : ")
    jumlah = int(input("masukan jumlah : "))
    time.sleep(1)
    try :
        for i in range(jumlah):
            print ("MENGIRIM VIRUS TROJAN KE NOMER"),nomor
    except keyboardInterrupt:
         print "        SELESAI        "

    nanya()

menu()