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
    int uzunluk = strlen(p), i, j;
    char c, unluler[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    for(i = 0; i < uzunluk; i++)
    {
        for(j = 0; j < 10; j++)
        {
           if(p[i] == unluler[j])
               p[i] = '*';
        }
    }
    return *p;
}