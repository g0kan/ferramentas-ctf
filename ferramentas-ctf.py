import requests
import os
import getpass
from time import sleep
from colorama import Fore

os.system(['clear', 'cls'][os.name == 'nt'])

red = Fore.RED 
green = Fore.GREEN 
cyan = Fore.CYAN
white = Fore.WHITE
yellow = Fore.YELLOW

def loading ():
    os.system(['clear', 'cls'][os.name == 'nt'])
    print(cyan + "[*]" + white + " Loading.")
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    print(cyan + "[*]" + white + " Loading..")
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])
    print(cyan + "[*]" + white + " Loading...")
    sleep(1)
    os.system(['clear', 'cls'][os.name == 'nt'])

loading()
avatar = yellow + f"""
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb     
    dZP          qKKb       Username: {getpass.getuser()} 
   fZP            SMMb      Ferramentas CTF
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' 

{cyan}[1] Abrir servidor HTTP na máquina (Python - Necessita de permissão administrador / root).
[2] Escutar na porta que desejar (Necessita do Ncat).
[3] Realiza uma requisição POST no site desejado.
[4] Fecha a aplicação.                            
"""
print(avatar)
inp = int(input(white + ">> "))

if(inp == 1):
    loading()
    print(cyan + "[*]" + white + " Servidor rodando na porta 80.")
    print("")
    os.system('python3 -m http.server 80')
elif(inp == 2):
    loading()
    print(cyan + "[*]" + white + " Digite a porta que deseja escutar.")
    print("")
    inp2 = input(">> ")
    print("")
    print(cyan + "[*]" + white + " Escutando na porta: " + inp2)
    print("")
    os.system("ncat -lvp " + inp2)
elif(inp == 3):
    loading()
    print(cyan + "[*]" + white + " Digite o site. Não se esqueça do HTTP ou HTTPS.") 
    print("")
    inp3 = input(">> ")
    print("")
    print(cyan + "[*]" + white + " Alvo: " + inp3)
    print("")
    sleep(2)
    res = requests.post(inp3)
    print(res.text)
    print("")
    print(cyan + "[*]" + white + " Request realizado.")
elif(inp == 4):
    print("")
    print("SAINDO!!!")
    sleep(2)
    os.system('exit')          
else:
    print("")
    print(red + "[*]" + white + " Digite uma opção válida.")

    


