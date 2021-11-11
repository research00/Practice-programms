class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        def __init__(self):
            """Constructor"""
            pass
        res_arr = []
        all_int = nums1 + nums2 + nums3
        #print(all_int)
        for i in range(len(all_int)):
            tmp = all_int[i]
            if ((tmp in nums1 and tmp in nums2) or (tmp in nums1 and tmp in nums3) or (tmp in nums2 and tmp in nums3)):
                res_arr.append((tmp))
        tmp_set = set(res_arr)
        res_arr = list(tmp_set)
        return res_arr

def main():
    nums1 = [1, 2]
    nums2 = [2, 3]
    nums3 = [3, 4]
    print(Solution.twoOutOfThree(Solution, nums1, nums2, nums3))
    return Solution.twoOutOfThree(Solution, nums1, nums2, nums3)


if __name__ == '__main__':
    main()
