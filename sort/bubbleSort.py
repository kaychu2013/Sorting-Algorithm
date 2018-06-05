from timeit import timeit
from sort import util


def bubble_sort():
    seq = util.random_int_list(1, 100, 20)
    print("random seq : ", seq)
    for i in range(len(seq)):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    print("sorted seq : ", seq)
    return seq


print("bubble sort : ")
print("time for 10 times : ", timeit('bubble_sort()', 'from __main__ import bubble_sort', number=10))
print("=================================================================")
