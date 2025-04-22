#include<stdio.h>
int main() {
    int i,j,k, alpha=10, beta = 20;
    // int arr[500][500], brr[500];
    int tmp[500][500], A[500][500], B[500][500], C[500][500], D[500][500];

    for (i = 0; i < 100; i++)
      for (j = 0; j < 150; j++){
        tmp[i][j] = 0;
          for (k = 0; k < 200; ++k)
            tmp[i][j] += alpha * A[i][k] * B[k][j];
        }
    for (i = 0; i < 150; i++)
      for (j = 0; j < 200; j++){
        D[i][j] *= beta;
        for (k = 0; k < 250; ++k)
          D[i][j] += tmp[i][k] * C[k][j];
        }
    return 0;
}