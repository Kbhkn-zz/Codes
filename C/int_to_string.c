#include <stdio.h>

char int_to_string(int *);

int main(void)
{
	int dizi[]={1,2,3,4,5};
	
	int_to_string(dizi);
	
	return 0;
}

char int_to_string(int *p)
{	
	char dizi[100];
	int j,i;
	
	for(j=0;p[j];j++){}//Dizinin uzunluğu hesaplandı.
	for(i=0;i<(j-1);i++)
		dizi[i]= '0' + p[i];//Her elemanı bellekte string yaparak diziye kopyaladık.
	
	dizi[i] = '\0';//Stringlerin sonunda '\0' karakteri vardır.
	
	printf("Stringe donusmus dizi sirasiyla: ");
	printf("%s\n",dizi);
	
	return *dizi;
}