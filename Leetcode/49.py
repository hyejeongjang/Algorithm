class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=collections.defaultdict(list)
        
        for word in strs:
            j=''.join(sorted(word))
            anagram[j].append(word)
        # print(anagram)
        return anagram.values()
        
