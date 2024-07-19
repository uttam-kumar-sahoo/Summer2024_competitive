#This is code for leetcode daily problem for 19th July and problem number is 1380 finding lucky number in a matrix


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_ = {min(each) for each in matrix}
        max_ = {max(row)for row in zip(*matrix)}
        return min_.intersection(max_)
        