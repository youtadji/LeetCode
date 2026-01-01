class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join(map(str, digits))

        number = int(s)
        number += 1
        result = map(int, str(number))
        return result
