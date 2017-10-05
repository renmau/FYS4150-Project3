#ifndef SOLARSYSTEM_H
#define SOLARSYSTEM_H

#include "celestialbody.h"
#include <vector>
#include <string>
#include <fstream>

class SolarSystem
{
public:
    SolarSystem();
    void createCelestialBody(vec3 position, vec3 velocity, double mass);
    void calculateForcesAndEnergy();
    int numberOfBodies() const;

    double totalEnergy() const;
    double potentialEnergy() const;
    double kineticEnergy() const;
    void writeToFile(std::string filename);
    std::vector<CelestialBody> &bodies();

    std::vector<CelestialBody> m_bodies;
private:
    std::ofstream m_file;
    double m_kineticEnergy;
    double m_potentialEnergy;
    double m_G;
};

#endif // SOLARSYSTEM_H