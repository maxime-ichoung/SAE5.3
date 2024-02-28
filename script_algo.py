import pickle
import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier

with open('data/visages.pkl', 'rb') as fh:
    visages = pickle.load(fh)

with open('data/noms.pkl', 'rb') as fh:
    noms = pickle.load(fh)

print('Shape of visages matrix --> ', visages.shape)

N = len(noms)

visages = visages.reshape(N, -1)

knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(visages, noms)

cascade_visage = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0) # 0 pour 'built-in' caméra, 1 pour caméra externe

while True:
    
    ret, trame = camera.read()
    if ret == True:
        
        gris = cv2.cvtColor(trame, cv2.COLOR_BGR2GRAY)
        
        # Ajustez les paramètres ici
        coordonnees_visage = cascade_visage.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in coordonnees_visage:
            visage = trame[y:y + h, x:x + w, :]
            visage_redimensionne = cv2.resize(visage, (50, 50)).flatten().reshape(1,-1)
            
            texte = knn.predict(visage_redimensionne)

            if texte[0] in noms:
                statut = texte[0]
            else:
                statut = "Non admis"
            print(statut)

            cv2.putText(trame, statut, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.rectangle(trame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('Reconnaissance faciale en temps réel', trame)
        
        if cv2.waitKey(1) == 27:
            break
            
    else:
        
        print("erreur")
        break

cv2.destroyAllWindows()
camera.release()
