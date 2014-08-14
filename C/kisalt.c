#include <stdio.h>
#include <locale.h>

char kisalt(char *);

int main(void) 
{
	setlocale(LC_ALL,"Turkish");

	char cumle[100];

	printf("Cumlenizi giriniz: ");
	gets(cumle);

	printf("Cümleniz  : %s\n",cumle);

	kisalt(cumle);

	return 0;
}

char kisalt(char *p)
{
	printf("Kısa hali : ");

	int i;

	for (i=0; p[i] != '\0'; i++) {
		if (i == 0)
			printf("%c", p[i]);
		if (p[i - 1] == ' ')
			printf("%c", p[i]);
	}
	printf("\n");
}