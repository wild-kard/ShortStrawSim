draw = [1, 2, 3]


#wrap in a while loop

playerOne = math.random()
playerTwo = math.random()
house = null
houseCount = 0

if playerOne < 0.33:
	playerOne = draw[0]
elif playerOne > 0.33 && < 0.66:
	playerOne = draw[1]
elif playerOne > 0.66:
	playerOne = draw[2]

if playerOne == draw[0]:
	if playerTwo < 0.5:
		playertwo = draw[1]
	elif playerTwo > 0.5:
		playerTwo = draw[2]


if playerOne == draw[1]
	if playerTwo < 0.5:
		playertwo = draw[0]
	elif playerTwo > 0.5:
		playerTwo = draw[2]


if playerOne == draw[2]	
	if playerTwo < 0.5:
		playertwo = draw[0]
	elif playerTwo > 0.5:
		playerTwo = draw[1]

if (playerOne == draw[0] && playerTwo == draw[1]) || (playerOne == draw[1] && playerTwo == draw[0]):
	house = draw[2]
elif (playerOne == draw[0] && playerTwo == draw[2]) || (playerOne == draw[2] && playerTwo == draw[0]):
	house = draw[1]
elif (playerOne == draw[1] && playerTwo == draw[2]) || (playerOne == draw[2] && playerTwo == draw[1]):
	house = draw[0]

if house == draw[2]:
	houseCount += 1
	
#divide houseCount by total number of games to get house's odds. 
