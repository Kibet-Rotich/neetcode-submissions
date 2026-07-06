class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedstring = []
        for text in strs:
            encodedstring.append(str(len(text))+"#"+text)
        return "".join(encodedstring)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i< len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])

            start = j+1
            end = start+length

            parsed = s[start:end]

            decoded.append(parsed)
            i = end
        return decoded