from tkinter import *
from tkinter import filedialog
from sweepy import SweePy

class TkinterConsole(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=master, bg='black')

        self.output = Text(self, font=('Times', 11), fg='white', bg='black')
        self.scroll_bar = Scrollbar(self, command=self.output.yview, orient='vertical')
        self.output.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
        self.output.pack(side=LEFT, fill=BOTH, padx=5, pady=5)

        self.output.tag_configure('reg', background='black', foreground='white')
        self.output.tag_configure('info', background='black', foreground='lightblue')
        self.output.tag_configure('err', background='black', foreground='red')

        self.output.config(state='disabled')

class RedirectStdOut:
    def __init__(self, cmd_line):
        self.cmd_line = cmd_line

    def write(self,string):
        self.cmd_line.config(state='normal')
        if string.startswith('inf: '):
            tag = 'info'
        elif string.startswith('err: '):
            tag = 'err'
        else:
            tag = 'reg'
        self.cmd_line.insert(END, string[5:], tag)
        self.cmd_line.see(END)
        self.cmd_line.config(state='disabled')

class App:
    def __init__(self):
        self.root = Tk()
        self.root.configure(background='#fff8e1')
        self.root.title('SweePy - A Smart Way to Organize Files')
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.sweepy = SweePy()

    def run(self):
        self.__render_screen()
        self.root.mainloop()

    def __change_path(self):
        try:
            self.txt_path.set(filedialog.askdirectory())
            self.sweepy.set_path(self.txt_path.get())
        except OSError as ose:
            print('err: \n Invalid Path to sweep. Choose a valid one!\n') #An exception

    def __sweep(self):
        self.sweepy.sweep()

    def __render_screen(self):
        self.lbl_text_path = Label(self.root, text='Choose a path to sweep', anchor=W, justify=LEFT, bg='#fff8e1')
        self.lbl_text_path.pack(side=TOP, padx=5, fill=X)

        browse_frame = Frame(self.root)
        browse_frame.pack(padx=10, pady=5, fill=BOTH, side=TOP)
        self.txt_path = StringVar()
        self.txt_path.set(self.sweepy.get_path())
        self.lbl_path = Label(browse_frame, textvariable=self.txt_path, fg='black', bg='#e0e0e0', border=5)
        self.lbl_path.pack(fill=X)

        button_frame = Frame(self.root, bg='#fff8e1')
        button_frame.pack(padx=10, fill=BOTH, side=TOP)
        self.btn_browse = Button(button_frame, text='Browse', command=self.__change_path, padx=3, pady=3, relief='groove', bg='#ffe0b2')
        self.btn_browse.pack(side=LEFT, padx=95)
        self.btn_sweep = Button(button_frame, text='Sweep', command=self.__sweep, padx=3, pady=3, relief='groove', bg='#ffe0b2')
        self.btn_sweep.pack(side=LEFT, padx=95)

        btn_quit = Button(self.root, text='Quit', command=self.root.destroy, padx=10, pady=3, relief='groove', bg='#ffe0b2')
        btn_quit.pack(side=BOTTOM, pady=5)

        console = TkinterConsole(self.root)
        console.pack(padx=15, pady=5, fill=BOTH)
        sys.stdout = RedirectStdOut(console.output)
        sys.stderr = RedirectStdOut(console.output)
        console.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
