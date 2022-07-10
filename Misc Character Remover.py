from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import sys
import os

#Class containt GUI elements
class MainGUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.mDes()

    #mDes contains all elements for the home page
    def mDes(self):
        iFile = open(os.path.dirname(sys.argv[0])+"\\iFile.txt", "r")
        iText = iFile.read()
        iFile.close()
        self.iPar = tk.Message(self, font=("Times", 11), width=400, text=iText)
        self.iPar.pack(side="top", fill="x")

        self.sp0 = tk.Frame(self, bg="Black", width=380, height=1)
        self.sp0.pack(side="top", padx=5, pady=5)

        self.hFrame = tk.Frame(self, width=400, height=100)
        self.hFrame.grid_propagate(False)
        self.hFrame.pack(side="top")

        self.fPath = tk.Entry(self.hFrame, font=("Helvetica", 14), width=26, relief="solid")
        self.fPath.insert(0, "Folder Path...")
        self.fPath.grid(row=0,column=0, padx=(8,5), pady=10)

        self.jLabe = tk.Label(self.hFrame, text="Junk Character:", font=("Helvetica", 14))
        self.jLabe.grid(row=1, column=0, padx=5, sticky="w")
        
        self.jChar = tk.Entry(self.hFrame, font=("Helvetica", 14), width=3, relief="solid")
        self.jChar.grid(row=1, column=0,padx=(19,0))

        self.eButt = tk.Button(self.hFrame, text="Execute", font=("Helvetica", 10), relief="solid", borderwidth=1, bg="lightGray", width=25, command=self.execute)
        self.eButt.grid(row=1,column=0,columnspan=2, padx=(183,0))

        def hover(event):
            event.widget.config(bg="darkGray")

        def uHover(event):
            event.widget.config(bg="lightGray")

        def fBrowse():
            foPath = filedialog.askdirectory()
            self.fButt.config(relief="solid")

            if foPath.replace(" ", "") != "":
                self.fPath.delete(0, "end")
                self.fPath.insert(0, foPath)
            else:
                pass

        self.fButt = tk.Button(self.hFrame, text="Browse", font=("Helvetica", 10), relief="solid", borderwidth=1, bg="lightGray", width=10, command=fBrowse)
        self.fButt.grid(row=0,column=1)

        self.fButt.bind("<Enter>", hover)
        self.fButt.bind("<Leave>", uHover)
        self.eButt.bind("<Enter>", hover)
        self.eButt.bind("<Leave>", uHover)

    def execute(self):
        foPath = self.fPath.get()
        jChara = self.jChar.get()

        if os.path.isdir(foPath):
            if jChara.replace(" ", "") != "":
                for base, dirs, files in os.walk(foPath):
                    for file in files:
                        bFile = file.split(".")
                        lFile = [x.lower() for x in bFile]
                        nFile = ""

                        try:
                            nFile = " ".join(bFile[:lFile.index("v")])+" "+bFile[lFile.index("v")]+".".join(bFile[lFile.index("v")+1:])
                        except Exception as e:
                            nFile = " ".join(bFile[:-1])+"."+bFile[-1]
                            os.rename(os.path.join(base,file),os.path.join(base,nFile))
                        else:
                            os.rename(os.path.join(base,file),os.path.join(base,nFile))

                    for fir in dirs:
                        os.rename(os.path.join(base,fir),os.path.join(base," ".join(fir.split("."))))

                messagebox.showinfo("Congradulations!", "Your files have been cleaned please enjoy!")
                self.fPath.delete(0,"end")
                self.jChar.delete(0,"end")
            else:
                messagebox.showerror("Error!", "You must enter a valid character!")
        else:
            messagebox.showerror("Error!", "You must use a valid folder path!")

if __name__ == "__main__":
    root  = tk.Tk()
    root.title("Misc Character Remover Alpha 1.0")
    root.iconbitmap(os.path.dirname(sys.argv[0])+"\\Icon.ico")
    root.geometry("400x250")
    root.resizable(0,0)
    MainGUI(root).pack(side="top", fill="both")
    root.mainloop()
