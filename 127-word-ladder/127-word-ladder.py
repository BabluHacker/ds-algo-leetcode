
class Solution:
    def __init__(self):
        self.g = defaultdict(list)
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord not in wordList:
            wordList.append(beginWord)
        self.construct_graph(wordList)
        
        queue = [beginWord]
        visited = set([beginWord])
        
        dist = {}
        dist[beginWord] = 0
        
        while queue:
            
            node = queue.pop(0)
            
            if node == endWord:
                return dist[node]+1
                   
            print(node, end=" ")
            for i in range(len(node)):
                pattern = node[:i]+"*"+node[i+1:]
                for w in self.g[pattern]:
                    if w not in visited:
                        queue.append(w)
                        visited.add(w)
                        dist[w] = 1 + dist[node]

        return 0
    
    
    def construct_graph(self, words):
        for word in words:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                self.g[pattern].append(word)
        print(self.g)
            
    
    def find_diff(self, start, end):
        c = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                c += 1
        return c
        