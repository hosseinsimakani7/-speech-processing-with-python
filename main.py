import nltk
from nltk.corpus import gutenberg

# بارگیری پیکره متنی
nltk.download('gutenberg')
corpus = gutenberg.sents()

# تبدیل لیست جملات به یک رشته متنی
corpus_text = ' '.join([' '.join(sent) for sent in corpus])

def check_sentence_presence(sentence, text):
    if sentence in text:
        return True
    else:
        return False

# جمله‌ای که می‌خواهید بررسی کنید
sentence_to_check = "This is a sample sentence to check."

# بررسی حضور جمله در پیکره
result = check_sentence_presence(sentence_to_check, corpus_text)

if result:
    print("جمله موردنظر یافت شد!")
else:
    print("جمله موردنظر یافت نشد!")
