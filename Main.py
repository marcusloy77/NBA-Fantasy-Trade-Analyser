import pandas as pd
import Player_Class

#defining url for panda to read
url = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
df = pd.read_html(url, header = 0)

#len(df) prints how many tables are in html

df2021 = df[0]
df2021 = df2021.drop(df2021[df2021.Age == 'Age'].index)


# these print n. rows, row of a single player
#print(df2021.shape[0])
#print(df2021.iloc[2,:])



#uses object class to create list of players - now we can loop through and create more lists
player_list = []
for i in range(df2021.shape[0]):
	player_list.append( Player_Class.players(df2021.iloc[i,0], df2021.iloc[i,1], df2021.iloc[i,2] , df2021.iloc[i,3] , df2021.iloc[i,4] , df2021.iloc[i,5] , df2021.iloc[i,6] , df2021.iloc[i,7] , df2021.iloc[i,8] , df2021.iloc[i,9] , df2021.iloc[i,10] , df2021.iloc[i,11] , df2021.iloc[i,12] , df2021.iloc[i,13] , df2021.iloc[i,14] , df2021.iloc[i,15] , df2021.iloc[i,16] , df2021.iloc[i,17] , df2021.iloc[i,18] , df2021.iloc[i,19] , df2021.iloc[i,20] , df2021.iloc[i,21] , df2021.iloc[i,22] , df2021.iloc[i,23] , df2021.iloc[i,24] , df2021.iloc[i,25] , df2021.iloc[i,26] , df2021.iloc[i,27] , df2021.iloc[i,28] , df2021.iloc[i,29]))


#function that creates new list, with player totals used as well as tm being current team

def no_repeats(player_list):
	aug_player_list = []
	aug_player_list.append(player_list[0])
	for i in range(len(player_list)):
		if (i > 0):
			if player_list[i].name == player_list[i-1].name:
				aug_player_list[-1].tm = player_list[i].tm
			else:
				aug_player_list.append(player_list[i])
	return aug_player_list

aug_list = no_repeats(player_list)

def team_searcher(list, team):
	teaming = []
	for i in range(len(list)):
		if (list[i].tm == team):
			teaming.append(list[i])
	return teaming

brooklyn = team_searcher(aug_list, "BRK")
#for i in range(len(brooklyn)):
#	print(brooklyn[i].name + " " + brooklyn[i].pts)


def threshold_searcher(list, type, tot):
	
	if (type == "pts"):
		for i in range(len(list)):
			if (float(list[i].pts) > tot):
				print(list[i].name + " " + list[i].pts)

threshold_searcher(aug_list, "pts", 22)


#print(df[df['Literacy %']>90]) - this function filters based on value of literacy


#Team name convention - tot = overall, last team is current team played for





#for website - data loads either once a day at the end of last game - say 6pm est
#in a seperate module, data has a bunch of functions run on it
# for searching, could search by numbers, name etc and would need to write functions for all of it
# could also 'create teams', and save those teams if you pay like $3 a month
# suggestions is a possible later feature to be implemented
# could also work with specific fantasy styles - might need to play bidding style to make this work tho

#there are 700ish vals because when players are traded they get + a row