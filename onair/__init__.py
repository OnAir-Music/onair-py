from .audio_classes import MultiTrack, Source, Target
from os import path as op
import stempeg
import urllib.request
import collections
import numpy as np
import functools
import zipfile
import yaml
import onair
import errno
from .config import onair_subsets, onair_stems, stem_ids, sample_rate, onair_sources, onair_targets
import os


class DB(object):
    def __init__(
        self,
        root=None,
    ):
        self.sample_rate = sample_rate
        if root is None:
            if "ONAIR_PATH" in os.environ:
                self.root = os.environ["ONAIR_PATH"]
            else:
                raise RuntimeError("Variable `ONAIR_PATH` has not been set.")
        else:
            self.root = op.expanduser(root)

        self.tracks = self.load_mus_tracks()

    def __getitem__(self, index):
        return self.tracks[index]

    def __len__(self):
        return len(self.tracks)

    def get_track_indices_by_names(self, names):
        """Returns musdb track indices by track name

        Can be used to filter the musdb tracks for 
        a validation subset by trackname

        Parameters
        == == == == ==
        names : list[str], optional
            select tracks by a given `str` or list of tracknames

        Returns
        -------
        list[int]
            return a list of ``Track`` Objects
        """
        if isinstance(names, str):
            names = [names]
        
        return [[t.name for t in self.tracks].index(name) for name in names]

    def load_mus_tracks(self):
        """Parses the musdb folder structure, returns list of `Track` objects

        Returns
        -------
        list[Track]
            return a list of ``Track`` Objects
        """
        tracks = []

        for subset in onair_subsets:
            subset_folder = op.join(self.root, subset)
            for _, folders, files in os.walk(subset_folder):
                # parse pcm tracks and sort by name
                for track_name in sorted(folders):
                    track_folder = op.join(subset_folder, track_name)

                    if track_name not in onair_stems.keys():
                        continue

                    # create new mus track
                    track = MultiTrack(
                        name=track_name,
                        path=[
                            op.join(
                                track_folder,
                                t
                            )
                            for t in onair_stems[track_name]['mix']
                        ],
                        stem_id=stem_ids['mix'],
                        sample_rate=self.sample_rate
                    )

                    # add sources to track
                    sources = {}
                    for src in onair_sources:
                        # create source object
                        abs_path = [
                            op.join(
                                track_folder,
                                t
                            )
                            for t in onair_stems[track_name][src]
                        ]
                        sources[src] = Source(
                            track,
                            name=src,
                            path=abs_path,
                            stem_id=stem_ids[src],
                            sample_rate=self.sample_rate
                        )
                    track.sources = sources
                    track.targets = self.create_targets(track)

                    # add track to list of tracks
                    tracks.append(track)

        return tracks

    def create_targets(self, track):
        # add targets to track
        targets = collections.OrderedDict()
        for name, target_srcs in list(onair_targets.items()):
            # add a list of target sources
            target_sources = []
            for source, gain in list(target_srcs.items()):
                if source in list(track.sources.keys()):
                    # add gain to source tracks
                    track.sources[source].gain = float(gain)
                    # add tracks to components
                    target_sources.append(track.sources[source])
                    # add sources to target
            if target_sources:
                targets[name] = Target(
                    track,
                    sources=target_sources,
                    name=name
                )

        return targets

    def save_estimates(
        self,
        user_estimates,
        track,
        estimates_dir,
        write_stems=False
    ):
        """Writes `user_estimates` to disk while recreating the musdb file structure in that folder.

        Parameters
        ==========
        user_estimates : Dict[np.array]
            the target estimates.
        track : Track,
            musdb track object
        estimates_dir : str,
            output folder name where to save the estimates.
        """
        track_estimate_dir = op.join(
            estimates_dir, track.name
        )
        if not op.exists(track_estimate_dir):
            os.makedirs(track_estimate_dir)

        # write out tracks to disk
        if write_stems:
            pass
            # to be implemented
        else:
            for target, estimate in list(user_estimates.items()):
                target_path = op.join(track_estimate_dir, target + '.wav')
                stempeg.write_audio(
                    path=target_path,
                    data=estimate,
                    sample_rate=track.rate
                )

    def _check_exists(self):
        return op.exists(op.join(self.root, "train"))
