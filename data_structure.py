#coding:utf-8

import helpers

class Max_Heap(object):
    """自定义堆结构，默认为大顶堆"""

    @classmethod
    def build_heap(cls, lis):
        """建堆函数，从后往前处理数组进行堆化，堆化操作从上向下"""
        if len(lis) == 1:return lis
        # 索引0位置置None，使得首元素的索引为1，
        # 则左子节点索引为父节点索引乘2，右子节点为乘2加1,方便处理
        lis.insert(0, None)
        n = len(lis)
        # 从n//2位置开始迭代堆化，因为以索引1为根节点的数组中，n+1//2开始到n的节点全部是叶子节点
        # 建堆的堆化操作从第一个非叶子节点开始
        for i in range(n//2, 0, -1):
            cls._heapify(lis, n, i)
        lis.pop(0)  # 去掉开头的None
        return lis

    @classmethod
    def _heapify(cls, lis, length, i):
        """堆化操作，使的堆符合堆的定义"""
        while True:
            # 从上往下对每一个非叶子节点和其两个子节点进行比大小，把最大的换到父节点位置
            max_pos = i
            if i*2<length and lis[i*2]>lis[max_pos]: max_pos = i*2
            if i*2+1<length and lis[i*2+1]>lis[max_pos]: max_pos = i*2+1
            if i == max_pos: break # 没有交换表示父节点就是最大的，break
            lis[max_pos], lis[i] = lis[i], lis[max_pos]
            # 对刚才换过位的节点继续进行往下进行下一轮比大小
            # （没换过的不需要比因为是从下往上遍历数组的，下面的都排好了）
            i = max_pos

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):
        """利用堆进行排序"""
        lis = Max_Heap.build_heap(lis)
        lis.insert(0, None)  # 依旧在首位插入一个None，方便操作
        n = len(lis)-1
        while n > 1:
            # 每次将堆顶元素往后换，换完之后对堆顶进行一次堆化操作
            lis[n], lis[1] = lis[1], lis[n]
            n -= 1
            cls._heapify(lis, n, 1)  # 堆化的时候不能包含已经挪到下面的元素
        lis.pop(0)
        return lis





if __name__ == "__main__":
    heap1 = Max_Heap.build_heap([2, 5, 6, 10, 1, 8])
    list2 = Max_Heap.sort([1,50,22,6,77,12,5,3,8,28,100,29,24])