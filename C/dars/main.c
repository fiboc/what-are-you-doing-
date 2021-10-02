#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int xonalar(int num){
    return num / 10 == 0 ? 1 : 1 + xonalar(num / 10);
}

int daraja_anq(int num, int n){
    return n == 0 ? 1 : num * daraja_anq(num, n-1);
}

int main()
{
    int son, n, a, b, c;

    scanf("%d %d", &son, &n);

    a = daraja_anq(son, n);

    for (int i = 1; a / 10 != 0; i++){
        b += a % 10;
        a /= 10;
    }

}
