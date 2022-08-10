一个问题：一个列表，比如是[1,2,3]，我打算在最右边增加一个数字。
方法一：
lst = [1, 2, 3]
lst.append(4)
lst
[1, 2, 3, 4]
方法二：
nl = [7]
nl.extend(lst)
nl
[7, 1, 2, 3, 4]

方法三：
将列表转化为deque。deque在汉语中有一个名字，叫做“双端队列”（double-ended queue）。
from collections import deque
qlst = deque(lst)
qlst.append(5) #从右边增加     
qlst.appendleft(7) #从左边增加
qlst.pop() #删除最右
qlst.popleft() #删除最左
qlst.rotate(3) #首尾链接成闭环，向右（顺时针）平移3位,如果为负数，向左（逆时针）平移
例如deque([1, 2, 3, 4]) --> deque([2, 3, 4, 1])


