#include <stdio.h>
#define n 9

int main(void)
{

	int a[n][n];
	int i,j;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
			a[i][j]=0;
	}
	int kat = 0;
	int fark = 0;
	for(i = n/2 ;i>=0;i--)
	{
		a[i][i] = n*n-fark;
		kat++;
		fark = fark + kat*8;
			for(j = i+1;j<n-i;j++)
				a[i][j]=a[i][j-1]+1;
	}
	kat = 2;
	fark = 0;
	for(i = n/2 ;i>0;i--)
	{
		fark = fark +kat;
		a[n-i][i-1] = n*n-fark;
		kat = kat+8;
		for(j = i;j<n-i+1;j++)
			a[n-i][j]=a[n-i][j-1]-1;
	}
    for(i = n/2 ;i>0;i--)
    {
		for(j = i;j<n-i+1;j++)
			a[j][n-i]=a[j-1][n-i]+1;
	}
	kat = 2;
	fark = 0;
	for(i = 0 ;i<n/2;i++)
	{
		for(j = i+2;j<n-i;j++)
			a[n-j ][i]=a[n-j+1][i]+1;
	}
	for(i=0;i<n;i++){
		for(j=0;j<n;j++)
			printf("%d\t",a[i][j]);
		printf("\n");
	}
	return 0;
}