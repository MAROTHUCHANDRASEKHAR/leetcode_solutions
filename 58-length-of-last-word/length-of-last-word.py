class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces
        s = s.rstrip()

        # Find the index of the last space
        last_space_index = s.rfind(' ')

        # If no space is found, the whole string is the last word
        if last_space_index == -1:
            return len(s)
        else:
            # The length of the last word is from the last space to the end
            return len(s) - last_space_index - 1

