import os
# CBT Nuggets - Cisco DEVNET Associate - 200-901 DEVASC


def read_file_list():
    f = open('./video/list.txt', 'r')
    lines = f.read().splitlines()
    f.close()

    x = {}
    for line in lines:
        if line.startswith("##"):
            continue
        else:
            video_no = line.split("-")[0]
            if len(video_no) < 3:
                video_no = "0"*(3-len(video_no))+video_no
            video_name = line.split("-")[1]
            x[video_no] = video_name
    return x


def read_file_name(file_list):
    list = sorted(os.listdir('video/'))
    for file in list:
        if file.startswith('DevNet ('):
            video_no = file.split('DevNet (')[1].split(").mp4")[0]
            if len(video_no) < 3:
                video_no = "0"*(3-len(video_no))+video_no
                file_name = file_list[video_no]
            else:
                file_name = file_list[video_no]
            old_file_name = 'video/'+file
            new_file_name = 'video/'+video_no+" - "+file_name+".mp4"
            os.rename(old_file_name, new_file_name)


def main():
    file_list = read_file_list()
    print(file_list)
    read_file_name(file_list)


if __name__ == "__main__":
    main()
