class Solution:

    # abcd\r\ns1s2s3s4
    def encode(self, strs: List[str]) -> str:
        lengths = ""
        literals = ""

        if not strs:
            return ""

        for s in strs:
            lengths += f'{str(len(s))}-'
            literals += s
        
        return f'{lengths}\r\n{literals}'


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
            
        lengths = []
        literals = ""
        decoded = []

        prev_r = False
        for i, l in enumerate(s):
            if l == '\n' and prev_r:
                lengths = s[:i-2].split("-")
                literals = s[i+1:]
                break
            elif l == '\r':
                prev_r = True
            else:
                prev_r = False

        i = 0
        for l in lengths:
            n = int(l)
            decoded.append(literals[i : i + n])
            i += n
        
        return decoded

