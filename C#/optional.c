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

    printf("\n");

    /* adaugare elemente in vector la sfarsit */

    scanf("%d",&a[n]);
    n++;

    /* adaugare elemente in vector la inceput */

    for(i=n; i>=1; i--)
    {
        a[i]=a[i-1];
    }
    n++;
    scanf("%d", &a[0]);

    /* stergere elemente in vector de la sfarsit */
    
    scanf("%d",&a[n]);
    n--;
    
    for(i=0; i<n; i++)
    {
        printf("%d", a[i]);
    }
}



