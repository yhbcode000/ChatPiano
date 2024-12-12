import pretty_midi

F_IN = 'guojiao_3track.mid'

how_many_bars = int(input('how many bars? > '))
assert how_many_bars < 12 # longer, and the timing may be wrong. pleaes remeasure

CUTOFF = 11.0 / 4 * how_many_bars
F_OUT = f'guojiao_3track_{how_many_bars}bars.mid'

def main():
    midi_data = pretty_midi.PrettyMIDI(F_IN)
    for ins in midi_data.instruments:
        ins: pretty_midi.Instrument
        new_notes = []
        for note in ins.notes:
            note: pretty_midi.Note
            if note.start < CUTOFF:
                new_notes.append(note)
                note.end = min(note.end, CUTOFF)
            else:
                break
        ins.notes = new_notes
        new_control_changes = []
        for cc in ins.control_changes:
            cc: pretty_midi.ControlChange
            if cc.time < CUTOFF:
                new_control_changes.append(cc)
            else:
                break
        ins.control_changes = new_control_changes
    midi_data.write(F_OUT)

if __name__ == '__main__':
    main()
