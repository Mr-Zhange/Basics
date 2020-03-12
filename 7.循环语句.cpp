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
	
	return 0;
}