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
    audio_converter.other_to_wav_int16(path_in.get(), path_out.get(), transfer_format.get())
    print(path_in.get())
    print(path_out.get())
    hint.set('convert finished')


# 生成窗口
window = tk.Tk()
window.title('批量文件格式转换')
window.geometry('450x300')

tk.Label(window, text='格式转换').place(x=200, y=10)

# 输入文件夹：输入框及上传按钮
path_in = tk.StringVar()  # 定义变量
path_in.set(r'/Users/uniubi/PycharmProjects/audio_converter_kit/data')
label1 = tk.Label(window, text='输入文件夹:').place(x=50, y=50)
entry1 = tk.Entry(window, textvariable=path_in).place(x=160, y=50)
btn1 = tk.Button(window, text='上传地址', command=select_direction_path1).place(x=360, y=53)  # 按钮

# 目标地址：输入框及上传按钮
path_out = tk.StringVar()
path_out.set(r'/Users/uniubi/Desktop/dudu')
label2 = tk.Label(window, text='输出文件夹:').place(x=50, y=100)  # 从左偏，从上偏
entry2 = tk.Entry(window, textvariable=path_out).place(x=160, y=100)
btn2 = tk.Button(window, text='上传地址', command=select_direction_path2).place(x=360, y=103)

# 转换的格式
# aim_f = tk.StringVar()
# label3 = tk.Label(window, text='目标格式:').place(x=50, y=150)  # 从左偏，从上偏
# entry4 = tk.Entry(window, textvariable=aim_f).place(x=160, y=150)

transfer_format = tk.StringVar()
normal_ddl = Label(window, text='转换格式：').place(x=50, y=150)
ddl = tk.OptionMenu(window, transfer_format, 'wav', 'mp3').place(x=160, y=150)


submit_btn = tk.Button(window, text='  提 交  ', command=execute).place(x=200, y=190)

# 提示区域
hint = tk.StringVar()
hint.set('')
tk.Label(window, textvariable=hint).place(x=190, y=240)

# 不停的刷新显示
window.mainloop()
