from ftplib import FTP
import os.path
import os


def ftpconnect(host, port=21, uname=None, pwd=None):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(uname, pwd)
    return ftp

def uploadfile(ftp, localfile, remotefile):
    print("|__准备开始上传到ftp")
    if not localfile or (not remotefile):
        return None
    buf_size = 1024
    # 先判断ftp上有无此文件
    localfile_size = os.path.getsize(localfile)
    try:
        ftpfile_size = ftp.size(remotefile)
        if localfile_size != ftpfile_size:
            raise Exception
        else:
            print("|__ftp服务器已包含此文件，不重复上传，删除本地文件")
            # os.remove(localfile)
    except Exception as no_file:
        print("|__检查ftp后无此文件")
        print(no_file)
        try:
            print("|__准备打开文件")
            with open(localfile, 'rb') as fp:
                # remotefile = "20181220_test.mp4"
                ftp.storbinary('STOR ' + remotefile, fp, buf_size)
            # 通过对比本地文件大小与上传到ftp的文件大小，判断是否上传成功
            print("|__上传成功，准备校验")
            ftpfile_size = ftp.size(remotefile)
            if localfile_size != ftpfile_size:
                print("|__上传ftp的文件校验失败")
                raise Exception ("上传文件校验失败")
            else:
                print("|__上传校验通过")
                # 删除本地文件
                # os.remove(localfile)
                print("|__本地文件删除成功")
        except Exception as bug:
            print(bug)
            return bug
    return True

file_test = ""
remote_file_test = os.path.split(file_test)[-1]
ftp_conn = ftpconnect("192.168.1.104",1023,"zouyaowu6","zouyaowu$163")
ftp_conn.cwd("6_upload")
upresult = uploadfile(ftp_conn, file_test, remote_file_test)