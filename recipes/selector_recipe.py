import tkinter as tk
languages = ['Mandarin', 'English', 'French']
global counter
counter = 1
class LanguageFamilies(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global canv, canv_id # IN ORDER TO MAKE THEM ACCESSIBLE TO OnDouble EVENT HANDLER
        canv = tk.Canvas(self, width=675, height=530, bg="white", relief="sunken")
        canv.config(scrollregion=(0,0,300,650), highlightthickness=0)
        canv.pack(side="right", expand=True, fill="both")

        # Create scroll bar
        sbar = tk.Scrollbar(self)
        canv.config(yscrollcommand=sbar.set)
        sbar.config(command=canv.yview)
        sbar.pack(side="right", fill="both")

        # Create Scroll List
        lstbox = tk.Listbox(self, width=240, height=530, relief="sunken", font="Courier")
        lst_scrollbar = tk.Scrollbar(self)
        lstbox.config(yscrollcommand=lst_scrollbar.set)
        lst_scrollbar.config(command=lstbox.yview)
        lstbox.pack(side="left", expand=True, fill="both")
        lst_scrollbar.pack(side="right", fill="both")
        lstbox.bind("<Double-Button-1>", self.OnDouble)

        # Add items to the lstbox
        i = 0
        while i < len(languages):
            lstbox.insert(i, languages[i])
            i += 1

        # Create a text inside canvas
        global textmatter
        textmatter = tk.Text(canv) # THE TEXT SHOULD BE PRINTED ON THE CANVAS
        textmatter.insert("end", "Double-click on a language on the left to view information.")
        textmatter.pack()

    #Binding Handler, ONE INDENTATION LEVEL IS REMOVED AS PER BRYAN'S SUGGESTION
    def OnDouble(self, event):
        global counter
        self.widget = event.widget
        selection = self.widget.curselection()
        content = self.widget.get(selection[0])
        if counter == 1:
            textmatter.delete(1.0, "end") # CLEAR THE TEXT WHICH IS DISPLAYED AT FIRST RUNNING
            textmatter.insert("end", content)
            counter += 1 #ONE ITEM HAS BEEN SELECTED AND PRINTED SUCCESSFULLY
        elif counter > 1:
            textmatter.delete(1.0, "end")
            textmatter.insert("end", content)
            counter = 1 # RESET THE COUNTER SO THAT NEXT SELECTED ITEM DISPLAYS PROPERLY

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("930x530")
    root.title("Language Families")
    LanguageFamilies(root).pack(fill="both", expand=True)
    root.mainloop()