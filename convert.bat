ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda -framerate 60 -f image2 -i "2024-11-29T22-17-01\%%04d.bmp" -c:a copy -c:v h264_nvenc -b:v 5M out.mp4
pause
exit
