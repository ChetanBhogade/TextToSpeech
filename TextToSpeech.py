# TEXT-TO-SPEECH with tkinter

from pyttsx3 import init
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from tkinter import filedialog as fd
import subprocess as sp


engin = init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voice', voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()


class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self._entry = ttk.Entry(self, textvariable=self.filepath)
        self._button = ttk.Button(self, text="Browse...", command=self.browse)

    def _display_widgets(self):
        self._entry.pack(fill='x', expand=True)
        self._button.pack(anchor='se')

    def getPath(self):
        return self.filepath.get()
    
    def browse(self):
        """ Browses a .png file or all files and then puts it on the entry.
        """

        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                             filetypes=self._filetypes))
        


root = tk.Tk()
root.title("Chetan")

# LabelFrame
label_frame = tk.LabelFrame(root, text = "Text-to-Speech")
label_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

# creating labels 
text_label = ttk.Label(label_frame, text = "Enter the text to speech : ")
text_label.grid(row = 0, column = 0, padx = 5, pady = 5)

divider_label = ttk.Label(label_frame, text = " Or ")
divider_label.grid(row = 1, columnspan = 2, padx = 2, pady = 2)

file_label = ttk.Label(label_frame, text = "Choose Your Text File : ")
file_label.grid(row = 2, column = 0, padx = 5, pady = 5)

# creating entry boxes
text_var = tk.StringVar()
text_entrybox = ttk.Entry(label_frame, width = 25, textvariable = text_var)
text_entrybox.grid(row = 0, column = 1, padx = 5, pady = 5)


file_browser = Browse(label_frame, initialdir=r"C:\Users", filetypes = (('Text File', '*.txt'),
                                                                        ("All files", "*.*")))
file_browser.grid(row=2, column=1, pady=5, padx=10)


# create button
def action():
    speck_text = text_var.get()
    file_path = file_browser.getPath()
    if speck_text != "" and file_path != "":
        m_box.showerror(title="Choose Only One", message="Please Check One of this!")
    elif speck_text != "" and file_path == "":
        speak("Your Text is ")
        speak(speck_text)
    elif file_path != "" and speck_text == "":
        try :
            with open(file_path, 'r') as rf:
                ans = m_box.askyesno(title="File", message="Would You Want to open a file? ")
                if ans:
                    programName = "notepad.exe"
                    sp.Popen([programName, file_path])
                speak("Your File Text is ")
                speak(rf.read())
        except FileNotFoundError as e:
            m_box.showerror(title=e, message="File Not Found. Please select proper file.")
        except :
            m_box.showerror(title="Error", message="Error Occur while reading your file.")
    else : 
        m_box.showerror(title="Choose Only One", message="Please Check One of this!")

    

submit_btn = ttk.Button(root, text = "Speak", command = action)
submit_btn.grid(row = 1, column = 0, padx = 5, pady = 4)


root.mainloop()

