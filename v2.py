import requests, random, time, keep_alive
locked = 0
closed = 0
claimable = 0
scanned = 0
errors = 0
s = requests.Session()
keep_alive.keep_alive()
while True:
        print(f"Errors: {errors} Locked groups: {locked} Closed groups: {closed} Claimable groups: {claimable} Scanned groups: {scanned}")
        id = random.randint(1000000 ,5000000)
        r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}")
        scanned = scanned + 1
        if 'owned by' not in r.text:
                if r.status_code == 200:
                        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
                        #print(re)
                        if re.status_code == 200:
                                if re.json()['publicEntryAllwed'] == True and 'isLocked' not in re.text and re.json()['owner'] == None:
                                        f = open("groups.txt","a+")
                                        f.write(f"https://www.roblox.com/groups/group.aspx?gid={id}\n")
                                        f.close()
                                        claimable = claimable + 1
                                elif 'isLocked' in r.text:
                                        locked = locked + 1           
                                elif re.json()["publicEntryAllowed"] == False:
                                        closed = closed + 1  
                                else:
                                        pass          
                        elif re.status_code == 429:
                                print("Ratelimited")
                                errors = errors + 1
                                time.sleep(60)  
                        elif re.status_code == 400:
                                errors = errors + 1               
                        else:
                                pass        
                       
