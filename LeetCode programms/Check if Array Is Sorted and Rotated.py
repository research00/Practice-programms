class Solution:
    def __init__(self):
            """Constructor"""
            pass

    def check(self, nums):
        tmp_nums = nums[:]
        tmp_nums.sort()
        for i in range(len(nums)):
            if tmp_nums[i:] + tmp_nums[:i] == nums:
                return True
        return False


def main():
    nums = [2,1,3,4]
    answer = Solution.check(Solution, nums)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
