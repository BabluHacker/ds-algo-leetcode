class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        strs1 = []
        for s in strs:
            encoded = str(len(s)) + '#' + s
            strs1.append(encoded)
        # print(strs1)
        return "".join(strs1)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i, decoded = 0, []
        print(s)
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j += 1
            # index j has #
            l = int(s[i:j]) # getting range bcz there could be "6433#hgsjhdghs...." length = 6433
            dummy = s[j+1 : j+l+1]
            decoded.append(dummy)
            # print(j+1, j+l+1)
            i = j+l+1
        # print(decoded)
        return decoded
        
        
            
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))