import os
import numpy as np
import stempeg


class Track(object):
    """
    Generic audio Track that can be wav or stem file

    Attributes
    ----------
    name : str
        Track name
    path : str
        Absolute path of mixture audio file
    stem_id : int
        stem/substream ID
    targets : OrderedDict
        OrderedDict of mixted Targets for this ``track``.
    sources : Dict
        Dict of ``Source`` objects for this ``track``.
    chunk_start : float
        sets offset when loading the audio, defaults to 0 (beginning).
    chunk_duration : float
        sets duration for the audio, defaults to ``None`` (end).
    """

    def __init__(
        self,
        path="None",
        stem_id=None,
        subset="all",
        chunk_start=0,
        chunk_duration=None,
        sample_rate=None
    ):
        self.path = path
        self.stem_id = stem_id
        self.subset = subset
        self.chunk_start = chunk_start
        self.chunk_duration = chunk_duration
        self.sample_rate = sample_rate

        # load and store metadata
        single_path = None
        if type(self.path) == list:
            info = None
            samples = None
            duration = None
            rate = None
            for path in self.path:
                info_ = stempeg.Info(path)
                samples_ = int(info_.samples(self.stem_id))
                duration_ = info_.duration(self.stem_id)
                rate_ = info_.rate(self.stem_id)

                info = info_ if not info else info
                samples = samples_ if not samples else samples
                duration = duration_ if not duration else duration
                rate = rate_ if not rate else rate

                assert(info == info_)
                assert(samples == samples_)
                assert(duration == duration_)
                assert(rate == rate_)

                info = info_
                samples = samples_
                duration = duration_
                rate = rate_

            self.info = info
            self.samples = samples
            self.duration = duration
            self.rate = rate

        elif os.path.exists(self.path):
            self.info = stempeg.Info(self.path)
            self.samples = int(self.info.samples(self.stem_id))
            self.duration = self.info.duration(self.stem_id)
            self.rate = self.info.rate(self.stem_id)

        self._audio = None

    def __len__(self):
        return self.samples

    @property
    def audio(self):
        # return cached audio if explicitly set by setter
        if self._audio is not None:
            return self._audio
        # read from disk to save RAM otherwise
        else:
            return self.load_audio(
                self.path,
                self.stem_id,
                self.chunk_start,
                self.chunk_duration,
                self.sample_rate
            )

    @audio.setter
    def audio(self, array):
        self._audio = array

    def load_audio(
        self,
        paths,
        stem_id,
        chunk_start=0,
        chunk_duration=None,
        sample_rate=None
    ):
        """array_like: [shape=(num_samples, num_channels)]
        """
        if type(paths) == list:
            stem_id = 0
            audios = []
            for path in paths:
                if os.path.exists(path):
                    audio, rate = stempeg.read_stems(
                        filename=path,
                        stem_id=stem_id,
                        start=chunk_start,
                        duration=chunk_duration,
                        info=self.info,
                        sample_rate=sample_rate,
                        ffmpeg_format="s16le"
                    )
                    audios.append(audio)
                else:
                    raise ValueError(f"path {path} doesn't exist")
                self._rate = rate

            if len(audios) == 0:
                audio = np.zeros_like(self.audio)
            else:
                minlen = min([audio_.shape[0] for audio_ in audios])
                audio = sum([audio_[:minlen, :] for audio_ in audios])
            return audio
        elif os.path.exists(paths):
            stem_id = 0
            audio, rate = stempeg.read_stems(
                filename=paths,
                stem_id=stem_id,
                start=chunk_start,
                duration=chunk_duration,
                info=self.info,
                sample_rate=sample_rate,
                ffmpeg_format="s16le"
            )
            self._rate = rate
            return audio
        else:
            self._rate = None
            self._audio = None
            raise ValueError("Oops! %s cannot be loaded" % path)

    def __repr__(self):
        return "%s" % (self.path) if type(self.path) is not list else ','.join(["%s" % (p) for p in self.path])


class MultiTrack(Track):
    def __init__(
        self,
        path=None,
        name=None,
        subset="all",
        artist=None,
        title=None,
        sources=None,
        targets=None,
        sample_rate=None,
        *args,
        **kwargs
    ):
        super(MultiTrack, self).__init__(path=path, *args, **kwargs)

        self.name = name
        self.path = path
        try:
            split_name = name.split(' - ')
            self.artist = split_name[0]
            self.title = split_name[1]
        except IndexError:
            self.artist = artist
            self.title = title

        self.sources = sources
        self.targets = targets
        self.sample_rate = sample_rate
        self._stems = None

    @property
    def stems(self):
        """array_like: [shape=(stems, num_samples, num_channels)]
        """

        # return cached audio it explicitly set bet setter
        if self._stems is not None:
            return self._stems
        # read from disk to save RAM otherwise
        else:
            rate = self.rate
            S = []
            S.append(self.audio)
            # append sources in order of stem_ids
            for k, v in sorted(self.sources.items(), key=lambda x: x[1].stem_id):
                S.append(v.audio)

            # in case any stems have a length mismatch
            minlen = min([S_.shape[0] for S_ in S])
            S = np.array([S_[:minlen, :] for S_ in S])
            self._rate = rate
            return S

    def __repr__(self):
        return "%s" % (self.name)


class Source(Track):
    """
    An audio Target which is a linear mixture of several sources

    Attributes
    ----------
    name : str
        Name of this source
    stem_id : int
        stem/substream ID is set here.
    path : str
        Absolute path to audio file
    gain : float
        Mixing weight for this source
    """
    def __init__(
        self,
        multitrack,    # belongs to a multitrack
        name=None,     # has its own name
        path=None,     # might have its own path
        stem_id=None,  # might have its own stem_id
        gain=1.0,
        *args,
        **kwargs
    ):
        self.multitrack = multitrack
        self.name = name
        self.path = path
        self.stem_id = stem_id
        self.gain = gain
        self._audio = None

    def __repr__(self):
        return "%s" % (self.path) if type(self.path) is not list else ','.join(["%s" % (p) for p in self.path])

    @property
    def audio(self):
        # return cached audio if explicitly set by setter
        if self._audio is not None:
            return self._audio
        # read from disk to save RAM otherwise
        else:
            return self.multitrack.load_audio(
                self.path,
                self.stem_id,
                self.multitrack.chunk_start,
                self.multitrack.chunk_duration,
                self.multitrack.sample_rate
            )

    @audio.setter
    def audio(self, array):
        self._audio = array

    @property
    def rate(self):
        return self.multitrack.rate

# Target Track from musdb DB mixed from several musdb Tracks
class Target(Track):
    """
    An audio Target which is a linear mixture of several sources

    Attributes
    ----------
    multitrack : Track
        Track object
    sources : list[Source]
        list of ``Source`` objects for this ``Target``
    """
    def __init__(
        self, 
        multitrack,
        sources,
        name=None,  # has its own name
    ):
        self.multitrack = multitrack
        self.sources = sources
        self.name = name

    @property
    def audio(self):
        """array_like: [shape=(num_samples, num_channels)]

        mixes audio for targets on the fly
        """
        mix_list = []
        for source in self.sources:
            audio = source.audio
            if audio is not None:
                mix_list.append(
                    source.gain * audio
                )
        return np.sum(np.array(mix_list), axis=0)

    @property
    def rate(self):
        return self.multitrack.rate

    def __repr__(self):
        parts = []
        for source in self.sources:
            parts.append(source.name)
        return '+'.join(parts)
