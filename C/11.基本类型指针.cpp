/**
 * 11、基本类型指针
 */

# include <stdio.h>

int main()
{
	int * p;

	int i = 5 ;

	p = &i;

	printf("%d\n", p);

	*p = i;

	printf("%d\n", *p);
	printf("%d\n", p);

	//free(指针)，指针释放
}