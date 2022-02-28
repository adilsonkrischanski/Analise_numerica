//seidel corrigido
#include <stdio.h>
#include <math.h>
#define ROWS 4
#define COLS 4

void seidel(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n);

int main(void){

    double a[ROWS][COLS] = {{-10.53227, 3.45783, -3.21381, -1.87573},{1.34861, -7.14457, 3.25359, -0.55747},{3.10466, 4.18969, 12.08501, 2.80577},{4.32387, -0.71983, 4.01609, -11.04468}};
    double b[ROWS] = {-4.2223, -1.58599, 2.85266, -0.24103};

    double chute[COLS] = {1.20418, 0.09681, -4.52342, 0.07922};

    int n = 18;

    seidel(a,b,chute,n);

    return 0;
}

void seidel(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    for(int it = 0; it < n; it++){
        for(int i=0; i<ROWS; i++){
            double xi = b[i];
            for(int j = 0; j<COLS; j++){
                if(i!=j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            chute[i] = xi;
        }
        printf("X^(%d) ->", it +1);
        for(int k=0;k<COLS; k++){
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
        
    }
}
