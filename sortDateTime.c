#include <stdio.h>

#define MAX_ROWS 500

//made a struct of data to fill
struct data {
    char date[11];
    char datenum[6];
    char time[9];
    int c_score;
    float foF2;
    float foF1;
    float foE;
    float foEs;
    float hEs;
    float hmF2;
    float hmF1;
    float hmE;
    float B0;
    float B1;
};

int main(void) {
    //getting ready to scan/parse our file
    FILE *fp;
    char buffer[120];
    int row = 0;
    struct data table[MAX_ROWS];

    //try to open file
    fp = fopen("AU930_ROAM.TXT", "r");

    //if failed to open, return error
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }

    //call fgets and ignore the header line
    fgets(buffer, sizeof(buffer), fp);

    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        //scan buffer and insert elements of each row into proper table
        sscanf(buffer, "%10s %5s %8s %d %f %f %f %f %f %f %f %f %f %f",
               table[row].date, table[row].datenum, table[row].time, &table[row].c_score,
               &table[row].foF2, &table[row].foF1, &table[row].foE, &table[row].foEs,
               &table[row].hEs, &table[row].hmF2, &table[row].hmF1, &table[row].hmE,
               &table[row].B0, &table[row].B1);

        row++;
    }

    fclose(fp);

    //print the parsed data (debugging)
    for (int i = 0; i < row; i++) {
        printf("%s %s %s %d %f %f %f %f %f %f %f %f %f %f\n",
               table[i].date, table[i].datenum, table[i].time, table[i].c_score,
               table[i].foF2, table[i].foF1, table[i].foE, table[i].foEs,
               table[i].hEs, table[i].hmF2, table[i].hmF1, table[i].hmE,
               table[i].B0, table[i].B1);
    }

    //stopped here because I couldn't find a good fix for the "---" values in time, switched to programming this in Python

    return 0;
}

