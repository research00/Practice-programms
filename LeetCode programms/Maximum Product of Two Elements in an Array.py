class Solution:
    def maxProduct(self, nums):
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        return (max1 - 1)*(max2 - 1)


def main():
    nums = [1,5,4,5]
    answer = Solution.maxProduct(Solution, nums)
    print(answer)
    return answer


if __name__ == '__main__':
    main()
