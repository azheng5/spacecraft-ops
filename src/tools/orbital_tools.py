'''
Library for orbital mechanics math
'''

import numpy as np
import math

import tools.planetary_data as pd

def two_body_ode(t, state, mu = pd.earth['mu']):
    '''
    Calculates current state derivative

    t: current time
    state: [rx, ry, rz, vx, vy, vz]

    returns statedot = [vx,vy,vz,ax,ay,az]

    t remains unused for the 2-body problem, but required for 
    proper formatting for the RK4 soln
    '''

    r = state[:3]
    a = (-mu * r) / np.linalg.norm(r)**3

    return np.array([
        state[3],state[4],state[5],a[0],a[1],a[2]])

def state2coes(state, args={}):
    '''
    Converts state vector to classical orbital elements
    '''
    _args = {
        'mu': pd.earth['mu']
    }
    for key in args.keys():

def state2coes( state, args = {} ):
	_args = {
		'et'        : 0,
		'mu'        : pd.earth[ 'mu' ],
		'deg'       : True,
		'print_coes': False
	}
	for key in args.keys():
		_args[ key ] = args[ key ]

	rp,e,i,raan,aop,ma,t0,mu,ta,a,T = spice.oscltx( 
		state, _args[ 'et' ], _args[ 'mu' ] )

	if _args[ 'deg' ]:
		i    *= nt.r2d
		ta   *= nt.r2d
		aop  *= nt.r2d
		raan *= nt.r2d

	if _args[ 'print_coes' ]:
		print( 'a'   , a    )
		print( 'e'   , e    )
		print( 'i'   , i    )
		print( 'RAAN', raan )
		print( 'AOP' , aop  )
		print( 'TA'  , ta   )
		print()

	return [ a, e, i, ta, aop, raan ]