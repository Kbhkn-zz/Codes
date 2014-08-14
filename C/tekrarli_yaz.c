#include <stdio.h>

void tekrar_yaz(char *, int );

int main(void)
{

	char metin[100];
	int i;

	printf("Cumleyi giriniz: ");
	gets(metin);

	printf("Tekrar sayisini giriniz: ");
	scanf("%d",&i);

	tekrar_yaz(metin, i);

	return 0;
}

void tekrar_yaz(char *metin, int n)
{
	int tekrar = 0, i = 0;

	for(i; metin[i] != '\0'; i++)
	{
		while (tekrar++ < n)
			printf("%c", metin[i]);
		tekrar = 0;
	}
	printf("\n");
}