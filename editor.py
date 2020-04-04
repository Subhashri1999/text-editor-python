import tkinter
from tkinter import *
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename 
from tkinter.filedialog import asksaveasfilename 
import tkinter.simpledialog
import tkinter.font
import tkinter.ttk
import tkinter.colorchooser as colorchooser
from tkinter import Tk, Frame, Menu, Button
from tkinter import LEFT, TOP, X, FLAT, RAISED, BOTH, END
from PIL import Image,ImageTk



current_font_family = "TimesNewRoman"
current_font_size = 12





class Notepad:
    root=tkinter.Tk()
   
    width=1000
    height=1000
    _text=Text(root,height=1000,width=1000)
    _text.pack()
    
    
    
    frame=Frame(root)
    menubar=Menu(root)
    File=Menu(menubar)
    Edit=Menu(menubar)
    Help=Menu(menubar)
    Format=Menu(menubar)
    Tools=Menu(menubar)
    Font=Menu(menubar)
    Insert=Menu(menubar)
    Font_Size=Menu(menubar)
    scroll=Scrollbar(_text)
    toolbar=Frame(root)

    __file=None
    def __init__(self,**kwargs):
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        try:
            self.width=kwargs['width']
        except KeyError:
            pass
        try:
            self.height=kwargs['height']
        except KeyError:
            pass
        self.root.title("Untitled-Pyeditor")
        self.File.add_command(label="New",command=self.newfile,accelerator="Ctrl+n")
        self._text.bind('<Control-n>',self.newfile)
        self.File.add_command(label="Open",command=self.openfile,accelerator="Ctrl+o")
        self._text.bind('<Control-o>',self.openfile)
        self.File.add_command(label="Save",command=self.savefile,accelerator="Ctrl+s")
        self._text.bind('<Control-s>',self.savefile)
        self.File.add_command(label="Exit",command=self.quit)
        self.menubar.add_cascade(label="File",menu=self.File)
        self.Edit.add_command(label="Cut",command=self.cut,accelerator="Ctrl+x")
        self._text.bind('<Control-x>',self.cut)
        self.Edit.add_command(label="Copy",command=self.copy,accelerator="Ctrl+c")
        self._text.bind('<Control-c>',self.copy)
        self.Edit.add_command(label="Paste",command=self.paste,accelerator="Ctrl+v")
        self._text.bind('<Control-v>',self.paste)
        self.menubar.add_cascade(label="Edit",menu=self.Edit)
        
        
        self.menubar.add_cascade(label="Format",menu=self.Format)
        
        self.Format.add_command(label="Bold",command=self.bold,accelerator="Ctrl+b")
        self.Format.add_command(label="Italic",command=self.italic,accelerator="Ctrl+i")
        self.Format.add_command(label="Strike",command=self.strike)
        self.Format.add_command(label="Highlight",command=self.highlight)
        self.Format.add_command(label="Underline",command=self.underline,accelerator="Ctrl+u")
        self._text.bind('<Control-b>',self.bold)
        self._text.bind('<Control-i>',self.italic)
        self._text.bind('<Control-u>',self.underline)
        
        self.Format.add_command(label="Align Center",command=self.align_center)
        self.Format.add_command(label="Align Left",command=self.align_left)
        self.Format.add_command(label="Align Right",command=self.align_right)
        self.Format.add_command(label="Justify",command=self.align_justify)
        self.Format.add_command(label="Undo",command=self.undo)
        self.Format.add_command(label="Redo",command=self.redo)
        self.Format.add_command(label="Select All",command=self.select_all)
        self.Format.add_command(label="Delete All",command=self.delete_all)
        
        self.menubar.add_cascade(label="Tools",menu=self.Tools)
        self.Tools.add_command(label="Find Text",command=self.find_text,accelerator="Ctrl+f")
        self._text.bind('<Control-f>',self.find_text)
        self.Tools.add_command(label="Replace Text",command=self.replace_text,accelerator="Ctrl+r")
        self._text.bind('<Control-r>',self.replace_text)
        self.Tools.add_command(label="Change Color",command=self.change_color)
        
        
        
        self.menubar.add_cascade(label="Font",menu=self.Font)
        self.Font.add_command(label="Arial",command=self.arial)
        self.Font.add_command(label="Calibri",command=self.calibri)
        self.Font.add_command(label="Times New Roman",command=self.tnr)
        self.Font.add_command(label="Algerian",command=self.algerian)
        self.Font.add_command(label="Verdana",command=self.verdana)
        self.Font.add_command(label="Cambria",command=self.cambria)
        self.menubar.add_cascade(label="Font_Size",menu=self.Font_Size)
        self.Font_Size.add_command(label="11",command=self.eleven)
        self.Font_Size.add_command(label="12",command=self.twelve)
        self.Font_Size.add_command(label="14",command=self.fourteen)
        self.Font_Size.add_command(label="18",command=self.eighteen)
        self.Font_Size.add_command(label="20",command=self.twenty)
        self.Font_Size.add_command(label="24",command=self.twentyfour)
        self.Font_Size.add_command(label="28",command=self.twentyfour)
        self.Font_Size.add_command(label="32",command=self.thirtytwo)
        
        
        
        
        self.menubar.add_cascade(label="Insert",menu=self.Insert)
        self.Insert.add_command(label="Image",command=self.image)
        self.Help.add_command(label="About Notepad",command=self.about)
        self.menubar.add_cascade(label="Help",menu=self.Help)
        
        
       
        self.toolbar = Frame(self.root, borderwidth=2, relief=RAISED)

        

        exitButton = Button(self.toolbar,text="new", relief=FLAT,
            command=self.quit)
        
        exitButton.pack(side=LEFT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)
        
        self.root.config(menu=self.menubar)
        self._text.bind("<space>", self.Spellcheck)

       
        self._words=open("words.txt").read().split("\n")
        

    
   
    
        
    def Spellcheck(self, event):
        index = self._text.search(r'\s', "insert", backwards=True, regexp=True)
        if index == "":
            index ="1.0"
        else:
            index = self._text.index("%s+1c" % index)
        word = self._text.get(index, "insert")
        if word in self._words:
            self._text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        else:
            self._text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))
            self._text.tag_config("misspelled",foreground="red")
    
       
    def image(self):
        self.__file = askopenfilename(initialdir="/",title="Select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        load = Image.open(self.__file)
        render = ImageTk.PhotoImage(load)
        
        img = tkinter.Label(image=render)
        img.image = render
        img.place(x=0,y=0)
        
        
    def arial(self):
        self._text.config(font="Arial")
    def tnr(self):
        self._text.config(font="TimesNewRoman")
    def calibri(self):
        self._text.config(font="Calibri")
    def algerian(self):
        self._text.config(font="Algerian")
    def verdana(self):
        self._text.config(font="Verdava")
    def cambria(self):
        self._text.config(font="Cambria")
    def delete_all(self):
        self._text.delete(1.0, END)
    def eleven(self):
        self._text.config(font=(False,11))
    def twelve(self):
        self._text.config(font=(False,12))
    def fourteen(self):
        self._text.config(font=(False,14))
    def eighteen(self):
        self._text.config(font=(False,18))
    def twenty(self):
        self._text.config(font=(False,20))
    def twentyfour(self):
        self._text.config(font=(False,24))
    def twentyeight(self):
        self._text.config(font=(False,28))
    def thirtytwo(self):
        self._text.config(font=(False,32))
    
    def undo(self,event=None):
        
        self._text.event_generate("<<Undo>>")
        return
    def redo(self,event=None):
        self._text.event_generate("<<Redo>>")
    def select_all(self):
        self._text.tag_add(SEL, "1.0", END)
    def quit(self):
        
        if self.__file==None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")])
        self.root.destroy()
        
    def about(self):
        messagebox.showinfo("PyEditor"," Copyrights- Subhashri 2019")
    def run(self):
        self.root.mainloop()
    def openfile(self,event=None):
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
        if self.__file=="":
            self.__file=None
			
        else:
            self.root.title(os.path.basename(self.__file) + " - Notepad") 
            self._text.delete(1.0,END) 
            file = open(self.__file,"r") 
            self._text.insert(1.0,file.read()) 
            file.close() 
    def newfile(self,event=None):
        self.root.title("Untitled-Pyeditor")
        self.__file=None
        self._text.delete(1.0,END)
    def savefile(self,event=None):
        
        if self.__file==None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 
            if self.__file=="":
                self.__file=None
            else:
                file=open(self.__file,"w")
                file.write(self._text.get(1.0,END))
                self.root.title(self.__file+"-Pyeditor")
                file.close()
        else:
            file=open(self.__file,"w")
            file.write(self._text.get(1.0,END))
            file.close()
    def make_tag(self):
        current_tag=self._text.tag_names()
        if "bold" in current_tag:
            weight="bold"
        else:
            weight="normal"
        if "italic" in current_tag:
            slant="italic"
        else:
            slant="roman"
        if "overstrike" in current_tag:
            overstrike = 1
        else:
            overstrike = 0
        if "underline" in current_tag:
            underline=1
        else:
            underline=0
       
        big_font = tkinter.font.Font(self._text, self._text.cget("font"))
        big_font.configure(slant= slant , weight= weight , underline= underline , overstrike= overstrike , family= current_font_family , size= current_font_size )
        self._text.tag_config("BigTag", font=big_font , foreground= "black" , background= "white") 
        if "BigTag" in  current_tag:
            self._text.tag_remove("BigTag" , "sel.first" , "sel.last")
        self._text.tag_add("BigTag" , "sel.first" , "sel.last")
            
    def cut(self,event=None):
        self._text.event_generate("<<Cut>>")
    def copy(self,event=None):
        self._text.event_generate("<<Copy>>")
    def paste(self,event=None):
        self._text.event_generate("<<Paste>>")
    def bold(self,event=None):
        
        current_tags = self._text.tag_names("sel.first")
        
        if "bold" in current_tags:
            self._text.tag_delete("bold","sel.first","sel.last")
            self._text.configure(font=("TimesNewRoman", 12,"normal"))
        else:
            self._text.tag_add("bold","sel.first","sel.last")
            self._text.tag_configure("bold",font=("TimesNewRoman", 12, "bold"))
           
        self.make_tag()
    def highlight(self):
        
        current_tags = self._text.tag_names()
        
        if "high" in current_tags:
            self._text.tag_delete("high","sel.first","sel.last")
            self._text.configure(background='white')
        else:
            self._text.tag_add("high","sel.first","sel.last")
            self._text.tag_configure("high",background="yellow")
        self.make_tag()
    def italic(self,event=None):
        
        
        current_tags = self._text.tag_names()
        
        if "italic" in current_tags:
            self._text.tag_delete("italic","sel.first","sel.last")
            self._text.configure(font=("TimesNewRoman", 12,"normal"))
        else:
            self._text.tag_add("italic","sel.first","sel.last")
            self._text.tag_configure("italic",font=("TimesNewRoman", 12, "italic"))
        self.make_tag()
    def strike(self):
        
        current_tags = self._text.tag_names()
        
        if "overstrike" in current_tags:
            self._text.tag_delete("overstrike","sel.first","sel.last")
            self._text.configure(font=("TimesNewRoman", 12,"normal"))
        else:
            self._text.tag_add("overstrike","sel.first","sel.last")
            self._text.tag_configure("overstrike",font=("TimesNewRoman", 12, "overstrike"))
        self.make_tag()
    def underline(self,event=None):
        current_tags = self._text.tag_names()
        if "underline" in current_tags:
            self._text.tag_delete("underline", "sel.first","sel.last")
            self._text.configure(font=("Times New Roman", 12,"normal"))
        else:
            self._text.tag_add("underline", "sel.first","sel.last")
            self._text.tag_configure("underline",font=("TimesNewRoman", 12, "underline"))
        self.make_tag()
    def check(self,value):
        self._text.tag_remove('found', '1.0', END)
        
        if value:
            idx = '1.0'
        while 1:
            idx = self._text.search(value, idx, nocase=1, stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(value))
           
            self._text.tag_add('found', idx, lastidx)
            idx = lastidx
            
            self._text.tag_config('found', foreground='red')
            
            
    
    def find_text(self,event=None):
        search_toplevel = Toplevel(self.root)
        search_toplevel.title('Find Text')
        search_toplevel.transient(self.root)
        search_toplevel.resizable(False, False)
        Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
        search_entry_widget = Entry(search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
        search_entry_widget.focus_set()
        Button(search_toplevel, text="Ok", underline=0, command=lambda: self.check( search_entry_widget.get())).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=5)
        Button(search_toplevel, text="Cancel", underline=0, command=lambda: self.find_text_cancel_button(search_toplevel)).grid(row=0, column=4, sticky='e' +'w', padx=2, pady=2)

    def replace_text(self,event=None):
        search_toplevel = Toplevel(self.root)
        search_toplevel.title('Replace Text')
        search_toplevel.transient(self.root)
        search_toplevel.resizable(False, False)
        Label(search_toplevel, text="Find All:").grid(row=0, column=0)
        search_entry_widget1 = Entry(search_toplevel, width=25)
        search_entry_widget1.grid(row=0, column=1, padx=2, pady=2)
        search_entry_widget1.focus_set()
        Label(search_toplevel, text="Replace All:").grid(row=1, column=0)
        search_entry_widget2 = Entry(search_toplevel, width=25)
        search_entry_widget2.grid(row=1, column=1, padx=2, pady=2)
        search_entry_widget2.focus_set()
        Button(search_toplevel, text="Ok", underline=0, command=lambda: self.check1( search_entry_widget1.get(),search_entry_widget2.get())).grid(row=0, column=2, sticky='e' +'w', padx=2, pady=5)
        Button(search_toplevel, text="Cancel", underline=0, command=lambda: self.find_text_cancel_button(search_toplevel)).grid(row=0, column=4, sticky='e' +'w', padx=2, pady=2)

    def check1(self,value1,value2):
        self._text.tag_remove('found', '1.0', END)
        
        if value1:
            idx = '1.0'
        while 1:
            idx = self._text.search(value1, idx, nocase=1, stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(value1))
           
            self._text.tag_add('found', idx, lastidx)
            #idx = lastidx
            
            self._text.tag_config('found', foreground='red')
            self._text.replace(idx,lastidx,value2)
    def find_text_cancel_button(self,search_toplevel):
        self._text.tag_remove('found', '1.0', END)
        search_toplevel.destroy()
        return "break"
    def remove_align_tags(self):
        all_tags = self._text.tag_names(index=None)
        if "center" in all_tags:
            self._text.tag_remove("center", "1.0", END)
        if "left" in all_tags:
            self._text.tag_remove("left", "1.0", END)
        if "right" in all_tags:
            self._text.tag_remove("right", "1.0", END)
    
    def align_center(self):
        self.remove_align_tags()
        self._text.tag_configure("center", justify='center')
        self._text.tag_add("center", 1.0, "end")
        
    def align_justify(self):
        self.remove_align_tags()
        
    def align_left(self):
        self.remove_align_tags()
        self._text.tag_configure("left", justify='left')
        self._text.tag_add("left", 1.0, "end")
    def align_right(self):
        self.remove_align_tags()
        self._text.tag_configure("right", justify='right')
        self._text.tag_add("right", 1.0, "end")
    def change_color(self):
        color = colorchooser.askcolor(initialcolor='#ff0000')
        color_name = color[1]
        global fontColor
        fontColor = color_name
        
        self._text.configure(foreground=fontColor)
        self.make_tag()

        

    
    
    
        
        
            
    
            
        
            
            
Notepad=Notepad(width=1000,height=200)
Notepad.run()
    
    
              
    
        
