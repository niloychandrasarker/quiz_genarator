from io import BytesIO

from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS



load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def note_genarator(images):
    prompt="""summarize the picture in notes formate at max 100 words,
        makesure to include all the important points and make it concise"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text

def audio_Transcription(text):
    speech = gTTS(text=text, lang='en', slow=False)

    audio_buffer = BytesIO()
    speech.write_to_fp(audio_buffer)
    
    return audio_buffer

def quiz_genarator(images, difficulty):
    prompt=f"""Genarate 5 quiz questions based on the picture with the given {difficulty} difficulty level.
        Make sure the questions are relevant to the content of the picture and are appropriate for the selected difficulty level...please provide mcq formate quiz
        make sure add markdown format in the question and answer"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text