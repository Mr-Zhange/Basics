/**
 * 4、PrintfAndScanf
 * 
 * printf 	输出
 * scanf 	输入
 *
 * 控制符
 * %d		整数十进制
 * %o		整数八进制
 * %x		整数十六进制(小写)
 * %X		整数十六进制(大写)
 * %f		单精度
 * %lf		双精度
 * %c		字符
 * %s 		字符串
 */

# include <stdio.h>

int main()
{
    int i;
    char ch;

    printf("请输入一个数字：");

    while ((ch=getchar())!='\n')
        continue;

    scanf("%d",&i);

    printf("你输入的数字是：%d。\n",i);

    return 0;
}