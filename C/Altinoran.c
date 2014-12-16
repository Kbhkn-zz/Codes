#include <stdio.h>

int fibonacci(int a)
{
  if (a == 0 || a == 1)
    return a;
  else
    return fibonacci(a-1) + fibonacci(a-2);
}

int main(void)
{
  int x = 1;
  double s1 = fibonacci(x), s2 = fibonacci(x+1), sonuc = s2/s1;
  while (sonuc != 1.618033988749895){
    s1 = fibonacci(x);
    s2 = fibonacci(x+1);
    sonuc = s2/s1;
    printf("Fibonacci %d, Altın oranı: %5.25f\n",x,sonuc);
    x++;
  }
  printf("Altın orana en yakın %d.sırada yaklaşıldı.\n",x);
}

/*real  0m5.541s
  user  0m5.542s
*/
