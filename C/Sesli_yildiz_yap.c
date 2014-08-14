#include <stdio.h>
#include <string.h>

char SesliDegistir(char *);

int main(void)
{
    char cumle[250];

    printf("Turkce karakter kullanmadan cumleyi giriniz: ");
    gets(cumle);
    
    SesliDegistir(cumle);
    
    printf("Cumlenin son hali: %s\n",cumle);
    return 0;
}

char SesliDegistir(char *p)
{
    int uzunluk = strlen(p), n = 0;
    char c;

    for(n=0;n<uzunluk;n++)
    {
        switch(p[n])
		{
	    case 'a' : p[n] = '*'; break;
	    case 'e' : p[n] = '*'; break;
	    case 'i' : p[n] = '*'; break;
	    case 'o' : p[n] = '*'; break;
	    case 'u' : p[n] = '*'; break;
	    case 'A' : p[n] = '*'; break;
	    case 'E' : p[n] = '*'; break;
	    case 'I' : p[n] = '*'; break;
	    case 'O' : p[n] = '*'; break;
	    case 'U' : p[n] = '*'; break;
	    default : break;
		}
    }
    return *p;
}