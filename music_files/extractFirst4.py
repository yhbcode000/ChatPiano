import pretty_midi

F_IN = 'guojiao_3track.mid'
F_OUT = 'guojiao_3track_4bars.mid'

CUTOFF = 11.0

def main():
    midi_data = pretty_midi.PrettyMIDI(F_IN)
    for ins in midi_data.instruments:
        ins: pretty_midi.Instrument
        new_notes = []
        for note in ins.notes:
            note: pretty_midi.Note
            if note.start < 11:
                new_notes.append(note)
                note.end = min(note.end, CUTOFF)
            else:
                break
        ins.notes = new_notes
        new_control_changes = []
        for cc in ins.control_changes:
            cc: pretty_midi.ControlChange
            if cc.time < 11:
                new_control_changes.append(cc)
            else:
                break
        ins.control_changes = new_control_changes
    midi_data.write(F_OUT)

if __name__ == '__main__':
    main()
