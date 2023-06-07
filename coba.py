class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class SpellChecker:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def get_corrections(self, word, max_distance=1):
        corrections = []
        stack = [(self.root, "", word, max_distance)]

        while stack:
            node, prefix, current_word, distance = stack.pop()

            if distance < 0:
                continue

            if current_word == "":
                if node.is_word:
                    corrections.append(prefix)
                continue

            if current_word[0] in node.children:
                stack.append(
                    (node.children[current_word[0]], prefix + current_word[0], current_word[1:], distance)
                )

            if distance > 0:
                for char, child in node.children.items():
                    stack.append(
                        (child, prefix + char, current_word, distance - (char != current_word[0]))
                    )

        return corrections


# Example usage
spellchecker = SpellChecker()

# Build the dictionary
dictionary = [
    "apple", "banana", "orange", "peach", "grape", "kiwi", "mango", "watermelon",
    "strawberry", "blueberry", "pineapple", "cherry", "pear", "lemon", "lime"
]
for word in dictionary:
    spellchecker.insert(word)

# Spell-check a word and get corrections
input_word = "gape"
corrections = spellchecker.get_corrections(input_word, max_distance=1)
print("Input Word:", input_word)
print("Corrections:", corrections)
