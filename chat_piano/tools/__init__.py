from .midiPlayerTool import MidiPlayer, playAccompanimentTrackRealtimeTempo
from .generateMidiTool import generate_midi, check_generate_midi_status

FUNCTION_MAPPING = {
    "play_accompaniment_track_realtime_tempo": playAccompanimentTrackRealtimeTempo,
    "play_midi_on_piano": MidiPlayer.startPlaying,
    "generate_midi": generate_midi, 
    "checkGenerateMidiStatus": check_generate_midi_status,
}

TOOLS_DEFINE = [
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
                    "description": "Description of the music. ### Contents. It has to include the following information. 1. Meter and Tempo: Time signature and the pace (e.g., \"4/4 time signature,\" \"moderate tempo\"). 2. Duration: Total playtime of the music (e.g., \"40 seconds,\" \"31 ~ 45 seconds\"). 3. Pitch Range: Octave range and its impact on the music (e.g., \"limited pitch range of 5 octaves\"). 4. Key: Tonality of the music (e.g., \"major key,\" \"minor key\"). 5. Instrumental Arrangement: The instruments used and their role in the piece (e.g., \"grand piano, guitar, bass, violin, synthesizer, and drum\"). 6. Musical Character/Emotion: Descriptive terms about the mood or feeling of the music (e.g., \"energetic beat,\" \"filled with chill\"). 7. Structural Elements: Number of bars and other compositional elements (e.g., \"13 ~ 16 bars\"). 8. Style or Genre Influence: Specific styles or influences that define the music (e.g., \"pop sound,\" \"classical genre\"). 9. Additional Descriptive Elements: Any unique qualities or character of the music (e.g., \"vibrant and dynamic sound,\" \"powerful and intense atmosphere\"). ### Example. \"This music has a meter of 4/4 and a balanced beat. Its playtime is about 40 seconds. The use of grand piano, guitar, bass, violin, synthesizer, and drum is vital to the music's overall sound and performance. The song spans approximately 13 ~ 16 bars.\"",
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

MidiPlayer()
