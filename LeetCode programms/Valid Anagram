class Solution:

    def isAnagram(self, s: str, t: str):
        """the function finds out if one string
        is an anagram of another string"""
        s_temp = list(s)
        s_temp.sort()
        t_temp = list(t)
        t_temp.sort()
        flag = True
        if not Solution.len_checker(Solution, s, t):
           return False
        for i in range(len(s)):
            if s_temp[i] != t_temp[i]:
                flag = False
        return flag

    def len_checker(self, s: str, t: str):
        """the function compares the length of the
        given strings, if they are not equal, the program returns false"""
        if len(s) != len(t):
            return False
        return True


def main():
    # s = input()
    # t = input()
    s = "anagram"
    t = "nagaram"
    print(Solution.isAnagram(Solution, s, t))
    return Solution.isAnagram(Solution, s, t)

if __name__ == '__main__':
    main()
