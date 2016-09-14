#coding:gbk

"""
Ҫ�󣺸���һ������Ϊ8������A{1,3,5,2,4,6,7,8}���������"��������"������Ϊ{1,2,4,6,7,8}������Ϊ6.
"""


def getMaxIncrSeriesList(series_array):
    """
    ���һ���б��У�����ѭ��������������
    """
    #������ÿ��Ԫ��ֵ���Լ���߱����Ԫ�ر�����Ԫ�ص��б�
    dict_list = {}
    for  i in range(len(series_array)):
        dict_list[series_array[i]] = [item for item in series_array if item > series_array[i]]
    # print dict_list
    # {1: [3, 5, 2, 4, 6, 7, 8], 2: [3, 5, 4, 6, 7, 8], 3: [5, 4, 6, 7, 8], 4: [5, 6, 7, 8], 5: [6, 7, 8], 6: [7, 8],7: [8], 8: []}
    #ͨ����õ��ֵ䣬����key���ҵ�key�ĵ�һ��ֵ��ͨ������һ��ֵ����key�ҵ���һ��key�ĵ�һ��ֵ��һֱ�Ƚϵ�key��ֵλ��[]��(��Ϊ����ֵ�϶�Ϊ�ա���
    series_list = []
    for key in dict_list:
        temp_list = []
        temp_list.append(key)
        while dict_list[key]:
            key = dict_list[key][0]
            temp_list.append(key)
        series_list.append(temp_list)
    # print series_list

    max_len_series =  max(series_list,key=lambda x:len(x))
    return len(max_len_series),max_len_series

def getMaxIncrSeriesList2(series_array):
    """
    ���һ���б��У�����ѭ��������������
    """
    #
    dict_list = {}
    for i in series_array:
        for item in series_array:
            if i < item :
                dict_list[i]=item
                break
    # print dict_list
    #{1: 3, 2: 3, 3: 5, 4: 5, 5: 6, 6: 7, 7: 8, 8: 44, 11: 44}

    series_list = []
    for item in dict_list:
        temp_list = []
        temp_list.append(item)
        while dict_list.has_key(item):
            item = dict_list[item]
            temp_list.append(item)
        series_list.append(temp_list)
    max_len_series =  max(series_list,key=lambda x:len(x))
    return len(max_len_series), max_len_series

if __name__ == "__main__":
    A = [1, 3, 5, 2, 4, 6, 7, 8,44,11]
    print getMaxIncrSeriesList(A)
    print getMaxIncrSeriesList2(A)
