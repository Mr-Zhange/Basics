/**
 * 7、循环语句
 *
 * for 循环，格式
 * 		for(int i = 0; i <= number; ++i)
 * 		{
 * 			代码快
 * 		}
 *
 *		执行顺序：
 *		1、int i = 0;
 *		2、i <= number;		//如果判断条件为真，则跳出循环，结束
 *		3、代码快
 *		4、++i
 *
 *
 * while 与 do...while
 * 	while 格式
 *
 * 	while(判断条件)			//条件成立，则执行代码段，条件不成立，结束循环
 * 	{
 * 		代码段
 * 	}
 *
 * 	do...while 格式
 *
 * 	do 						//不管条件是否成立，都先执行一次代码段，之后在判断条件，
 * 	{						//成立则继续执行代码段，不成立则结束循环
 * 		代码段
 * 	}while(判断条件)
 * 
 */

# include <stdio.h>

int main()
{
	for (int i = 1; i <= 100; ++i)
	{
		printf("I = %d\n", i);
	}

	printf("For循环结束！\n");

	// 循环嵌套,99乘法表
	for (int i = 1; i <= 9; ++i) {

	    for (int j = 1; j <= i; ++j) {

	        printf("%d * %d = %d \t",i,j,(i*j));

	    }

	    printf("\n");
	    
	}

    int i = 1;

    while (i <= 10)
    {
        printf("%d\n",i);
        ++i;
    }

    int j = 1;

    do 
    {
        printf("%d\n", j);
        ++j;
    } while (j <= 10);
	
	return 0;
}