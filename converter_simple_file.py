# 导入os模块
import os


def converter(target_file, destination_dir, format):
    destination_file = destination_dir + '/' + target_file.split('/')[-1]
    print(destination_file)


# 定义输入文件路径（其中r是转义字符，为了让 \ 不起作用）
path_in = r'/Users/uniubi/PycharmProjects/audio_converter_kit/data/test_1.m4a'
# 定义输出文件路径
path_out = r'/Users/uniubi/PycharmProjects/audio_converter_kit/data/test_1.mp3'
# 拼接cmd下的命令
cmd = 'ffmpeg -i ' + path_in+' ' + path_out
# 执行cmd命令
# os.system(cmd)


if __name__ == '__main__':
    converter('/Users/uniubi/PycharmProjects/audio_converter_kit/data/test_1.mp3', '/audio_converter_kit')
