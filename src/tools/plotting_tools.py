'''
Automated plotting tools
'''

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
plt.style.use('dark_background')

def plot_states(times,states,title='6 State Trajectory'):
    '''
    Plots 6 states over time
    '''

    fig, axs = plt.subplots(2,1)

    fig.suptitle(title)
    
    axs[0].plot(times,states[:,0])
    axs[0].plot(times,states[:,1])
    axs[0].plot(times,states[:,2])
    axs[0].set(ylabel='Position (km))')
    axs[0].legend(['rx','ry','rz'],loc='upper right')

    axs[1].plot(times,states[:,3])
    axs[1].plot(times,states[:,4])
    axs[1].plot(times,states[:,5])
    axs[1].set(xlabel='Time (s)',ylabel='Velocity (km/s))')
    axs[1].legend(['vx','vy','vz'],loc='upper right')

    for ax in range(2):
        axs[ax].grid(color='white',linestyle='--')

    plt.show()

def plot_orbits(states,title='Orbital Trajectory'):
    '''
    Plots orbit
    '''

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(states[:,0],states[:,1],states[:,2])

    plt.show()