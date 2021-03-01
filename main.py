import os 
try:
	import requests, random, keep_alive
except ModuleNotFoundError:
	os.system("pip install requests") # i swear requests is prebuit in tho 
keep_alive.keep_alive()	
while True:
	id = random.randint(5000000, 8500000)
	r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") # yes dont bully me it searches html which is not the best idea but it does its job lol
	if 'owned' not in r.text: # from the html
		re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
		if 'isLocked' not in re.text:
			if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
				print(f"\033[92m[ VALID ]https://www.roblox.com/groups/group.aspx?gid={id}\033[39m")	
				requests.post("https://discord.com/api/webhooks/815709937258463293/QKOw0GCaPTYWp67wWEYUbRZvjToaYJQ6-CZriZvQ3Z3wGDWYftUSl1t7K3MJHdJ_4eda",json={'content':f'https://www.roblox.com/groups/group.aspx?gid={id}'})
		else:
			print(f"\033[91m[ INVALID ] > {id}\033[39m")
	else:
			print(f"\033[91m[ INVALID ] > {id}\033[39m")
