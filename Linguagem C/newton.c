#include <stdio.h>
#include <math.h>

double df(double x){
    //return 2*x://derivada da função
    //return 3141.59265*x*x-17090.26403*x;
    return 42000*x + 71*pow(x,(3/2.0))-902.52;

    
}

double f(double x){
    return (2*71*pow(x,(5/2.0)))/(5.0)+(1/2.0)*42000*x*x - 92*9.81*x -92*9.81*0.55;

}

void newton(double x0, int n){
    double x1;
    for(int i = 0; i< n; i++){
        x1 = x0 - f(x0)/df(x0);
        printf("x_%d = %.7f\n",i+1, x1);
        x0=x1;
    }
}

int main(void){
   
    double x0 = 1.17;
    int n = 6;
    newton(x0,n);

    return 0;
}

