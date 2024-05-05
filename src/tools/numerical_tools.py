'''
Library for numerical methods
'''

def rk4_step(f,t,x,h):
    '''
    Calculate one RK4 step

    f: 1st order derivative function
    t: current time
    x: current state
    h: time step
    '''

    k1 = f(t,x)
    k2 = f(t+0.5*h, x+0.5*k1*h)
    k3 = f(t+0.5*h, x+0.5*k2*h)
    k4 = f(t+h,x+k3*h)
    kwmean = (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return x + h*kwmean # x_n+1