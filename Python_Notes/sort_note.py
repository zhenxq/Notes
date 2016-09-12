#coding:utf-8

num_list = [12,44,13,67,11,556,6]

def insertionSort(num_list):
    """
    插入排序
    思想：首先认为第一个数已经排好序，我们应该从第二个数开始，和前边排好序的数列的数据进行比较。

        首先将需要比较的数选出来；获得比较数的index索引值。
        根据需要，比较当前index的数和index索引递减的数。
        假如是递增数列，大数在后:
            如果index的数小：就和前边的数交换（由于是递减比较 ，所以每次交换的都是相邻的数据位的值），然后继续向前比较。
            如果index的数大，就不用和前边交换，而且也不用再比较，因为前面的数列已经排序好。

    """
    for index in range(1,len(num_list)):#每轮比较的数据索引，从第二个元素开始
        value = num_list[index]          #挑选出需要比较的数据
        i = index - 1                    #获得比较数据的前一个数据，作为比较的开始
        while i >= 0:
            if value < num_list[i]:     #从小到大排序
                num_list[i+1] = num_list[i]
                num_list[i] = value
                i = i - 1
            else:                      #直接退出，因为前边已经排好序列。
                break
    return num_list

def insertionSort2(num_list):
    """
    简化的插入排序
    """
    for index in range(1,len(num_list)):
        value = num_list[index]
        i = index - 1
        while i>=0 and (value < num_list[i]):
            num_list[i+1] = num_list[i]
            num_list[i] = value
            i = i-1

if __name__ == "__main__":
    insertionSort(num_list)
    insertionSort2(num_list)
    print(num_list)