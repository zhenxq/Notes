/**
�������򷽷�
*/
public class BubbleSort
{
    public static void main(String[] args)
    {	
		System.out.println("һ�ֱ���������,��ǰ�������");
        //ѡȡ��ߵ�Ԫ�أ��� �ұߵıȽϣ��������ֵ�ͽ������ô���ֵ�����Ƚ�ʣ�µ�Ԫ�ء������ֵ�����ҡ�
        int num[] = {705,826,680,654,696};
        int c;
        for (int i=0 ;i < num.length -1 ;i++ )//��һ��Ԫ�أ��������ڶ�λ
        {
            for (int j=i+1 ;j<= num.length -1 ; j++)//�ڶ���Ԫ�أ���i�����һλ
            {
                if(num[i] > num[j]){//��һ��Ԫ�� �� ��ߵ�Ԫ�� ���бȽ�;���Ƚϵ���ֵ�ŵ�����ߡ�
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

		
		System.out.print("ð������һ��");
        //ð�������Ǹ������ڵ����������бȽϣ���ֵ���н����������ֵ���� ���ұߡ�
        int[] num2 = {705,826,680,654,696};
        for (int i=0;i<num2.length-1 ;i++ )//���ƱȽϵ�������n.length-1��
        {
            for (int j=0;j<num2.length-1-i ;j++ )//����ÿһ�ֱȽϵĴ�����n.length-1-������
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

		System.out.print("\nð���������");
		int[] num3 = {705,826,680,654,696};
		for (int j=1; j<num.length ;j++ )
		{
			for (int i=0; i<num.length-j ;i++ )//���ǵ�һ����-1�����һλ�Ѿ��ź���,�ڶ�����-2�������ڶ�λ�Ѿ��ź���),...
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
