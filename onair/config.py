sample_rate = 44100.

onair_subsets = [
    'OnAir-Music-Dataset-v4-misc',
    'OnAir-Music-Dataset-v4-LoFi-Vol-3',
]

onair_sources = [
    'vocals', 'drums', 'bass', 'other'
]

stem_ids = {
    'mix': 0,
    'drums': 1,
    'bass': 2,
    'other': 3,
    'vocals': 4,
}

onair_targets = {
    'vocals': {'vocals': 1},
    'drums': {'drums': 1},
    'bass': {'bass': 1},
    'other': {'other': 1},
    'accompaniment': {'bass': 1, 'drums': 1, 'other': 1},
    'linear_mixture': {'bass': 1, 'drums': 1, 'other': 1, 'vocals': 1},
}

onair_stems = {
        'Under My Skin - OnAir Music':
        {
            'mix': ['Under My Skin - OnAir Music.wav'],
            'drums': ['Break Drums.wav', 'Build Drums.wav', 'Kick.wav', 'Snare.wav'],
            'bass': ['Bass.wav'],
            'vocals':  ['Vox.wav'],
            'other': ['Guitar.wav', 'Piano.wav', 'Chords.wav', 'FX, Ambience, Drones.wav'],
        },
        'Set Me Free - OnAir Music':
        {
            'mix': ['Set Me Free - OnAir Music.wav'],
            'drums': ['Hats.wav', 'Kick.wav', 'Snare.wav'],
            'bass': ['Bass.wav'],
            'vocals':  ['Vox.wav'],
            'other': ['Lead Fill.wav', 'FX, Ambience, Drones.wav', 'Pluck.wav'],
        }
}

