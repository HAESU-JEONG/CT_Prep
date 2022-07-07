#include <stdio.h> //Header file

int main(void) { // miain function
    int n; // number of arguments
    int m; // number of arguments

    scanf("%d %d", &n, &m); //receive value
    
    for(int i = 0; i < m; i++) //repeat as many as i
    {
        for(int k = 0; k < n; k++) //repeat as many as k
        {
            printf("*"); //print "*"
        }
        printf("\n"); //enter
    }
    
    return 0; //return value
}