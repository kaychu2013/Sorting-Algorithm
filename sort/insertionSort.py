from timeit import timeit
from sort import util


def insertion_sort():
    seq = util.random_int_list(1, 100, 20)
    print("random seq : ", seq)
    for i in range(1, len(seq)):
        j = i
        while j >= 1 and seq[j-1] > seq[j]:
            seq[j], seq[j-1] = seq[j-1], seq[j]
            j -= 1
    print("sorted seq : ", seq)
    return seq


print("insertion sort : ")
print("time for 10 times : ", timeit('insertion_sort()', 'from __main__ import insertion_sort', number=10))
print("=================================================================")
