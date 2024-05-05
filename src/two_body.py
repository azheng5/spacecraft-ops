'''
Solves the two body problem
'''

# 3rd party libraries
import numpy as np

# Built in library
import tools.planetary_data as pd
import tools.numerical_tools as nt
import tools.orbital_tools as ot
import tools.plotting_tools as pt

if __name__ == '__main__':
    r0_norm = pd.earth['radius'] + 450 # km
    v0_norm = ( pd.earth[ 'mu' ] / r0_norm ) ** 0.5 # km/s
    state0 = [r0_norm, 0, 0, 0, v0_norm, 0]
    tspan = 100.0 * 60.0 # sec
    dt = 100.0 # sec
    steps = int(tspan/dt)
    times = np.linspace(0,tspan,steps)
    states = np.zeros((steps,6))
    states[0] = state0

    for step in range(steps-1):
        # get next state
        states[step+1] = nt.rk4_step(
            ot.two_body_ode,times[step],states[step],dt)

    # pt.plot_states(times,states)
    pt.plot_orbits(states)