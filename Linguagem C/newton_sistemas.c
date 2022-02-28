#include <stdio.h>

double f(double x){
    return x*x -2;
}

double df(double x){
    return 2*x;
}

void newton(double (*f) (double),double (*df)(double), double x0, int n){
     double x1;
    for(int i=0;i<n;i++){
        x1 = x0- (f(x0)/df(x0));
        printf("x_%i = %.16f\n",i+1,x1);
        x0=x1;
    }
}

int main(void){
    double x0=1.0;
    int n =5;
    newton(f,df, x0,n);
}