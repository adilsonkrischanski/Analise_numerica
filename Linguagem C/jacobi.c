//jacobi corrigido
#include <stdio.h>
#include <math.h>
#define ROWS 4
#define COLS 4

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n);

int main(void){

    double a[ROWS][COLS] = {{12.17, -3.86, 2.19, 4.73}, {-4.31, 8.95, 2.1, -1.15}, {1.23, -3.17, -5.86, 0.07},{3.9, 3.92, 1.55, -10.76}};
    double b[ROWS] = {0.27, 4.69, -3.81, 0.09};

    double chute[COLS] = {-2.85, 0.55, 1.19, -2.22};

    int n = 16;

    jacobi(a,b,chute,n);

    return 0;
}

void jacobi(double a[ROWS][COLS], double b[COLS], double chute[COLS], int n){
    for(int it = 0; it < n; it++){
        double temp[COLS]; 
        for(int i=0; i<ROWS; i++){
            double xi = b[i];
            for(int j = 0; j<COLS; j++){
                if(i!=j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            temp[i] = xi;
        }
        printf("X^(%d) ->", it +1);
        for(int k=0;k<COLS; k++){
            chute[k] = temp[k];
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
        }
    }
