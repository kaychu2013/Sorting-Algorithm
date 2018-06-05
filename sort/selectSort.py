from timeit import timeit
from sort import util


def select_sort():
    seq = util.random_int_list(1, 100, 20)
    print("random seq : ", seq)
    for i in range(0, len(seq)):
        min_num = i
        for j in range(i, len(seq)):
            if seq[j] < seq[min_num]:
                min_num = j
        seq[min_num], seq[i] = seq[i], seq[min_num]
    print("sorted seq : ", seq)
    return seq


print("select sort : ")
print("time for 10 times : ", timeit('select_sort()', 'from __main__ import select_sort', number=10))
print("=================================================================")
