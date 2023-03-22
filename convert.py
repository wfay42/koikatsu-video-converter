import os
import subprocess
import sys

def pad_files(dir_path):
    files = os.listdir(dir_path)
    files_renamed = 0
    for file in files:
        if file.endswith(".bmp"):
            fname = file.split(".")[0]
            new_fname = "%04d.bmp" % int(fname)
            # print(new_fname)
            if (new_fname != file):
                file_path = os.path.join(dir_path, file)
                new_file_path = os.path.join(dir_path, new_fname)
                os.rename(file_path, new_file_path)
                files_renamed += 1
    print ("Found %s files, and renamed %s of those" % (len(files), files_renamed))

def create_video(dir_path):
    dir_name = os.path.basename(dir_path)
    input_glob = '%s\\\\%%04d.bmp' % dir_path
    output_filename = "%s.mp4" % dir_name
    subprocess_args = ['ffmpeg', '-y', '-vsync', '0',
                       '-hwaccel', 'cuda',
                       '-hwaccel_output_format', 'cuda',
                       '-framerate', '60',
                       '-f', 'image2',
                       '-i', input_glob,
                       '-c:a', 'copy', '-c:v', 'h264_nvenc', '-b:v', '5M',
                       output_filename]

    success = subprocess.call(subprocess_args)
    print("Success? %s" % success)

def main():
    if len(sys.argv) < 2:
        print("Usage: convert.py dir_path")
        return

    dir_path = sys.argv[1]
    pad_files(dir_path)
    create_video(dir_path)

if __name__ == '__main__':
    main()
