// program to transform stress:
//
// sigmaX' = sigmaX * cos^2(theta) + sigmaY * sin^2(theta) + 2 * tauXY sin(theta)cos(theta)
// sigmaY' = sigmaX * sin^2(theta) + sigmaY * cos^2(theta) - 2 * tauXY sin(theta)cos(theta)
// tauXY' = (sigmaY-sigmaX) * sin(theta)cos(theta) + tauXY(cos^2(theta) - sin^2(theta))
//
// write a program to take:
// 1: 4 inputs: sigmaX, sigmaY, tauXY, theta and output transformed stresses: sigmaX', sigmaY', tauXY'
// 2: 3  inputs: sigmaX, sigmaY, tauXY and output transformed stresses: sigmaX', sigmaY', tauXY' for every 10 degrees
//
// NOTE: perform the transformation inside a function that cannot be named main
//
// Extend to possibly include all outputs for a Mohr circle, were the theta now provided is a deltaTheta

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void transformStress(const float *stressIN, float theta, float *stressTransformed) {
    float sigmaX = stressIN[0];
    float sigmaY = stressIN[1];
    float tauXY = stressIN[2];

    float thetaRad = theta * M_PI / 180.0; // Convert theta to radians

    float cosTheta = cos(thetaRad);
    float sinTheta = sin(thetaRad);
    float cosTheta2 = cosTheta * cosTheta;
    float sinTheta2 = sinTheta * sinTheta;

    stressTransformed[0] = sigmaX * cosTheta2 + sigmaY * sinTheta2 + 2 * tauXY * sinTheta * cosTheta;
    stressTransformed[1] = sigmaX * sinTheta2 + sigmaY * cosTheta2 - 2 * tauXY * sinTheta * cosTheta;
    stressTransformed[2] = (sigmaY - sigmaX) * sinTheta * cosTheta + tauXY * (cosTheta2 - sinTheta2);
}

int main(int argc, char **argv) {
    if (argc < 4) {
        printf("Usage: appName sigmaX sigmaY tauXY [optional: theta]\n");
        exit(-1);
    }

    float sigmaX = atof(argv[1]);
    float sigmaY = atof(argv[2]);
    float tauXY = atof(argv[3]);

    float stressIN[3];
    stressIN[0] = sigmaX;
    stressIN[1] = sigmaY;
    stressIN[2] = tauXY;

    if (argc == 5) {
        float theta = atof(argv[4]);
        float stressTransformed[3];
        transformStress(stressIN, theta, stressTransformed);
        printf("%.4f, %.4f, %.4f\n", stressTransformed[0], stressTransformed[1], stressTransformed[2]);
    } else {
        for (int i = 0; i < 360; i += 10) {
            float theta = i;
            float stressTransformed[3];
            transformStress(stressIN, theta, stressTransformed);
            printf("%.4f, %.4f, %.4f\n", stressTransformed[0], stressTransformed[1], stressTransformed[2]);
        }
    }

    printf("%.4f, %.4f, %.4f\n", sigmaX, sigmaY, tauXY);
    return 0;
}