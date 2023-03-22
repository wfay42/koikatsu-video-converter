This repo is used to convert the frames from Koikatsu's VideoExport plugin and convert them into a video using ffmpeg

The steps should look like
1. Take in a directory name
2. Zero-pad the frame images in that directory so they all are 4 digits long
3. Run ffmpeg on the files to create a video file with the same name as the folder
