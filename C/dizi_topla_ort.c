#include <stdio.h>

int dizi_topla_ort(int *);

int main(void)
{
	int dizi[]={1,2,3,4,5,6,7,8,8,10,11};
	
	dizi_topla_ort(dizi);
	
	return 0;
}

int dizi_topla_ort(int *p)
{
	int toplam=0, i=0;
	float ortalama=0;

	for(i;p[i];i++)
		toplam+=p[i];
	
	ortalama = (float)toplam/i;
	
	printf("Dizi icerigi toplamı: %d\n",toplam);
	printf("Dizinin ortalamasi: %f\n",ortalama);
	
	return (toplam);
}