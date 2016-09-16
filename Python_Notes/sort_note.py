#coding:utf-8

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
    print("插入排序一:"),
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
    print("插入排序二:"),
    for index in range(1,len(num_list)):
        value = num_list[index]
        i = index - 1
        while i>=0 and (value < num_list[i]):
            num_list[i+1] = num_list[i]
            num_list[i] = value
            i = i-1
    return num_list

def insertionSort3(num_list):
    """
    插入排序，num_list[0]已经排序好，共num_list[1]到最后num_list[-1],每次挑选出一个之，与每个值之前排序好的数列进行比较；
    如果不符合大小规则，就将临近的连个值进行交换（其中一个是挑选出的值）。
    如果符合就跳出，不再继续向前，因为前边已经排序。
    接着挑选下一个需要比较的值，与前面进行比较。
    """
    print("插入排序三:"),
    for index in xrange(1,len(num_list)):
        while index >0:                                                              #5)跳出
            if num_list[index-1] > num_list[index]:                                   #1)比较
                num_list[index],num_list[index-1] = num_list[index-1],num_list[index] #2）交换
                index = index - 1                                                     #3）向前比较
            else:
                break                                                                #4)已经排好序
    return num_list

def bubbleSort(num_list):
    """
    冒泡排序：选择第一个元素和第二个元素进行比较，如果不符合规则就交换
            然后第二个和第三个，以及第三个和第四个。。。
            相邻的进行比较，最后将极值放到最后。
    比较的轮数;j = n-1
    每轮比较的次数:n-1-j
    """
    print("冒泡排序一："),
    for j in xrange(len(num_list)-1):
        for i in xrange(len(num_list)-1-j):#第一轮比较到n-1,第二轮比较到n-1-1
            if num_list[i] > num_list[i+1]:
                num_list[i] ,num_list[i+1] = num_list[i+1],num_list[i]
    return num_list

def bubbleSort2(num_list):
    """
    先考虑一轮，最后的数为最值，已经排好序
    考虑下一轮，最后一个值不用比较
    """
    print("冒泡排序二："),
    for j in xrange(1,len(num_list)):
        for i in xrange(len(num_list)-j):
            if num_list[i] > num_list[i+1]:
                num_list[i] ,num_list[i+1] = num_list[i+1],num_list[i]
    return num_list

def shellSort(num_list):
    """
    希尔排序：改进的插入排序，不稳定。插入排序在初始的数据有序时，速度较快。为了在初始数比较乱时有更快的排序速度，就有了希尔排序。
    希尔排序基本思想：首先选择一个步长，步长的两个值进行对比：
                    1）对于大于步长的值可以逆向递减比较。（1）起始元素<--->起始元素索引+步长所在的元素。（2）起始元素+1<-->起始元素索引+步长所在的元素+1.。。。直到起始元素+1<步长(3)对于后边的元素进行逆向的递减步长判断
                    2）或者进行步长的再次扩张进行比较。（1）起始元素<--->起始元素索引+步长所在的元素。（2）起始元素索引+步长+步长所在的元素。。。。（3）对于后边的元素进行逆向的递减步长判断
                     最后当步长为1的时候，就是对整个序列进行排序。
        步长的停止：最后一次的子列表，为分到步长的前一个元素。
    程解思想：
        首先设置步长为整个序列的一半（整除），然后每次减少一个步长，直到步长为0，退出。
        比较方法:
            当前元素i,步长step_size
            s首先比较从num_list[i]到num_list[step_size-1],
            对于后边没有比较到的，及索引值大于2*step_size-1的，每取一个值，就跟前边减去步长的对应的元素进行比较。
    例子：  [4,6,3,8,1]  步长为2   4-3 6-8 比较
            [3,6,4,8,1] 然后比较1-4
            [3,6,1,8,4] 然后比较3-1
            [1,6,3,8,4] 步长减少1，为1
            []1-6不变；3--6交换[1,3,6,8,4]；3-1不变；8-6不变；4-8交换[1,3,6,4,8];4-6交换[1,3,4,6,8]
    """
    print("希尔排序一："),
    length_list = len(num_list)
    step_size = length_list/2
    while step_size >0:
        #进行步长间的值的比较
        for i in range(step_size):
            if num_list[i] > num_list[i+step_size]:
                num_list[i],num_list[i+step_size] = num_list[i+step_size],num_list[i]
                index = i-step_size
                while index >= 0:
                    if num_list[index] > num_list[index + step_size]:
                        num_list[index], num_list[index + step_size] = num_list[index + step_size], num_list[index]
                    index = index - step_size


        # 比较超过一个步长的值
        i+=1
        while i+step_size < length_list:
            if num_list[i] > num_list[i+step_size]:
                num_list[i], num_list[i+step_size] = num_list[i+step_size], num_list[i]
                index = i - step_size
                while index >= 0:
                    if num_list[index] > num_list[index + step_size]:
                        num_list[index], num_list[index + step_size] = num_list[index + step_size], num_list[index]
                    index = index - step_size
            i+= 1

        # 每次步长递减
        step_size -= 1
    return num_list

if __name__ == "__main__":
    num_list = [12, 44, 13, 67, 11, 556, 6,3]
    print(insertionSort(num_list[:]))
    print(insertionSort2(num_list[:]))
    print(insertionSort3(num_list[:]))
    print(bubbleSort(num_list[:]))
    print(bubbleSort2(num_list[:]))
    print(shellSort(num_list[:]))
