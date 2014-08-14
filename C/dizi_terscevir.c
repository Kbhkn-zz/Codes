#include <stdio.h>
 
int dizi_cevir(int *);

int main()
{
  int i,dizi[] = {1,2,3,4,5,6,7,8,9,10};
  
  printf("Normal dizi:  ");
  
  for(i=0;dizi[i];i++)
    printf("%d ",dizi[i]);

  printf("\nReverse dizi: ");
  
  dizi_cevir(dizi);
}

int dizi_cevir(int *p)
{
  
  int n, c, d, b[250];
  
  for(n=0;p[n];n++){}//Dizi uzunluğunu hesaplattık.
  for (c = n-1, d = 0; 0 <= c; c--, d++)
    b[d] = p[c];
  for (c = 0; c < n; c++)
    p[c] = b[c];
  for (c = 0; c < n; c++)
    printf("%d ", p[c]);
  
  printf("\n");
}