from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import leer_datos

count_vect = CountVectorizer()
#se leen los datos de entrenamiendo.
training = leer_datos.readTexts(0,4000)
count_vect_train = count_vect.fit_transform(training)
print("Cantidad de palabras difenretes en los textos:", count_vect.vocabulary_.get(u'algorithm'))

tfidf_transformer = TfidfTransformer()
train_tfidf = tfidf_transformer.fit_transform(count_vect_train)