from pathlib import Path
from openai import OpenAI
import pygame

client = OpenAI(api_key="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")

speech_file_path = Path('C:\\Users\\elisa\\Documents\\GitHub\\Eva\\data') / "speech.mp3"


def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error playing audio: {e}")

    finally:
        pygame.quit()


# Replace 'your_audio_file.mp3' with the path to your audio file
audio_file_path = 'C:\\Users\\elisa\\Documents\\GitHub\\Eva\\data\\speech.mp3'


def voice_response(response):
    """
    cette fonction cree lq voix a partir de response et la joue
    :param response:
    :return:
    """

    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=response)

    response.stream_to_file(speech_file_path)
    play_audio(audio_file_path)
