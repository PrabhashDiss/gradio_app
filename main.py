import gradio as gr
from fastapi import FastAPI

# Define a simple Gradio function
def echo(text):
    return text

# Create Gradio interface
gradio_app = gr.Interface(fn=echo, inputs="text", outputs="text", allow_flagging="never")

# Create FastAPI app
app = FastAPI()

# Mount Gradio app
app = gr.mount_gradio_app(app, gradio_app, path="/gradio")

@app.get("/")
def read_root():
    return {"message": "Gradio app is running at /gradio"}
