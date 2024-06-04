# Gerekli kütüphanelerin ve araçların ithal edilmesi
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

def preprocess(line):
    ps = PorterStemmer()  # PorterStemmer nesnesi oluşturma

    # 1. Sadece harfleri bırakmak için metindeki diğer karakterleri boşluk ile değiştirme
    review = re.sub('[^a-zA-Z]', ' ', line)
    
    # 2. Tüm metni küçük harfe çevirme
    review = review.lower()
    
    # 3. Metni kelime listesine dönüştürme
    review = review.split()
    
    # 4. Stop kelimelerini kaldırma ve stemming uygulama
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    
    # 5. Kelime listesini tekrar cümleye dönüştürme
    review = ' '.join(review)
    
    return review
