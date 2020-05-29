import heapq
import random

import helpers
from data_structure import Max_Heap

class Find_TopK(object):
    @classmethod
    def find(cls):
        pass


class Find_Topk_by_Quick_Select(Find_TopK):

    @classmethod
    @helpers.function_cost_time
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
        if k>=len(lis): return lis
        length = len(lis)
        recur(0, length-1, k)
        return lis[:k]


class Find_Topk_by_heap(Find_TopK):

    @classmethod
    @helpers.function_cost_time
    def find(cls, lis, k):
        if k >=len(lis):return lis
        if k == 0 : return []

        heap = Max_Heap.build_heap(lis[:k])
        for item in lis[k:]:
            if item <= heap[0]:
                heap = Max_Heap.remove(heap)
                heap = Max_Heap.insert(heap, item)
        return heap


class BackPack(object):
    """背包问题"""
    @classmethod
    def pack_without_value(cls,weights,size):
        """0-1背包问题（无价值）"""
        """
        状态：dp[i]：当前weights值所达到的最大weights值
        """
        assert all([x<=size for x in weights])
        dp = [0]*(size+1)
        for i in range(len(weights)):
            for j in range(size, weights[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weights[i]]+weights[i])
        return dp[-1]


    @classmethod
    def pack_with_value(cls,values,weights,size):
        """0-1背包问题（带价值）"""
        """
        状态：dp[i]：当weights为i时的最大价值
        """
        assert len(values) == len(weights)
        assert all([x<=size for x in weights])
        dp = [0]*(size+1)  # 状态初始化（0-size）
        # 放入第i个元素（不放入的情况可以省略，保持当前dp状态就好了）
        for i in range(len(weights)):
            # 从dp[size-wight]遍历至dp[0]，叠加之前的状态。
            # dp[0]表示之前什么都没放入，当前是第一个元素。
            for j in range(size, weights[i]-1, -1):
                # 状态转移方程（对当前已有值和新值求最大值）
                # 之所以反向遍历，是因为正向遍历会导致重复计算：
                # 比如dp[3]可能加上了dp[1]，但是dp[5]又加上dp[3]，这样dp[1]就被加了两次
                dp[j] = max(dp[j], dp[j-weights[i]]+values[i])
        return dp[-1]


if __name__ == "__main__":
    test1 = [27, 10, 1, 4, 77, 29, 19, 10, 50, 5, 2, 333, 5,1]
    Find_Topk_by_Quick_Select.find(test1, 5)
    values = [2, 6, 10, 1]
    weights = [2, 5, 4, 2]
    print(BackPack.pack_with_value(values,weights,7))
    print(BackPack.pack_without_value(weights,10))
    print(Find_Topk_by_heap.find([1, 4, 5143, 123,13,545,764,22,45,6],4))





