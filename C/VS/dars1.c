#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int yigindi(int a){
    if (a / 10 == 0){
        return 1;
    }
    return 1 + yigindi(a / 10);
}

int main()
{
    int son, daraja, a, b;
    scanf("%d %d", &son, &daraja);
    a = pow(son, daraja);

    yigindi(a);

    for (int i = 1; a / 10 != 0; i++)
    {
        b += a % 10;
        a /= 10;
    }
    printf("%d", b);
     
}