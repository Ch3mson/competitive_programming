# Initial approach:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        if endWord not in wordList: return 0

        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        wordListSet = set(wordList)

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for w in wordListSet:
                if w not in visited and self.diff(word, w):
                    q.append((w, dist + 1))
                    visited.add(w)
        return 0


    def diff(self, word1, word2):
        differ = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differ += 1
        
        return differ == 1

# Optimal approach:

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
        if endWord not in wordList: return 0

        nei = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1
        
        return 0
