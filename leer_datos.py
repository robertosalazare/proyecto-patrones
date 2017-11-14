from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    """textos = []
    for i in range(4292):
        n = str(i)
        f = open("datos/TESTING_NEW/TEST_" + n.zfill(5) + ".eml","r")
        cadena = f.read()
        soup = BeautifulSoup(cadena, 'html.parser')
        textos.append(soup.get_text())"""
    eliminar = ['.', ';', ':', '!', '?', '/', '\\', ',', ')', '(', "\"","-",'*','_',"|"]
    f = open("datos/TESTING_NEW/TEST_00005.eml","r")
    texto = f.read()
    texto = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',texto)
    texto = BeautifulSoup(texto,'html.parser').get_text()
    #texto = ' '.join(texto.split())
    #texto = texto.lower()
    #texto = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','',texto)
    texto = re.sub(r'[\w\.-]+@[\w\.-]+', " ", texto)
    texto = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', ' ',  texto)
    #for e in eliminar:
    #    texto = texto.replace(e,'')
    #texto = ' '.join(texto.split())
    print(texto)