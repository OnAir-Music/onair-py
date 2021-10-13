"""
script that demonstrate the use of musdb for evaluating separation results of musdb

"""

import onair
import museval


def mix_as_estimate(track):
    # get the mixture path for external processing
    track.path

    # get the sample rate
    track.rate

    # return any number of targets
    estimates = {
        'vocals': track.audio,
        'accompaniment': track.audio,
    }

    return estimates


# initiate musdb
onair_db = onair.DB()

for track in onair_db:
    print(f'track: {track}')
    estimates = mix_as_estimate(track)
    scores = museval.eval_mus_track(track, estimates)
    print(scores)
