import os

digit_prefix = 3
list_file = "list.txt"
target_folder = "target"
OS_file = [".DS_Store"]
file_extension = ".mp4"
ignore_file = [list_file]
ignore_file.extend(OS_file)
file_delimiter = "-"


def read_file_list():
    f = open("./" + target_folder + "/" + list_file, 'r')
    lines = f.read().splitlines()
    f.close()

    x = {}
    for line in lines:
        if line.startswith("##"):
            continue
        else:
            seq_num = line.split(file_delimiter)[0]
            if len(seq_num) < digit_prefix:
                seq_num = "0"*(digit_prefix-len(seq_num))+seq_num
            video_name = line.split(file_delimiter)[1]
            x[seq_num] = video_name
    return x


def read_file_name(file_list):
    path = './' + target_folder
    for root, directories, files in os.walk(path, topdown=False,):
        for file in files:
            if file not in ignore_file:
                seq_num = file.split(file_delimiter)[0]
                if len(seq_num) < digit_prefix:
                    seq_num = "0"*(digit_prefix-len(seq_num))+seq_num
                    file_name = file_list[seq_num]
                else:
                    file_name = file_list[seq_num]

                old_file_name = os.path.join(root, file)
                new_file_name = os.path.join(
                    root, seq_num + " " + file_delimiter + " " + file_name + file_extension)
                os.rename(old_file_name, new_file_name)


def main():
    file_list = read_file_list()
    # print(file_list)
    read_file_name(file_list)


if __name__ == "__main__":
    main()
