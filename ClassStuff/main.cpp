#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <stdlib.h>
#include "solarsystem.h"
#include "euler.h"
#include "velocityverlet.h"
#include <fstream>
#include <iomanip>
#include "time.h"
#include <chrono>

using namespace std;

SolarSystem TwoBodyProblem(){
    SolarSystem solarSystem;
    // The Sun
    solarSystem.createCelestialBody( vec3(0, 0, 0), vec3( 0, 0, 0), 1.0 );
    //The Earth
    solarSystem.createCelestialBody( vec3(1, 0, 0), vec3( 0, 2*M_PI, 0 ), 3e-6 );
    return solarSystem;

}
SolarSystem ThreeBodyProblem(bool fixed_CM){
    vec3 vJ(0, sqrt(4*M_PI*M_PI/5.2), 0);

    //For unmoving center-of-mass of three body system jupiter,earth,sun
    if (fixed_CM == true){
        SolarSystem solarSystem;
        double mE = 3e-6;
        double mJ = 9.5e-4;
        vec3 vE(0, sqrt(4*M_PI*M_PI), 0);

        vec3 vSun=-mE*vE - mJ*vJ;
        vec3 CM = (vec3(1, 0, 0)*mE + vec3(5.2,0,0)*mJ)/(mE+mJ+1.);

        // The Sun
        solarSystem.createCelestialBody( vec3(0, 0, 0)-CM, vSun, 1.0 );
        //The Earth
        solarSystem.createCelestialBody( vec3(1, 0, 0)-CM, vE, 3e-6 );
        // Jupiter
        solarSystem.createCelestialBody( vec3(5.2,0,0)-CM, vJ, 9.5e-4);
        return solarSystem;

    }
    // Three body problem without correction for center-of-mass
    else{
        SolarSystem solarSystem = TwoBodyProblem();
        // Jupiter
        solarSystem.createCelestialBody( vec3(5.2,0,0), vJ, 9.5e-4);
        return solarSystem;
    }
}

SolarSystem FullSystem(){

    SolarSystem solarSystem;
    // The Sun
    solarSystem.createCelestialBody( vec3(2.280645281880971E-03,5.669034916996534E-03,-1.316063812538178E-04), vec3(-5.124710550422158E-06*365., 5.551631297499966E-06*365., 1.189826204505761E-07*365.), 1.0 );
    //The Earth
    solarSystem.createCelestialBody( vec3(9.776084084140449E-01, 2.252978885335488E-01, -1.428938088034023E-04), vec3(-4.062408436217812E-03*365.,1.671862543878177E-02*365.,-1.806432427648686E-07*365.), 3e-6 );
    // Jupiter
    solarSystem.createCelestialBody( vec3(-4.627833494978254,-2.854717085491127,1.153513368222256E-01), vec3(3.873869902389083E-03*365.,-6.064150861099257E-03*365.,-6.145176060277265E-05*365.), 9.5e-4);
    // Mercury
    solarSystem.createCelestialBody( vec3(-3.896475834228487E-01,-2.816359732979998E-02,3.305924612088227E-02), vec3(-3.438017523837078E-03,-2.681547759811458E-02,-1.876572045563162E-03)*365., 1.65e-7);
    // Venus
    solarSystem.createCelestialBody( vec3(-5.122691445263290E-01,5.057193230515091E-01,3.642042956185625E-02), vec3(-1.417569102004634E-02,-1.460561845394588E-02,6.174282365295180E-04)*365., 2.45e-6 );
    // Mars
    solarSystem.createCelestialBody( vec3(-1.510556500968014, 7.016843752438682E-01,5.158146872545729E-02), vec3(-5.328917141208186E-03,-1.151197416056758E-02,-1.105814511135091E-04)*365., 3.3E-7 );
    // Saturn
    solarSystem.createCelestialBody( vec3(-4.106878033627468E-01,-1.004669994513129E+01,1.910286401217743E-01), vec3(5.268654062679371E-03,-2.458299042190405E-04,-2.054537524214767E-04)*365., 2.75e-4);
    // Neptune
    solarSystem.createCelestialBody( vec3(2.860387845165146E+01,-8.854538501256135,-4.768631616180988E-01), vec3(9.072716295025177E-04,3.016975531099665E-03,-8.333936157206056E-05)*365., .515e-4);
    // Uranus
    solarSystem.createCelestialBody( vec3(1.787905976395623E+01,8.773022260100626,-1.990427195843487E-01), vec3(-1.761322338307447E-03,3.347557466700209E-03,3.516031928207541E-05)*365., 4.4e-5);
    // Pluto
    solarSystem.createCelestialBody( vec3(1.051352392432785E+01,-3.171624029129188E+01,3.527021366368159E-01), vec3(3.048301492667712E-03,3.404636168561237E-04,-9.058944090468905E-04)*365., 6.55e-9);

    return solarSystem;
}

