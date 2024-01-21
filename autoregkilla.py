import asyncio
from async_trendymanga import AsyncTrendymanga
from async_mail import AsyncClient
from colorama import init, Fore, Back, Style
from pyfiglet import figlet_format
from nickname_generator import generate
async def register_account(password):
	try:
		email_client=AsyncClient()
		trendy_manga= AsyncTrendymanga()
		data = await email_client.new_email()
		email=data['email']
		await trendy_manga.register(email=email,password=password,username=generate("en"))
		print(f"account {email} register")
		accounts= open("accounts.json", "a+")
		json_data={'email':email,'password':password}
		accounts.write(f"{json_data}\n")
		accounts.close()
	except Exception as e:
		print(e)
init()
print(f"{Fore.BLUE} script by Dos-kun \n github:https://github.com/l0v3m0n3y  \n{figlet_format('autoreg killa',font='rectangles')}")
password=input("password»")
while True:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(register_account(password))
