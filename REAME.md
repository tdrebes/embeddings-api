# Embeddings Generation API

```bash
conda create -n embeddings_api python=3.10
conda activate embeddings_api
pip install -r requirements.txt
python download_models.py
```

# Build
```bash
docker image build -t embeddings_api .
```

# Run

```bash
docker run -p 5000:5000 embeddings_api
```
