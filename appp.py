import pickle

model = pickle.load(open(filename, "rb"))
X_new = np.array([[2000, 20], [10, 1000]])

y_new = model.predict(X_new)
