#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>

void buu(char * );

int main()
{
	char kelime[20];
	setlocale(LC_ALL,"Turkish");
	printf("Bir kelime girin: ");
	gets(kelime);
	buu(kelime);
	return 0;
}

void buu(char *b)
{
	int i=0,k=0;

	switch(*b)
	{
		case 'a' : k++; break;
		case '�' : k++; break;
		case 'o' : k++; break;
		case 'u' : k++; break;
		case 'e' : i++; break;
		case 'i' : i++; break;
		case '�' : i++; break;
		case '�' : i++; break;
		case 'A' : k++; break;
		case 'I' : k++; break;
		case 'O' : k++; break;
		case 'U' : k++; break;
		case 'E' : i++; break;
		case '�' : i++; break;
		case '�' : i++; break;
		case '�' : i++; break;
		default  : break;
	}
	if ((k != 0 && i != 0) || (k == 0 && i == 0))
		printf("Kelime BUU uyumuna uyar.\n");
	else
		printf("Kelime BUU uyumuna uymaz.\n");
}