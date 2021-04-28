
try:
    import Tkinter as tk
except:
    import tkinter as tk
try:
    import ttk
except:
    from tkinter import ttk

def createCustomEntry(style):
    if 'Custom.Entry.field' not in style.element_names():
        style.element_create('Custom.Entry.field', 'from', 'default')
    if style.theme_use() in ['alt', 'clam', 'default', 'classic']:
        style.layout('Custom.Entry', style.layout('TEntry'))
    else:
        style.layout("Custom.Entry", [
            ("Custom.Entry.field", {'sticky': 'nswe', 'border': '1', 'children': [
                ("Custom.Entry.padding", {'sticky':'nswe', 'children': [
                    ("Custom.Entry.textarea", {'sticky':'nswe'})
                ]})
            ]})
        ])
    style.configure('Custom.Entry', **style.configure('TEntry'))
    style.map('Custom.Entry', **style.map('TEntry'))
    style.map('Custom.Entry',
        fieldbackground=[(['invalid','!disabled'], '#ff4040'),
                            (['invalid','disabled'], '#ffc0c0')])

def show_invalid():
    [w.state(['invalid']) for w in (entry, entry2)]

def show_valid():
    [w.state(['!invalid']) for w in (entry, entry2)]


root = tk.Tk()
# Simple version:
style = ttk.Style()
style.layout("Custom.Entry", style.layout('TEntry'))
style.configure("Custom.Entry", **style.configure('TEntry'))
style.map("Custom.Entry", **style.map('TEntry'))
style.map("Custom.Entry",
    fieldbackground=[(['invalid','!disabled'], '#ff4040'),
                     (['invalid','disabled'], '#ffc0c0')])

#createCustomEntry(style)

root.title("Testing of Style Customization")

appframe = tk.Frame(root, padx=12, pady=12)
appframe.pack(expand=True, fill=tk.BOTH)

entry_var = tk.StringVar()
entry = ttk.Entry(appframe, textvariable=entry_var, width=40,
                  exportselection=False, style="Custom.Entry")
entry.grid(row=0, column=0, padx=3, pady=3, sticky=tk.EW)

entry2 = ttk.Entry(appframe, textvariable=entry_var, width=40,
                   exportselection=False, style="Custom.Entry")
entry2.grid(row=1, column=0, padx=3, pady=3, sticky=tk.EW)
entry2.state(['disabled'])

btnframe = ttk.Frame(appframe)
btnframe.grid(row=2, column=0)
invalid_btn = ttk.Button(btnframe, text="Make invalid", command=show_invalid)
valid_btn = ttk.Button(btnframe, text="Make valid", command=show_valid)
invalid_btn.grid(row=0, column=0, padx=3, pady=3)
valid_btn.grid(row=0, column=1, padx=3, pady=3)

root.mainloop()
