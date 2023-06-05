# Mock Interview with Tural Ismayilzade (Oracle)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_map = Counter(words)
        lenght_of_permutation = len(words[0]) * len(words)
        word_length = len(words[0])
        output = []

        for i in range(len(s) - lenght_of_permutation + 1):
            j = i
            temp_map = word_map.copy()
            string = ""

            while j < i + lenght_of_permutation:
                while len(string) < word_length:
                    string += s[j]
                    j += 1
                
                if string in temp_map:

                    temp_map[string] -= 1

                    if temp_map[string] == 0:
                        del temp_map[string]

                    if not temp_map:
                        output.append(i)

                    string = ""
                else:
                    string = ""
                    break
    
                string = ""
            
        return output
