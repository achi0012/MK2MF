# Process short videos

All steps below require `python3` and IDOL Media Server running on localhost, port 14000.

The following Python libraries are also required:
- pip install requests
- pip install Pillow
- pip install Jinja2

## Train golden records

### Extract target frames from golden record videos

python process.py normal/5974_Golden_DTV_3-2-1_1_220310141442.mp4 target_frames.cfg
python process.py normal/5984_Golden_DTV_2-2-1_1_220310140949.mp4 target_frames.cfg
python process.py normal/6006_Golden_DTV_4-3-1_1_220310141534.mp4 target_frames.cfg

### Train golden record video target frames

python train_image_hash.py target_frames/5974_Golden_DTV_3-2-1_1_220310141442
python train_image_hash.py target_frames/5984_Golden_DTV_2-2-1_1_220310140949
python train_image_hash.py target_frames/6006_Golden_DTV_4-3-1_1_220310141534

http://localhost:14000/a=gui#/train/imageHash(tool:select)

### Check we get no anomalies in target frames from golden record videos

python pair_target_frames.py target_frames/5974_Golden_DTV_3-2-1_1_220310141442 5974_Golden_DTV_3-2-1_1_220310141442 80
python pair_target_frames.py target_frames/5984_Golden_DTV_2-2-1_1_220310140949 5984_Golden_DTV_2-2-1_1_220310140949 80
python pair_target_frames.py target_frames/6006_Golden_DTV_4-3-1_1_220310141534 6006_Golden_DTV_4-3-1_1_220310141534 80

### Generate summary reports

python report_gen.py 5974_Golden_DTV_3-2-1_1_220310141442.json 5974_Golden_DTV_3-2-1_1_220310141442
python report_gen.py 5984_Golden_DTV_2-2-1_1_220310140949.json 5984_Golden_DTV_2-2-1_1_220310140949
python report_gen.py 6006_Golden_DTV_4-3-1_1_220310141534.json 6006_Golden_DTV_4-3-1_1_220310141534

## Process test videos

### Extract target frames from test videos

python process.py abnormal/5974_Golden_DTV_3-2-1_1_220310161818.mp4 target_frames.cfg
python process.py abnormal/5974_Golden_DTV_3-2-1_1_220310162217.mp4 target_frames.cfg
python process.py abnormal/5974_Golden_DTV_3-2-1_1_220310164959.mp4 target_frames.cfg
python process.py abnormal/5984_Golden_DTV_2-2-1_1_220310161326.mp4 target_frames.cfg
python process.py abnormal/6006_Golden_DTV_4-3-1_1_220310161910.mp4 target_frames.cfg
python process.py abnormal/6006_Golden_DTV_4-3-1_1_220310162302.mp4 target_frames.cfg

### Look for anomalies in target frames from test videos

python pair_target_frames.py target_frames/5974_Golden_DTV_3-2-1_1_220310161818 5974_Golden_DTV_3-2-1_1_220310141442 80
python pair_target_frames.py target_frames/5974_Golden_DTV_3-2-1_1_220310162217 5974_Golden_DTV_3-2-1_1_220310141442 80
python pair_target_frames.py target_frames/5974_Golden_DTV_3-2-1_1_220310164959 5974_Golden_DTV_3-2-1_1_220310141442 80
python pair_target_frames.py target_frames/5984_Golden_DTV_2-2-1_1_220310161326 5984_Golden_DTV_2-2-1_1_220310140949 80
python pair_target_frames.py target_frames/6006_Golden_DTV_4-3-1_1_220310161910 6006_Golden_DTV_4-3-1_1_220310141534 80
python pair_target_frames.py target_frames/6006_Golden_DTV_4-3-1_1_220310162302 6006_Golden_DTV_4-3-1_1_220310141534 80

### Generate summary reports

python report_gen.py 5974_Golden_DTV_3-2-1_1_220310161818.json 5974_Golden_DTV_3-2-1_1_220310141442 80
python report_gen.py 5974_Golden_DTV_3-2-1_1_220310162217.json 5974_Golden_DTV_3-2-1_1_220310141442 80
python report_gen.py 5974_Golden_DTV_3-2-1_1_220310164959.json 5974_Golden_DTV_3-2-1_1_220310141442 80
python report_gen.py 5984_Golden_DTV_2-2-1_1_220310161326.json 5984_Golden_DTV_2-2-1_1_220310140949 80
python report_gen.py 6006_Golden_DTV_4-3-1_1_220310161910.json 6006_Golden_DTV_4-3-1_1_220310141534 80
python report_gen.py 6006_Golden_DTV_4-3-1_1_220310162302.json 6006_Golden_DTV_4-3-1_1_220310141534 80

## Summary of these tests

### Training

Golden video | Keyframes produced
--- | ---
5974_Golden_DTV_3-2-1_1_220310141442 | 1
5984_Golden_DTV_2-2-1_1_220310140949 | 1
6006_Golden_DTV_4-3-1_1_220310141534 | 1

### Testing

> TP - True positive, i.e. correctly detected matches
> TN - True negative, i.e. correctly detected anomalies
> FP - False positive, i.e. incorrectly detected matches
> FN - False negative, i.e. incorrectly detected anomalies
> ACC - Accuracy, i.e. 100*(TP + TN) / (TP + TN + FP + FN)

#### Self check

Golden video | TP | TN | FP | FN | ACC
--- | --- | --- | --- | --- | ---
5974_Golden_DTV_3-2-1_1_220310141442 | 1 | 0 | 0 | 0 | 100%
5984_Golden_DTV_2-2-1_1_220310140949 | 1 | 0 | 0 | 0 | 100%
6006_Golden_DTV_4-3-1_1_220310141534 | 1 | 0 | 0 | 0 | 100%

#### Probe check

Golden video | Keyframes produced
--- | ---
5974_Golden_DTV_3-2-1_1_220310161818 | 1
5974_Golden_DTV_3-2-1_1_220310162217 | 21
5974_Golden_DTV_3-2-1_1_220310164959 | 5
5984_Golden_DTV_2-2-1_1_220310161326 | 2
6006_Golden_DTV_4-3-1_1_220310161910 | 1
6006_Golden_DTV_4-3-1_1_220310162302 | 2

Probe video | Golden video | TP | TN | FP | FN | ACC
--- | --- | --- | --- | --- | --- | ---
5974_Golden_DTV_3-2-1_1_220310161818 | 5974_Golden_DTV_3-2-1_1_220310141442 | 0 | 1 | 0 | 0 | 100%
5974_Golden_DTV_3-2-1_1_220310162217 | 5974_Golden_DTV_3-2-1_1_220310141442 | 1 | 20 | 0 | 0 | 100%
5974_Golden_DTV_3-2-1_1_220310164959 | 5974_Golden_DTV_3-2-1_1_220310141442 | 1 | 4 | 0 | 0 | 100%
5984_Golden_DTV_2-2-1_1_220310161326 | 5984_Golden_DTV_2-2-1_1_220310140949 | 1 | 1 | 0 | 0 | 100%
6006_Golden_DTV_4-3-1_1_220310161910 | 6006_Golden_DTV_4-3-1_1_220310141534 | 0 | 1 | 0 | 0 | 100%
6006_Golden_DTV_4-3-1_1_220310162302 | 6006_Golden_DTV_4-3-1_1_220310141534 | 0 | 2 | 0 | 0 | 100%
