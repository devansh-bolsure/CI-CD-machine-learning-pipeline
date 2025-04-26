import gradio as gr
import skops.io as sio
import pandas as pd
import numpy as np
file_path='Model/drug_pipeline.skops'

#open the file in binary mode to get all untrusted types

with open(file_path,'rb') as f:
    untrusted=sio.get_untrusted_types(file=f)

with open(file_path,'rb') as f:
    model = sio.load(file=f, trusted=untrusted)
pipe = model

def predict_drug(age,sex,blood_pressure,cholestrol,na_to_k_ratio):
    '''
    Predict drugs based on patient features
    Args:
        age (int): Age of patient
        sex (str): Sex of patient
        blood_pressure (str): Blood pressure level
        cholesterol (str):Cholesterol level 
        na_to_k_ratio (float): Ratio of sodium to potassium in blood
    Returns:
        str: Predicted drug label
    '''
    if na_to_k_ratio is None or na_to_k_ratio == "":
        return "Error: Na_to_K value is missing!"
    
    features=[age,sex,blood_pressure,cholestrol,na_to_k_ratio]
    predicted_drug=pipe.predict([features])[0]
    
    label=f'predicted drug: {predicted_drug}'
    
    return label

inputs=[
    gr.Slider(15,74,step=1,label='Age'),
    gr.Radio(['M','F'],label='Sex'),
    gr.Radio(['HIGH','LOW','NORMAL'],label='Blood Pressure'),
    gr.Radio(['HIGH','NORMAL'],label='cholestrol'),
    gr.Slider(6.2,38.2,step=0.1,label='Na_to_K_Ratio')
]
outputs=[gr.Label(num_top_classes=5)]

examples=[
    [30, "M", "HIGH", "NORMAL", 15.4],
    [35, "F", "LOW", "NORMAL", 8],
    [50, "M", "HIGH", "HIGH", 34]
]

title="Drug Classification"
description="Enter the details to correctly identify Drug type?"
article='This app is a part of a simple CI/CD maachine learning project. it uses github Actions for automation and Huggingface for deployment'

gr.Interface(
    fn=predict_drug,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    
    description=description,
    article=article,
    theme=gr.themes.Soft(),
    
).launch()

