#ifndef SOLARSYSTEM_H
#define SOLARSYSTEM_H

#include "celestialbody.h"
#include <vector>
#include <string>
#include <fstream>
#include "velocityverlet.h"
#include "euler.h"
class SolarSystem
{
public:
    SolarSystem();
    void createCelestialBody(vec3 position, vec3 velocity, double mass);
    void calculateForcesAndEnergy();

    int numberOfBodies() const;
    void setIntegrator(VelocityVerlet *integrator);
    void mercuryAngles(int timestep, std::string angles_filename);
    double totalEnergy() const;
    double potentialEnergy() const;
    double kineticEnergy() const;
    vec3 angularMomentum() const;
    void writePositionsToFile(std::string filename);
    void writeEnergyToFile(std::string energy_filename);
    std::vector<CelestialBody> &bodies();
    std::vector<CelestialBody> m_bodies;
private:
    std::ofstream m_file;
    std::ofstream m_file_angle;
    std::ofstream m_file_energy;
    double m_kineticEnergy;
    double m_potentialEnergy;
    vec3 m_angularMomentum;
    double m_G;
    double c;
    double r_1;
    double r_2;
    double r_now;
    double x_merc;
    double y_merc;
    double x_sun;
    double y_sun;
    double m_angle;
    VelocityVerlet *m_integrator;
};

#endif // SOLARSYSTEM_H
