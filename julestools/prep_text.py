import string
string.punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer

def clean_text(text):
    for punctuation in string.punctuation:
           text = text.replace(punctuation, '')

    text = text.lower()
    text = ''.join(word for word in text if not word.isdigit())
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    text = [w for w in word_tokens if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in text]
    text = lemmatized
    text = ' '.join(text)
    return text

if __name__ == '__main__':
    clean_text(text)
