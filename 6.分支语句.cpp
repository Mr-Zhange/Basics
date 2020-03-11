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

    return 0;
}