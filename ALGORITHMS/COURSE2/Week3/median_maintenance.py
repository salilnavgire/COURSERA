from heapq import *


class Heap:
    def __init__(self):
        self.h1_priority_list = []
        self.h2_priority_list = []
        self.count = 0
        self.medians = []

    def rebalance_heaps(self):
        if (len(self.h1_priority_list) - len(self.h2_priority_list)) > 1:
            node = heappop(self.h1_priority_list)
            heappush(self.h2_priority_list, ~node + 1)
        else:
            node = heappop(self.h2_priority_list)
            heappush(self.h1_priority_list, ~node + 1)

    def calculate_median(self):
        if self.count % 2 != 0:
            if len(self.h1_priority_list) > len(self.h2_priority_list):
                self.medians.append(~self.h1_priority_list[0] + 1)
            else:
                self.medians.append(self.h2_priority_list[0])
        else:
            self.medians.append(~self.h1_priority_list[0] + 1)

    def median_maintenance(self, file='test1.txt'):
        fp = open(file)
        for data in fp.readlines():
            # print(int(foo.strip()))
            foo = int(data.strip())
            # print(foo, ~foo + 1)
            self.count += 1
            if not self.h1_priority_list:
                heappush(self.h1_priority_list, ~foo + 1)
            # elif not self.h2_priority_list:
            #     heappush(self.h2_priority_list, foo)
            # elif foo >= self.h2_priority_list[0]:
            #     heappush(self.h2_priority_list, foo)
            elif foo < ~self.h1_priority_list[0] + 1:
                heappush(self.h1_priority_list, ~foo + 1)
            else:
                heappush(self.h2_priority_list, foo)
            while abs(len(self.h1_priority_list) -
                      len(self.h2_priority_list)) > 1:
                self.rebalance_heaps()
            self.calculate_median()
            # print(h.h1_priority_list)
            # print(h.h2_priority_list)
            # print(h.medians)
            # print()


if __name__ == '__main__':
    h = Heap()
    h.median_maintenance(file='test2.txt')
    print(h.h1_priority_list)
    print(h.h2_priority_list)
    print(h.medians, sum(h.medians) % 10000)
    # test1 142
    # test2 9355
    # test4 717
