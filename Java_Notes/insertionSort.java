/**
��������
	��Ϊ��һ��Ԫ���Ѿ�����
	�ӵڶ���Ԫ�ؿ�ʼ����ǰ���ź����Ԫ�ؽ��бȽϣ�λ�ý��н�����
*/

public class insertionSort
{
	public static void main(String[] args)
	{
		System.out.print("�������򷽷�һ��\n");
		int[] num = {2,33,4,66,14,7};
		//ԭʼ����
		for (int i=0;i<num.length ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();

		//��������
		for (int i=1;i<num.length ;i++ )//�ӵڶ���Ԫ�ؿ�ʼ��ǰ���ź����Ԫ�ؽ��бȽϡ�
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
		for (int i=0;i<num.length ;i++ )
		{
			System.out.print(num[i]+",");
		}
		System.out.println();



		System.out.print("�������򷽷�����\n");
		int[] num_list = {2,33,4,66,14,7};
		//��ӡԭʼ�б�����
		for (int i=0; i<num_list.length ;i++ )
		{
			System.out.print(num_list[i]+",");
		}
		System.out.print("\n");
		
		//�������򣻴ӵڶ���Ԫ�ؿ�ʼ��ǰ�ߵ�Ԫ�ؽ��бȽ�
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
		
		//��ӡ������б�
		for (int i=0; i<num_list.length; i++ )
		{
			System.out.print(num_list[i]+",");
		}
		System.out.println();
	}
}