import leer_datos
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
import graphviz

def predict(training,trainingLabels,testing,testingLabels,classifier,name):
    types = ["spam","non spam"]

    text_clf = Pipeline([
        ('vect',CountVectorizer()), #Bag of words
        ('tfidf',TfidfTransformer()), #transformacion tf-idf
        ('clf',classifier) #clasificador k vecino proximos
    ])

    #se entrena el clasificador
    text_clf.fit(training,trainingLabels)

    #se clasifican los datos de testing
    predicted = text_clf.predict(testing)

    #se calcula el porcentaje de bien clasificados
    well_clasified = 0
    for pred,value in zip(predicted,testingLabels):
        if pred == value:
            well_clasified += 1

    print(name,(well_clasified/327)*100)

    return predicted

if __name__ == "__main__":
    labels = leer_datos.readClasses()

    #se leen los datos de entrenamiendo.
    training = leer_datos.readTexts(0,4000)
    trainingLabels =labels[0:4000]
    print("leidos los datos de entrenamiendo.")

    #se obtienen los datos de testing
    testing = leer_datos.readTexts(4000)
    testingLabels = labels[4000:]
    print("Se terminaron de leer los datos de testing.")

    classifiers = [
        MultinomialNB(),
        BernoulliNB(),
        svm.SVC(kernel='linear'),
        svm.SVC(kernel='sigmoid'),
        svm.SVC(kernel='poly'),
        KNeighborsClassifier(n_neighbors=3),
        tree.DecisionTreeClassifier(),
        BaggingClassifier(KNeighborsClassifier(n_neighbors=3),
                             max_samples=0.5, max_features=0.5),
        RandomForestClassifier(n_estimators=100),
        AdaBoostClassifier(n_estimators=100)
    ]

    names = [
        "MultinomialNB",
        'BernoulliNB',
        'linear svm',
        'sigmoid svm',
        'poly svm',
        'k neightbours',
        'decision tree',
        'bagging with k neightbours',
        'random forest',
        'adaboost'
    ]

    for i in range(len(classifiers)):
        predict(training,trainingLabels,testing,testingLabels,classifiers[i],names[i])
