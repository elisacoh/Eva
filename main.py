# The main program file that orchestrates the AI assistant and handles user interactions.
from src import assistant, voice_output
#from src import voice_input #todo: remettre quand utilise vocal
import keyboard
import openai
import json
import os


# todo: change it to this implementation:
# import json
import sys
#
# def load_config(api_keys_file_path, prompts_file_path):
#     try:
#         with open(api_keys_file_path, 'r') as api_keys_file:
#             api_keys_config = json.load(api_keys_file)
#
#         with open(prompts_file_path, 'r') as prompts_file:
#             prompts_config = json.load(prompts_file)
#
#         return api_keys_config, prompts_config
#     except FileNotFoundError:
#         print("Error: Configuration file not found.")
#         sys.exit(1)
#
# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python main.py api_keys_file prompts_file")
#         sys.exit(1)
#
#     api_keys_file_path = sys.argv[1]
#     prompts_file_path = sys.argv[2]
#
#     api_keys_config, prompts_config = load_config(api_keys_file_path, prompts_file_path)
#
#     # Now you can access the loaded configuration data as needed.
#

#JSON FILES IMPORT / API_KETS / PROMPTS
# Get the directory path where main.py is located
current_directory = os.path.dirname(__file__)
# Construct the file paths to the JSON files
api_keys_file_path = os.path.join(current_directory, 'config', 'api_keys.json')
prompts_file_path = os.path.join(current_directory, 'config', 'prompts.json')
# Load API keys configuration
with open(api_keys_file_path, 'r') as api_keys_file:
    api_keys_config = json.load(api_keys_file)
# # Load prompts configuration
# with open(prompts_file_path, 'r') as prompts_file:
#     prompts_config = json.load(prompts_file)
# Access API keys
openai_api_key = api_keys_config["openai"]["api_key"]
# # Access prompts
# client_prompt = prompts_config["client_prompts"]["client_1"]


openai.api_key = openai_api_key


if __name__ == '__main__':
    print("Start recording: Press 'r'\nStop recording: Press 'q'\nQuit program: Press 'Esc'")
    # speak("Cabinet dentaire du Docteur Carole Sion, bonjour. Comment puis-je vous aider?")

    # run the program ask for key to press
    while True:
        voice_input.start_recording()

        if keyboard.is_pressed('r'):  # Press 'r' to start recording
            voice_input.start_recording()

        while keyboard.is_pressed('q'):
            audio_file = open("recorded_audio.wav", "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            user_input = transcript['text']
            print("User:", user_input)
            response = assistant.generate_response(user_input)
            print("Eva:", response)
            voice_output.speak(response)
            assistant.prompt += response

        if keyboard.is_pressed('Esc'):
            audio_file = open("recorded_audio.wav", "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            user_input = transcript['text']
            print("User:", user_input)
            response = assistant.generate_response(user_input)
            voice_output.speak(response)
            print("Eva:", response)
            break

    print("Goodbye Eva!")
    # Initialize the text-to-speech engine
