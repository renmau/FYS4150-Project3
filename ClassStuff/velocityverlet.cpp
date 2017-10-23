#include "velocityverlet.h"
#include "solarsystem.h"

VelocityVerlet::VelocityVerlet(double dt) :
    m_dt(dt)
{

}

void VelocityVerlet::integrateOneStep(SolarSystem &system)
{
    r_rel.zeros();
    r_rel += system.m_bodies[1].position - system.m_bodies[0].position;
    for (unsigned int i = 0; i < system.bodies().size();i++){
        CelestialBody& planet = system.m_bodies[i];

        planet.position  = planet.position + m_dt*planet.velocity + m_dt*m_dt/2*planet.force/planet.mass;
        planet.velocity = planet.velocity + m_dt/2*planet.force/planet.mass;


    }
    system.calculateForcesAndEnergy();
    for (unsigned int i = 0; i < system.bodies().size();i++){
        CelestialBody& planet = system.m_bodies[i];
        planet.velocity = planet.velocity + m_dt/2*planet.force/planet.mass;
    }
}
