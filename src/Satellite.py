'''
Class for simulating satellite orbit trajectory using the 2 body problem
'''

# standard libraries
import os
import math

# 3rd party libraries
import numpy as np
import matplotlib.pyplot as plt

def null_config():
    return {
        'orbit_state': [], # 6 element orbital state
        'coes': [], # 6 classical orbital elements
        'm0': 0, # initial mass
        'stop_conditions':{}
    }

class Satellite:

    def __init__(self,config):
        self.config = null_config()
        for key in config.keys():
            self.config[key] = config[key]

    