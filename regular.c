#include <stdio.h>

struct data{
    short a;
    char b;
    int c;
}x;


int main()
{
    printf("%d", sizeof(x));
    return 0;
}

