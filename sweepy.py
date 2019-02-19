import os
import pathlib
import shutil
import sys

class SweePy:
    docs_ext_list = ['doc', 'docx', 'odt', 'pdf']
    sheets_ext_list = ['xls','xlsx', 'ods']
    ppt_ext_list = ['ppt', 'pptx']
    text_ext_list = ['txt', 'rtf']
    imgs_ext_list = ['jpg', 'jpeg', 'png', 'bmp']
    music_ext_list = ['mp3', 'wav', 'aac', 'ogc', 'wma']
    mov_ext_list = ['mp4', 'mkv', 'wmv']
    web_ext_list = ['html', 'css', 'js', 'php']
    code_ext_list = ['c', 'cpp', 'java', 'go', 'cs']
    py_ext_list = ['py', 'pyc']
    inst_and_exe_ext_list = ['msi', 'tar', 'gz', 'bzip2', 'rpm', 'deb', 'sit', 'dmg', 'exe', 'out']
    compress_ext_list = ['zip', 'rar', '7z']

    def __init__(self):
        """Initialize PATH variable depending on the platform"""
        if 'win' in sys.platform:
            self.os = 'win'
            self.__PATH = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        elif 'lin' in sys.platform or 'mac' in sys.platform:
            self.os = 'unix'
            self.__PATH = os.environ['HOME']
        os.chdir(self.__PATH)

    def set_path(self, path):
        """Set the PATH varibale"""
        self.__PATH = path
        os.chdir(self.__PATH)

    def get_path(self):
        """Return the value of PATH variable"""
        return self.__PATH

    def sweep(self):
        """Organize the files baed on their extension"""
        self.__print_sep()
        print(f'reg: \n Inside "{self.__PATH}" directory...')
        try:
            for file in os.listdir(self.__PATH):
                if os.path.isfile(os.path.join(self.__PATH, file)):
                    print(f'inf: \n Moving {file} .......... ', end='')
                    ext = file.split('.')[-1].lower()
                    if ext in SweePy.docs_ext_list:
                        if not os.path.exists('Docs'):
                            os.mkdir('Docs')
                        shutil.move(file, 'Docs')
                    elif ext in SweePy.sheets_ext_list:
                        if not os.path.exists('Sheets'):
                            os.mkdir('Sheets')
                        shutil.move(file, 'Sheets')
                    elif ext in SweePy.ppt_ext_list:
                        if not os.path.exists('PPTs'):
                            os.mkdir('PPTs')
                        shutil.move(file, 'PPTs')
                    elif ext in SweePy.text_ext_list:
                        if not os.path.exists('Text Docs'):
                            os.mkdir('Text Docs')
                        shutil.move(file, 'Text Docs')
                    elif ext in SweePy.imgs_ext_list:
                        if not os.path.exists('Images'):
                            os.mkdir('Images')
                        shutil.move(file, 'Images')
                    elif ext in SweePy.music_ext_list:
                        if not os.path.exists('Musics'):
                            os.mkdir('Musics')
                        shutil.move(file, 'Musics')
                    elif ext in SweePy.mov_ext_list:
                        if not os.path.exists('Videos'):
                            os.mkdir('Videos')
                        shutil.move(file, 'Videos')
                    elif ext in SweePy.web_ext_list:
                        if not os.path.exists('Web'):
                            os.mkdir('Web')
                        shutil.move(file, 'Web')
                    elif ext in SweePy.code_ext_list:
                        if not os.path.exists('Coding'):
                            os.mkdir('Coding')
                        shutil.move(file, 'Coding')
                    elif ext in SweePy.py_ext_list:
                        if not os.path.exists('Python Scripts'):
                            os.mkdir('Python Scripts')
                        shutil.move(file, 'Python Scripts')
                    elif ext in SweePy.inst_and_exe_ext_list:
                        if not os.path.exists('Installers and Executables'):
                            os.mkdir('Installers and Executables')
                        shutil.move(file, 'Installers and Executables')
                    elif ext in SweePy.compress_ext_list:
                        if not os.path.exists('Win Archives'):
                            os.mkdir('Win Archives')
                        shutil.move(file, 'Win Archives')
                    else:
                        if not os.path.exists('Other Types'):
                            os.mkdir('Other Types')
                        shutil.move(file, 'Other Types')
                    print('inf: Done\n')
            print('inf: \n ----- Files SweePy-ed successfully -----\n')
            self.__print_sep()
        except Exception as e:
            print('err: ', e)

    def __print_sep(self):
        print('reg: **************************************************************')
