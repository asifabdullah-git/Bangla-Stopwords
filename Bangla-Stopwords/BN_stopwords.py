import words
from nltk.tokenize import word_tokenize

example_sent = "ইহা শুনতে ভালো লাগছে "

def sw(text):
    word_tokens = word_tokenize(text)
    #filtered_sentence = [w for w in word_tokens if not w in words.bn_stopwords]
    filtered_sentence = []

    for w in word_tokens:
        if w not in words.bn_stopwords:
            filtered_sentence.append(w)

    #print(word_tokens)
    print(filtered_sentence)



def test_func():
    test = "এটা খুব ভালো কাজ করেছ"
    #test = "i love you :###.."
    sw(test)


if __name__ == '__main__':
    text = "আমি একজন অপারগ, আমি বাঁচতে চাই না।"
    sw(text)





