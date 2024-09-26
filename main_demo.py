from openai import OpenAI
import openai
text2text_client = OpenAI(api_key="")

assistant = text2text_client.beta.assistants.create(
    name="Chat Piano",
    instructions="You are a helpful assistant who chats with users to help them craft musical ideas. Once the user has provided enough detail about their musical concept, such as time signature, tempo, key, instrumentation, pitch range, and emotional character, you must always convert their ideas into structured musical instructions and pass them to the 'convert_text_to_midi' tool to generate a MIDI file. Ensure you always call the tool after the user has provided sufficient details or explicitly want you to generate it. Besides, keep your reply short and concise, not too long during normal conversation.",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "convert_text_to_midi",
                "description": "This tool converts structured musical instructions into a MIDI file. The input should include key musical elements such as time signature, tempo, key, instrumentation, pitch range, and emotional character. Based on these details, the tool generates a MIDI file that reflects the described musical piece.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "text_command": {
                            "type": "string",
                            "description": """
As a seasoned musician, I excel at transforming general instructions into meticulously crafted musical terminology. My expertise lies in interpreting creative directions and translating them into precise musical elements, whether it be phrasing, dynamics, articulation, or orchestration. Please provide your instructions, and I will convert them into detailed, music-specific language that aligns with your vision.

The returned instruction has to include the following information:

### Evaluation of the Current Entries:

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

### Template for Future Entries:

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

---

You should only return one paragraph in a format similar to any above entry, and keep the reply simple and clear as an instruction for later processing.

### Example:

**User Query**: I want a happy music.

**Assistant Response**:

"The composition is set in a 4/4 meter, played at a lively and upbeat tempo, and spans approximately 35 seconds. The music is in a major key, which creates a bright and joyful atmosphere. It features a pitch range of 5 octaves, allowing for dynamic variation and energetic expression. The instrumental arrangement includes grand piano, acoustic guitar, bass, violin, and drums, each contributing to a vibrant and uplifting sound. The structure unfolds over 12 to 14 bars, and the cheerful rhythm, influenced by pop and folk genres, gives the music a catchy and engaging quality. This piece is defined by its playful mood and celebratory character, making it a memorable and enjoyable listening experience."
                            """
                        }
                    },
                    "required": ["text_command"],
                    "additionalProperties": False
                }
            }
        }
    ],
    model="gpt-4o",
)

thread = text2text_client.beta.threads.create()


# %%
import time
import requests
from midi2audio import FluidSynth
from IPython.display import Audio, display

class TextToMidiClient:
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
    
# Initialize the client with the base URL of your Flask server
text2midi_client = TextToMidiClient(base_url="http://localhost:5000")


# %%
# Define an assistant tool to handle music conversion
def convert_text_to_midi(text_command):
    try:
        # Step 1: Submit text for MIDI conversion
        submit_response = text2midi_client.submit_text(text_command)
        job_id = submit_response['jobId']
        print(f"Job submitted. Job ID: {job_id}")

        # Step 2: Poll the job status until it's completed
        while True:
            status_response = text2midi_client.check_status(job_id)
            status = status_response['status']
            # print(f"Job Status: {status}")
            if status == 'completed':
                break
            elif status == 'failed':
                print("Job failed.")
                return None
            time.sleep(10)  # Wait for 2 seconds before checking again

        # Step 3: Retrieve the result (metadata)
        result_response = text2midi_client.get_result(job_id)
        meta_data = result_response['metaData']
        print("Metadata:")
        print(meta_data)

        # Step 4: Download the MIDI file
        midi_file_path = text2midi_client.download_midi(job_id, save_path=f"storage/{job_id}.mid")
        print(f"MIDI file downloaded to {midi_file_path}")

        return midi_file_path, meta_data

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err.response.json()}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

# %%
import threading
import queue
import time
import re

def handle_midi_conversion(text_command, result_queue):
    """Thread function to handle MIDI conversion and store results."""
    midi_result = convert_text_to_midi(text_command)
    result_queue.put(midi_result)  # Place the result in a queue for the main thread to retrieve.


import sounddevice as sd
import numpy as np
import openai
import threading
import os
from scipy.io.wavfile import write as wavWrite
from gtts import gTTS
from playsound import playsound

def listAudioDevices():
    print(sd.query_devices())

