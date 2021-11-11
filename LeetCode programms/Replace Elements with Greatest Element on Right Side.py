class Solution:
    def replaceElements(self, arr):
        for i in range(1, len(arr)):
            arr_sliced = arr[i:]
            arr[i - 1] = max(arr_sliced)
        arr[-1] = -1
        return arr

def main():
    arr = [17, 18, 5, 4, 6, 1]
    answer = Solution.replaceElements(Solution, arr)
    print(answer)
    return answer

if __name__ == '__main__':
    main()
