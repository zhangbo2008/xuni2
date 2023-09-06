import gradio as gr
import os


def video_identity(video):
    return 


demo = gr.Interface(video_identity,
                    gr.Video(), 
                    "playable_video",  outputs=None
                   )

if __name__ == "__main__":
    demo.launch()