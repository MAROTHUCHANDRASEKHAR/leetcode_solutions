
class Solution:
    def clearStars(self, s: str) -> str:
            
        ch_stacks = dict()
        for ch in string.ascii_lowercase:
            ch_stacks[ch] = []
        
        keep = [True] * len(s)

        ch_in_stack = [] 

        for idx, ch in enumerate(s):
            if ch == '*':
                keep[idx] = False
                keep[ch_stacks[ch_in_stack[0]].pop()] = False
                
                if not ch_stacks[ch_in_stack[0]]:
                    heapq.heappop(ch_in_stack)
            else:
                if not ch_stacks[ch]:
                    heapq.heappush(ch_in_stack, ch)

                ch_stacks[ch].append(idx)

        return ''.join([ch for is_keep, ch in zip(keep, s) if is_keep])