# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。
def longestCommonPrefix(strs:list): 
    s = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            s += i[0]
        else:
            break
    return s
longestCommonPrefix(["flower","flow","flight"])


strs = ["flower","flow","ight"]
def longestCommonPrefix1(strs:list): 
    s = strs[0]
    for i in range(1,len(strs)):
        while s not in strs[i]:
            s = s[:len(s) - 1]
            if s == '':
                return s
    return s
        