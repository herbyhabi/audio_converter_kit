from ffmpy import FFmpeg
import os


def other_to_wav_int16(src_dir, dst_dir, aim_format, sampling_rate):
    """
    将其他格式的音频文件转化为wav格式且int16数据类型、单声道、16000Hz采样率
    root： 父级目录
    dirs：root中每一个文件夹的名字
    files：所有文件的文件名
    """
    settings = []
    if sampling_rate != '请选择':
        settings.append('-ar')
        settings.append(sampling_rate[:-2])

    for root, dirs, files in os.walk(src_dir):
        for name in files:
            # print(os.path.join(root, name))    # 打印出src_dir目录下所有的文件的绝对路径名
            audio_name_src = os.path.join(root, name)

            if aim_format == '请选择':
                audio_name_dst = os.path.join(dst_dir, name)
            else:
                audio_name_dst = os.path.join(dst_dir, name.split('.')[0] + '.' + aim_format)

            # 将other格式文件转化为‘pcm-16位 float、1通道、16000Hz采样率的wav文件: ['-acodec', 'pcm_s16le', '-ac', '1', '-ar', '16000']'
            ff = FFmpeg(
                inputs={audio_name_src: None},
                outputs={audio_name_dst: settings}
            )
            ff.run()


if __name__ == '__main__':
    other_to_wav_int16('/Users/uniubi/PycharmProjects/audio_converter_kit/data',
                       '/Users/uniubi/Desktop/dudu', 'mp3', '44100HZ')
