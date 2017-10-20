#ifndef VELOCITYVERLET_H
#define VELOCITYVERLET_H

#include "vec3.h"

class VelocityVerlet
{
public:
    double m_dt;
    VelocityVerlet(double dt);
    void integrateOneStep(class SolarSystem &system);
    vec3 r_rel;
};

#endif // VELOCITYVERLET_H
