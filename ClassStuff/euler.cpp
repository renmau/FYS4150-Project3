#include "euler.h"
#include "solarsystem.h"

Euler::Euler(double dt) :
    m_dt(dt)
{

}

void Euler::integrateOneStep(SolarSystem &system)
{
    system.calculateForcesAndEnergy();

    //for(CelestialBody &body : system.bodies()) {

    for (unsigned int i = 0; i < system.bodies().size(); i++) {
        CelestialBody& planet = system.m_bodies[i];

        planet.position = planet.position + planet.velocity * m_dt;
        planet.velocity = planet.velocity + planet.force*m_dt/planet.mass;
    }
}
