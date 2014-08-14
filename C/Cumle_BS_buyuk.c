#include <stdio.h>

char BS_Buyuk(char *);

int main()
{
    char cumle[500];

    printf("Cümlenizi giriniz: ");
    gets(cumle);
    
    BS_Buyuk(cumle);

    return 0;
}

char BS_Buyuk(char *p)
{
    int i;
    
    for(i=0;i<strlen(p);i++)
    {
        if(i==0 && p[i]>='a' && p[i]<='z')
            p[i]=toupper(p[i]);
        if(p[i+1]==' ' && p[i]>='a' && p[i]<='z' || p[i+1]==NULL )
            p[i]=toupper(p[i]);    
        if(p[i-1]==' ' && p[i]>'a' && p[i]<='z' )
            p[i]=toupper(p[i]);
    }
    
    printf("Cümlenin son hali:\n");
    
    puts(p);
}