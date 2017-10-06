import matplotlib as mpl
mpl.use('TkAgg') # Ensure that the Tkinter backend is used for generating figures

import numpy as np
import matplotlib.pyplot as plt

N = np.genfromtxt('exercice_3f_full_system.txt') 	 # read file, ignore first two lines

x_sun = N[:,0]						 							 # x from file
y_sun = N[:,1] 					 							 # analytical result, extract from file
z_sun = N[:,2]													 # numerical result, extract from file
x_earth = N[:,3]
y_earth = N[:,4]
z_earth = N[:,5]
x_jup = N[:,6]
y_jup = N[:,7]
z_jup = N[:,8]

x_merc,y_merc,z_merc = N[:,9],N[:,10],N[:,11]
x_venus, y_venus, z_venus = N[:,12],N[:,13],N[:,14]
x_mars, y_mars, z_mars = N[:,15],N[:,16],N[:,17]
x_saturn, y_saturn, z_saturn = N[:,18],N[:,19],N[:,20]
x_neptune, y_neptune, z_neptune = N[:,21],N[:,22],N[:,23]
x_uranus, y_uranus, z_uranus = N[:,24],N[:,25],N[:,26]
x_pluto, y_pluto, z_pluto = N[:,27],N[:,28],N[:,29]


#plt.plot(x,u)
plt.plot(x_sun,y_sun,label='sun')
plt.plot(x_earth,y_earth,label='earth')
plt.plot(x_jup,y_jup,label='jupiter')
plt.plot(x_merc,y_merc,label='mercury')
plt.plot(x_venus,y_venus,label='venus')
plt.plot(x_mars,y_mars,label='mars')
plt.plot(x_saturn,y_saturn,label='saturn')
plt.plot(x_neptune,y_neptune,label='neptune')
plt.plot(x_uranus,y_uranus,label='uranus')
plt.plot(x_pluto,y_pluto, label='pluto')
plt.axis('equal')
plt.legend()
plt.xlabel('x')
plt.ylabel('y(x)')
#plt.title('Change in gravitational force')
#plt.legend(['analytical','numerical'])
plt.show()