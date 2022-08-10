实现二叉堆就是通过二叉树实现的。其应该具有如下特点：
节点的值大于等于（或者小于等于）任何子节点的值。
节点左子树和右子树是一个二叉堆。如果父节点的值总大于等于任何一个子节点的值，其为最大堆；若父节点值总小于等于子节点值，为最小堆。上面图示中的完全二叉树，就表示一个最小堆。

在计算机科学中，二叉树（英语：Binary tree）是每個节点最多有兩個子树的树结构。通常子树被称作「左子树」（left subtree）和「右子树」（right subtree）。二叉树常被用於实现二叉查找树和二叉堆。

# heapq模块
heapq中的heap是堆，q就是queue（队列）的缩写。此模块包括：
import heapq
heapq.__all__
['heappush', 'heappop', 'heapify', 'heapreplace', 'merge', 'nlargest', 'nsmallest', 'heappushpop']

import heapq
heap = []    
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 0)
heapq.heappush(heap, 8)
heap
[0, 2, 3, 9, 4, 8]
利用**heappush()**函数将数据放到堆里面之后，会自动按照二叉树的结构进行存储。
heappop(heap)：删除最小元素
如果已经建立了一个列表，利用heapify()可以将列表直接转化为堆。

heapreplace()

是heappop()和heappush()的联合，也就是删除一个，同时加入一个。例如：
heap
[2, 4, 3, 9, 8]
heapq.heapreplace(heap, 3.14)
2
heap
[3, 4, 3.14, 9, 8]

堆在编程实践中的用途在哪方面呢？
主要在**排序**上。