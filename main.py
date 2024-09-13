import time
import requests
from midi2audio import FluidSynth
from IPython.display import Audio, display
from openai import OpenAI


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
- The music's limited pitch range of 5 octaves allows for a greater emphasis on the nuances of tone and phrasing, while its use of major key creates a distinct atmosphere. With a runtime of 31 ~ 45 seconds, this song showcases a highly vigorous rhythm and features grand piano, guitar, bass, violin, synthesizer, and drum. It is played at a moderate speed, adhering to a 4/4 meter, and is characterized by its religious and pop sound.
- The music being described here has a limited pitch range of 5 octaves, which creates a focus on the nuances of tone and phrasing. It is played in the minor key, giving it a distinct and resonant sound. The song's length is about 40 seconds, but despite its brevity, it boasts an exceptionally energetic beat. The music is further enriched by the use of grand piano, drum, and voice, and its 4/4 time signature gives it a unique structure. This music is played at a moderate tempo and is imbued with a strong sense of contentment. Overall, it is a captivating piece that showcases the skillful composition and performance of its creators.
- The tempo in this song is very fast-paced, and the music is based on a 4/4 time signature. Piano, drum, and voice should be included in the music, creating a vibrant and dynamic sound. The music is defined by delight, evoking a powerful and intense atmosphere. With a structure consisting of about 14 bars, the song carries its energetic momentum throughout. This song has a duration of about 40 seconds.
- The about 40-second song with a limited pitch range of 4 octaves allows for a greater emphasis on the nuances of tone and phrasing, while the minor key contributes to its special emotional quality. The rhythm of the song is just right, not too fast or too slow, and the grand piano, drum, and bass play an important role in creating its overall sound. It is performed at a rapid pace, using the 4/4 time signature, and is characterized by its downhearted nature.
- The compact pitch range of 5 octaves results in a focused and impactful musical performance, while the choice of minor key adds to the captivating and memorable experience. With a duration of about 50 seconds, the rapid tempo of this song combined with the distinct sound of organ, guitar, bass, voice, brass, and drum creates its unique musical identity. The meter of the music follows 4/4, and it is played at a moderate tempo, further enhancing its overall effect. The song's style is defined by its pop influences, culminating in a compelling musical composition.
- The music in question is a quintessential example of the classical genre, progressing over 13 ~ 16 bars. What adds a unique flavor to this music is the minor key used throughout the song. This song has a fast-paced rhythm that is very easy on the ears. The time signature of this song is not commonly used.
- The music in question has a limited pitch range of 6 octaves, which in turn allows for a greater emphasis on the nuances of tone and phrasing. The song itself progresses through 13 ~ 16 bars and has a duration of about 20 seconds. Additionally, the music is based on a 4/4 time signature, giving it a distinct rhythmic structure. Overall, these elements combine to create a unique musical experience that is both technically precise and aesthetically pleasing to the ear. The song with its quick beat and invigorating rhythm creates an energizing experience for the listener.
- The major key in this music provides a powerful and memorable sound, while the running time of the song is 31 ~ 45 seconds. The rhythm in this song is very calming, and it has a time signature of 4/4. The music is brought to life through the use of grand piano and bass. The tempo of this song is rapid.
- With a pitch range spanning 1 octave, this music offers a diverse and dynamic listening experience. Composed in the major key, the song lasts 31 ~ 45 seconds and features a heavy beat. It showcases drum and guitar and has a time signature of 4/4, while being played at a moderate speed. Characterized by unease, the music comprises 13 ~ 16 bars, resulting in a captivating musical composition.
- The music offers a unique and memorable listening experience with its pitch range of 3 octaves. It creates a rich and dynamic sonic palette through its use of minor key. Lasting 16 ~ 30 seconds, the song maintains a smooth and steady rhythm, played at a swift pace. The music features piano, synthesizer, drum, and bass and follows the time signature of 4/4. Moreover, it is imbued with misery.
- The compact pitch range of 7 octaves results in a focused and impactful musical performance, enhanced by the powerful and memorable sound of the major key. With a duration of about 50 seconds, the song captivates listeners with its energetic beat, while grand piano and bass add depth and texture to the composition. Following a 4/4 meter, the music maintains a medium tempo and fills the air with zeal.
- The music's pitch range of 3 octaves offers a unique and memorable listening experience, while its use of major key creates a rich and dynamic sonic palette. The song runs for 31 ~ 45 seconds and has a very peaceful beat, yet the fast-paced rhythm, 4/4 time signature, and use of piano and guitar add to the musical composition's complexity. The music is also filled with chill, making it an immersive and captivating experience for listeners.
- This music, composed in the major key, is brought to life through the use of grand piano, strings, and drum, and its pitch range of 5 octaves adds a distinctive character, emphasizing its emotional depth. The tempo of the song is moderate and enjoyable, with a brisk tempo in some sections, and plays for about 40 seconds over about 14 bars in 4/4. The music projects anxiety, creating a rich auditory experience for listeners.
- The musical piece showcases a pitch range within 6 octaves and uses a major key to create a distinct atmosphere. It is a 46 ~ 60-second-long song with a rhythm that is neither too fast nor too slow. The music is given its sound through strings, trumpet, trombone, brass, sax, clarinet, piccolo, and sound effect and follows a meter of 4/4. With a slow tempo, this music is unmistakably symphony in character.
- The compact pitch range of 5 octaves results in a focused and impactful musical performance composed in the major key, playing for 1 ~ 15 seconds. The rhythm in this song is incredibly stimulating, and the music should feature grand piano, strings, drum, and bass. It features a 4/4 meter and is played at a quick pace, evoking suspense. The song structure is made up of about 6 bars.
- With its use of the minor key, this music conveys a unique and resonant sound, while its meter is defined by the 4/4. Enriched by the inclusion of piano and strings, the music projects a profound animation throughout its about 10 bars.

