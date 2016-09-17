#coding:utf-8
import time

def usetimeDecorate(fun):
    def wrapper(num_list):
        start_time = time.time()
        num_list = fun(num_list)
        print "Time:",time.time() - start_time
        return num_list
    return wrapper

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
            [3,6,4,8,1] 然后比较1-4  ，如果没有发生交换，就不用继续向前比较。
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
                    else:
                        break
            i+= 1

        # 每次步长递减
        step_size -= 1
    return num_list

def shellSort2(num_list):
    """
    每次比较的时候，根据步长来比较，最后一次比较的步长为1
    每次比较的时候，选取基准索引和索引+一个或者多个步长的元素进行比较。
    """
    print("希尔排序二："),
    length_list = len(num_list)
    step = length_list/2
    while step>0:
        for i in range(step):
            index = i
            while index+step  < length_list: #判断i,i+step，i+step+step。。。一直判断到最后的索引+step大于list的长度。取得值是 从第i个元素和对应的i+多个步长所在的元素。
                # print num_list, num_list[index],num_list[index+step]
                if num_list[index] > num_list[index+step]:
                    num_list[index],num_list[index+step] = num_list[index+step],num_list[index]
                index = index+step
        step -= 1
    return num_list


def shellSort3(num_list):
    """
    正确的希尔排序：
        步长的选择是希尔排序的重要部分。只要最终步长为1任何步长序列都可以工作。
        当步长为1时，算法变为插入排序，这就保证了数据一定会被排序。
        Donald Shell最初建议步长选择为 n/2,并且对步长取半直到步长达到1。
    排序思想:先选取步长的元素进行比对（插入排序），通过逐渐减少步长（步长的选取最后一次一定为1--插入排序）来进行排序。
        是改进的插入排序，插入排序在数据有序的时候排序的速度会更快。因为插入排序比较的是前边已经排序好的序列。
    """
    print("希尔排序三："),
    length_list = len(num_list)
    step = length_list/2

    while step > 0:
        for index in range(0,step): #进行某个步长内的元素的遍历排序。
            while index+step < length_list:
                while index>=0: #插入排序，和前边的已经排序好的比较.
                    if num_list[index] > num_list[index+step]:
                        num_list[index],num_list[index+step] = num_list[index+step],num_list[index]
                        index = index - step         #选取交换的元素与前边已经排序好的元素进行比较。
                    else:
                        break                       #前边的元素已经有序，就不用再比对（这是插入排序的重要特点）
                index = index + step
        step = step/2#每次用新的步长
    return num_list

def quickSort(num_list,left,right):
    """
    快速排序：
        思想：分治法，将一个序列分成两个子序列。
              1：选取第一个元素作为标尺。（看做将其取出）
              2：小于标尺元素的所有元素，放在左边。大于标尺元素的所有元素，放在右边。
              3：每次比较的时候，当与标尺元素进行交换的时候 ，比较的方向要发生变化，因为另一个方向的元素 是已经比较完的，所以需要变换方向。
                一直比较到左，右的索引值相等。

    """
    if left >= right :
        return None
    key = num_list[left] #基准元素-标尺
    low = left           #记住需要比较的范围
    high = right

    while left < right:
        while left < right and num_list[right] >= key: #当右边数据比基准数据key大
            right -= 1
        num_list[left]= num_list[right] #此时将数据进行交换，标尺相当于放到num_list[right]然后又取出来，所以没写。
        while left < right and num_list[left] <= key: #转换比较的方向
            left += 1
        num_list[right] = num_list[left]
    num_list[right] = key
    quickSort(num_list,low,left-1)
    quickSort(num_list,left+1,high)
    return num_list

def quickSort2(num_list):
    if len(num_list) == 0:
        return []
    else:
        return quickSort2([x for x in num_list[1:] if x < num_list[0]]) + [num_list[0]] + quickSort2([x for x in num_list[1:] if x > num_list[0]])


if __name__ == "__main__":
    num_list = [12, 44, 13, 67, 11, 556, 6,3,77]
    # print(insertionSort(num_list[:]))
    # print(insertionSort2(num_list[:]))
    # print(insertionSort3(num_list[:]))
    # print(bubbleSort(num_list[:]))
    # print(bubbleSort2(num_list[:]))
    # print(shellSort(num_list[:]))
    # print(shellSort2(num_list[:]))
    # print(shellSort3(num_list[:]))
    print(quickSort(num_list[:],0,len(num_list)-1))
    print(quickSort2(num_list[:]))
