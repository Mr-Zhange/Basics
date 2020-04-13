/**
 * 6、分支语句
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

# include <stdio.h>

int main() {
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

    int i = 1;
    char ch = '1';

    switch (ch)
    {
        case '1':
            printf("这是1");
            break;
        case '2':
            printf("这是2");
            break;
        case '3':
            printf("这是3");
            break;
        case '4':
            printf("这是4");
            break;
        case '5':
            printf("这是5");
            break;
        default:
            printf("这是其他值");
    }

    return 0;
}