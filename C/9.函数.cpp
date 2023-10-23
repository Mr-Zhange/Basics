/**
 * 9、函数
 */

# include <stdio.h>

// 函数申明
void max(int i,int j);

int main()
{
	int i = 100;
	int j = 101223;

	max(i,j);

	return 0;
}

// 带参，无返回值函数
void max(int i,int j)
{
	if (i > j)
	{
		printf("%d\n", i);
	}
	else
	{
		printf("%d\n", j);
	}
}