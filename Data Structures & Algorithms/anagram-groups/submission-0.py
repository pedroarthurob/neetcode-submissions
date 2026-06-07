class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            current_freq = [0] * 26
            for c in word:
                current_freq[ord(c)-97] += 1
            
            key = tuple(current_freq)
            if key in groups:
                groups[key].append(word)

            else:
                groups[key] = [word]

        return list(groups.values())

        