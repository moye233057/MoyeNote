def bubble_sort(arr):
    """ð������"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """ѡ������"""
    # ��һ�����ѭ������
    for i in range(len(arr) - 1):
        min_index = i
        # �ڶ���for��ʾ��СԪ�غͺ���Ԫ������Ƚ�
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # ����һ�����СԪ������ʼԪ�ػ���
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insert_sort(arr):
    """��������"""
    # ��һ�����ѭ������
    for i in range(1, len(arr)):
        # ���õ�ǰ��Ҫ�����Ԫ��
        current = arr[i]
        # �뵱ǰԪ�رȽϵ�Ԫ��
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # ���Ƚ�Ԫ�ش��ڵ�ǰԪ����ѱȽ�Ԫ�غ���
            arr[pre_index + 1] = arr[pre_index]
            # ��ǰѡ����һ���Ƚ�Ԫ��
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


def shell_sort(list):
    """ϣ������"""
    n = len(list)
    # ��ʼ����
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # ÿ���������в�������
            temp = list[i]
            j = i
            # ��������
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # �õ��µĲ���
        gap = gap // 2
    return list


# �ݹ鷨
def merge_sort(list):
    """�鲢����"""
    # ��Ϊ���Ȳ�����1�������������
    if len(list) <= 1:
        return list
    # �����б�
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    # ���һ�κϲ�
    return merge(left, right)


# �ϲ�
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        result += left[l:]
        result += right[r:]
    return result


"""
����
������������һ��Ԫ�أ���Ϊ����׼����pivot����
�����������У�����Ԫ�رȻ�׼ֵС�İڷ��ڻ�׼ǰ�棬����Ԫ�رȻ�׼ֵ��İ��ڻ�׼�ĺ��棨��ͬ�������Ե���һ�ߣ����������������֮�󣬸û�׼�ʹ������е��м�λ�á������Ϊ������partition��������
�ݹ�أ�recursive����С�ڻ�׼ֵԪ�ص������кʹ��ڻ�׼ֵԪ�ص�����������
"""


def quick_sort(list):
    """��������"""
    less = []
    pivotList = []
    more = []
    # �ݹ����
    if len(list) <= 1:
        return list
    else:
        # ����һ��ֵ��Ϊ��׼
        pivot = list[0]
        for i in list:
            # ���ȼ�תС��ֵ�ŵ�less����
            if i < pivot:
                less.append(i)
            # ���Ȼ�׼���ֵ�ŵ�more����
            elif i > pivot:
                more.append(i)
            # ���ͻ�׼��ͬ��ֵ�����ڻ�׼����
            else:
                pivotList.append(i)
        # ��less���к�more���м�����������
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more
