
class Solution:
    def __init__(self):
        self.g = defaultdict(list)
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        self.construct(wordList)
        
        # print(self.g)
        
        q = [beginWord]
        visit = set([beginWord])
        dist = {}
        dist[beginWord] = 0
        
        
        while q:
            w = q.pop(0)
            l = len(w)
            
            if w == endWord:
                return dist[w]+1
            
            for i in range(l):
                pattern = w[:i]+'*'+w[i+1:]
                for child in self.g[pattern]:
                    if child not in visit:
                        q.append(child)
                        visit.add(child)
                        dist[child] = 1 + dist[w]
                        
        return 0
        
    def construct(self, words):
        for word in words:
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                self.g[pattern].append(word)
        
        
        