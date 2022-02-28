// Fixed Point
#include <stdio.h>

double ex1(double x);
double ex2(double x);
void fixed_point(double (*f)(double),double x0, int n);

int main(void){

    double x0;
    int n;

    double ex1(double x){
        return x / 2.0 + 1.0 / x;
    }  

    double ex2(double x){
        return (x*x -1.0)-3.0;
    }

    x0 = -1.678;
    n = 10;

    printf("Funcao 1\n");
    fixed_point(ex1,x0,n);
    printf("Funcao 2\n");
    fixed_point(ex2,x0, n);
    return 0;
}

void fixed_point(double (*f)(double),double x0, int n){
    for(int i=0; i<n;i++){
        double xn = f(x0);
        printf("X_%d - %.16f\n",i,xn);
        x0 = xn;

    }
}