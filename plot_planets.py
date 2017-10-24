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

def plot_planet_orbit(x,y,planet_label='_nolegend_', title_label=' ',hold=False):
	""" Plots planet orbits, entire system, or a singla planet.
		Use hold=True to add plots or do other things in the function calling on this one"""

	plot_formatting()
	if y.ndim>1: # if y is a array of arrays
		if planet_label =='_nolegend_': planet_label=['_nolegend_' for i in range(len(y[:,0]))]
		[plt.plot(x[i], y[i], label=planet_label[i]) for i in range(len(y[:,0]))]
		#if planet_label !='_nolegend_': plt.legend()
	else: 
		plt.plot(x,y,label=planet_label)

	plt.axis('equal')
	plt.xlabel('position $x$ [AU]')
	plt.ylabel('position $y(x)$ [AU]')
	plt.title(title_label)
	plt.tight_layout()
	if hold !=True: 
		plt.legend()
		plt.show()

def plot_conserved(x,y,plot_label,y_label,title_label='   ',hold=False,):
	""" Plots the conserved quantities kinetic and potential energy, and the angular momentum
		Use hold=True to add plots or do other things in the function calling on this one"""
	plot_formatting()
	if y.ndim> 1: # if x is a array of arrays
		[plt.plot(x, y[i], label=plot_label[i]) for i in range(len(y[:,0]))]
		#if planet_label !='_nolegend_': plt.legend()
	else: 	plt.plot(x,y,label=plot_label)

	plt.xlabel('time [years]')
	plt.ylabel(y_label)
	plt.tight_layout()
	if hold==False:
		plt.title(title_label)
		plt.legend()
		plt.tight_layout()
		plt.show()

def two_body_problem():
	""" Plots the orbit of the Sun-Earth system"""

	N1 = np.genfromtxt('earth_10000_euler.txt')
	N2 = np.genfromtxt('earth_10000_verlet.txt')
	nsteps = 10000
	x_sun_e, y_sun_e, z_sun_e 			= N1[:,0], N1[:,1], N1[:,2]						 							 
	x_earth_e, y_earth_e, z_earth_e 	= N1[:,3], N1[:,4], N1[:,5]

	x_sun_v, y_sun_v, z_sun_v 			= N2[:,0], N2[:,1], N2[:,2]						 							 
	x_earth_v, y_earth_v, z_earth_v 	= N2[:,3], N2[:,4], N2[:,5]

	x_planet = np.array([x_sun_e, x_earth_e, x_sun_v, x_earth_v])
	y_planet = np.array([y_sun_e, y_earth_e, y_sun_v, y_earth_v])
	planet_label = ['_nolegend_','Earth Euler','_nolegend_','Earth V-Verlet']

	plot_planet_orbit(x_planet, y_planet, planet_label,title_label='Two-body-problem Sun-Earth %d steps/year' % nsteps)

def conservation():
	""" Plots the conserved quantities kinetic energy, potential energy, angular momentum
		of the Sun-Earth system for Euler and Velocity-Verlet integrator """

	N1 = np.genfromtxt('2body_euler.txt')
	N2 = np.genfromtxt('2body_verlet.txt')	

	Ke, Ve, Le 	= N1[:,0], N1[:,1], N1[:,2]						 							 
	Kv, Vv, Lv 	= N2[:,0], N2[:,1], N2[:,2]
	
	t = np.linspace(0,100,len(Lv))
	
	# put in one array for plotting purposes

	K = np.array([Ke, Kv])
	V = np.array([Ve, Vv])
	Etot = K+V
	L = np.array([Le, Lv])
	plot_label = ['Euler','V-Verlet']
	plot_conserved(t, L, hold=False, plot_label=plot_label, y_label='Angular momentum [$M_\odot$ AU$^2/$yr]')
	plot_conserved(t,np.array([Ke,Ve,Etot[0]]), hold=False, plot_label=['$E_k$','$E_p$','$E_{tot}$'],y_label='Energy [$M_\odot$ AU$^2/$yr$^2$]',title_label='Energy conservation (Euler)')
	plot_conserved(t,np.array([Kv,Vv,Etot[0]]), hold=False, plot_label=['$E_k$','$E_p$','$E_{tot}$'],y_label='Energy [$M_\odot$ AU$^2/$yr$^2$]',title_label='Energy conservation (VV)')


def three_body_problem():
	""" Plots orbits of Sun-Earth-Jupiter system """

	N = np.genfromtxt('exercice_3e.txt')

	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	
	# put in one array for plotting purposes
	x_planet = np.array([x_sun, x_earth, x_jupiter])
	y_planet = np.array([y_sun, y_earth, y_jupiter])
	planet_label = ['Sun','Earth','Jupiter']

	nTimesteps = 1000 #[5,10,100,1000]
	'''
	#When calculating for different Jupiter masses
	mass = [10,100]
	title_label ='Sun-Earth-Jupiter, %dM_J, %d steps/year' %(mass,nTimesteps)
	'''
	title_label='Three-body-problem Sun-Earth-Jupiter (%d steps/year)' %nTimesteps
	
	plot_planet_orbit(x_planet, y_planet, planet_label,title_label=title_label)

