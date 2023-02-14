import os
import argparse
from tqdm.auto import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--working_dir', type=str, help='working directory를 입력하세요.',
                    default='C:/Users/USER/Desktop/python/competition/CarCrashAnalysisAIContest/')
args = parser.parse_args()

DATA_PATH = os.path.join(args.working_dir, 'data/')
FFMPEG_PATH = os.path.join(
    args.working_dir, 'ffmpeg-5.1.2-essentials_build/bin')
TRAIN_VIDEO_PATH = os.path.join(DATA_PATH, 'train/')
TEST_VIDEO_PATH = os.path.join(DATA_PATH, 'test/')


if not FFMPEG_PATH in os.environ['PATH']:
    os.environ['PATH'] += f';{FFMPEG_PATH}'
    print('ffmpeg added to the PATH')
else:
    print('already added to the PATH')

train_videos = os.listdir(TRAIN_VIDEO_PATH)
test_videos = os.listdir(TEST_VIDEO_PATH)
TRAIN_THUMBNAIL_PATH = os.path.join(DATA_PATH, 'train_thumbnail/')
TEST_THUMBNAIL_PATH = os.path.join(DATA_PATH, 'test_thumbnail/')
if not os.path.isdir(TRAIN_THUMBNAIL_PATH):
    os.makedirs(TRAIN_THUMBNAIL_PATH)

if not os.path.isdir(TEST_THUMBNAIL_PATH):
    os.makedirs(TEST_THUMBNAIL_PATH)


print('making train videos thumbnail...')
for video in tqdm(train_videos):
    file_name = video[:-4]
    os.popen(
        f'ffmpeg -hide_banner -loglevel error -y  -i {TRAIN_VIDEO_PATH}{video} -vframes 1 -vf thumbnail=50 {TRAIN_THUMBNAIL_PATH}{file_name}.jpg')

print('making test videos thumbnail...')
for video in tqdm(test_videos):
    file_name = video[:-4]
    os.popen(
        f'ffmpeg -hide_banner -loglevel error -y  -i {TEST_VIDEO_PATH}{video} -vframes 1 -vf thumbnail=50 {TEST_THUMBNAIL_PATH}{file_name}.jpg')
