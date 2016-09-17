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

def directselectSort(num_list):
    """
    直接选择排序：(每次选择最小的数)
        基本思想：第1趟，在待排序记录r[1] ~ r[n]中选出最小的记录，将它与r[1]交换；
                 第2趟，在待排序记录r[2] ~ r[n]中选出最小的记录，将它与r[2]交换；
                 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
    """
    print("直接选择排序："),
    for i in range(len(num_list)):
        min = i
        for j in  range(i+1,len(num_list)):
            if num_list[j] < num_list[min]:
                min = j
        if min !=i:
            num_list[i],num_list[min] = num_list[min],num_list[i]
    return num_list

def heapSort(num_list):
    """
    堆排序(Heapsort)是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。
    大根堆的要求是每个节点的值都不大于其父节点的值.
    二叉树:是每个节点最多有两个子树的树结构。通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）
           满二叉树：一棵深度为 k，且有 2k - 1 个节点称之为满二叉树
           完全二叉树：虽然不是满二叉树，但是拥有的节点和满二叉树对应。除了最底层之外，每一层都是满的。叶子从左向右。
    树和二叉树的三个主要差别：
        树的结点个数至少为 1，而二叉树的结点个数可以为 0
        树中结点的最大度数没有限制，而二叉树结点的最大度数为 2
        树的结点无左、右之分，而二叉树的结点有左、右之分
    堆（二叉堆）可以视为一棵完全的二叉树
    堆排序就是把最大堆堆顶的最大数取出，将剩余的堆继续调整为最大堆，再次将堆顶的最大数取出，这个过程持续到剩余数只有一个时结束。在堆中定义以下几种操作：
        最大堆调整（Max-Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
        创建最大堆（Build-Max-Heap）：将堆所有数据重新排序，使其成为最大堆
        堆排序（Heap-Sort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算

    在完全二插树中节点的编号：父节点A,左子节点2A+1,右子节点2A+2.(节点编号从0开始，对应列表的编号。)
        加入拿到一个节点编号为5，那么它的左右孩子编号为11,12，父节点的编号为2.
    堆是完全二叉树，最大值在数组的第0位；在需要排序即堆排序的时候，将最大值第0位的值和最后一位的值进行交换。
        然后除了最后一位重新建堆，再进行交换，最后列表都被排序。

    总体实现步骤：
    1：调整为最大堆：父节点大于任意一个子节点。
    2：创建堆：从数组最后一个节点到根节点，进行调整为最大堆
    3:堆排序：由于最大堆的最大值在第一位，将第一位和最后一位进行替换。然后重新创建堆。最后将数组都进行了排序。
    """
    print("堆排序："),
    def heapify(A,i,size):
        """
        规范二叉树数据：让父节点大于子 节点
            在一个子树，将最大值换到父节点的位置
        :param A: 完全二叉树--堆数组
        :param i: 看中的那个父节点
        :param size: 节点总数(堆数组的长度)--目的是防止判断左右孩子的时候出界限
        """
        if i >= size:
            return None
        left = 2*i + 1   #左孩子
        right = 2*i + 2  #右孩子
        largest = i  # 最大值

        if left < size:
            if A[largest] < A[left]:
                largest = left
        if right<size:
            if A[largest] < A[right]:
                largest = right

        if largest != i:#交换判断
            A[largest],A[i] = A[i],A[largest]
            heapify(A,largest,size) #对于交换过的子节点，进行其作为父节点的二叉树的交换比对。

    def create_heapify(A,size):
        """
        创建堆：从最后一个节点进行堆的创建。
            从堆数组最后一个节点，到根节点，对于每一个节点都做一个heapify（保证父节点值最大）
        :param A:堆数组
        :param size:堆数组的大小
        最后显示的结果中数组的第一个元素是最大的。
        """
        for i in range(size-1,-1,-1): #从后向前选取一个节点，比对每一个节点和其子节点，将最大值放到父节点。
            heapify(A,i,size)

    def heap_sort(A,size):
        """
        堆排序 : 每次创建堆，然后堆的最大值放到最后，然后除了最后一个值，重新迭代堆的创建和最大值的提取。
        :param A: 堆数组
        :param size: 堆数组的大小
        首先由堆A，将索引0（即最大值）和最后一个索引位置进行交换，
                    此时的堆长度为size-1,由于进行了交换，小的值在第一位，所以需要 重新建堆。
                    然后再进行最大值（index=0）和最后一位(index=-1)的交换。
        """
        for i in range(size-1,0,-1): #这个范围到i=1,因为i=0时，就只有一个元素，就不用对比了
            create_heapify(A,i+1)#首先建立堆
            A[0],A[i] = A[i],A[0] #每次将根节点和数组最后的数字进行交换 。由于堆得最大值一直是A[0]，交换后的位置 就是排序好的数据。


    heap_sort(num_list,len(num_list))
    # create_heapify(num_list,len(num_list))#测试堆的创建
    return num_list



if __name__ == "__main__":
    num_list = [12, 44, 13, 67, 11, 556, 6,3,77]
    # print(insertionSort(num_list[:]))
    # print(insertionSort2(num_list[:]))
    # print(insertionSort3(num_list[:]))
    # print(bubbleSort(num_list[:]))
    # print(bubbleSort2(num_list[:]))
    # print(shellSort(num_list[:]))
    # print(shellSort2(num_list[:]))
    # # print(shellSort3(num_list[:]))
    # print("快速排序一："),
    # print(quickSort(num_list[:],0,len(num_list)-1))
    # print("快速排序二："),
    # print(quickSort2(num_list[:]))
    print(directselectSort(num_list[:]))
    print(heapSort(num_list[:]))