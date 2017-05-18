#include<stdio.h>

void main()
{
    double dnum;
    float fnum;
    char *buf;
    int i;
    int chose;
    while(1)
    {
        printf("Input 1 or 2 or 3 chose float or double or exit:");
        scanf("%d",&chose);
        if(chose==1)
        {
            printf("Input a float:");
            scanf("%f",&fnum);
            buf = ((char*)&fnum);
            printf("%f in memory is 0x",fnum);    
            for(i=0;i<4;i++)
            {
                printf("%2x",(unsigned char)buf[i]);
            }
            printf("\n");
        }else if(chose==2)
        {
            printf("Input a double:");
            scanf("%lf",&dnum);
            buf = ((char*)&dnum);
            printf("%lf in memory is 0x",dnum);    
            for(i=0;i<8;i++)
            {
                printf("%2x",(unsigned char)buf[i]);
            }
            printf("\n");
        }else if(chose==3)
        {
            break;
        }
        else
        {
            printf("Input Error Chose!\n");
        }
    }    
    
}