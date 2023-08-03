/**
 * printf 	输出
 * scanf_s 	输入
 */

# include <stdio.h>

int main()
{
    char c1;
    char c2;

    printf("请输入一个小写字母,自动转大写输出:");

    c1 = getchar();

    printf("%c,%d\n", c1, c1);
    c2 = c1 - 32;
    printf("%c,%d\n", c2, c2);

    return 0;
}