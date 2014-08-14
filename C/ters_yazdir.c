#include <stdio.h>
#include <string.h>

void ters_yazdir(char* );

int main(void)
{
	char dizi[100];

	printf("Bir cumle giriniz: ");
	gets(dizi);

	ters_yazdir(dizi);
	printf("\n");

	return 0;
}

void ters_yazdir(char* string)
{
	int i = 0;
	int boyut = strlen(string);

	for(boyut; boyut > 0; boyut--)
		printf("%c", string[boyut - 1]);
}