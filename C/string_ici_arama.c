#include <stdio.h>
#include <locale.h>

int String_ara(char *, char );

int main(void)
{
	setlocale(LC_ALL,"Turkish");

	char harf, cumle[100];

	printf("Cümleyi giriniz: ");
	gets(cumle);
	printf("Aradığınız harfi giriniz ");
	scanf("%c", &harf);

	printf("Aradığınız harf kelime içinde ");
	if (String_ara(cumle, harf) == 1)
		printf("vardır.\n");
	else
		printf("yoktur.\n");

	return 0;
}

int String_ara(char *p, char k)
{
	int i, kontrol = 0;
	
	for(i=0;p[i] != '\0';i++)
	{
		if (p[i] == k)
			kontrol = 1;
	}
	
	return kontrol;
}