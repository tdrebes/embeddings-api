from sentence_transformers import SentenceTransformer

modelPath = 'model'
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
model.save(modelPath)
model = SentenceTransformer(modelPath)
