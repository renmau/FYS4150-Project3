import numpy as np
import matplotlib.pyplot as plt

positions = np.genfromtxt('pow2.txt')
x_e = positions[:,3]
y_e = positions[:,4]
x_s = positions[:,0]
y_s = positions[:,1]

positions1 = np.genfromtxt('pow22.txt')
x_e1 = positions1[:,3]
y_e1 = positions1[:,4]

positions2 = np.genfromtxt('pow24.txt')
x_e2 = positions2[:,3]
y_e2 = positions2[:,4]

positions3 = np.genfromtxt('pow26.txt')
x_e3 = positions3[:,3]
y_e3 = positions3[:,4]

positions4 = np.genfromtxt('pow28.txt')
x_e4 = positions4[:,3]
y_e4 = positions4[:,4]

positions5 = np.genfromtxt('pow295.txt')
x_e5 = positions5[:,3]
y_e5 = positions5[:,4]

positions6 = np.genfromtxt('pow3.txt')
x_e6 = positions6[:,3]
y_e6 = positions6[:,4]

plt.plot(x_e6,y_e6)
#plt.plot(x_e5,y_e5)
#plt.plot(x_e4,y_e4)
#plt.plot(x_e3,y_e3)
#plt.plot(x_e2,y_e2) #nei
#plt.plot(x_e1,y_e1) #nei
plt.plot(x_e,y_e)
plt.plot(x_s,y_s)
plt.axis('equal')
plt.legend([r'$\beta=3$',r'$\beta=2$'],fontsize=11)
plt.xlabel('x [AU]', fontsize=11)
plt.ylabel('y [AU]', fontsize=11)
plt.title(r'Gravitational force goes as $\propto 1/r^{\beta}$ ', fontsize=11)
plt.show()

'''
positions = np.genfromtxt('d_an.txt')
x_e = positions[:,3]
y_e = positions[:,4]
x_s = positions[:,0]
y_s = positions[:,1]

positions1 = np.genfromtxt('d_an15.txt')
x_e1 = positions1[:,3]
y_e1 = positions1[:,4]

positions2 = np.genfromtxt('d_an25.txt')
x_e2 = positions2[:,3]
y_e2 = positions2[:,4]

plt.plot(x_e,y_e)
plt.plot(x_e1,y_e1)
plt.plot(x_e2,y_e2)
plt.plot(x_s,y_s)
plt.legend([r'$v=\sqrt{2}2\pi$',r'$v=\sqrt{2}2\pi-1/5$',r'$v=\sqrt{2}2\pi-2/5$','sun'], fontsize=11)
plt.xlabel('x [AU]', fontsize=11)
plt.ylabel('y [AU]', fontsize=11)
plt.title('Escape velocity, Sun-Earth system (15 year period)', fontsize=11)
plt.show()
'''
'''
energy = np.genfromtxt('energyeuler.txt')

E_k = energy[:,0]
E_p = energy[:,1]
angmom = energy[:,2]

t = np.linspace(0,100,len(E_k))

plt.plot(t,E_k)
plt.plot(t,E_p)
plt.plot(t,E_p+E_k)
#plt.plot(t,angmom)
plt.legend([r'$E_k$',r'$E_p$',r'$E_{tot}$'])
plt.xlabel('time [years]')
plt.ylabel(r'Energy $[M_{\odot}AU^2/yr^2]$')
plt.title('Energy conservation (VV)')
plt.show()
'''
