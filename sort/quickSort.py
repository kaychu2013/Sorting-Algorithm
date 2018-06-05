from timeit import timeit
from sort import util


def quick_sort(seq, start, end):
    if start < end:
        i, j = start, end
        base = seq[i]

        while i < j:
            while (i < j) and (seq[j] >= base):
                j = j - 1

            seq[i] = seq[j]

            while (i < j) and (seq[i] <= base):
                i = i + 1
            seq[j] = seq[i]
        seq[i] = base

        quick_sort(seq, start, i - 1)
        quick_sort(seq, j + 1, end)
    return seq


seq = util.random_int_list(1, 10, 10)
print("random seq : ", seq)
quick_sort(seq, 0, len(seq) - 1)
print("sorted seq : ", seq)
