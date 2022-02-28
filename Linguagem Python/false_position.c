#include <stdio.h>
#include <math.h>

void fpos(double (*f) (double),double a, double b, int n ){
    double fa = f(a);
    double fb = f(b);

    if(fa*fb >=0){
        printf("nao sei se dizer se f possui uma raiz no intervalo [%f][%f]",a,b);
        return;
    }
    else{
        for (int i=0;i<n;i++){
            double x = (a*fb-b*fa) / (fb-fa);
            printf("x_%d=%.7f\n",i+1,x);
            double fx = f(x);

            if (fx ==0){
                printf("A raiz procurada e: x= %.16f",x);
                return;
            }
            else{
                if(fa*fx <0){
                    b=x;
                    fb= fx;
                }
                else{
                    a=x;
                    fa=fx;
                }} 
        }
    }
}




double f(double x){
    //return (-35.6+((9.81*x)/22.39)*(1-(pow(M_E,-(22.39/x)*9.36)))); //function;
    return 1000*((M_PI*(7.91-x))/3.0)*(pow((2.72+x*(7.96-2.72)/7.91),2)+pow(7.96,2) + (2.72+x*(7.96-2.72)/7.91)*7.96) - 273.91*((M_PI*7.91)/3.0)*(pow(2.72,2)+pow(7.96,2) + 2.72*7.96);
;
}

int main(void){

    double a =  0.0;
    double b = 7.91;
    int n =11;

    fpos(f,a,b,n);

    return 0;
}