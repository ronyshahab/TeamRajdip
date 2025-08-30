# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.getenv("Apikey")

format_structured_data = ''
format_structured_data_1 = ''
format_structured_data_2 = ''
format_structured_data_3 = ''
format_structured_data_4 = ''

with open("format.txt", "r") as file:
    format_structured_data = file.read()




def generate(place):
    client = genai.Client(
        api_key=(api_key),  # <-- better to load from env var
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text="Identifying where to grow in surat, gujrat the hydrogen ecosystem  do Cost Estimation: Land price Refinery setup (detailed breakdown) Pipelines Labour Transportation Raw materials Time estimation (setup duration)  and show the data of all existing/planned assets (plants, storage, pipelines, distribution hubs) and uses data-driven models to guide new investments. just give answer in good html format and add location of place using and also make pineline using leaftlet.js"
                ),
            ],
        ),

        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text= format_structured_data)
                 ],    
         ), 

        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"Identifying where to grow in {place} the hydrogen ecosystem, do Cost Estimation: Land price Refinery setup (detailed breakdown) Pipelines Labour Transportation Raw materials Time estimation (setup duration) and show the data of all existing/planned assets (plants, storage, pipelines, distribution hubs) and uses data-driven models to guide new investments. just give answer in good html format and add location of place using leaftlet.js"
                ),
            ],
        ),


    ]

    tools = [
        types.Tool(
            googleSearch=types.GoogleSearch()
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
    )

    # Instead of streaming, call generate_content
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Print the full response at once
    return(response.text)


