// Gauss Mehtod && Reverse Substitution
#include <stdio.h>
#include <math.h>
#define ROWS 3
#define COLS 3

void print_matrix(double array[ROWS][COLS]);
void gauss(double E[ROWS][COLS]);
void reverse_substitution(double E[ROWS][COLS]);

double f(double x){
    return(pow(M_E,(5*x))-2);
}

double df(double x){
    return(5*pow(M_E,(5*x)));
}

int main(void){
    double E[ROWS][COLS] = {{-4.891, -1.484, -0.322}, {-1.658, 2.694, 0.331}, {-3.81, -3.666, -2.668}};

    print_matrix(E);

    gauss(E);

    reverse_substitution(E);

}

void print_matrix(double array[ROWS][COLS]){
    for(int i = 0; i < ROWS; i++){
        for(int j = 0; j< COLS; j++){
            printf("%.8f\t",array[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]){
    int i,j,k,m,n;
    double temp, a;

    for( j = 0; j<COLS-2;j++){ // Coluna
        for( i = j; i<ROWS;i++){
            if(E[i][j] != 0){
                if(i != j){
                    // trocar linhas
                    for(k=0;k<COLS;k++){
                        temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                // O pivot (Elemento E[i][j] seja nao nulo)
                for(m = j+1; m<ROWS; m++){
                    a = -E[m][j] / E[j][j];
                    for(n=j; n<COLS; n++){
                        E[m][n] += a *E[j][n];
                    }
                }
                print_matrix(E);printf("\n");
                break;
            }
            else{
                if( i == ROWS -1){
                    printf("Sistema sem solucao\n");
                }
            }
        }
    }
}

void reverse_substitution(double E[ROWS][COLS]){
    double answer[ROWS];

    for(int i=0; i<ROWS; i++){
        int d = ROWS - 1 - i;
        double b = E[d][COLS -1];
        for(int j = d+1; j<COLS -1;j++){
            b -= E[d][j] * answer[j];

        }
        double xd = b/E[d][d];
        answer[d] = xd;
        printf("X_%d = %.16f\n",d,xd);
    }
}