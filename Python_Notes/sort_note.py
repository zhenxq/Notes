#coding:utf-8

num_list = [12,44,13,67,11,556,6]

def insertionSort(num_list):
    """
    插入排序
    思想：首先认为第一个数已经排好序，我们应该从第二个数开始，和前边排好序的数列的数据进行比较。

        首先将需要比较的数选出来；获得比较数的index索引值。
        根据需要，比较当前index的数和index索引递减的数。
        假如是递增数列，大数在后:
            如果index的数小：就和前边的数交换，然后继续向前比较。
            如果index的数大，就不用和前边交换，而且也不用再比较，因为前面的数列已经排序好。
    """
    for index in range(1,len(num_list)):
        value = num_list[index]
        i = index - 1
        while i >=0:
            if value < num_list[i]:
                num_list[i+1] = num_list[i]
                num_list[i] = value
                i = i - 1
            else:
                break
    return num_list

if __name__ == "__main__":
    insertionSort(num_list)
    print(num_list)