#include<stdio.h>
void main()
{
    int a[10],i;
    printf("Enter 10 numbers:");
    for(i=0;i<10;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("The numbers are:");
    for(i=0;i<10;i++)
    {
        printf("%d ",a[i]);
    }
}