you should only return one paragraph in a format similar to any above entry, and keep the reply simply and clear as a instruction for later process. 

Give example: Query: I want a happy music:

Return exactly: The composition is set in a 4/4 meter, played at a lively and upbeat tempo, and spans approximately 35 seconds. The music is in a major key, which creates a bright and joyful atmosphere. It features a pitch range of 5 octaves, allowing for dynamic variation and energetic expression. The instrumental arrangement includes grand piano, acoustic guitar, bass, violin, and drums, each contributing to a vibrant and uplifting sound. The structure unfolds over 12 to 14 bars, and the cheerful rhythm, influenced by pop and folk genres, gives the music a catchy and engaging quality. This piece is defined by its playful mood and celebratory character, making it a memorable and enjoyable listening experience.

"""

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


def main(input_query):
    
    message = text2text_client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"{input_query}[return the instruction only, do not contain any further instruction about the way it plays]"
    )

    run = text2text_client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
    )

    if run.status == 'completed': 
        messages = text2text_client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages.data[0].content[0].text.value)
    else:
        print(run.status)

    text_command = messages.data[0].content[0].text.value

    try:
        # Step 1: Submit text for MIDI conversion
        submit_response = text2midi_client.submit_text(text_command)
        job_id = submit_response['jobId']
        print(f"Job submitted. Job ID: {job_id}")

        # Step 2: Poll the job status until it's completed
        while True:
            status_response = text2midi_client.check_status(job_id)
            status = status_response['status']
            print(f"Job Status: {status}")
            if status == 'completed':
                break
            elif status == 'failed':
                print("Job failed.")
                return
            time.sleep(10)  # Wait for 2 seconds before checking again

        # Step 3: Retrieve the result (metadata)
        result_response = text2midi_client.get_result(job_id)
        meta_data = result_response['metaData']
        print("Metadata:")
        print(meta_data)

        # Step 4: Download the MIDI file
        midi_file_path = text2midi_client.download_midi(job_id, save_path=f"storage/{job_id}.mid")
        print(f"MIDI file downloaded to {midi_file_path}")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err.response.json()}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    text2text_client = OpenAI(api_key="")

    assistant = text2text_client.beta.assistants.create(
    name="Chat Piano",
    instructions=instructions,
    tools=[],
    model="gpt-4o",
    )

    thread = text2text_client.beta.threads.create()
    
    # Initialize the client with the base URL of your Flask server
    text2midi_client = TextToMidiClient(base_url="http://localhost:5000")
    
    while input_query := input("Please input your query: ") != "exit":
        main(input_query)