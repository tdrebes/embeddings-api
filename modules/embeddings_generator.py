import numpy as np
from sentence_transformers import SentenceTransformer
from nltk import sent_tokenize, download, data
from modules.exception.mode_exception import ModeException

class EmbeddingsGenerator():
    def __init__(self, model_path='model', device='cpu'):
        self.model = SentenceTransformer(model_path).to(device=device)

        try:
            data.find('tokenizers/punkt')
            print('Tokenizer punkt already installed.')
        except:
            print('Downloading punkt tokenizer...')
            download('punkt')

    def generate_embedding(self, input, mode = 'mean'):
        sentences = sent_tokenize(input)
        embeddings = self.model.encode(sentences)

        match mode:
            case 'mean':
                return np.mean(embeddings, axis=0)
            case 'max':
                return np.max(embeddings, axis=0)
            case 'min':
                return np.min(embeddings, axis=0)
            case _:
                raise ModeException('Invalid mode')
