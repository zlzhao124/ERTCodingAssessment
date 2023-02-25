#include <stdio.h>
#include "iri2016.h"

#define NUM_ALT 101
#define ALT_MIN 0.0
#define ALT_MAX 1000.0

int main(void) {
    double alt;
    double lat = 40.0;
    double lon = -105.0;
    double f107 = 150.0;
    double f107a = 150.0;
    double ap[IRI2016_NUM_AP];
    double output[IRI2016_NUM_OUTPUTS];

    FILE *fp;

    for (int i = 0; i < IRI2016_NUM_AP; i++) {
        ap[i] = 4.0;
    }
    
    fp = fopen("edp.dat", "w");
    if (fp == NULL) {
        printf("error opening file\n");
        return 1;
    }
    
    for (int j = 0; j < NUM_ALT; j++) {
        alt = ALT_MIN + j * (ALT_MAX - ALT_MIN) / (NUM_ALT - 1);
        
        if (iri2016(alt, lat, lon, f107, f107a, ap, output) != 0) {
            printf("iri2016 error\n");
            fclose(fp);
            return 1;
        }
        
        fprintf(fp, "%g %g\n", output[IRI2016_ELEC_DENS], alt);
    }
    return 0;
}
   
