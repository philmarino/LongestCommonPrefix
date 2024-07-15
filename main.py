def longestCommonPrefix(words):
    answer = ""
    shortest = min(len(word) for word in words)
    for i in range(0, shortest):
        thisLetter = words[0][i]
        for word in words:
            if word[i] != thisLetter:
                return answer
        answer += thisLetter
        
    return answer

#Example 1:
#Input: 
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
#Output: "fl"

#Example 2:
#Input: 
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
#Output: ""
#Explanation: There is no common prefix among the input strings.
