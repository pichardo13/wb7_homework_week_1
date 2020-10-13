"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

#first attempt
# def reverseWords(s):
#     wordList = s.split(' ')

#     for i in range(len(wordList)):
#         wordList[i] = wordList[i][::-1]

#     return ' '.join(wordList)

#second attemp, much cleaner
def reverseWords(s):
    return ' '.join([i[::-1] for i in s.split(' ')])


input_1 = "Let's take LeetCode contest"
print(reverseWords(input_1) == "s'teL ekat edoCteeL tsetnoc")