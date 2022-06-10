class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        words = {}
        
        # 특수문자 제거 후 소문자 변환
        paragraph = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', paragraph)
        paragraph=paragraph.lower().split(" ")
        
        while '' in paragraph:
            paragraph.remove('')

        for word in paragraph:
            if word not in banned: 
                words[word]=paragraph.count(word)
                
        # value값이 가장 큰 순서대로 sort!
        words=sorted(words.items(), key=lambda x : x[1], reverse=True)
        
        print(words)
        
        # value 값이 큰 것 반환
        return words[0][0]
        
