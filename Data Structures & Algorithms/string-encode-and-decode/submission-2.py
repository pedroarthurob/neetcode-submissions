class Solution:

    def encode(self, strs: List[str]) -> str:
        formatted = []
        for word in strs:
            formatted.append(f"{len(word)}#{word}")

        return "".join(formatted)

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):

            length = ""

            while i < len(s) and s[i] != '#':
                length += s[i]
                i += 1
            
            length = int(length)
            word_start = i + 1
            word_end = word_start + length 
            word = s[word_start:word_end]
            decoded.append(word)
            i = word_end

        return decoded
