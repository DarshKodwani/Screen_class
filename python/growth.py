import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from classy import Class
from scipy.optimize import fsolve
from scipy.interpolate import interp1d
import math

common_settings = {# we need to set the output field to something although
                   # the really releveant outpout here will be set with 'k_output_values'
                   'output':'mPk',
                   # value of k we want to polot in [1/Mpc]
                   # LambdaCDM parameters
                   'h':0.67556,
                   'omega_b':0.022032,
                   'omega_cdm':0.12038,
                   'A_s':2.215e-9,
                   'n_s':0.9619,
                   'tau_reio':0.0925,
                   # Take fixed value for primordial Helium (instead of automatic BBN adjustment)
                   'YHe':0.246,
                   # other options and settings
                   'compute damping scale':'yes', # needed to output the time of damping scale crossing
                   'gauge':'newtonian'}
M = Class()
M.set(common_settings)
M.compute()

growth = M.get_background()['gr.fac. D'] 
zs = M.get_background()['z']
scalefactor = 1/zs
#plt.semilogx(zs, growth,label = "D(z)")
plt.semilogx(scalefactor, growth,label = "D(a)")
plt.legend()
plt.show()
