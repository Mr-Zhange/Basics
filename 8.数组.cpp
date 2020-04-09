/**
 * 8、数组
 *
 * 	格式：
 * 		int arry[10] = {1,2,3,4,5,6,7,8,9,0};
 * 		数组类型 数组名称[数组长度] = {值1,值2,值3,......}
 * 		数组长度与等号右边的值个数要一致
 *
 * 	获取数组的元素个数：
 * 		int len = sizeof(arry) / sizeof(arry[0]) - 1;
 * 		数组占内存总空间除以单个元素占内存空间大小，即等于元素个数
 * 		因为数组下标是从0开始的，及 -1
 */ 

# include <stdio.h>

int main()
{
	int arry[10] = {1,2,3,4,5,6,7,8,9,0};

    int len = sizeof(arry) / sizeof(arry[0]) - 1;

    for (int i = 0; i <= len; ++i)
    {
        printf("%d ", arry[i]);
    }

    printf("\n");

    return 0;
}