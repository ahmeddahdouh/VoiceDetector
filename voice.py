import os
import speech_recognition as sr
import pyaudio
import wave

# Directory to store user voice samples
VOICE_DIR = "voice_samples"

# Ensure the directory exists
if not os.path.exists(VOICE_DIR):
    os.makedirs(VOICE_DIR)

def record_voice(filename):
    """Record voice and save it as a WAV file."""
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    rate = 44100  # Record at 44100 samples per second
    seconds = 5
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print("Recording...")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=rate,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 5 seconds
    for _ in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print("Finished recording.")

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def register_user(username):
    """Register a new user by recording their voice."""
    filename = os.path.join(VOICE_DIR, f"{username}.wav")
    record_voice(filename)
    print(f"User {username} registered successfully.")

def authenticate_user(username):
    """Authenticate a user by comparing their voice with the stored sample."""
    recognizer = sr.Recognizer()
    filename = os.path.join(VOICE_DIR, f"{username}.wav")

    if not os.path.exists(filename):
        print(f"No voice sample found for user {username}.")
        return False

    print("Please speak to authenticate...")
    record_voice("temp.wav")

    try:
        with sr.AudioFile(filename) as source:
            stored_audio = recognizer.record(source)
        with sr.AudioFile("temp.wav") as source:
            temp_audio = recognizer.record(source)

        stored_text = recognizer.recognize_google(stored_audio)
        temp_text = recognizer.recognize_google(temp_audio)

        if stored_text == temp_text:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return False
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return False
    finally:
        os.remove("temp.wav")
    
if __name__ == "__main__":
    while True:
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            register_user(username)
        elif choice == '2':
            username = input("Enter username: ")
            authenticate_user(username)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")