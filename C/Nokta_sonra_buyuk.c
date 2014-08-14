#include <stdio.h>
#include <locale.h>

char buyuk_yap(char *);

int main(void)
{
   setlocale(LC_ALL,"Turkish");
   
   char cumle[250];
   
   printf("Cümlenizi giriniz: ");
   gets(cumle);

   buyuk_yap(cumle);
   
   puts(cumle);

   return 0;
}

char buyuk_yap(char *p)
{
   int i = 0, n = 0;

   for(i;p[i];i++)
   {
      if(p[i] == '.')
         p[i+1] = toupper(p[i+1]);
   }
   return(*p);
}