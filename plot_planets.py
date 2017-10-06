import matplotlib as mpl
mpl.use('TkAgg') # Ensure that the Tkinter backend is used for generating figures
import numpy as np
import matplotlib.pyplot as plt

def plot_formatting(fam='serif',fam_font='Computer Modern Roman',font_size=14,tick_size=14):
	""" you get to define what font and size of xlabels and axis ticks you"""
	"""like, if you want bold text or not.								  """
	
	plt.rc('text',usetex=True)
	axis_font={'family': fam,'serif':[fam_font],'size':font_size}
	plt.rc('font',**axis_font)
	plt.rc('font',weight ='bold')
	#plt.rcParams['text.latex.preamble']=[r'\boldmath']
	plt.xticks(fontsize=tick_size)
	plt.yticks(fontsize=tick_size)

def plot_planet_oribt(x,y,planet='planet',title_label='some title'):
	#plot_formatting()
	if isinstance(x[0,:],np.ndarray)==True: # if x is a array of arrays
		[plt.plot(x[i],y[i],label=planet[i]) for i in range(len(x[:,0]))]
	else: plt.plot(x,y,label=planet)
	plt.axis('equal')
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y(x)')
	plt.title(title_label)
	plt.show()

def three_body_problem():
	N = np.genfromtxt('exercice_3f_je.txt') 	 
	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	
	x_planet = np.array([x_sun, x_earth, x_jupiter])
	y_planet = np.array([y_sun, y_earth, y_jupiter])
	planet_label = ['Sun','Earth','Jupiter']
	plot_planet_oribt(x_planet,y_planet,planet_label,'Three-body-problem Sun-Earth-Jupiter')

def full_system():# entire classical solar system
	N = np.genfromtxt('exercice_3f_full_system.txt') 	
	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]

	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_mercury, y_mercury, z_mercury = N[:,9],N[:,10],N[:,11]
	x_venus, y_venus, z_venus 		= N[:,12],N[:,13],N[:,14]
	x_mars, y_mars, z_mars 			= N[:,15],N[:,16],N[:,17]
	x_saturn, y_saturn, z_saturn 	= N[:,18],N[:,19],N[:,20]
	x_neptune, y_neptune, z_neptune = N[:,21],N[:,22],N[:,23]
	x_uranus, y_uranus, z_uranus 	= N[:,24],N[:,25],N[:,26]
	x_pluto, y_pluto, z_pluto 		= N[:,27],N[:,28],N[:,29]

	x_planet=np.array([x_sun,x_mercury,x_venus,x_earth,x_mars,x_jupiter,x_saturn,x_neptune,x_uranus,x_pluto])
	y_planet=np.array([y_sun,y_mercury,y_venus,y_earth,y_mars,y_jupiter,y_saturn,y_neptune,y_uranus,y_pluto])
	planet_label = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Neptune','Uranus','Pluto']

	plot_planet_oribt(x_planet,y_planet,planet_label,'The classic solar system')
three_body_problem()
full_system()
'''
plt.plot(x_sun,y_sun,label='sun')
plt.plot(x_mercury,y_mercury,label='mercury')
plt.plot(x_venus,y_venus,label='venus')
plt.plot(x_earth,y_earth,label='earth')
plt.plot(x_mars,y_mars,label='mars')

plt.plot(x_jupiter,y_jupiter,label='jupiter')
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
plt.show()'''