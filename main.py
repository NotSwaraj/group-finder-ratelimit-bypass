import os 
try:
	import requests, random, threading
except ModuleNotFoundError:
	os.system("pip install requests") # i swear requests is prebuit in tho 
def main():
	id = random.randint(5000000, 8500000)
	r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") # yes dont bully me it searches html which is not the best idea but it does its job lol
	if 'owned by' not in r.text: # from the html
		if 'isLocked' not in r.text and 'owner' in r.text: #if you live in america or near where the ping to roblox is awesome, you will defo luv this :D
			re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
			if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
				print(f"\033[92m[ VALID ]https://www.roblox.com/groups/group.aspx?gid={id}\033[39m")	
				requests.post("https://discord.com/api/webhooks/815709937258463293/QKOw0GCaPTYWp67wWEYUbRZvjToaYJQ6-CZriZvQ3Z3wGDWYftUSl1t7K3MJHdJ_4eda",json={'content':f'https://www.roblox.com/groups/group.aspx?gid={id}'})
			else:
				print(f"\033[91m[ INVALID ] > {id}\033[39m")
		else:
			print(f"\033[91m[ INVALID ] > {id}\033[39m")
	else:
		print(f"\033[91m[ INVALID ] > {id}\033[39m")	

for i in range(50): # i know this says 50 but try not to edit this cause it will most likely get you ratelimited
	threading.Thread(target=main).start()
