#include <stdio.h>
#include <stdlib.h>

#include "stresstransform.h"

int main(int argc, char **argv) {

	STRESS S0 = {strtod(argv[1],NULL), strtod(argv[2],NULL), strtod(argv[3],NULL)};
	STRESS Sp = {0.0, 0.0, 0.0};

    if (argc == 5) {
        StressTransform(S0, &Sp, strtod(argv[4],NULL));
        printf("sigx' = %12.6f\nsigy' = %12.6f\ntau'  = %12.6f\n\n", Sp.sigx, Sp.sigy, Sp.tau);
    }
    else {
        for (int i = 0; i < 360; i += 45) {
            StressTransform(S0, &Sp, i);
            printf("theta = %d\nsigx' = %12.6f\nsigy' = %12.6f\ntau'  = %12.6f\n\n", i, Sp.sigx, Sp.sigy, Sp.tau);
        }
    }
    return 0;
}


