
from collections import defaultdict

# Create a node with the current value
    # { char : TrieNode }

class TrieNode(defaultdict):
    def __init__(self):
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        
    def addWord(self, word: str) -> None:
        trie = self.trie
        
        for char in word:
            if char not in trie:
                trie[char] = TrieNode()
            trie = trie[char]
        
        trie.is_word = True

    def search(self, word: str) -> bool:
        return self.process_word(word, 0, self.trie)

    def process_word(self, word, index, current_node):
        if index == len(word) and current_node.is_word:
            return True

        if index == len(word) or (word[index] != '.' and word[index] not in current_node):
            return False
        
        if word[index] == '.':
            for next_character in current_node:
                if self.process_word(word, index + 1, current_node[next_character]):
                    return True
        else:
            return self.process_word(word, index + 1, current_node[word[index]])
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

