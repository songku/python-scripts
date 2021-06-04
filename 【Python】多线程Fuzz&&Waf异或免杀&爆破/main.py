# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ftplib
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ftp_check():
    while not q.empty():
        dict=q.get()
        dict=dict.split('|')
        username=dict[0]
        password=dict[1]
        ftp=ftplib.FTP()
        try:
            ftp.connect('192.168.0.101',21)
            ftp.login(username,password)
            ftp.retrlines('list')#读取ftp服务器上内容
            ftp.close()
            print('success!'+username+'|'+password)
        except ftplib.all_errors:#账号密码连接错误的异常处理
            print('failed'+username+'|'+password)
            ftp.close()
            pass
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