SolarSystem MercuryPerihelionPrecession(){
    // For Mercury perihelion precession:
    SolarSystem solarSystem;

    double mM = 1.65e-7;
    vec3 vM(0,12.44,0);
    vec3 rM = vec3(0.3075, 0, 0);
    vec3 rSun = vec3(0, 0, 0);
    //vec3 vSun = vec3(0,0,0);
    vec3 vSun=-mM*vM;
    vec3 CM = (rM*mM)/(mM+1.);
    // The Sun
    solarSystem.createCelestialBody( rSun-CM, vSun, 1.0 );
    //Mercury
    solarSystem.createCelestialBody( rM-CM, vM, mM );

    return solarSystem;
}
int main(int numArguments, char **arguments)
{
    char *outfilename;
    outfilename = arguments[1];
    double years = 10.0;
    int numTimesteps = years*1000;
    double dt = years / (numTimesteps-1);
    if(numArguments >= 3) numTimesteps = atoi(arguments[2]);
    bool fixed_CM = true;
    bool mercury = true;

    //SolarSystem solarSystem = TwoBodyProblem();
    //SolarSystem solarSystem = ThreeBodyProblem(fixed_CM);
    //SolarSystem solarSystem = FullSystem();
    SolarSystem solarSystem = MercuryPerihelionPrecession();


    // To get a list (a reference, not copy) of all the bodies in the solar system, we use the .bodies() function
    vector<CelestialBody> &bodies = solarSystem.bodies();

    for(int i = 0; i<bodies.size(); i++) {
        CelestialBody &body = bodies[i]; // Reference to this body
        cout << "The position of this object is " << body.position << " with velocity " << body.velocity << endl;
    }

    // advance all planets:

    //Euler integrator(dt);
    VelocityVerlet integrator(dt);

    solarSystem.writeToFile(outfilename);     // get initial values in text file as well
    solarSystem.calculateForcesAndEnergy();

    //write initial energy to file:
    solarSystem.calculateForcesAndEnergy();
    ofstream ofile;
    ofile.open("3body.txt",ofstream::app);
    ofile<<setprecision(30) << solarSystem.kineticEnergy() <<"  "<< setprecision(30) << solarSystem.potentialEnergy()<<"  "<< setprecision(30) << solarSystem.angularMomentum().length()<<endl;
    ofile<<endl;
    ofile.close();

    clock_t start1, finish1;
    start1 = clock();

    // forward loop
    for(int timestep=0; timestep<numTimesteps; timestep++) {
        integrator.integrateOneStep(solarSystem);
        solarSystem.writeToFile(outfilename);

        //write energy to file for each step to test conservation:
        solarSystem.calculateForcesAndEnergy();
        ofstream ofile;
        ofile.open("3body.txt",ofstream::app);
        // test to write perihelion angle to file for mercury case:
        /*
        if mercury = true{
                double x_p = ?;
                double y_p = ?;
                tan_theta = x_p/y_p;
                ofile<<setprecision(30) << solarSystem.kineticEnergy() <<"  "<< setprecision(30) << solarSystem.potentialEnergy()<<"  "<< setprecision(30) << solarSystem.angularMomentum().length()<<"  "<< setprecision(30) <<tan_theta<<endl;
                } */
        ofile<<setprecision(30) << solarSystem.kineticEnergy() <<"  "<< setprecision(30) << solarSystem.potentialEnergy()<<"  "<< setprecision(30) << solarSystem.angularMomentum().length()<<endl;
    }
    ofile<<endl;
    ofile.close();

    finish1=clock();
    double timeused1 = (double)(finish1-start1)/(CLOCKS_PER_SEC);
    cout <<"time used to calculate orbits (and write to file): "<<timeused1<<endl;

    cout << "I just created my first solar system that has " << solarSystem.bodies().size() << " objects." << endl;
    return 0;
}

