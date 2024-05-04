import time

class CompoundWordFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.words_set = set()

    def read_words_from_file(self):
        with open(self.file_path, 'r') as file:
            self.words = [line.strip() for line in file]
        self.words_set = set(self.words)

    def is_construction_possible(self, word, is_original=True):
        if word in self.words_set and not is_original:
            return True
        
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in self.words_set and self.is_construction_possible(suffix, is_original=False):
                return True
        return False

    def find_longest_compound_words(self):
        self.read_words_from_file()
        self.words.sort(key=len, reverse=True)
        
        longest_word, second_longest_word = None, None
        for word in self.words:
            if self.is_construction_possible(word):
                if longest_word is None:
                    longest_word = word
                elif second_longest_word is None:
                    second_longest_word = word
                    break
        return longest_word, second_longest_word

if __name__ == "__main__":
    file_paths = ["Input_01.txt", "Input_02.txt"]
    for file_path in file_paths:
        print(f"Results for {file_path}:")
        finder = CompoundWordFinder(file_path)
        start_time = time.time()
        longest, second_longest = finder.find_longest_compound_words()
        print(f"1. Longest Compound Word: {longest}")
        print(f"2. Second Longest Compound Word: {second_longest}")
        print(f"Time taken: {time.time() - start_time:.4f} seconds\n")
