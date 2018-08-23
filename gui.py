# GUI
# GUI program
# Anatoli Penev
# 14.02.2018

import tkinter


class Showinfo:
    def __init__(self):
        # create main window
        self.window = tkinter.Tk()

        # create frames
        self.top_frame = tkinter.Frame(self.window)
        self.bot_frame = tkinter.Frame(self.window)
        self.mid_frame = tkinter.Frame(self.window)

        # create widgets
        self.prompt_label = tkinter.Label(self.top_frame, text="Press to show information or quit to exit program!")

        # pack widgets
        self.prompt_label.pack(side="left")

        # create widgets mid
        self.desc_label = tkinter.Label(self.mid_frame, text="Click!")

        # string with object method
        self.value = tkinter.StringVar()
        self.show_info = tkinter.Label(self.bot_frame, textvariable=self.value)

        # pack widgets mid
        self.desc_label.pack(side="left")
        self.show_info.pack(side="left")

        # create buttons
        self.show_info_button = tkinter.Button(self.mid_frame, text="Show Info", command=self.info_show)
        self.quit_button = tkinter.Button(self.top_frame, text="Quit", command=self.window.destroy)

        # pack buttons
        self.show_info_button.pack()
        self.quit_button.pack()

        # pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        # enter in main loop
        tkinter.mainloop()

    def info_show(self):
        info = "Anatoli Penev" + "\n" + "Lollandsgade 34, 5000 Odense C"

        # display info
        self.value.set(info)


gui = Showinfo()
print.meseflf