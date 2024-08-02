#include <stdio.h>
#include <stdlib.h>
#include <math.h>    // need this for the constant pi = M_PI

#include "stresstransform.h"


int main(int argc, char **argv) {

	// get dth from the first argument.  This is given in degrees!
	  
	// might be smart to set a default value, just in case the user
	// forgets when calling this  program;)

    double dth = 10; // default value
    if (argc > 1) {
        dth = strtod(argv[1], NULL);
    }

	// set the initial stress state
	STRESS S0;

	S0.sigx = 12.0;
	S0.sigy = -5.5;
	S0.tau  =  3.5;
    S0.theta = 0;
	S0.next =  0;

	
	STRESS *results = &S0;

	// MISSING CODE
    for (float theat = dth; theat <=180; theat += dth) {
        STRESS *newStress = (STRESS *)malloc(sizeof(STRESS));
        StressTransform(S0, newStress, theat);
        newStress->theta = theat;
        newStress->next = results;
        results = newStress;
    }

    STRESS *current = results;

    // Open CSV file for writing
    FILE *file = fopen("list.csv", "w");
    if (file == NULL) {
        perror("Unable to open file");
        return 1;
    }

    // Write the header row
    fprintf(file, "theta, sigx, sigy, tau\n");

    // Write the stress values to the CSV file
    // and free the allocated memory
	while (current != NULL) {
	  fprintf(file, "%f, %f, %f, %f\n", current->theta, current->sigx, current->sigy, current->tau);
      STRESS *temp = current;
      current = current->next;
      if (temp != &S0){ // Do not free the initial stress state
          free(temp);
      }
	}
    // Close the file
    fclose(file);

    return 0;
    }


