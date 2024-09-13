from musecoco_text2midi_service.control import Text2Midi
from musecoco_text2midi_service.dao import load_config_from_file

if __name__=="__main__":
    config = load_config_from_file("storage/config/main_config.yaml")
    text2midi = Text2Midi(config)

    input_text = "This music's use of major key creates a distinct atmosphere, with a playtime of 1 ~ 15 seconds. The rhythm in this song is very pronounced, and the music is enriched by grand piano, cello and drum. Overall, the song's length is around about 6 bars. The music conveys edginess."

    midi_data, meta_data = text2midi.text_to_midi(input_text, return_midi=True)