/**
��������
	��Ϊ��һ��Ԫ���Ѿ�����
	�ӵڶ���Ԫ�ؿ�ʼ����ǰ���ź����Ԫ�ؽ��бȽϣ�λ�ý��н�����
*/

public class insertionSort
{
	public static void main(String[] args)
	{
		int[] num = {2,33,4,66,14,7};
		//ԭʼ����
		for (int i=0;i<num.length-1 ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();

		//��������
		for (int i=1;i<num.length-1 ;i++ )//�ӵڶ���Ԫ�ؿ�ʼ��ǰ���ź����Ԫ�ؽ��бȽϡ�
		{
			int value = num[i]; //��ס�Ƚϵ�Ԫ��
			int j = i - 1;      //ǰ�ߵ�Ԫ��
			while (j >= 0)
			{
				if (value < num[j])
				{
					num[j+1] = num[j]; //����ֵ����ƶ�
					num[j] = value; //ֻ����������������ֵ����䣬���ÿ���̫��
					j = j -1;
				}else{
					break;
				}
			}

		}

		//���
		for (int i=0;i<num.length-1 ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();
		
	}
}