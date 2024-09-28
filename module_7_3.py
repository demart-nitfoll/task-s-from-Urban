class WordsFinder:
    def __init__(self, *args: str):
        self.file_names = args
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                strf = file.read()
                strf = strf.lower()
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    strf = strf.replace(punct, '')
                all_words[i] = strf.split()
        return all_words
    def find(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res
    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            res[name] = 0
            for i in words:
                if word.lower() == i:
                    res[name] += 1
        return res

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего