class Anagram:
    def __init__(self, word):
        self.word=word
        
    def match(self, list):
        word_list = [letter for letter in self.word]
        
        def check_match(item):
            item_list = [letter for letter in item]
            return "matched" if sorted(word_list) == sorted(item_list) else "not a match"
      
        matches = [item for item in list if check_match(item) == "matched"]
        
        return matches