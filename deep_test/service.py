import joblib
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class Wine:
    def __init__(self, a, b, c, d):
        self.volatile_acidity = a
        self.citric_acid = b
        self.sulphates = c
        self.alcohol = d

class Service:
    def getResult(self, wine:Wine):
        model = joblib.load('winequality_model.pkl')  #모델 파일 로드
        res = model.predict(np.array([[wine.volatile_acidity, wine.citric_acid, wine.sulphates, wine.alcohol]]))
        print(res)
        return res

    def getResult2(self, wine:Wine):
        model = torch.load(f='wine_torch.pt')  #모델 파일 로드
        data = torch.FloatTensor([[wine.volatile_acidity, wine.citric_acid, wine.sulphates, wine.alcohol]])
        pred = model(data)
        res = F.softmax(pred, dim=1).argmax(dim=1)
        print(res)
        return res