class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def hashtable(s):
            res = []
            idx = defaultdict(int)
            for i, c in enumerate(s):
                idx[c] = i
                
            start = 0
            end = idx[s[0]]
            if end == len(s) - 1:
                return [len(s)]

            for i , c in enumerate(s):
                if i == end and i < len(s) - 1:
                    res.append(end - start + 1)
                    start = end + 1
                    end = idx[s[i+1]]
                    continue
                end = max(end, idx[c])
                if end == len(s) - 1:
                    res.append(end - start + 1)
                    break
            return res

        def brute_force(s):
            res = []
            start = 0
            end = 0
            for i in range(len(s)):
                end = max(end, s.rfind(s[i]))
                if i == end:
                    res.append(end - start + 1)
                    start = end + 1
            return res
        
        def merge_interval(s):
            startInterval = {}
            endInterval = {}
            for i, c in enumerate(s):
                if c in startInterval:
                    endInterval[c] = i
                else:
                    startInterval[c] = i
                    
            interval = []
            for c in startInterval:
                if c in endInterval:
                    interval.append([startInterval[c], endInterval[c]])
                else:
                    interval.append([startInterval[c], startInterval[c]])
                    
                    
            res = []
            start = interval[0][0]
            end = interval[0][1]
            for i in range(1, len(interval)):
                if interval[i][0] > end: # find partition, current start is larger than previous end
                    res.append(end - start + 1)
                    start = interval[i][0]
                    end = interval[i][1]
                else: # extend end
                    end = max(end, interval[i][1])
            res.append(end - start + 1)
            return res
                    
        
        return merge_interval(s)