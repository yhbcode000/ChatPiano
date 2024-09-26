import time
import requests
from midi2audio import FluidSynth
from openai import OpenAI
import openai
import sounddevice as sd
from scipy.io.wavfile import write as wav_write
from gtts import gTTS
from playsound import playsound
import threading
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
import os
import sys

# Your existing 'instructions' variable
instructions = """
As a seasoned musician, I excel at transforming general instructions into meticulously crafted musical terminology. My expertise lies in interpreting creative directions and translating them into precise musical elements, whether it be phrasing, dynamics, articulation, or orchestration. Please provide your instructions, and I will convert them into detailed, music-specific language that aligns

The returned instruction have to include the following information:

### Evaluation of the Current Entries

The entries provided are descriptive analyses of various pieces of music. Each entry follows a structure that includes the following elements:

1. **Meter and Tempo**: Time signature and the pace (e.g., "4/4 time signature," "moderate tempo").
2. **Duration**: Total playtime of the music (e.g., "40 seconds," "31 ~ 45 seconds").
3. **Pitch Range**: Octave range and its impact on the music (e.g., "limited pitch range of 5 octaves").
4. **Key**: Tonality of the music (e.g., "major key," "minor key").
5. **Instrumental Arrangement**: The instruments used and their role in the piece (e.g., "grand piano, guitar, bass, violin, synthesizer, and drum").
6. **Musical Character/Emotion**: Descriptive terms about the mood or feeling of the music (e.g., "energetic beat," "filled with chill").
7. **Structural Elements**: Number of bars and other compositional elements (e.g., "13 ~ 16 bars").
8. **Style or Genre Influence**: Specific styles or influences that define the music (e.g., "pop sound," "classical genre").
9. **Additional Descriptive Elements**: Any unique qualities or character of the music (e.g., "vibrant and dynamic sound," "powerful and intense atmosphere").

### Template for Future Entries

Here's a suggested template for future entries to ensure consistency, clarity, and completeness:

---

**Template for Music Description:**

1. **Time Signature and Tempo:**
   - Start with the time signature and tempo of the music.
   - Example: "The composition is in a 4/4 time signature and is played at a moderate tempo."

2. **Duration:**
   - Mention the total duration or runtime of the music.
   - Example: "The piece lasts approximately 40 seconds."

3. **Pitch Range:**
   - Specify the pitch range and its impact on the musical performance.
   - Example: "The limited pitch range of 5 octaves allows for nuanced expression in tone and phrasing."

4. **Key and Tonality:**
   - Describe the key (major or minor) and its effect on the music's atmosphere.
   - Example: "Composed in a minor key, the piece evokes a resonant and introspective sound."

5. **Instrumentation:**
   - List the instruments used and their significance to the overall sound.
   - Example: "The music features a grand piano, guitar, bass, violin, synthesizer, and drums, each contributing to its distinct sonic character."

6. **Mood and Emotional Character:**
   - Provide a description of the mood or emotional quality of the piece.
   - Example: "The music is characterized by a lively and dynamic mood, creating a sense of delight and energy."

7. **Structure and Form:**
   - Include details about the structural elements, such as the number of bars.
   - Example: "The composition unfolds over 13 to 16 bars."

8. **Style or Genre Influence:**
   - Specify any genre or style influences that shape the music.
   - Example: "The piece is influenced by pop music, blending modern elements with a traditional structure."

9. **Additional Descriptive Details:**
   - Highlight any unique qualities or aspects of the music that stand out.
   - Example: "The rapid tempo combined with a distinctive rhythmic pattern creates an engaging and memorable listening experience."

---

For example:
Here is the converted text list:

- This music has a meter of 4/4 and a balanced beat. Its playtime is about 40 seconds. The use of grand piano, guitar, bass, violin, synthesizer, and drum is vital to the music's overall sound and performance. The song spans approximately 13 ~ 16 bars.
- ...

you should only return one paragraph in a format similar to any above entry, and keep the reply simply and clear as a instruction for later process.

Give example: Query: I want a happy music:

Return exactly: The composition is set in a 4/4 meter, played at a lively and upbeat tempo, and spans approximately 35 seconds. The music is in a major key, which creates a bright and joyful atmosphere. It features a pitch range of 5 octaves, allowing for dynamic variation and energetic expression. The instrumental arrangement includes grand piano, acoustic guitar, bass, violin, and drums, each contributing to a vibrant and uplifting sound. The structure unfolds over 12 to 14 bars, and the cheerful rhythm, influenced by pop and folk genres, gives the music a catchy and engaging quality. This piece is defined by its playful mood and celebratory character, making it a memorable and enjoyable listening experience.

"""

