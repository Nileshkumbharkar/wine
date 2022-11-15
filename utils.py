import pickle
import numpy as np
import os
# path = os.path.join(r"C:\Users\hp\AppData\Local\Programs\Python\Flask_python_framwork\My_Wine_Randomforest_API\Project_Wine","rf_model.pkl")



class Wine():
    def __init__(self,alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols,proanthocyanins, color_intensity, hue,
       diluted_wines, proline):
        self.alcohol = alcohol
        self.malic_acid = malic_acid
        self.ash = ash
        self.alcalinity_of_ash = alcalinity_of_ash
        self.magnesium = magnesium
        self.total_phenols = total_phenols
        self.flavanoids = flavanoids
        self.nonflavanoid_phenols = nonflavanoid_phenols
        self.proanthocyanins = proanthocyanins
        self.color_intensity = color_intensity
        self.hue = hue
        self.diluted_wines = diluted_wines
        self.proline = proline
       

    def load_model(self):
        
        with open('rf_model1' ,'rb') as f :
            self.rf_model = pickle.load(f)

    def get_predict(self):
        self.load_model()
        test = np.zeros(13)
        test[0]=self.alcohol 
        test[1]=self.malic_acid 
        test[2]=self.ash
        test[3]=self.alcalinity_of_ash 
        test[4]=self.magnesium 
        test[5]=self.total_phenols 
        test[6]=self.flavanoids 
        test[7]=self.nonflavanoid_phenols 
        test[8]=self.proanthocyanins
        test[9]=self.color_intensity 
        test[10]=self.hue 
        test[11]=self.diluted_wines 
        test[12]=self.proline 

        predict_wine = self.rf_model.predict([test])[0]
        return predict_wine


if __name__ == '__main__':
    wine = Wine()