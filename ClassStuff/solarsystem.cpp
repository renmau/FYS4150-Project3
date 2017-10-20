#define _USE_MATH_DEFINES
#include "solarsystem.h"
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

SolarSystem::SolarSystem() :
    m_kineticEnergy(0),
    m_potentialEnergy(0),
    m_angularMomentum(0,0,0)
{
    m_G = 4*M_PI*M_PI;
    c = 63239.7263;                   //AU/yr
}

void SolarSystem::createCelestialBody(vec3 position, vec3 velocity, double mass) {
    m_bodies.push_back( CelestialBody(position, velocity, mass) );
}

void SolarSystem::calculateForcesAndEnergy()
{
    m_kineticEnergy = 0;
    m_potentialEnergy = 0;
    m_angularMomentum.zeros();

    for(CelestialBody &body : m_bodies) {
        // Reset forces on all bodies
        body.force.zeros();
    }

    for(int i=0; i<numberOfBodies(); i++) {
        CelestialBody &body1 = m_bodies[i];
        for(int j=i+1; j<numberOfBodies(); j++) {
            CelestialBody &body2 = m_bodies[j];
            vec3 deltaRVector = body1.position - body2.position;
            double dr = deltaRVector.length();

            //body1.force += -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector;
            //body2.force -= -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector;
            //body1.force += -m_G*body1.mass*body2.mass/pow(dr,3.95)*deltaRVector;
            //body2.force -= -m_G*body1.mass*body2.mass/pow(dr,3.95)*deltaRVector;

            // for mercury perihelion precession:
            body1.force += -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector;// (3*body2.position.cross(body2.velocity).lengthSquared())/(dr*dr*dr*c*c)*deltaRVector;
            body2.force -= -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector - (3*body2.position.cross(body2.velocity).lengthSquared())/(dr*dr*dr*c*c)*deltaRVector;




            m_potentialEnergy += -m_G*body1.mass*body2.mass/(dr);
        }

        m_kineticEnergy += 0.5*body1.mass*body1.velocity.lengthSquared();
        m_angularMomentum += (body1.position.cross(body1.velocity*body1.mass));
    }
}


void SolarSystem::mercuryAngles(int timestep)
{
    m_angle = 0;
    r_2 = r_1;
    r_1 = r_now;
    r_now = (m_bodies[1].position-m_bodies[0].position).length();

    if(r_1<r_2 && r_1<r_now && timestep>3){
        if(!m_file_angle.good()) {
            m_file_angle.open("mercury_angle_10-9.txt", ofstream::out);
            if(!m_file_angle.good()) {
                cout << "Error opening file " << "mercury_angle_10-9.txt" << ". Aborting!" << endl;
                terminate();
            }
        }
        double xp = m_integrator->r_rel[0];
        double yp = m_integrator->r_rel[1];
        m_angle += atan2(yp,xp);
        m_file_angle << setprecision(10) << m_angle<<"    "<< r_1;
        m_file_angle << endl;
        //cout<< setprecision(10) << m_angle <<"    "<< r_1 << endl;
    }

}

int SolarSystem::numberOfBodies() const
{
    return m_bodies.size();
}

void SolarSystem::setIntegrator(VelocityVerlet *integrator)
{
    m_integrator = integrator;
}

double SolarSystem::totalEnergy() const
{
    return m_kineticEnergy + m_potentialEnergy;
}

double SolarSystem::potentialEnergy() const
{
    return m_potentialEnergy;
}

double SolarSystem::kineticEnergy() const
{
    return m_kineticEnergy;
}

vec3 SolarSystem::angularMomentum() const
{
    return m_angularMomentum;
}

void SolarSystem::writeToFile(string filename)
{
    if(!m_file.good()) {
        m_file.open(filename.c_str(), ofstream::out);
        if(!m_file.good()) {
            cout << "Error opening file " << filename << ". Aborting!" << endl;
            terminate();
        }
    }


    for(CelestialBody &body : m_bodies) {
        m_file << setprecision(10) << body.position.x() << " " << setprecision(10) << body.position.y() << " " << setprecision(10) << body.position.z() << " ";
    }
    m_file << endl;
}

std::vector<CelestialBody> &SolarSystem::bodies()
{
    return m_bodies;
}