class TextToMidiClient:
    # Your existing TextToMidiClient class
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def submit_text(self, text):
        url = f"{self.base_url}/submit-text"
        headers = {'Content-Type': 'application/json'}
        data = {'text': text}

        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def check_status(self, job_id):
        url = f"{self.base_url}/check-status/{job_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_result(self, job_id):
        url = f"{self.base_url}/get-result/{job_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def download_midi(self, job_id, save_path):
        url = f"{self.base_url}/download-midi/{job_id}"
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return save_path

def list_audio_devices():
    print(sd.query_devices())


def record_audio(filename='storage/tmp/input.wav', fs=44100):
    """
    Records audio to a WAV file until the Enter key is pressed.
    
    Args:
    filename (str): Path to save the recorded audio file.
    fs (int): Sampling rate in Hz.
    """
    
    def callback(indata, frames, time, status):
        """Callback function called by sounddevice for each audio block."""
        recording.append(indata.copy())  # Append current block of data to the recording list

    def listen_for_stop():
        """Listens for the Enter key press to stop recording."""
        input("Press Enter to stop recording...\n")
        nonlocal recording_active
        recording_active = False
    
    print("Recording...")
    recording_active = True
    recording = []

    # Start the thread to listen for Enter key
    stop_thread = threading.Thread(target=listen_for_stop)
    stop_thread.start()
    
    with sd.InputStream(callback=callback, dtype='float32', channels=1, samplerate=fs):
        while recording_active:
            pass

    stop_thread.join()  # Ensure the thread is properly closed

    if recording:
        # Concatenate all recorded frames
        recording_array = np.concatenate(recording, axis=0)
        print("Recording complete.")

        # Normalize and convert to 16-bit integers
        recording_int = np.int16(recording_array / np.max(np.abs(recording_array)) * 32767)
        wav_write(filename, fs, recording_int)
        print(f"Audio written to {filename}")
    else:
        print("No audio data recorded.")
    
    return filename

def transcribe_audio(audio_file_path):
    audio_file = open(audio_file_path, "rb")
    transcript = openai.audio.transcriptions.create(
        file=audio_file, 
        model="whisper-1",
        language="en",
        prompt="english back with prompt like expansion"
        )
    return transcript.text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tmp_path = "storage/tmp/response_audio.mp3"
    tts.save(tmp_path)
    # https://stackoverflow.com/questions/69245722/error-259-on-python-playsound-unable-to-sound
    playsound(tmp_path)
    os.remove(tmp_path)

def get_image_path_from_text(text="neutral"):
    # Simple keyword matching to select image
    if 'happy' in text.lower():
        return 'storage/assets/img/happy.jpg'
    elif 'sad' in text.lower():
        return 'storage/assets/img/sad.gif'
    elif 'sorry' in text.lower():
        return 'storage/assets/img/sorry.gif'
    elif 'speak' in text.lower():
        return 'storage/assets/img/speak.jpg'
    else:
        return 'storage/assets/img/neutral.jpg'

