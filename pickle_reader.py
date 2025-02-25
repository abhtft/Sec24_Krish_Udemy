import pickle


# Read the model from the file
with open('artifacts/model.pkl', 'rb') as file:
    model = pickle.load(file)