def record_audio(filename='storage/tmp/input.wav', fs=44100):
    """
    Records audio to a WAV file, starting and stopping with Enter key press.
    
    Args:
    filename (str): Path to save the recorded audio file.
    fs (int): Sampling rate in Hz.
    """
    
    def callback(indata, frames, time, status):
        """Callback function called by sounddevice for each audio block."""
        recording.append(indata.copy())  # Append current block of data to the recording list

    def listenForStop():
        """Listens for the Enter key press to stop recording."""
        input("Press Enter again to stop recording...\n")
        nonlocal recordingActive
        recordingActive = False
    
    print("Recording... Press Enter to stop.")
    recordingActive = True
    recording = []

    # Start the thread to listen for Enter key
    stopThread = threading.Thread(target=listenForStop)
    stopThread.start()
    
    with sd.InputStream(callback=callback, dtype='float32', channels=1, samplerate=fs):
        while recordingActive:
            pass

    stopThread.join()  # Ensure the thread is properly closed

    if recording:
        # Concatenate all recorded frames
        recordingArray = np.concatenate(recording, axis=0)
        print("Recording complete.")

        # Normalize and convert to 16-bit integers
        recordingInt = np.int16(recordingArray / np.max(np.abs(recordingArray)) * 32767)
        wavWrite(filename, fs, recordingInt)
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

def speakText(text):
    """Converts text to speech and plays it."""
    tts = gTTS(text=text, lang='en')
    tmpPath = "storage/tmp/response_audio.mp3"
    tts.save(tmpPath)
    # https://stackoverflow.com/questions/69245722/error-259-on-python-playsound-unable-to-sound
    playsound(tmpPath)
    os.remove(tmpPath)


import sounddevice as sd
import queue
import threading
import openai
import time
import json

# Combined main function
def main():
    conversion_thread = None
    result_queue = queue.Queue()

    listAudioDevices()
    sd.default.device = int(input("Select the device index for recording: "))

    openai.api_key = ""
    
    try:
        while True:
            # Start and stop recording with Enter key
            if input("Press Enter to start recording, or type 'exit' to close: ").lower() == "exit":
                speakText("Goodbye!")
                break
            
            # Record audio input
            audioFile = record_audio()
            user_input = transcribe_audio(audioFile)
            print(f"{"-"*80}\n{"-"*80}\nUser: {user_input}")

            if user_input.lower() == 'exit':
                speakText("Goodbye!")
                break
            
            message = text2text_client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=user_input+"[reply me short and concise, with less than 20 words.]"
            )

            run = text2text_client.beta.threads.runs.create_and_poll(
                thread_id=thread.id,
                assistant_id=assistant.id
            )

            while run.status == 'requires_action':
                tool_outputs = []

                # Loop through each tool in the required action section
                for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                    if tool_call.function.name == "convert_text_to_midi":
                        tool_outputs.append({
                            "tool_call_id": tool_call.id,
                            "output": "generating, would take sometime to complete.",
                        })
                        arguments = json.loads(tool_call.function.arguments)
                        text_command = arguments.get("text_command")
                        print(f"{"-"*80}\nAssistant Background: {text_command}")

                        conversion_thread = threading.Thread(target=handle_midi_conversion,
                                                             args=(text_command, result_queue))
                        conversion_thread.start()

                # Submit all tool outputs at once after collecting them in a list
                if tool_outputs:
                    try:
                        run = text2text_client.beta.threads.runs.submit_tool_outputs_and_poll(
                            thread_id=thread.id,
                            run_id=run.id,
                            tool_outputs=tool_outputs
                        )
                        print("Client: Tool outputs submitted successfully.")
                    except Exception as e:
                        print("Client: Failed to submit tool outputs:", e)
                else:
                    print("No tool outputs to submit.")

            if run.status == 'completed':
                response = text2text_client.beta.threads.messages.list(thread_id=thread.id)
                message = response.data[0].content[0].text.value  # Get the latest response
                print(f"{"-"*80}\nAssistant: {message}")
                speakText(message)
            else:
                print(f"Assistant run status: {run.status}")

            # Check if there's a MIDI conversion in progress
            if conversion_thread and conversion_thread.is_alive():
                # speakText("MIDI conversion is in progress...")
                pass
            else:
                # If the MIDI conversion has finished, handle the result
                if conversion_thread and not conversion_thread.is_alive():
                    if not result_queue.empty():
                        midi_result = result_queue.get()
                        if midi_result:
                            midi_file_path, meta_data = midi_result
                            speakText(f"MIDI file saved successfully.")
                        else:
                            speakText("MIDI conversion failed.")
                        conversion_thread = None  # Reset the thread

    except KeyboardInterrupt:
        speakText("Program exited by user.")

    # Ensure that any remaining thread is completed before exiting
    if conversion_thread and conversion_thread.is_alive():
        conversion_thread.join()
        if not result_queue.empty():
            midi_result = result_queue.get()
            if midi_result:
                midi_file_path, meta_data = midi_result
                speakText(f"MIDI file saved successfully.")
            else:
                speakText("MIDI conversion failed.")

# Entry point
if __name__ == "__main__":
    main()
