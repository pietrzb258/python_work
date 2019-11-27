alien_0 = {
'color':'green',
'points':5
}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 100
alien_1['x_position'] = 25
alien_1['y_position'] = 35
print(alien_1)

print(f"\nalien_0 is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"\nNow alien_0 is {alien_0['color']}")

print("\n")

alien_2 = {
    'x_position':0,
    'y_position':25,
    'speed':'medium',
    'points':10,
    }
print(alien_2)
print(f"Original position: {alien_2['x_position']}")
# Move the alien to the right.
# Determine how far the alien should move based on its current speed.
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
elif alien_2['speed'] == 'fast':
    x_increment = 3
# The new position is the old position plus the increment
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"New position: {alien_2['x_position']}")
del alien_2['points']
print(alien_2)
