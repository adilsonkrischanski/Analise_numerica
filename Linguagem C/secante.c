#include <stdio.h>
#include <math.h>


double f(double x){
    //return (-34.14+((9.81*x)/17.78)*(1-(pow(M_E,-(17.78/x)*9.61))));
    return 1000*((M_PI*(7.91-x))/3.0)*(pow((2.72+x*(7.96-2.72)/7.91),2)+pow(7.96,2) + (2.72+x*(7.96-2.72)/7.91)*7.96) - 273.91*((M_PI*7.91)/3.0)*(pow(2.72,2)+pow(7.96,2) + 2.72*7.96);

}

void secante(double x0, double x1, int n){
    double x2;
    for(int i=0; i<n; i++){
        double fx0 = f(x0);
        double fx1 = f(x1);
        if(fx1 == fx0){
            printf("Divisao por 0 na iteracao \n");
        }
        double x2 = (x0 * fx1 - x1 * fx0)/(fx1 - fx0);
        printf("x_%d = %.7f\n", i+2,x2);
        x0 = x1;
        x1 = x2;
    }
}

int main(void){

    double x0 = 0.16;
    double x1 = 6.95;
    int n = 8;

    secante(x0, x1, n);
    return 0;
}