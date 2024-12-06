from .midiPlayerTool import MidiPlayer, playAccompanimentTrackRealtimeTempo
from .generateMidiTool import generate_midi, check_generate_midi_status
from .searchOnlineTool import fetch_web_page, search_duckduckgo

FUNCTION_MAPPING = {
    "play_accompaniment_track_realtime_tempo": playAccompanimentTrackRealtimeTempo,
    "play_midi_on_piano": MidiPlayer.startPlaying,
    "generate_midi": generate_midi, 
    "checkGenerateMidiStatus": check_generate_midi_status,
    "fetch_web_page": fetch_web_page,
    "search_duckduckgo": search_duckduckgo,
}

TOOLS_DEFINE = [
    {
    "name": "fetch_web_page",
    "description": "Fetches and returns the content of a web page.",
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL of the web page to fetch."
            }
        },
        "required": [
            "url"
        ]
    }
    },
    {
        "name": "search_duckduckgo",
        "description": "This tool function will take a query about a topic and return the search results from Duck Duck Go.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to look up on Duck Duck Go."
                }
            },
            "required": [
                "query"
            ]
        }
    },
    {
        "name": "play_accompaniment_track_realtime_tempo",
        "description": "Enter the phase to play the accompaniment track on the piano, attending and adapting to the human player's tempo.",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": [],
        }
    },
    {
        "name": "play_midi_on_piano",
        "description": "Starts to play a MIDI file on the player piano.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "The Midi file to play."
                }
            },
            "required": ["filename"]
        }
        
    },
    {
        "name": "generate_midi",
        "description": "This tool converts structured musical instructions into a MIDI file. The input should include key musical elements such as time signature, tempo, key, instrumentation, pitch range, and emotional character. Based on these details, the tool generates a MIDI file that reflects the described musical piece.",
        "parameters": {
            "type": "object",
            "properties": {
                "text_command": {
                    "type": "string",
                    "description": "As a seasoned musician, I excel at transforming general instructions into meticulously crafted musical terminology. My expertise lies in interpreting creative directions and translating them into precise musical elements, whether it be phrasing, dynamics, articulation, or orchestration. Please provide your instructions, and I will convert them into detailed, music-specific language that aligns with your vision.\\n\\nThe returned instruction has to include the following information:\\n\\n### Evaluation of the Current Entries:\\nThe entries provided are descriptive analyses of various pieces of music. Each entry follows a structure that includes the following elements:\\n\\n1. Meter and Tempo: Time signature and the pace (e.g., \"4/4 time signature,\" \"moderate tempo\").\\n2. Duration: Total playtime of the music (e.g., \"40 seconds,\" \"31 ~ 45 seconds\").\\n3. Pitch Range: Octave range and its impact on the music (e.g., \"limited pitch range of 5 octaves\").\\n4. Key: Tonality of the music (e.g., \"major key,\" \"minor key\").\\n5. Instrumental Arrangement: The instruments used and their role in the piece (e.g., \"grand piano, guitar, bass, violin, synthesizer, and drum\").\\n6. Musical Character/Emotion: Descriptive terms about the mood or feeling of the music (e.g., \"energetic beat,\" \"filled with chill\").\\n7. Structural Elements: Number of bars and other compositional elements (e.g., \"13 ~ 16 bars\").\\n8. Style or Genre Influence: Specific styles or influences that define the music (e.g., \"pop sound,\" \"classical genre\").\\n9. Additional Descriptive Elements: Any unique qualities or character of the music (e.g., \"vibrant and dynamic sound,\" \"powerful and intense atmosphere\").\\n\\n### Template for Future Entries:\\nHere's a suggested template for future entries to ensure consistency, clarity, and completeness:\\n\\n---\\n\\nTemplate for Music Description:\\n\\n1. Time Signature and Tempo:\\n - Start with the time signature and tempo of the music.\\n - Example: \"The composition is in a 4/4 time signature and is played at a moderate tempo.\"\\n\\n2. Duration:\\n - Mention the total duration or runtime of the music.\\n - Example: \"The piece lasts approximately 40 seconds.\"\\n\\n3. Pitch Range:\\n - Specify the pitch range and its impact on the musical performance.\\n - Example: \"The limited pitch range of 5 octaves allows for nuanced expression in tone and phrasing.\"\\n\\n4. Key and Tonality:\\n - Describe the key (major or minor) and its effect on the music's atmosphere.\\n - Example: \"Composed in a minor key, the piece evokes a resonant and introspective sound.\"\\n\\n5. Instrumentation:\\n - List the instruments used and their significance to the overall sound.\\n - Example: \"The music features a grand piano, guitar, bass, violin, synthesizer, and drums, each contributing to its distinct sonic character.\"\\n\\n6. Mood and Emotional Character:\\n - Provide a description of the mood or emotional quality of the piece.\\n - Example: \"The music is characterized by a lively and dynamic mood, creating a sense of delight and energy.\"\\n\\n7. Structure and Form:\\n - Include details about the structural elements, such as the number of bars.\\n - Example: \"The composition unfolds over 13 to 16 bars.\"\\n\\n8. Style or Genre Influence:\\n - Specify any genre or style influences that shape the music.\\n - Example: \"The piece is influenced by pop music, blending modern elements with a traditional structure.\"\\n\\n9. Additional Descriptive Details:\\n - Highlight any unique qualities or aspects of the music that stand out.\\n - Example: \"The rapid tempo combined with a distinctive rhythmic pattern creates an engaging and memorable listening experience.\"\\n\\n---\\n\\nFor example:\\nHere is the converted text list:\\n\\n- This music has a meter of 4/4 and a balanced beat. Its playtime is about 40 seconds. The use of grand piano, guitar, bass, violin, synthesizer, and drum is vital to the music's overall sound and performance. The song spans approximately 13 ~ 16 bars.\\n\\n---\\n\\nYou should only return one paragraph in a format similar to any above entry, and keep the reply simple and clear as an instruction for later processing.\\n\\n### Example:\\n\\nUser Query: I want a happy music.\\n\\nAssistant Response:\\n\\n\"The composition is set in a 4/4 meter, played at a lively and upbeat tempo, and spans approximately 35 seconds. The music is in a major key, which creates a bright and joyful atmosphere. It features a pitch range of 5 octaves, allowing for dynamic variation and energetic expression. The instrumental arrangement includes grand piano, acoustic guitar, bass, violin, and drums, each contributing to a vibrant and uplifting sound. The structure unfolds over 12 to 14 bars, and the cheerful rhythm, influenced by pop and folk genres, gives the music a catchy and engaging quality. This piece is defined by its playful mood and celebratory character, making it a memorable and enjoyable listening experience.\"\n\n\n\n\n\n\n\n\n\n\n\n\nChatGPT can make mistakes. Check important info.\n?\nChatGPT says: As a seasoned musician, I excel at transforming general instructions into meticulously crafted musical terminology. My expertise lies in interpreting creative directions and translating them into precise musical elements, whether it be phrasing, dynamics, articulation, or orchestration. Please provide your instructions, and I will convert them into detailed, music-specific language that aligns with your vision.\\n\\nThe returned instruction has to include the following information:\\n\\n### Evaluation of the Current Entries:\\nThe entries provided are descriptive analyses of various pieces of music. Each entry follows a structure that includes the following elements:\\n\\n1. **Meter and Tempo**: Time signature and the pace (e.g., \"4/4 time signature,\" \"moderate tempo\").\\n2. **Duration**: Total playtime of the music (e.g., \"40 seconds,\" \"31 ~ 45 seconds\").\\n3. **Pitch Range**: Octave range and its impact on the music (e.g., \"limited pitch range of 5 octaves\").\\n4. **Key**: Tonality of the music (e.g., \"major key,\" \"minor key\").\\n5. **Instrumental Arrangement**: The instruments used and their role in the piece (e.g., \"grand piano, guitar, bass, violin, synthesizer, and drum\").\\n6. **Musical Character/Emotion**: Descriptive terms about the mood or feeling of the music (e.g., \"energetic beat,\" \"filled with chill\").\\n7. **Structural Elements**: Number of bars and other compositional elements (e.g., \"13 ~ 16 bars\").\\n8. **Style or Genre Influence**: Specific styles or influences that define the music (e.g., \"pop sound,\" \"classical genre\").\\n9. **Additional Descriptive Elements**: Any unique qualities or character of the music (e.g., \"vibrant and dynamic sound,\" \"powerful and intense atmosphere\").\\n\\n### Template for Future Entries:\\nHere's a suggested template for future entries to ensure consistency, clarity, and completeness:\\n\\n---\\n\\n**Template for Music Description:**\\n\\n1. **Time Signature and Tempo:**\\n - Start with the time signature and tempo of the music.\\n - Example: \"The composition is in a 4/4 time signature and is played at a moderate tempo.\"\\n\\n2. **Duration:**\\n - Mention the total duration or runtime of the music.\\n - Example: \"The piece lasts approximately 40 seconds.\"\\n\\n3. **Pitch Range:**\\n - Specify the pitch range and its impact on the musical performance.\\n - Example: \"The limited pitch range of 5 octaves allows for nuanced expression in tone and phrasing.\"\\n\\n4. **Key and Tonality:**\\n - Describe the key (major or minor) and its effect on the music's atmosphere.\\n - Example: \"Composed in a minor key, the piece evokes a resonant and introspective sound.\"\\n\\n5. **Instrumentation:**\\n - List the instruments used and their significance to the overall sound.\\n - Example: \"The music features a grand piano, guitar, bass, violin, synthesizer, and drums, each contributing to its distinct sonic character.\"\\n\\n6. **Mood and Emotional Character:**\\n - Provide a description of the mood or emotional quality of the piece.\\n - Example: \"The music is characterized by a lively and dynamic mood, creating a sense of delight and energy.\"\\n\\n7. **Structure and Form:**\\n - Include details about the structural elements, such as the number of bars.\\n - Example: \"The composition unfolds over 13 to 16 bars.\"\\n\\n8. **Style or Genre Influence:**\\n - Specify any genre or style influences that shape the music.\\n - Example: \"The piece is influenced by pop music, blending modern elements with a traditional structure.\"\\n\\n9. **Additional Descriptive Details:**\\n - Highlight any unique qualities or aspects of the music that stand out.\\n - Example: \"The rapid tempo combined with a distinctive rhythmic pattern creates an engaging and memorable listening experience.\"\\n\\n---\\n\\nFor example:\\nHere is the converted text list:\\n\\n- This music has a meter of 4/4 and a balanced beat. Its playtime is about 40 seconds. The use of grand piano, guitar, bass, violin, synthesizer, and drum is vital to the music's overall sound and performance. The song spans approximately 13 ~ 16 bars.\\n\\n---\\n\\nYou should only return one paragraph in a format similar to any above entry, and keep the reply simple and clear as an instruction for later processing.\\n\\n### Example:\\n\\n**User Query**: I want a happy music.\\n\\n**Assistant Response**:\\n\\n\"The composition is set in a 4/4 meter, played at a lively and upbeat tempo, and spans approximately 35 seconds. The music is in a major key, which creates a bright and joyful atmosphere. It features a pitch range of 5 octaves, allowing for dynamic variation and energetic expression. The instrumental arrangement includes grand piano, acoustic guitar, bass, violin, and drums, each contributing to a vibrant and uplifting sound. The structure unfolds over 12 to 14 bars, and the cheerful rhythm, influenced by pop and folk genres, gives the music a catchy and engaging quality. This piece is defined by its playful mood and celebratory character, making it a memorable and enjoyable listening experience.\"",
                }
            },
            "required": ["text_command"]
        }
        
    },
    {
        "name": "check_generate_midi_status",
        "description": "Obtain whether the previously initated MIDI generation job is completed.",
        "parameters": {
            "type": "object",
            "properties": {
            },
            "required": []
        }
    },
]