import pyaudio
import wave
import keyboard
import time
import sys

# CONSTANTS
FORMAT = pyaudio.paInt16  # format audio = 16-bit signed integer audio samples, pyaudio.paInt32 = higher quality but
# larger file sizes
CHANNELS = 1  # numbers of audio channels | 1 = mono audio recording (single channel), 2 = stereo recording (spatial
# audio information)
RATE = 44100  # sample rate = nombre d'echantillons audio/sec | 44100Hz = CD quality audio, @@)%)Hz= lower quality but
# reduce file size
CHUNK = 1024  # nombre de sample/buffer. Des plus petites valeures = lower latency but more frequent reads and more
# CPU-intensive.
RECORD_SECONDS = 60  # Adjust the recording duration as needed
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"


def start_recording():
    # Create an instance of PyAudio
    audio = pyaudio.PyAudio()

    # Open the audio stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording started. Press 'q' to stop recording or 'x' to exit.")

    frames = []
    start_time = time.time()
    recording_started = False
    while True:
        data = stream.read(CHUNK)
        frames.append(data)

        if keyboard.is_pressed('q') and recording_started:  # Press 'q' to stop recording
            break

        if keyboard.is_pressed('Esc'):  # Press 'x' to exit the program
            stream.stop_stream()
            stream.close()
            audio.terminate()
            sys.exit()

        if time.time() - start_time >= 1 and not recording_started:  # Skip the first second of recording
            recording_started = True

        if time.time() - start_time >= RECORD_SECONDS + 2:  # Add 1 second to the desired recording duration
            break

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print("Recording saved to", WAVE_OUTPUT_FILENAME)
