#include <iostream>
#include <iomanip>
#include <cmath>
#include "armadillo"
#include "time.h"
#include <chrono>
#include <fstream>

using namespace arma;
using namespace std;

void output(vec x , vec y, vec v_x, vec v_y, vec r, vec t, int n)
{
    ofstream ofile;
    ofile.open("test.txt");
    ofile<<setw(15)<<" n "<<endl;
    ofile<<setw(15) << setprecision(8) << n<<endl;
    ofile <<"x"<<endl;
    for (int i=0;i<n;i++){
        ofile << x(i)<<endl;
    }
    ofile <<"t"<<endl;
    for (int i=0;i<n;i++){
        ofile << t(i)<<endl;
    }
    ofile<<endl;
    ofile.close();
}

void sunearth_euler(double x_start, double y_start, int n)
{
    vec x(n);
    vec y(n);
    vec v_x(n);
    vec v_y(n);
    vec r(n);
    vec t(n);

    // initial conditions:
    x(0) = x_start;
    y(0) = y_start;
    r(0) = 1;
    v_x(0) = 0;
    v_y(0) = 2*M_PI;
    t(0) = 0;

    double dt = 0.001;

    for (int i=0;i<n-1;i++){
        double a_x = -4*M_PI*M_PI*x(i)/(r(i)*r(i)*r(i));
        double a_y = -4*M_PI*M_PI*y(i)/(r(i)*r(i)*r(i));
        v_x(i+1) = v_x(i) + dt*a_x;
        v_y(i+1) = v_y(i) + dt*a_y;
        x(i+1) = x(i) + dt*v_x(i);
        y(i+1) = y(i) + dt*v_y(i);
        r(i+1) = sqrt(x(i+1)*x(i+1) + y(i+1)*y(i+1));
        t(i+1) = t(i) + dt;

    }

    output(x,y,v_x,v_y,r,t,n);

}

void sunearth_verlet(double x_start, double y_start, int n)
{
    vec x(n);
    vec y(n);
    vec v_x(n);
    vec v_y(n);
    vec a_x(n);
    vec a_y(n);
    vec r(n);
    vec t(n);

    // initial conditions:
    x(0) = x_start;
    y(0) = y_start;
    r(0) = 1;
    v_x(0) = 0;
    v_y(0) = 2*M_PI;
    a_x(0) = -4*M_PI*M_PI*x(0)/(r(0)*r(0)*r(0));
    a_y(0) = -4*M_PI*M_PI*y(0)/(r(0)*r(0)*r(0));
    t(0) = 0;

    double dt = 0.001;

    for (int i=0;i<n-1;i++){
        x(i+1) = x(i) + dt*v_x(i) + (dt*dt/2)*a_x(i);
        y(i+1) = y(i) + dt*v_y(i) + (dt*dt/2)*a_y(i);
        r(i+1) = sqrt(x(i+1)*x(i+1) + y(i+1)*y(i+1));
        a_x(i+1) = -4*M_PI*M_PI*x(i+1)/(r(i+1)*r(i+1)*r(i+1));
        a_y(i+1) = -4*M_PI*M_PI*y(i+1)/(r(i+1)*r(i+1)*r(i+1));
        v_x(i+1) = v_x(i) + (dt/2)*(a_x(i+1) + a_x(i));
        v_y(i+1) = v_y(i) + (dt/2)*(a_y(i+1) + a_y(i));
        t(i+1) = t(i) + dt;

    }

    output(x,y,v_x,v_y,r,t,n);

}


