import os 
try:
	import requests, random
except ModuleNotFoundError:
	os.system("pip install requests") # i swear requests is prebuit in tho 

def check(id):
	r = requests.get(f"https://economy.roblox.com/v1/groups/{id}/currency")
	if r.status_code == 200:
		robux = r.json()['robux']
	else:
		robux = "Not public"
	return robux		

while True:
	id = random.randint(5000000, 8500000)
	r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") # yes dont bully me it searches html which is not the best idea but it does its job lol
	if 'owned' not in r.text: # from the html
		re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
		if 'isLocked' not in r.text and 'owner' in r.text: 
			if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
				print(f"\033[92m[ VALID ]https://www.roblox.com/groups/group.aspx?gid={id} | Robux Count: {check(id)}\033[39m")
				requests.post("Your_webhook_here",json={'content':f'https://www.roblox.com/groups/group.aspx?gid={id} | Robux Count' + check(id) + "Member Count" + re.json()['memberCount']})
			else:
				print(f"\033[91m[ INVALID ] > {id}\033[39m")
		else:
			print(f"\033[91m[ INVALID ] > {id}\033[39m")				
        else:
		print(f"\033[91m[ INVALID ] > {id}\033[39m")