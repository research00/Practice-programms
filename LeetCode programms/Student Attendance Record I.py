class Solution:
    def checkRecord(self, s: str):
        s = s.upper()
        if ("LLL" in s):
            return False
        elif s.count("A") >= 2:
            return False
        else:
            return True


def main():
    s = 'sdsaglllsgsdav'
    print(Solution.checkRecord(Solution, s))

if __name__ == '__main__':
    main()
