#include <studio.h>

int n, i, a[100];

void main(){
    scanf("%d", &n);

    for(i=0; i<=n-1; i++)
    {
        scanf("%d", &a[i]);
    }

    for(i=0; i<n; i++)
    {
        printf("%d", a[i]);
    }
}



