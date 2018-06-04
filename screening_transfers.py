import numpy as np
from matplotlib import pyplot as plt
from scipy.special import spherical_jn as jn
from scipy.integrate import quad
from scipy.interpolate import interp1d

transfer_full = np.loadtxt("screen_tk.dat", unpack=True)
ks = transfer_full[0,:]
phi = transfer_full[-2,:]
phi_interp = interp1d(ks, phi)

#plt.loglog(ks,phi, label = "$T_\phi(k)$")
#plt.xlabel("k (1/Mpc)")
#plt.legend()
#plt.show()

#Integrals for nu_l

#def int_rand1(x,d, ell, ns,eta_0, H0):
    #return (phi_interp(x)**2)*jn(ell,x*d)
    #return phi_interp(x)*jn(ell, x*d)*(x**(ns+1))*(eta_0**(ns-1))/(H0**3)

#plt.loglog(ks, int_rand1(ks,100, 1, 0.96, 0.1, 70))
#plt.show()

def nu_l(ell, kmin,kmax, d, H0, eta_0, ns):
    integrand_nul = lambda x : phi_interp(x)*jn(ell, x*d)*(x**(ns+1))*(eta_0**(ns-1))/(H0**3)
    return quad(integrand_nul, kmin, kmax)[0]

d = np.arange(200)
nu_d=[]
for i in d : 
    nu_d.append(nu_l(1,min(ks),max(ks), i, 70, 0.1, 0.96))

plt.loglog(d, nu_d, label= " nu_l ")
plt.xlabel("d(Mpc/h)")
plt.legend()
plt.show()
