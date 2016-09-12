/**
插入排序：
	认为第一个元素已经排序，
	从第二个元素开始，与前边排好序的元素进行比较，位置进行交换。
*/

public class insertionSort
{
	public static void main(String[] args)
	{
		int[] num = {2,33,4,66,14,7};
		//原始数据
		for (int i=0;i<num.length-1 ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();

		//插入排序
		for (int i=1;i<num.length-1 ;i++ )//从第二个元素开始与前边排好序的元素进行比较。
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
		for (int i=0;i<num.length-1 ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();
		
	}
}