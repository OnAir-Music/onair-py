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
            'other': ['Lead Fill.wav', 'Ambience, FX, Drones.wav', 'Pluck.wav'],
        },
        'Ronin - OnAir Music':
        {
            'mix': ['Ronin - OnAir Music.wav'],
            'drums': ['Ronin ft. KXNE Stems - Drums.wav'],
            'bass': ['Ronin ft. KXNE Stems - 808.wav'],
            'vocals':  ['Ronin ft. KXNE Stems - Acappella.wav'],
            'other': ['Ronin ft. KXNE Stems - Main Loop.wav', 'Ronin ft. KXNE Stems - Plucks.wav'],
        },
        'Yaku - OnAir Music':
        {
            'mix': ['Yaku - OnAir Music.wav'],
            'drums': ['Idea 3 Stems - Drums.wav'],
            'bass': ['Idea 3 Stems - Bass.wav'],
            'vocals': ['Idea 3 Stems - Ambience.wav'],
            'other': ['Idea 3 Stems - Guitar Lead.wav'],
        },
        'Ramen Rain - OnAir Music':
        {
            'mix': ['Ramen Rain - OnAir Music.wav'],
            'bass': ['Idea 2 Stems - Bass.wav'],
            'drums': ['Idea 2 Stems - Drums.wav', 'Idea 2 Stems - Brshes.wav'],
            'vocals': ['Idea 2 Stems - Ambience.wav'],
            'other': ['Idea 2 Stems - Chords.wav', 'Idea 2 Stems - Guitar Main.wav', 'Idea 2 Stems - Keys 2.wav', 'Idea 2 Stems - Sax FX.wav'],
        },
        'Bouncin Around - OnAir Music':
        {
            'mix': ['Bouncin Around - OnAir Music.wav'],
            'bass': ['Idea 1 Stems - Bass.wav'],
            'drums': ['Idea 1 Stems - Drums.wav', 'Idea 1 Stems - Brushes.wav', 'Idea 1 Stems - Tambo.wav'],
            'vocals': ['Idea 1 Stems - Ambience.wav'],
            'other': ['Idea 1 Stems - Main Gtr.wav', 'Idea 1 Stems - Keys 1.wav', 'Idea 1 Stems - Keys 2.wav'],
        },
        #'Vibin Vibin - OnAir Music':
        #{
        #    'mix': ['Vibin Vibin - OnAir Music.wav'],
        #    'bass': ['Idea 5 Stems - Bass.wav'],
        #    'drums': ['Idea 5 Stems - Drums.wav', 'Idea 5 Stems - Hats.wav', 'Idea 5 Stems - Shaker.wav'],
        #    'vocals': ['Idea 5 Stems - FX.wav', 'Idea 5 Stems - Ambience.wav'],
        #    'other': ['Idea 5 Stems - Ad Guitars.wav', 'Idea 5 Stems - Main Guitar.wav'],
        #},
        #'Autumn in NY - OnAir Music': - omitted due to length issues/mismatches
        #{
        #    'mix': ['Autumn in NY - OnAir Music.wav'],
        #    'bass': ['Idea 4 Stems - Bass.wav'],
        #    'drums': ['Idea 4 Stems - Drums.wav', 'Idea 4 Stems - Brushes.wav'],
        #    'vocals': [],
        #    'other': ['Idea 4 Stems - Amb.wav', 'Idea 4 Stems - Guitar Main.wav', 'Idea 4 Stems - Horns.wav', 'Idea 4 Stems - Keys Chords.wav', 'Idea 4 Stems - Keys Twinkle.wav', 'Idea 4 Stems - Trumps.wav'],
        #},
        #'Reflections - OnAir Music' - omitted due to bass and drums not provided separately
        #'Aurora Borealis - OnAir Music' - omitted due to bass and drums not provided separately
        #'Action - OnAir Music' - omitted due to bass and drums not provided separately
}
