"""
script that demonstrate the use of musdb for evaluating separation results of musdb

"""

import onair
import museval
import stempeg
import sys
import os
import numpy as np
import argparse
from onair.config import stem_ids


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="onair-py test program")

    parser.add_argument("--root", type=str, help="root path of dataset")
    parser.add_argument(
        "--out-stem-dir",
        type=str,
        default=None,
        help="provide output stem dir",
    )
    # Model Parameters
    parser.add_argument(
        "--eval-dir",
        type=str,
        default=None,
        help="perform BSS evaluation, store eval this dir",
    )

    args = parser.parse_args()

    # initiate musdb
    onair_db = onair.DB(root=args.root)

    for track in onair_db:
        print(f'track: {track}')
        track_stems = track.stems

        if args.out_stem_dir is not None:
            for stem, stem_idx in stem_ids.items():
                curr_track = track_stems[stem_idx, :, :]
                target_path = os.path.join(args.out_stem_dir, f'{track.name}-{stem}.wav')
                stempeg.write_audio(
                    path=target_path,
                    data=curr_track,
                    sample_rate=track.rate
                )
                print(f'wrote audio for stem {stem}, stem index {stem_idx}, to {target_path}')
        if args.eval_dir is not None:
            estimates = mix_as_estimate(track)
            scores = museval.eval_mus_track(track, estimates, output_dir=args.eval_dir)
            print(scores)
