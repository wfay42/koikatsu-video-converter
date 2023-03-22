ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda -framerate 60 -f image2 -i "2023-03-20T00-13-59\%%04d.bmp" -c:a copy -c:v h264_nvenc -b:v 5M out.mp4
pause
exit
