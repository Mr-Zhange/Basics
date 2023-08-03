#include <stdio.h>

/*
基本类型
    整型
        基本整型		    int             4	-32768~32767
        短整形		    short int	    2	-32768~32767
        长整型		    long int	    8	-214783648~214783647
        无符号型		    unsigned	    4	0~65535
        无符号长整型	    unsigned long	8	0~4294967295
    字符型
        字符型           char            1	C字符集
    浮点型
        单精度           float           4	3/4E-38~3/4E+38
        双精度           double          8	1/7E-308~1/7E+308
    枚举类型
构造类型
    数组类型
    结构体类型
    共用体类型
指针类型
空类型
*/

/*
    变量声明格式

  		数据类型 变量名称 = 赋与的值
  		int i = 10;
  	或者：
  		int i;
  		i = 10;
 
  		int j,x;
  		j = 10;
  		x = 11;
 
   	声明一个变量，需要初始化之后才能使用
*/

// 定义宏值
#define PRICE 10

// 全局变量
int x, y;

int main()
{
    // 函数内声明变量
    extern int x, y;

    // 定义常量.不可被改变的变量
    const int HIGHT = 1;
    const int WIDTH = 2;

    int a = 0;
    printf("int a的值是：%d,int a的长度是：%d\n\n", a, sizeof(a));

    short int b = 0;
    printf("short int b的值是：%d,short int b的长度是：%d\n\n", b, sizeof(b));

    long int c = 0;
    printf("long int c的值是：%d,long int c的长度是：%d\n\n", c, sizeof(c));

    unsigned d = 0;
    printf("unsigned d的值是：%d,unsigned d的长度是：%d\n\n", d, sizeof(d));

    unsigned long e = 0;
    printf("unsigned long e的值是：%d,unsigned long e的长度是：%d\n\n", e, sizeof(e));

    char f = ' ';
    printf("char f的值是：%c,char f的长度是：%d\n\n", f, sizeof(f));

    char s[] = "\"char数组可以理解成字符串使用\"";
    printf("char s[]的值是：%s,char s[]的长度是：%d\n\n", s, sizeof(s));

    float g = 0;
    printf("float g的值是：%f,float g的长度是：%d\n\n", g, sizeof(g));

    // printf("float最大值:%E\n\n", __FLT_MAX__);

    // printf("float最大值:%E\n\n", __FLT_MIN__);

    double h = 0;
    printf("double h的值是：%f,double h的长度是：%d\n\n", h, sizeof(h));

    return 0;
}
