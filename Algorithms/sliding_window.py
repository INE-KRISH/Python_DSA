#hard question based on sliding window
# Substring with Concatenation of All words:
import collections


class Solution(object):
    def findSubstring(self, s, words):
        if len(words)==0:
            return []
        K = len(words[0])
        N = len(s)
        W = len(words)
        ans = []
        
        def increment(word, number, counter):
            count[word] += number
            if count[word] == 0:
                del count[word]
        
        for start in range(K):
            current = start
            if current + W * K >N:
                continue
            count = collections.Counter()
            
            for word in words:
                count[word] += 1
            
            for _ in range(W):
                increment(s[current:current+K], -1, count)
                current += K
            
            if len(count) == 0:
                ans.append(current - (W*K))
                
            #sliding part
            while current + K <= N:
                increment(s[current:current+K], -1, count)
                increment(s[current-(W*K):current-((W-1)*K)], +1, count)
                current += K
                if len(count) == 0:
                    ans.append(current -(W*K))
        return ans