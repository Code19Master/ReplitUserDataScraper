from time import time

import findstuff
import os



while True:
	username = input("Username: ").lower()

	username.replace("@", "")
	print("Loading...\n\n")


	try:
		user = findstuff.find_user(username)
	except:
		print("Could not find user")
	if user:
		user.display_data()
	else:
		pass

	print("\n")
	print("\tLEADERBOARDS\n")


	leaderboards = {
		"" : "Past Seven Days",
		"past_30_days" : "Past Thirty Days",
		"past_year" : "Past Year",
		"all_time" : "All Time",
	}

	for i in leaderboards:
		print(leaderboards[i])
		leaderboard = findstuff.leaderboard(i)
		placing = leaderboard.placing(username)
		
		if placing:
			print(f"{username} is {placing} place on the leaderboard")
		else:
			print(f"{username} is not in the top 30 on the leaderboard")


	input("\n\nPress [enter] to continue")

	os.system('clear')