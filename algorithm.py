import heapq
import random

import helpers

class Find_TopK(object):

    @classmethod
    def find(cls):
        pass

class Find_Topk_by_Quick_Select(Find_TopK):

    @classmethod
    @helpers.sort_cost_time
    def find(cls, lis, k):
        """使用快速选择方法找到topk个元素（前k小）"""
        def recur(start_pos, end_pos, k):
            if start_pos>=end_pos: return
            pivot_index = random.randint(start_pos, end_pos)
            lis[end_pos], lis[pivot_index] = lis[pivot_index], lis[end_pos]  # 把pivot换到最后方便处理

            mark_index = start_pos
            for i in range(start_pos, end_pos):
                if lis[i]<lis[end_pos]:
                    lis[i], lis[mark_index] = lis[mark_index], lis[i]
                    mark_index += 1
            lis[mark_index], lis[end_pos] = lis[end_pos], lis[mark_index]
            num = mark_index-start_pos+1  # pivot到开头一共有多少个元素（包括pivot）
            if num == k: return  # 如果恰好等于k，说明我们已经找到了前k小的元素，pivot就是第k个元素
            if num > k:
                recur(start_pos, mark_index-1, k)  # 如果pivot大约k，说明符合要求的k个元素在pivot左侧，缩小范围继续查找
            elif num < k:
                recur(mark_index+1, end_pos, k-num)  # 如果pivot小于k，说明符合要求的k个元素有一部分在pivot右侧。

        if k==0: return []
        length = len(lis)
        recur(0, length-1, k)
        return lis[:k]


if __name__ == "__main__":
    test1 = [0,1,1,1,4,5,3,7,7,8,10,2,7,8,0,5,2,16,12,1,19,15,5,18,2,2,22,15,8,22,17,6,22,6,22,26,32,8,10,11,2,26,9,12,9,7,28,33,20,7,2,17,44,3,52,27,2,23,19,56,56,58,36,31,1,19,19,6,65,49,27,63,29,1,69,47,56,61,40,43,10,71,60,66,42,44,10,12,83,69,73,2,65,93,92,47,35,39,13,75]
    Find_Topk_by_Quick_Select.find(test1,75)




