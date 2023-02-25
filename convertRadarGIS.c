#include <stdio.h>
#include <math.h>

//I used chatGPT to get the formulas for conversion. The code is implemented on my own.
//I'm also assuming units of the parameters are in degrees and kilometers.

const double pi = 3.14159265358979323846;
const double earth_radius = 6371.0;

int GIS2Radar(double *range, double *bearing, double glonInit, double glatInit, double glonFinal, double glatFinal){
    // Convert latitudes and longitudes to radians
    double glonInit_rad = glonInit * pi / 180.0;
    double glatInit_rad = glatInit * pi / 180.0;
    double glonFinal_rad = glonFinal * pi / 180.0;
    double glatFinal_rad = glatFinal * pi / 180.0;

    //get distance between longitudes
    double dlon = glonFinal_rad - glonInit_rad;

    //calculate x and y to get radar bearing
    double y = sin(dlon) * cos(glatFinal_rad);
    double x = (cos(glatInit_rad) * sin(glatFinal_rad)) - (sin(glatInit_rad) * cos(glatFinal_rad) * cos(dlon));

    *bearing = atan2(y, x) * 180.0 / pi;
    if (*bearing < 0) {
        *bearing += 360.0;
    }

    //get distance
    *range = earth_radius * acos(sin(glatInit_rad) * sin(glatFinal_rad) + cos(glatInit_rad) * cos(glatFinal_rad) * cos(dlon));

    return 0;
}

int RtoG (double range, double bearing, double  glonInit, double glatInit, double *glonFinal, double *glatFinal){
    // Convert bearing, lat and lon to radians
    double bearing_rad = bearing * pi / 180.0;
    double glonInit_rad = glonInit * pi / 180.0;
    double glatInit_rad = glatInit * pi / 180.0;

    double glatFinal_rad = asin(sin(glatInit_rad) * cos(range / earth_radius) + cos(glatInit_rad) * sin(range / earth_radius) * cos(bearing_rad));
    double glonFinal_rad = glonInit_rad + atan2(sin(bearing_rad) * sin(range / earth_radius) * cos(glatInit_rad), cos(range / earth_radius) - sin(glatInit_rad) * sin(glatFinal_rad));

    *glonFinal = glonFinal_rad * 180 / pi;
    *glatFinal = glatFinal_rad * 180 / pi;

    return 0;
} 

int main() {
    double range, bearing;
    GIS2Radar(&range, &bearing, -75.0, 37.0, -66.0, 18.0);
    printf("Radar coords for Initial: Wallops Islands and Final: Puerto Rico are (bearing = %lf, range = %lf)\n", range, bearing);
    return 0;
}