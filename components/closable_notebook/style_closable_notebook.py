from tkinter import PhotoImage
from tkinter.ttk import Style


def set_icon_images():
    return (
        PhotoImage("img_close", data='''
                   R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                   d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                   5kEJADs=
                   '''),
        PhotoImage("img_closeactive", data='''
                   R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                   AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                   '''),
        PhotoImage("img_closepressed", data='''
                   R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                   d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                   5kEJADs=
               ''')
    )


def set_style():
    _style_closable_notebook = Style()
    _style_closable_notebook.element_create("close", "image", "img_close",
                                           ("active", "pressed", "!disabled", "img_closepressed"),
                                           ("active", "!disabled", "img_closeactive"), border=8, sticky='')
    _style_closable_notebook.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
    _style_closable_notebook.layout("CustomNotebook.Tab", [
        ("CustomNotebook.tab", {
            "sticky": "nswe",
            "children": [
                ("CustomNotebook.padding", {
                    "side": "top",
                    "sticky": "nswe",
                    "children": [
                        ("CustomNotebook.focus", {
                            "side": "top",
                            "sticky": "nswe",
                            "children": [
                                ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                            ]
                        })
                    ]
                })
            ]
        })
    ])
    return _style_closable_notebook