def full_system():
	"""plots orbit of the entire classical solar system"""

	N = np.genfromtxt('exercice_3f_full_system.txt') 

	x_sun, y_sun, z_sun 			= N[:,0], N[:,1], N[:,2]						 							 
	x_earth, y_earth, z_earth 		= N[:,3], N[:,4], N[:,5]

	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_jupiter, y_jupiter, z_jupiter = N[:,6], N[:,7], N[:,8]
	x_mercury, y_mercury, z_mercury = N[:,9], N[:,10], N[:,11]
	x_venus, y_venus, z_venus 		= N[:,12], N[:,13], N[:,14]
	x_mars, y_mars, z_mars 			= N[:,15], N[:,16], N[:,17]
	x_saturn, y_saturn, z_saturn 	= N[:,18], N[:,19], N[:,20]
	x_uranus, y_uranus, z_uranus 	= N[:,21], N[:,22], N[:,23]
	x_neptune, y_neptune, z_neptune = N[:,24], N[:,25], N[:,26]	
	x_pluto, y_pluto, z_pluto 		= N[:,27], N[:,28], N[:,29]

	x_planet=np.array([x_sun,x_mercury,x_venus,x_earth,x_mars,x_jupiter,x_saturn,x_uranus,x_neptune,x_pluto])
	y_planet=np.array([y_sun,y_mercury,y_venus,y_earth,y_mars,y_jupiter,y_saturn,y_uranus,y_neptune,y_pluto])
	planet_label = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']

	plot_planet_orbit(x_planet, y_planet, planet_label,title_label='The classic solar system')

def mercury_perihelion():
	"""Plots Mercury orbit, calculates the perihelion angle"""
	N1 = np.genfromtxt('mercury_1000_orbit.txt')	

	N3 = np.genfromtxt('mercury_angle_10_7_gr.txt')
	N4 = np.genfromtxt('mercury_angle_10_7_Newton.txt')

	nTimesteps=1e7
	years = 100.
	perihel=0.3075 # AU
	perangle = 43. # arcseconds
	print 'correct angle', perangle, ' arcseconds,   correct perihel', perihel

	# sun and mercury positions
	x_sun, y_sun, z_sun 			= N1[:,0], N1[:,1], N1[:,2]						 							 
	x_mercury, y_mercury, z_mercury	= N1[:,3], N1[:,4], N1[:,5]

	# constains already computed angles, the timesteps and r in perihelion for GR correction
	angles_gr, r_gr,dt_gr , = N3[:,0]*180*60*60/np.pi, N3[:,1], N3[:,2]*years/(years*nTimesteps-1)
	xp, yp = N3[:,3], N3[:,4]

	# constains already computed angles, the timesteps and r in perihelion for Newtonian gravity	
	angles_n, r_n,dt_n = N4[:,0]*180*60*60/np.pi, N4[:,1], N4[:,2]*years/(years*nTimesteps-1)

	print 'calculated angle GR: ',angles_gr[-1],' arcsecond,  rp:',r_gr[-1]
	print 'calculated angle newton: ',angles_n[-1],' arcsecond,  rp:',r_n[-1]

	# plot the perihelion angles
	plot_formatting()
	plt.plot(dt_gr,angles_gr,dt_n,angles_n)
	plt.xlabel('time [years]')
	plt.ylabel(r'$\theta_P$ [arcseconds]')
	plt.title('Perihelion angle of Mercury for $10^7$ steps/year')
	plt.legend(['GR gravity','Newtonian gravity'])	
	plt.show()

	x_planet=np.array([x_sun,x_mercury])
	y_planet=np.array([y_sun,y_mercury])
	planet_label = ['Sun','Mercury']

	plot_planet_orbit(x_mercury, y_mercury, 'Mercury','The Mercury orbit 10 000 steps/year',hold=True)
	plt.plot(x_sun,y_sun,'gx',label='Sun')
	plt.plot(xp[-1],yp[-1],'rx',label='perihelion')
	plt.legend()
	plt.show()

def perihelion_angles():
	N1 = np.genfromtxt('mercury_angle_10_5_gr.txt')
	N2 = np.genfromtxt('mercury_angle_10_6.txt')
	N3 = np.genfromtxt('mercury_angle_10_7_gr.txt')	

	years = 100.
	nTimesteps = np.array([1e5, 1e6, 1e7])
	angles1, r1, dt1 = N1[:,0]*180*60*60/np.pi, N1[:,1], N1[:,2]*years/(years*nTimesteps[0]-1)
	angles2, r2, dt2 = N2[:,0]*180*60*60/np.pi, N2[:,1], N2[:,2]*years/(years*nTimesteps[1]-1)
	angles3, r3, dt3 = N3[:,0]*180*60*60/np.pi, N3[:,1], N3[:,2]*years/(years*nTimesteps[2]-1)

	angles = np.array([ angles1, angles2, angles3 ])
	time = np.array([ dt1, dt2, dt3 ])
	plot_labels = ['$N = 10^5$','$N = 10^6$','$N = 10^7$']
	plot_formatting()
	[plt.plot(time[i], angles[i], label=plot_labels[i]) for i in range(0,len(angles[:,0]))]
	plt.xlabel('time [years]')
	plt.ylabel(r'$\theta_P$ [arcseconds]')
	plt.title('Mercury perihelion angle for different $N$=timesteps/year')
	plt.legend()
	plt.show()

#two_body_problem()
#conservation()
#three_body_problem()
full_system()
#mercury_perihelion()
#perihelion_angles()