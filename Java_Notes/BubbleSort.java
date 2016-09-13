/**
两种排序方法
*/
public class BubbleSort
{
    public static void main(String[] args)
    {	
		System.out.println("一种遍历的排序,从前向后排序：");
        //选取左边的元素，和 右边的比较，如果是最值就交换，用此最值继续比较剩下的元素。最后最值从左到右。
        int num[] = {705,826,680,654,696};
        int c;
        for (int i=0 ;i < num.length -1 ;i++ )//第一个元素，到倒数第二位
        {
            for (int j=i+1 ;j<= num.length -1 ; j++)//第二个元素，从i后到最后一位
            {
                if(num[i] > num[j]){//第一个元素 和 后边的元素 进行比较;将比较的最值放到最左边。
                    c = num[i];
                    num[i] = num[j];
                    num[j] = c;
                }
            }
        }
        for (int i=0;i<num.length ;i++ )
        {
            System.out.print(num[i]+" ");
        }
        System.out.println();

		
		System.out.print("冒泡排序一：");
        //冒泡排序，是根据相邻的两个数进行比较，最值进行交换，最后最值都在 最右边。
        int[] num2 = {705,826,680,654,696};
        for (int i=0;i<num2.length-1 ;i++ )//控制比较的轮数：n.length-1次
        {
            for (int j=0;j<num2.length-1-i ;j++ )//控制每一轮比较的次数：n.length-1-轮数。
            {
                if (num2[j] > num2[j+1])
                {
                    c = num2[j];
                    num2[j] = num2[j+1];
                    num2[j+1] = c;
                }
            }
        }
        for (int i=0;i<num2.length ;i++ )
        {
            System.out.print(num2[i]+" ");
        }

		System.out.print("\n冒泡排序二：");
		int[] num3 = {705,826,680,654,696};
		for (int j=1; j<num.length ;j++ )
		{
			for (int i=0; i<num.length-j ;i++ )//考虑第一次是-1（最后一位已经排好序）,第二次是-2（倒数第二位已经排好序),...
			{
				if (num3[i] > num3[i+1])
				{
					c = num3[i];
					num3[i] = num3[i+1];
					num3[i+1] = c;
				}
			}
		}
		for (int i=0; i<num3.length ; i++ )
		{
			System.out.print(num3[i]+",");
		}
		
    }
}
