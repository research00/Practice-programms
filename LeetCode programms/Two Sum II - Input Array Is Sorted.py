class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)):
            if (nums[i] == 0) and (nums[i] + nums[i + 1] != target):
                continue

            if nums[i] > target:
                return("Not found")
            else:
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        res.append(i+1)
                        res.append(j+1)
                        return res
        return ("not found")
    
def main():
    nums = [1, 2, 3, 4]
    target = 5
    a = Solution.twoSum(Solution, nums, target)
    print(a)

if __name__ == '__main__':
    main()
