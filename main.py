from sentence_transformers import SentenceTransformer
import fire
import gradio as gr
import hashlib
import numpy as np
from numpy import dot
from numpy.linalg import norm

#np.set_printoptions(suppress=True)

#sentences = ["This is an example sentence", "Each sentence is converted"]
model_path = "sentence-transformers/all-MiniLM-L12-v2"
global model

def main(device="cpu", model_path=model_path):
    global model
    model = SentenceTransformer(model_path).to(device=device)
    print(f"Loaded model \"{model_path}\" using device \"{device}\"")

    gr.Interface(
        generate_embedding,
        title="Embeddings",
        theme=gr.themes.Monochrome(),
        #textbox=gr.Textbox(placeholder="input", container=False, scale=7, autofocus=True),
        inputs=[
            gr.Textbox(placeholder="input", container=False, scale=7, autofocus=True),
        ],
        outputs=[
            gr.Textbox(placeholder="output", container=False, scale=7, show_copy_button=True),
        ]
    ).queue().launch(share=False, server_port=8080)

def generate_embedding(input):
    global model
    print("Generating embedding for input: " + input)
    embeddings = model.encode(input)
    print(hashlib.md5(embeddings.__str__().encode('UTF-8')).hexdigest())

    return embeddings

if __name__ == "__main__":
    fire.Fire(main)
