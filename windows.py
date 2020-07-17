import tkinter as tk
from tkinter.filedialog import *  # tkinter下的文件处理模块
import audio_converter


# from video_format_convert.convert import convert


# 点击“选择文件夹”调用该功能
def select_direction_path1():
    path_ = askdirectory(title='选择文件夹')
    path_in.set(path_)


def select_direction_path2():
    path_ = askdirectory(title='选择文件夹')
    path_out.set(path_)


# 点击提交执行的功能
def execute():
    hint.set('converting . . .')
    audio_converter.other_to_wav_int16(path_in.get(), path_out.get(), transfer_format.get(), sampling_rate_value.get())
    print(path_in.get())
    print(path_out.get())
    hint.set('convert finished')


# 生成窗口
window = tk.Tk()
window.title('批量文件格式转换')
window.geometry('600x450')

tk.Label(window, text='格式转换').place(x=200, y=10)

# 输入文件夹：输入框及上传按钮
path_in = tk.StringVar()  # 定义变量
# path_in.set(r'/Users/uniubi/PycharmProjects/audio_converter_kit/data')
label1 = tk.Label(window, text='Source folder:').place(x=50, y=50)
entry1 = tk.Entry(window, textvariable=path_in).place(x=160, y=50)
btn1 = tk.Button(window, text='Upload', command=select_direction_path1).place(x=360, y=53)  # 按钮

# 目标地址：输入框及上传按钮
path_out = tk.StringVar()
# path_out.set(r'/Users/uniubi/Desktop/dudu')
label2 = tk.Label(window, text='Target path:').place(x=50, y=100)  # 从左偏，从上偏
entry2 = tk.Entry(window, textvariable=path_out).place(x=160, y=100)
btn2 = tk.Button(window, text='Upload', command=select_direction_path2).place(x=360, y=103)

# 转换的格式
options_format = ['wav', 'mp3', 'wma', 'm4a']
transfer_format = tk.StringVar()
transfer_format.set('Please choose')
format_label = Label(window, text='Format：').place(x=50, y=150)
format_selector = tk.OptionMenu(window, transfer_format, *options_format).place(x=130, y=150)


# 采样率
options_sampling_rate = ['8000HZ', '11025HZ', '24000HZ', '32000HZ', '44100HZ']
sampling_rate_value = tk.StringVar()
sampling_rate_value.set('Please choose')
sampling_rate_l = Label(window, text='Sampling rate：').place(x=50, y=200)
sampling_rate_selector = tk.OptionMenu(window, sampling_rate_value, *options_sampling_rate).place(x=180, y=200)


submit_btn = tk.Button(window, text='  Submit  ', command=execute).place(x=200, y=250)

# 提示区域
hint = tk.StringVar()
hint.set('')
tk.Label(window, textvariable=hint).place(x=140, y=280)

# 不停的刷新显示
window.mainloop()
