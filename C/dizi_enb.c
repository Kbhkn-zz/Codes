#include <stdio.h>

int enbuyuk(int *);

int main(void)
{
    int dizi[] = {3,6,123,5,7,87,54};

    printf("Dizinin enbuyuk elemani: %d\n",enbuyuk(dizi));
    
    return 0;
}

int enbuyuk(int *p)
{
    int i=0, enb = p[0];

    for(i;p[i];i++)
    {
        if (p[i]>enb)
            enb = p[i];
    }
    return enb;
}