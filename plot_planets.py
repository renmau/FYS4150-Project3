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

def plot_planet_oribt(x,y,planet_label='_nolegend_',title_label=' ',hold=False):
	#plot_formatting()
	if isinstance(x[0],np.ndarray)==True: # if x is a array of arrays
		if planet_label =='_nolegend_': planet_label=['_nolegend_' for i in range(len(x[:,0]))]
		[plt.plot(x[i], y[i], label=planet_label[i], ) for i in range(len(x[:,0]))]
		#if planet_label !='_nolegend_': plt.legend()
	else: 
		plt.plot(x,y,label=planet_label)
	plt.axis('equal')
	plt.xlabel('x [AU]')
	plt.ylabel('y(x) [AU]')
	plt.title(title_label)
	plt.tight_layout()
	if hold !=True: 
		plt.legend()
		plt.show()


def two_body_problem():
	#N1 = np.genfromtxt('exercice_3b_se_euler.txt')
	#N2 = np.genfromtxt('exercice_3b_se_verlet.txt')
	N1 = np.genfromtxt('b_euler10_5yr.txt')
	N2 = np.genfromtxt('b_verlet10_5yr.txt')  	 
	x_sun_e, y_sun_e, z_sun_e 			= N1[:,0], N1[:,1], N1[:,2]						 							 
	x_earth_e, y_earth_e, z_earth_e 	= N1[:,3], N1[:,4], N1[:,5]

	x_sun_v, y_sun_v, z_sun_v 			= N2[:,0], N2[:,1], N2[:,2]						 							 
	x_earth_v, y_earth_v, z_earth_v 	= N2[:,3], N2[:,4], N2[:,5]

	x_planet = np.array([x_sun_e, x_earth_e, x_sun_v, x_earth_v])
	y_planet = np.array([y_sun_e, y_earth_e, y_sun_v, y_earth_v])
	planet_label = ['_nolegend_','Earth Euler','_nolegend_','Earth V-Verlet']
	plot_planet_oribt(x_planet, y_planet, planet_label,'Two-body-problem Sun-Earth, 5 years 10 steps/year')

def three_body_problem():
	N = np.genfromtxt('exercice_3f_je.txt')
	N = np.genfromtxt('exercice_3e.txt')
	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	
	x_planet = np.array([x_sun, x_earth, x_jupiter])
	y_planet = np.array([y_sun, y_earth, y_jupiter])
	planet_label = ['Sun','Earth','Jupiter']
	plot_planet_oribt(x_planet, y_planet, planet_label,'Three-body-problem Sun-Earth-Jupiter')

def full_system():# entire classical solar system
	N = np.genfromtxt('exercice_3f_full_system.txt') 

	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]

	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_mercury, y_mercury, z_mercury = N[:,9], N[:,10], N[:,11]
	x_venus, y_venus, z_venus 		= N[:,12], N[:,13], N[:,14]
	x_mars, y_mars, z_mars 			= N[:,15], N[:,16], N[:,17]
	x_saturn, y_saturn, z_saturn 	= N[:,18], N[:,19], N[:,20]
	# fix uranus before neptune here and in c++
	x_neptune, y_neptune, z_neptune = N[:,21], N[:,22], N[:,23]
	x_uranus, y_uranus, z_uranus 	= N[:,24], N[:,25], N[:,26]
	x_pluto, y_pluto, z_pluto 		= N[:,27], N[:,28], N[:,29]

	x_planet=np.array([x_sun,x_mercury,x_venus,x_earth,x_mars,x_jupiter,x_saturn,x_uranus,x_neptune,x_pluto])
	y_planet=np.array([y_sun,y_mercury,y_venus,y_earth,y_mars,y_jupiter,y_saturn,y_uranus,y_neptune,y_pluto])
	planet_label = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']

	plot_planet_oribt(x_planet, y_planet, planet_label,'The classic solar system')

def mercury_perihelion():
	N = np.genfromtxt('exercice_3g_mercury.txt') 

	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_mercury, y_mercury, z_mercury	= N[:,3], N[:,4], N[:,5]

	x_planet=np.array([x_sun,x_mercury])
	y_planet=np.array([y_sun,y_mercury])
	planet_label = ['Sun','Mercury']

	plot_planet_oribt(x_mercury, y_mercury, 'Mercury','The Mercury orbit',hold=True)
	plt.plot(x_sun,y_sun,'rx',label='Sun')
	plt.legend()
	plt.show()

plot_formatting()
two_body_problem()
#three_body_problem()
#full_system()
#mercury_perihelion()
