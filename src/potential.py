"""
Gravitational potential equations.
"""
import numpy as np
from scipy.integrate import quad

from constants import G


def flatten(potential, R, D, θ, *args, **kwargs):
    Φ = np.empty_like(θ)
    d = D*np.tan(θ)
    s_max = np.sqrt(R**2 - d**2)

    def r(s, d):
        return np.sqrt(s**2 + d**2)

    for i in range(len(d)):
        def potential_(s):
            return potential(r(s, d[i]), *args, **kwargs)

        Φ[i] = 2*quad(potential_, 0, s_max[i])[0]

    return Φ



def dehnen3D(r, *, γ, M, a):
    power  = 2 - γ
    const  = -G*M / (a * power)
    rest = 1 - (r / (r+a))**power

    return const * rest
