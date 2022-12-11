#array,deque
array是C语言的数组，它的存储是连续的内存空间
array和list最重要的区别，Python的array只能存储数值和字符。
从Python类型来看，只能存储整数，浮点数和unicode字符

1.需要一个不可变的数据容器来保存数据,可以考虑使用元组，提高数据的安全性
2.先进先出——双端队列
  有时，我们需要频繁地从序列的末尾添加或删除项。它要求项目按照先进先出顺序（先进先出）进行操作，即首先处理添加的第一项。使用列表，我们可以通过pop（0）函数来实现这一操作。但是，执行此操作的时间会很长，列表中的项必须进行移位，这是一个O（n）操作。
3.成员检查——集合
  如果应用程序需要频繁检查成员，就应考虑使用集合而不是列表。集合是Python中另一个重要的内置容器数据类型。集合的独特之处在于集合中的所有元素都必须是唯一的且可散列（哈希）的
  #Import needed modules
  from random import randint
  from timeit import timeit
  #Declare afunction to measure the time for membership testing
  def time_membership_testing(n):
    integers_list =list(range(n))
    integers_set =set(range(n))
    t_list =timeit(lambda : randint(0, 2*n) in integers_list, number=10000)
    t_set =timeit(lambda : randint(0, 2*n) in integers_set, number=10000)
    return f"{n: <9} list: {t_list:.4} | set: {t_set:.4}"

  numbers = (100, 1000, 10000, 100000)
  for number in numbers:
      print(time_membership_testing(number))

              100       list: 0.02304| set: 0.01333
              1000      list: 0.1042| set: 0.01309
              10000     list: 0.9028| set: 0.01713
              100000    list: 8.867| set: 0.01932

4.值检索——词典
根据哈希机制，检索特定键值对所需的时间是恒定的，时间复杂度为O（1）——使用Big-O表示法。这种O（1）时间复杂性意味着无论dict有多少个元素，检索特定项的时间总是保持在相同的量级上。
# Import needed modules
from random import randint
from timeit import timeit

# Declare afunction to measure the time for value retrieval
def time_value_retrieval_testing(n):
    id_list =list(range(n))
    score_list =list(range(n))
    scores_dict = {x: x for x inrange(n)}
    t_list =timeit(lambda : score_list[id_list.index(randint(0, n-1))], number=10000)
    t_dict =timeit(lambda : scores_dict[randint(0, n-1)], number=10000)
    returnf"{n: <9} list: {t_list:.4} | dict: {t_dict:.4}"
     
    numbers = (100, 1000, 10000, 100000)
    for number in numbers:
    print(time_value_retrieval_testing(number))
    
              100       list: 0.02423| dict: 0.01309
              1000      list: 0.07968| dict: 0.01322
              10000     list: 0.625| dict: 0.01565
              100000    list: 6.223| dict: 0.01583

5.大量表格型数据——数组
如果需要处理大量的数字型数据，应该考虑使用NumPy数组，这是NumPy包中实现的核心数据类型；如果需要处理具有混合数据类型（例如字符串、日期、数字）的结构化数据，则应该考虑使用Pandas DataFrame，这是Pandas包中实现的核心数据类型之一；如果进行机器学习，肯定需要研究张量，这是主要机器学习框架（如TensorFlow和PyTorch）中最重要的数据类型。
