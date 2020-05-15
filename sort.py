#coding=utf-8
from copy import deepcopy
import random

import helpers

class Sort(object):

    @classmethod
    def sort(cls):
        pass

class Bubble_Sort(Sort):

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):
        has_exchange = True
        length = len(lis)
        while has_exchange:  # 如果一次遍历未发生交换，则代表排序完毕
            has_exchange = False
            for i in range(length):
                if i == length-1: break
                if lis[i]>lis[i + 1]:  # 只能是大于，保证排序稳定性
                    lis[i], lis[i + 1] = lis[i + 1], lis[i]
                    has_exchange= True
        return lis

class Insert_Sort(Sort):

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):
        for i, element in enumerate(lis):
            if i == 0: continue
            for j in range(i, 0, -1):  # 倒着一个一个比较
                if lis[j]<lis[j-1]:  # 如果发现大小顺序不对则交换（小于保证稳定性）
                    lis[j], lis[j-1] = lis[j-1], lis[j]
                else:
                    break
        return lis

class Select_Sort(Sort):

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):
        if not lis: return lis

        length = len(lis)
        start_pos = 0  # 选择最小值的起始索引
        while start_pos<length:
            min_index = start_pos  # 最小值的索引和值
            min_element = lis[min_index]
            for i in range(start_pos, length):  #每次选出一个当前范围内最小值放到第一个，第二个...
                if lis[i]<min_element:
                    min_index = i
                    min_element = lis[i]
            lis[min_index], lis[start_pos] = lis[start_pos], lis[min_index]
            start_pos += 1
        return lis

class Quick_Sort(Sort):

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):

        def recur(start_pos, end_pos):
            """维持两个指针i，j。j用来遍历数组与pivot进行比较，i用来当之后分治的分界点。
            pivot为选定的基准值（不用记录它的位置，把它拿出来和队尾互换即可）
            当lis[j]<pivot时，i,j位置元素互换，i++
            最后将队尾pivot与i位置互换，至此i之前的部分都小于pivot，i之后的大于等于pivot
            把pivot放在i位置上，再对两部分分别进行递归排序"""
            if start_pos >= end_pos: return
            pivot_index = random.randint(start_pos, end_pos)  # 初始分区点
            lis[pivot_index], lis[end_pos] = lis[end_pos], lis[pivot_index]  # 将pivot 放到最后一个
            i = start_pos
            for j in range(start_pos, end_pos):
                if lis[j] < lis[end_pos]:
                    lis[j], lis[i] = lis[i], lis[j]
                    i += 1
            lis[i], lis[end_pos] = lis[end_pos], lis[i]
            recur(start_pos, i - 1)
            recur(i + 1, end_pos)

        length = len(lis)
        recur(0, length-1)
        return lis


class Merge_Sort(Sort):

    @classmethod
    @helpers.function_cost_time
    def sort(cls, lis):
        """归并排序分两步：第一步先分治递归进行排序，然后将两个有序子数组进行合并"""
        def recur(start, end):
            if start>=end: return
            mid = (start+end)//2

            recur(start, mid)
            recur(mid+1, end)

            merge(start,end,lis[start:mid+1], lis[mid+1:end+1])


        def merge(start,end,left,right):
            i = 0
            j = 0
            temp = []
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    j += 1

            if i<len(left):
                temp.extend(left[i:])

            if j<len(right):
                temp.extend(right[j:])

            lis[start:end+1] = temp


        recur(0,len(lis)-1)
        return lis






if __name__ == "__main__":
    lis1 = [21,14,2,6,7,10,1,2,0,41,17,2]
    lis2 = [1,5,20,11,4,7,10,9]
    lis3 = [1,4,5,22,56,7,10,3,20]
    lis4 = [0,1,1,1,4,5,3,7,7,8,10,2,7,8,0,5,2,16,12,1,19,15,5,18,2,2,22,15,8,22,17,6,22,6,22,26,32,8,10,11,2,26,9,12,9,7,28,33,20,7,2,17,44,3,52,27,2,23,19,56,56,58,36,31,1,19,19,6,65,49,27,63,29,1,69,47,56,61,40,43,10,71,60,66,42,44,10,12,83,69,73,2,65,93,92,47,35,39,13,75]
    lis5 = [1,2,5,563,6,547,5,0,243,13,24,6,6,567,365,7,634,8,9,11,67,56,24313,23,67]
    lis1 = Bubble_Sort.sort(lis1)
    lis2 = Insert_Sort.sort(lis2)
    lis3 = Select_Sort.sort(lis3)
    lis4 = Quick_Sort.sort(lis4)
    lis5 = Merge_Sort.sort(lis5)

