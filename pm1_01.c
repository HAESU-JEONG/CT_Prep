#include <stdio.h>

int main(void) {
    int n;
    int m;
    scanf("%d %d", &n, &m);
    
    for(int i = 0; i < m; i++)
    {
        for(int k = 0; k < n; k++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}