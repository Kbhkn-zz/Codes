#include <stdio.h>

char bosluk_sil(char *);

int main(void)
{
   char cumle[250];

   printf("Cumleyi giriniz: ");
   gets(cumle);
   
   bosluk_sil(cumle);
   
   return 0;
}

char bosluk_sil(char *p)
{
	int i=0, j=0;
	char y[250];

	for(i;p[i];i++,j++)
	{
		if(p[i] == ' ')
			i++;
		y[j] = p[i];
	}
	puts(y);
}