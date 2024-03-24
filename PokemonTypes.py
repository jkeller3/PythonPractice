## Pokemon weakness testing

def Normal(type):
	modifier = 1
	if(type == 'Fighting'):
		modifier = 2
	elif(type == 'Ghost'):
		modifier = 0
	return modifier

def Water(type):
	modifier = 1
	if(type == 'Grass' or type == 'Electric'):
		modifier = 2
	elif(type == 'Water' or type == 'Fire'):
		modifier = 0.5
	return modifier

attack = 'Grass'
power = 120
modifier1 = Water(attack)
modifier2 = Water(attack)
print('Your attack did',power*modifier1*modifier2,'damage!')