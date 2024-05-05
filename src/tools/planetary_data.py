'''
Library for planetary data
'''

# gravitational constant
G_meters = 6.67430e-11 # m**3/kg/s**2
G = G_meters * 10**-9 # km**3/kg/s**2

earth = {
    'name': 'Earth',
    'mass': 5.972e24,
    'mu': 5.972e24 * G,
    'radius': 6378.0
}

bodies = [earth]

for body in bodies:
    body['diameter'] = body['radius'] * 2