#coding:gbk

"""
要求：给定一个长度为8的数组A{1,3,5,2,4,6,7,8}，则其最长的"单调递增"子序列为{1,2,4,6,7,8}，长度为6.
"""


def getMaxIncrSeriesList(series_array):
    """
    获得一个列表中，按照循序，最大的增长序列
    """
    #首相获得每个元素值，以及后边比这个元素本身大的元素的列表
    dict_list = {}
    for  i in range(len(series_array)):
        dict_list[series_array[i]] = [item for item in series_array if item > series_array[i]]
    # print dict_list
    # {1: [3, 5, 2, 4, 6, 7, 8], 2: [3, 5, 4, 6, 7, 8], 3: [5, 4, 6, 7, 8], 4: [5, 6, 7, 8], 5: [6, 7, 8], 6: [7, 8],7: [8], 8: []}
    #通过获得的字典，根据key，找到key的第一个值，通过将第一个值当做key找到下一个key的第一个值。一直比较到key的值位空[]，(因为最大的值肯定为空。）
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
    获得一个列表中，按照循序，最大的增长序列
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
