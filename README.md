# onair-py

Python library for loading and using the OnAir Music Dataset, inspired by [sigsep-mus-db](https://github.com/sigsep/sigsep-mus-db).

### How to use

First download the zips of the [OnAir Music Dataset](https://github.com/OnAir-Music/OnAir-Music-Dataset), and unzip them in a common location:

```
$ mkdir -p ~/onair-music
$ mv ~/Downloads/OnAir-Music-Dataset-v4-*.zip ~/onair-music/
$ cd ~/onair-music
$ unzip OnAir-Music-Dataset-v4-misc.zip
$ unzip OnAir-Music-Dataset-v4-LoFi-Vol-3.zip
```

Install this library, set `ONAIR_PATH`, and run the example script:

```
$ export ONAIR_PATH=~/onair-music
$ python onair_example.py --eval-dir ./eval-stems/
track: Ronin - OnAir Music
vocals
accompaniment

vocals          ==> SDR:  -4.647  SIR:  -6.207  ISR:   0.009  SAR: -26.630
accompaniment   ==> SDR:  -2.666  SIR:   6.184  ISR:   0.091  SAR: -26.630

track: Set Me Free - OnAir Music
vocals
accompaniment
vocals          ==> SDR: -13.816  SIR:  -2.882  ISR:   0.858  SAR:  -3.895
accompaniment   ==> SDR: -11.614  SIR:   2.884  ISR:   3.593  SAR:  -3.895
```

### Mapping custom stems

The raw stems of the OnAir Music dataset are not provided with drums/bass/vocals/mix/other stems like MUSDB18-HQ.

Instead, the [onair/config.py](./onair/config.py) file defines how the custom stems should be assembled into musdb targets.

Some tracks are missing due to length mismatches in the stems or inappropriate stems (e.g. bass + kick are not provided separately). Also note that some of the LoFi hiphop tracks have very faint, ambient vocal components, and not a real singer.
