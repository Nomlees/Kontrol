import random
import timeit


class Sort:

    @staticmethod
    def bubble(self, arr):
        for i in range(len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def shell(self, arr):
        step = len(arr) // 2
        while step:
            for i in range(len(arr) - step):
                j = i
                while j >= 0 and arr[j] > arr[j + step]:
                    arr[j], arr[j + step] = arr[j + step], arr[j]
                    j = j - step
            step = step // 2
        return arr

    def insert(self, arr):
        n = len(arr)
        for i in range(1, n):
            current_value = arr[i]
            j = i - 1
            while j >= 0:
                if current_value < arr[j]:
                    arr[j + 1] = arr[j]
                    arr[j] = current_value
                    j = j - 1
                else:
                    break
        return arr

    def counting_time(self, namesort):
        """Метод считает.
        """
        timerand = dict()
        timeinc = dict()
        timedec = dict()
        for n in range(100000, 1000000 + 1, 100000):  # тут задаются размер и шаг массивов
            # по условию задачи размер массива 100к-1М элементов с шагом 100к элементов

            rand = [random.randint(0, 1000) for i in range(n)]
            inc = [random.randint(0, 1000) for i in range(n)]
            inc.sort()
            dec = [random.randint(0, 1000) for i in range(n)]
            dec.sort(reverse=True)

            start_time_rand = timeit.default_timer()
            namesort(self, rand)
            timerand[n] = timeit.default_timer() - start_time_rand

            start_time_inc = timeit.default_timer()
            namesort(self, inc)
            timeinc[n] = timeit.default_timer() - start_time_inc

            start_time_dec = timeit.default_timer()
            namesort(self, dec)
            timedec[n] = timeit.default_timer() - start_time_dec

        return timerand, timeinc, timedec

"""
    def partition(self, nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def quick_sort(self, nums):
        def _quick_sort( items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = Sort.partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)
        _quick_sort(nums, 0, len(nums) - 1)
"""