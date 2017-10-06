#define _USE_MATH_DEFINES
#include "solarsystem.h"
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

SolarSystem::SolarSystem() :
    m_kineticEnergy(0),
    m_potentialEnergy(0),
    m_angularMomentum(0)
{
    m_G = 4*M_PI*M_PI;
}

void SolarSystem::createCelestialBody(vec3 position, vec3 velocity, double mass) {
    m_bodies.push_back( CelestialBody(position, velocity, mass) );
}

void SolarSystem::calculateForcesAndEnergy()
{
    m_kineticEnergy = 0;
    m_potentialEnergy = 0;

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

            body1.force += -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector;
            body2.force -= -m_G*body1.mass*body2.mass/(dr*dr*dr)*deltaRVector;
            //body1.force += -m_G*body1.mass*body2.mass/pow(dr,3)*deltaRVector;
            //body2.force -= -m_G*body1.mass*body2.mass/pow(dr,3)*deltaRVector;



            m_potentialEnergy += -m_G*body1.mass*body2.mass/(dr);
        }

        m_kineticEnergy += 0.5*body1.mass*body1.velocity.lengthSquared();
        m_angularMomentum += (body1.position.cross(body1.velocity*body1.mass)).length();
    }
}

int SolarSystem::numberOfBodies() const
{
    return m_bodies.size();
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

double SolarSystem::angularMomentum() const
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
