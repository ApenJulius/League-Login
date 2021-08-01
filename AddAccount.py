summonerName = input("Summoner Name")
user = input("Account name: ")
passw = input("Password: ")

f = open(f"{summonerName}.py", "w")
f.write(f"from MainBranch import login\n\nlogin('{user}', '{passw}')")