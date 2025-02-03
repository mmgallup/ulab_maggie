# planet_functions.py

import numpy as np

def orbital_period(a):
    # Calculate the orbital period based on Kepler's third law.
    # Parameters: a (float or array-like): Semi-major axis in AU.
    # Returns: float or numpy array: Orbital period(s) in Earth years.
    return np.sqrt(a ** 3)
