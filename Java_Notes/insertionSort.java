/**
插入排序：
	认为第一个元素已经排序，
	从第二个元素开始，与前边排好序的元素进行比较，位置进行交换。
*/

public class insertionSort
{
	public static void main(String[] args)
	{
		System.out.print("插入排序方法一：\n");
		int[] num = {2,33,4,66,14,7};
		//原始数据
		for (int i=0;i<num.length ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();

		//插入排序
		for (int i=1;i<num.length ;i++ )//从第二个元素开始与前边排好序的元素进行比较。
		{
			int value = num[i]; //记住比较的元素
			int j = i - 1;      //前边的元素
			while (j >= 0)
			{
				if (value < num[j])
				{
					num[j+1] = num[j]; //将数值向后移动
					num[j] = value; //只是用来进行完整数值的填充，不用考虑太多
					j = j -1;
				}else{
					break;
				}
			}

		}

		//输出
		for (int i=0;i<num.length ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();



		System.out.print("插入排序方法二：\n");
		int[] num_list = {2,33,4,66,14,7};
		//打印原始列表数据
		for (int i=0; i<num_list.length ;i++ )
		{
			System.out.print(num_list[i]+",");
		}
		System.out.print("\n");
		
		//插入排序；从第二个元素开始与前边的元素进行比较
		int temp;
		for (int i=1; i<num_list.length ;i++ )
		{
			while (i>=1)
			{
				if (num_list[i-1] > num_list[i])
				{
					temp = num_list[i];
					num_list[i] = num_list[i-1];
					num_list[i-1] = temp;
					i = i-1;
				}else{
					break;
				}
			}
		}
		
		//打印排序的列表
		for (int i=0; i<num_list.length; i++ )
		{
			System.out.print(num_list[i]+",");
		}
		System.out.println();
	}
}