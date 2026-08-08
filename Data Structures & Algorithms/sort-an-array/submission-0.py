class Solution:
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        l = len(left)
        r = len(right)
        i = 0
        j = 0
        while i < l and j < r:
            if left[i] <= right[j]:
                left.append(left[i])
                i += 1
            else:
                left.append(right[j])
                j += 1
        if i < l:
            left += left[i:l]
        if j < r:
            left += right[j:]
        return left[l:]

    def mergesort(self, l: List[int]) -> List[int]:
        n = len(l)
        if n <= 1:
            return l
        left = self.mergesort(l[:n//2])
        right = self.mergesort(l[n//2:])
        return self.merge(left, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
        # selectionsort
        # worst: n^2
        # average: n^2
        # best: n^2
        # memory: 1
        # in-place
        # not stable

        # insertionsort
        # worst: n^2
        # average: n^2
        # best: n
        # memory: 1
        # in-place
        # stable

        # mergesort
        # worst: nlogn | nlog^2n for inplace
        # average: nlogn | nlog^2n for inplace
        # best: nlogn | same for inplace
        # memory: n | logn for inplace
        # not in-place
        # stable

        # quicksort
        # worst: n^2 due to sorted/reverse sorted/same elements/data patterns (eg: sawtooth pattern)
        # average: nlogn
        # best: nlogn
        # memory: logn
        # in-place
        # not stable

        # refer https://en.wikipedia.org/wiki/Sorting_algorithm
        # for all comparison sorting, non-comparison sorting and other sorting
        # total 43 listed as of typing this.

# Summary of Critical Sorting Algorithms
#
# | Algorithm    | Primary Use Case                  | Key Systems/Languages           | Critical Advantage                 |
# | :---         | :---                              | :---                            | :---                               |
# | Timsort      | General-purpose, Real-world data  | Python, Java (Objects), Android | Adaptive, Stable                   |
# | Introsort    | General-purpose, In-place         | C++ (std::sort), .NET, C#       | Fast average & worst-case          |
# | QuickSort    | Primitives, In-memory DB ops      | Java (Primitives), JS Engines   | Cache efficient, Low overhead      |
# | Merge Sort   | External sorting, Linked Lists    | Databases, C++ (stable_sort)    | Stable, Works with sequential I/O  |
# | Heap Sort    | Real-time, Priority Queues        | RTOS, Introsort fallback        | Guaranteed O(n log n), O(1) space  |
# | Radix Sort   | Large integer/string sets         | Bioinformatics, Routing, GPUs   | O(n) for fixed-length keys         |
#
# Algorithms like Bubble Sort, Selection Sort, Insertion Sort (except as a subroutine), 
# Shell Sort, and Cycle Sort are generally excluded from modern high-performance critical paths, 
# appearing mostly in educational contexts or highly constrained embedded niches.   