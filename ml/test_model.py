from model import Model

model = Model("../data/model.json", "../data/model.h5")

print(model.predict([1,1,1]))