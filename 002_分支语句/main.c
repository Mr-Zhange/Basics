#include <stdio.h>

/*
	分支语句
		if
		switch
	循环语句
		do while
		while
		for
	转向语句
		break
		goto
		continue
		return
*/

/**
 * 分支语句
 *
 * 	if 语句，格式
 * 		if (判断条件)	//判断条件为真，则执行代码段1,条件为假，则执行代码段2
 * 		{
 * 			代码段1
 * 		}
 * 		else
 * 		{
 * 			代码段2
 * 		}
 *
 * 	switch 语句，格式
 * 		seutch(i)	//i可以是数字或字符
 * 		{
 * 			case 1:
 * 				代码段
 * 				break;		//	停止执行的意思，跳出循环、分支
 * 			case 2:
 * 				代码段
 * 			default:
 * 				代码段
 * 		}
 */

 /**
  * 循环语句
  *
  * for 循环，格式
  * 		for(int i = 0; i <= number; ++i)
  * 		{
  * 			代码段
  * 		}
  *
  *		执行顺序：
  *		1、int i = 0;
  *		2、i <= number;		//如果判断条件为真，则跳出循环，结束
  *		3、代码段
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
  */

int main(void)
{
    int i = 94;

    if (i >= 95)
    {
        printf("你的成绩是：A+\n");
    }
    else if (i >= 90 && i < 95)
    {
        printf("你的成绩是：A\n");
    }
    else if (i >= 60 && i < 90)
    {
        printf("你的成绩是：B\n");
    }
    else
    {
        printf("你的成绩是：C\n");
    }

    printf("------------------------------------------\n");

    i = 1;
    char ch = '1';

    switch (ch)
    {
    case '1':
        printf("这是1\n");
        break;
    case '2':
        printf("这是2\n");
        break;
    case '3':
        printf("这是3\n");
        break;
    case '4':
        printf("这是4\n");
        break;
    case '5':
        printf("这是5\n");
        break;
    default:
        printf("这是其他值\n");
    }

    printf("------------------------------------------\n");

    for (int i = 1; i <= 100; ++i)
    {
        printf("I = %d\n", i);
    }

    printf("For循环结束！\n");

    printf("------------------------------------------\n");

    // 循环嵌套,99乘法表
    for (int i = 1; i <= 9; ++i) {

        for (int j = 1; j <= i; ++j) {

            printf("%d * %d = %d \t", i, j, (i * j));

        }

        printf("\n");

    }

    printf("------------------------------------------\n");

    i = 1;

    while (i <= 10)
    {
        printf("%d\n", i);
        ++i;
    }

    printf("------------------------------------------\n");

    int j = 1;

    do
    {
        printf("%d\n", j);
        ++j;
    } while (j <= 10);

    printf("------------------------------------------\n");

    return 0;
}