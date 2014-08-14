#include <stdio.h>
#include <string.h>
#include <locale.h>

char CharDegistir(char *, char , char );

int main(void)
{
    setlocale(LC_ALL,"Turkish");
    char cumle[250], aranan, yenideger;

    printf("%s\n", "Cümleyi giriniz: ");
    gets(cumle);
	
    printf("Once aranan sonra yenideğer harfini giriniz(ornek a-x): ");
    scanf("%c-%c",&aranan, &yenideger);

    CharDegistir(cumle, aranan, yenideger);
	
    printf("Cumlenin son hali: %s\n",cumle);
	
    return 0;
}

char CharDegistir(char *p, char ara, char degistir)
{
    int uzunluk = strlen(p) ,n; 
    
    for(n=0;n<uzunluk;n++)
    {
        if(p[n] == ara)
        p[n] = degistir;
    }
    return *p;
}