def show_listening_window():
    global assistant_reply  # Ensure this is accessible within the function
    root = tk.Tk()
    root.title("AI Assistant Listening")

    # Load and set up the initial image
    img = Image.open(current_image_path)
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)

    # Create a Label for the image
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Keep a reference
    image_label.pack()

    # Create a Label for the text below the image
    text_label = tk.Label(root, text=assistant_reply, wraplength=400, justify="center")
    text_label.pack()

    def update_image():
        if image_update_event.is_set():
            image_update_event.clear()
            # Load the new image
            img = Image.open(current_image_path)
            img = img.resize((400, 400))
            photo = ImageTk.PhotoImage(img)

            # Update the image label
            image_label.configure(image=photo)
            image_label.image = photo  # Keep a reference

            # Update the text label
            text_label.configure(text=assistant_reply)
        # Schedule the next check
        root.after(1000, update_image)  # Check every 1 second

    # Start the periodic image update check
    root.after(1000, update_image)

    # Start the Tkinter event loop
    root.mainloop()



def process_text2midi_job(text2midi_client, text_command, job_complete_event):
    global job_id_global
    try:
        # Step 1: Submit text for MIDI conversion
        submit_response = text2midi_client.submit_text(text_command)
        job_id = submit_response['jobId']
        print(f"Job submitted. Job ID: {job_id}")

        # Store the job_id globally
        job_id_global = job_id

        # Step 2: Poll the job status until it's completed
        while True:
            status_response = text2midi_client.check_status(job_id)
            status = status_response['status']
            # print(f"Job Status: {status}")
            if status == 'completed':
                break
            elif status == 'failed':
                print("Job failed.")
                job_complete_event.set()
                return
            time.sleep(10)  # Wait for 10 seconds before checking again

        # Step 3: Retrieve the result (metadata)
        result_response = text2midi_client.get_result(job_id)
        meta_data = result_response['metaData']
        print("Metadata:")
        print(meta_data)

        # Step 4: Download the MIDI file
        midi_file_path = text2midi_client.download_midi(job_id, save_path=f"storage/{job_id}.mid")
        print(f"MIDI file downloaded to {midi_file_path}")

        # Signal that the job is complete
        job_complete_event.set()

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err.response.json()}")
        job_complete_event.set()
    except Exception as err:
        print(f"An error occurred: {err}")
        job_complete_event.set()


