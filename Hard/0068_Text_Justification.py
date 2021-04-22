class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        temp = []
        leng = 0

        for i in range(len(words)):
            if len(words[i]) == maxWidth:
                if leng != 0:
                    res.append(self.mergeString(temp, maxWidth))

                res.append(words[i])
                temp = []
                leng = 0
            elif leng + len(words[i]) + 1 > maxWidth:
                res.append(self.mergeString(temp, maxWidth))
                temp = [words[i]]
                leng = len(words[i])
            else:
                temp.append(words[i])
                if leng == 0:
                    leng = len(words[i])
                else:
                    leng += len(words[i]) + 1

        if leng:
            res.append(self.mergeString(temp, maxWidth))

        res[-1] = " ".join(res[-1].split())
        res[-1] += (maxWidth - len(res[-1])) * " "

        return res

    def mergeString(self, words: List[str], maxWidth: int) -> str:
        if len(words) == 0:
            return

        res = ""
        blank_total = maxWidth - len(''.join(words))

        if len(words) > 1:
            blank_mid = blank_total // (len(words) - 1) * " "
            blank_extra = blank_total % (len(words) - 1)

            for i in range(len(words)):
                if i < len(words) - 1:
                    if i < blank_extra:
                        res += words[i] + blank_mid + " "
                    else:
                        res += words[i] + blank_mid
                else:
                    res += words[i]
        else:
            res = words[0] + (maxWidth - len(words[0])) * " "

        return res


