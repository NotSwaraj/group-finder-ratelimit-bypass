import os 
try:
	import requests, random
except ModuleNotFoundError:
	os.system("pip install requests") # i swear requests is prebuit in tho 
while True:
	id = random.randint(5000000, 8500000)
	r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") # yes dont bully me it searches html which is not the best idea but it does its job lol
	if 'owned by' not in r.text: # from the html
		if 'isLocked' not in r.text and 'owner' in r.text: #if you live in america or near where the ping to roblox is awesome, you will defo luv this :D
			re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
			if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
				print(f"\033[92m[ VALID ]https://www.roblox.com/groups/group.aspx?gid={id}\033[39m")	
				requests.post("Your_webhook_here",json={'content':f'https://www.roblox.com/groups/group.aspx?gid={id}'})
			else:
				print(f"\033[91m[ INVALID ] > {id}\033[39m")
		else:
			print(f"\033[91m[ INVALID ] > {id}\033[39m")
	else:
		print(f"\033[91m[ INVALID ] > {id}\033[39m")	

