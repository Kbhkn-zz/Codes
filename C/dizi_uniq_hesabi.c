#include <stdio.h>
#include <locale.h>

int uniq(int *);

int main(void)
{
	setlocale(LC_ALL,"Turkish");
	
	int i,dizi[]={2,3,1,3,6,2,9,11,4,6,5,7,1,9,8,10,11,2,2,12,13,14,15};
	uniq(dizi);

	printf("Dizinin güncellenmiş hali: \n");
	
	for(i=0;dizi[i];i++)
		printf("%d ",dizi[i]);
	printf("\n");
	return 0;
}

int uniq(int *p)
{
	int i,j,k,n=23;//n dizinin uzunluğudur ve girilmek zorundadır.
	
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;)
		{
			if(p[j]==p[i])
			{
				for(k=j;k<n;k++)
					p[k]=p[k+1];
				n--;
			}
			else
				j++;
		}
	}
	return *p;
}