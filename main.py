# The main program file that orchestrates the AI assistant and handles user interactions.
from src import assistant
# import keyboard
import openai
import json
import os

# import sys

# JSON FILES IMPORT / API_KETS / PROMPTS
# Get the directory path where main_vocal.py is located
current_directory = os.path.dirname(__file__)
# Construct the file paths to the JSON files
api_keys_file_path = os.path.join(current_directory, 'config', 'api_keys.json')
prompts_file_path = os.path.join(current_directory, 'config', 'prompts.json')
# Load API keys configuration
with open(api_keys_file_path, 'r') as api_keys_file:
    api_keys_config = json.load(api_keys_file)

openai_api_key = api_keys_config["openai"]["api_key"]
openai.api_key = openai_api_key

with open(prompts_file_path, 'r') as config_file:
    config = json.load(config_file)

if __name__ == '__main__':
    # print("Start recording: Press 'r'\nStop recording: Press 'q'\nQuit program: Press 'Esc'")
    # speak("Cabinet dentaire du Docteur Carole Sion, bonjour. Comment puis-je vous aider?")

    # run the program ask for key to press
    eva = assistant.Assistant(config)

    while True:
        # voice_input.start_recording()
        user_input = input("user: ")
        response = eva.generate_answer(user_input)
        print("Eva: " + response)

    #     if keyboard.is_pressed('r'):  # Press 'r' to start recording
    #         voice_input.start_recording()
    #     #          print("user:", )
    #
    #     while keyboard.is_pressed('q'):
    #         audio_file = open("recorded_audio.wav", "rb")
    #         transcript = openai.Audio.transcribe("whisper-1", audio_file)
    #         user_input = transcript['text']
    #         print("User:", user_input)
    #         response = assistant.generate_response(user_input)
    #         print("Eva:", response)
    #         voice_output.speak(response)
    #         assistant.prompt += response
    #
    #     if keyboard.is_pressed('Esc'):
    #         audio_file = open("recorded_audio.wav", "rb")
    #         transcript = openai.Audio.transcribe("whisper-1", audio_file)
    #         user_input = transcript['text']
    #         print("User:", user_input)
    #         response = assistant.generate_response(user_input)
    #         voice_output.speak(response)
    #         print("Eva:", response)
    #         break
    #
    # print("Goodbye Eva!")
    # # Initialize the text-to-speech engine