def main():
    list_audio_devices()
    sd.default.device = int(input("The device you want to use for recording (enter the index): "))

    global job_id_global  # To store the job ID globally
    global current_image_path, image_update_event, assistant_reply
    
    job_id_global = None
    image_update_event = threading.Event()
    
    assistant_reply = ""
    current_image_path = get_image_path_from_text("neutral")
    image_update_event.set()
    
    
    # Initialize OpenAI API key
    openai.api_key = ""
    text2text_client = OpenAI(api_key = openai.api_key)

    assistant_text_command = text2text_client.beta.assistants.create(
    name="Chat Piano",
    instructions=instructions,
    tools=[],
    model="gpt-4o",
    )

    text2text_thread = text2text_client.beta.threads.create()

    # Initialize the TextToMidi client
    text2midi_client = TextToMidiClient(base_url="http://localhost:5000")

    # Start the listening window in a separate thread
    gui_thread = threading.Thread(target=show_listening_window)
    gui_thread.daemon = True
    gui_thread.start()

    while True:
        try:
            # Step 1: Record user's query
            if input("Press enter to start, type exit to close: ") == "exit": # TODO hold until start
                print("Ok, see you next time.")
                speak_text("Ok, see you next time.")
                break
            audio_file = record_audio()
            input_query = transcribe_audio(audio_file)
            print(f"User said: {input_query}")

            if input_query.lower() == "exit":
                break

            # Step 2: Send the query to the assistant
            message = text2text_client.beta.threads.messages.create(
                thread_id=text2text_thread.id,
                role="user",
                content=f"{input_query}[return the instruction only, do not contain any further instruction about the way it plays, only generate 10 seconds.]"
            )

            run = text2text_client.beta.threads.runs.create_and_poll(
                thread_id=text2text_thread.id,
                assistant_id=assistant_text_command.id
            )
            
            if run.status == 'completed': 
                messages = text2text_client.beta.threads.messages.list(
                    thread_id=text2text_thread.id
                )
            else:
                print(run.status)

            text_command = messages.data[0].content[0].text.value
                        
            # Step 3: Speak out the assistant's reply (excluding the text command for text2midi)
            # Since the assistant's reply is the text command, we won't speak it out
            # If you have additional messages, you can speak them here

            # Step 4: Submit the text command to text2midi service

            # Start a thread to handle the text2midi job
            job_complete = threading.Event()
            job_thread = threading.Thread(target=process_text2midi_job, args=(text2midi_client, text_command, job_complete))
            job_thread.start()

            # While the text2midi job is processing, engage in conversation with the user
            assistant_reply = "The MIDI file is being prepared. Feel free to chat with me in the meantime."
            current_image_path = get_image_path_from_text("speak")
            image_update_event.set()
            speak_text(assistant_reply)
            
            assistant_reply = ""
            current_image_path = get_image_path_from_text("neutral")
            image_update_event.set()
            
            assistant_chatter = text2text_client.beta.assistants.create(
            name="Chatty",
            instructions=f"You are chatty, keep people around while waiting the music generation service is done. [What you are? A agent that can generate music. previous music query {input_query}, command: {text_command}, you are currently wait the result generated music return back with the user, chat for fun] [simple chat, answer me in short reply do not follow markdown format, only short reply is enough, free speech]",
            tools=[],
            model="gpt-4o",
            )
            
            while not job_complete.is_set():
                # Record user's response
                audio_file = record_audio()
                user_response = transcribe_audio(audio_file)
                print(f"User: {user_response}")
                
                input_query = user_response

                message = text2text_client.beta.threads.messages.create(
                thread_id=text2text_thread.id,
                role="user",
                content=f"User: {input_query}"
                )

                run = text2text_client.beta.threads.runs.create_and_poll(
                thread_id=text2text_thread.id,
                assistant_id=assistant_chatter.id
                )

                if run.status == 'completed': 
                    messages = text2text_client.beta.threads.messages.list(
                        thread_id=text2text_thread.id
                    )
                else:
                    print(run.status)

                assistant_reply = messages.data[0].content[0].text.value
                current_image_path = get_image_path_from_text("speak")
                image_update_event.set()
                print(f"Assistant: {assistant_reply}")
                speak_text(assistant_reply)
                assistant_reply = ""
                current_image_path = get_image_path_from_text("neutral")
                image_update_event.set()

            # Wait for the job_thread to finish
            job_thread.join()

            # Once the job is complete, notify the user, stop any ongoing conversation, and play the MIDI file
            assistant_reply = "Your MIDI file is ready. Playing it now."
            current_image_path = get_image_path_from_text("happy")
            image_update_event.set()
            print(assistant_reply)
            speak_text(assistant_reply)
            assistant_reply = ""
            current_image_path = get_image_path_from_text("neutral")
            image_update_event.set()

            # Play the MIDI file using the system default application
            midi_file_path = f"storage/{job_id_global}.mid"
            if os.name == 'nt':  # Windows
                os.startfile(os.path.join(os.getcwd(), midi_file_path))
            elif sys.platform == "darwin":  # macOS
                os.system(f"open '{os.path.join(os.getcwd(), midi_file_path)}'")
            else:  # Linux and others
                os.system(f"xdg-open '{os.path.join(os.getcwd(), midi_file_path)}'")

            # Optionally, you can exit the loop or continue
            # break  # Remove this if you want to continue the loop
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Error, please contact admin for help.")
            assistant_reply = ""
            current_image_path = get_image_path_from_text("sorry")
            image_update_event.set()
            speak_text("Error, please contact admin for help.")
            current_image_path = get_image_path_from_text("neutral")
            image_update_event.set()
            continue

if __name__ == "__main__":
    main()
