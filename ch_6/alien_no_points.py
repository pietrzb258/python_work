alien_0 = {'color':'green', 'speed':'slow'}
#print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assigned.')
# if the second argument in .get is left blank, python will return "None".
print(point_value)
