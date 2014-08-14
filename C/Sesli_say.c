#include <stdio.h>
#include <string.h>

int SesliSay(char *);

int main()
{
    char cumle[100];

    printf("(TR Karakter kullanmadan)Cumleyi giriniz: ");
    gets(cumle);
    printf("Cumledeki sesli harf sayisi: %d\n",SesliSay(cumle));
    return 0;
}

int SesliSay(char *p)
{
    int uzunluk = strlen(p), n = 0, j = 0, sayac = 0;
    char unluler[16] = {'a', 'e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    for(n = 0; n < uzunluk; n++)
    {
        for(j = 0; j < 16; j++)
        {
         if(p[n] == unluler[j])
             sayac++;
        }
    }
    return sayac;
}

