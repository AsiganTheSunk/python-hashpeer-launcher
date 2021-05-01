autocompleteList = ['Dora Lyons (7714)', 'Hannah Golden (6010)', 'Walker Burns (9390)', 'Dieter Pearson (6347)',
                    'Allen Sullivan (9781)', 'Warren Sullivan (3094)', 'Genevieve Mayo (8427)',
                    'Igor Conner (4740)', 'Ulysses Shepherd (8116)', 'Imogene Bullock (6736)',
                    'Dominique Sanchez (949)', 'Sean Robinson (3784)', 'Diana Greer (2385)',
                    'Arsenio Conrad (2891)', 'Sophia Rowland (5713)', 'Garrett Lindsay (5760)', 'Lacy Henry (4350)',
                    'Tanek Conley (9054)', 'Octavia Michael (5040)', 'Kimberly Chan (1989)',
                    'Melodie Wooten (7753)', 'Winter Beard (3896)', 'Callum Schultz (7762)',
                    'Prescott Silva (3736)', 'Adena Crane (6684)', 'Ocean Schroeder (2354)', 'Aspen Blevins (8588)',
                    'Allegra Gould (7323)', 'Penelope Aguirre (7639)', 'Deanna Norman (1963)',
                    'Herman Mcintosh (1776)', 'August Hansen (547)', 'Oscar Sanford (2333)', 'Guy Vincent (1656)',
                    'Indigo Frye (3236)', 'Angelica Vargas (1697)', 'Bevis Blair (4354)', 'Trevor Wilkinson (7067)',
                    'Kameko Lloyd (2660)', 'Giselle Gaines (9103)', 'Phyllis Bowers (6661)', 'Patrick Rowe (2615)',
                    'Cheyenne Manning (1743)', 'Jolie Carney (6741)', 'Joel Faulkner (6224)',
                    'Anika Bennett (9298)', 'Clayton Cherry (3687)', 'Shellie Stevenson (6100)',
                    'Marah Odonnell (3115)', 'Quintessa Wallace (5241)', 'Jayme Ramsey (8337)',
                    'Kyle Collier (8284)', 'Jameson Doyle (9258)', 'Rigel Blake (2124)', 'Joan Smith (3633)',
                    'Autumn Osborne (5180)', 'Renee Randolph (3100)', 'Fallon England (6976)',
                    'Fallon Jefferson (6807)', 'Kevyn Koch (9429)', 'Paki Mckay (504)', 'Connor Pitts (1966)',
                    'Rebecca Coffey (4975)', 'Jordan Morrow (1772)', 'Teegan Snider (5808)',
                    'Tatyana Cunningham (7691)', 'Owen Holloway (6814)', 'Desiree Delaney (272)',
                    'Armand Snider (8511)', 'Wallace Molina (4302)', 'Amela Walker (1637)', 'Denton Tillman (201)',
                    'Bruno Acevedo (7684)', 'Slade Hebert (5945)', 'Elmo Watkins (9282)', 'Oleg Copeland (8013)',
                    'Vladimir Taylor (3846)', 'Sierra Coffey (7052)', 'Holmes Scott (8907)',
                    'Evelyn Charles (8528)', 'Steel Cooke (5173)', 'Roth Barrett (7977)', 'Justina Slater (3865)',
                    'Mara Andrews (3113)', 'Ulla Skinner (9342)', 'Reece Lawrence (6074)', 'Violet Clay (6516)',
                    'Ainsley Mcintyre (6610)', 'Chanda Pugh (9853)', 'Brody Rosales (2662)', 'Serena Rivas (7156)',
                    'Henry Lang (4439)', 'Clark Olson (636)', 'Tashya Cotton (5795)', 'Kim Matthews (2774)',
                    'Leilani Good (5360)', 'Deirdre Lindsey (5829)', 'Macy Fields (268)', 'Daniel Parrish (1166)',
                    'Talon Winters (8469)']

from re import (
    compile, escape, IGNORECASE, match
)

from tkinter import (
    Frame, LEFT, BOTH, X, END
)
from interface.components.metro_ui.metro_entry_containter import MetroEntryContainer
from interface.components.metro_ui.metro_button_container import MetroButtonContainer


class MetroSearchEntryContainer(Frame):
    def __init__(self, master, button_text="Search", button_ipadx=16, button_background='#3C3F41',
                 button_foreground="white", button_font=None, opacity=0.8, placeholder=None,
                 placeholder_font=None, placeholder_color="grey", entry_highlightthickness=0,
                 entry_width=60, entry_font=None, command=None):

        Frame.__init__(self, master)

        self._command = command

        self.entry = \
            MetroEntryContainer(self, width=entry_width, placeholder_font=placeholder_font,
                                placeholder_color=placeholder_color, highlightthickness=entry_highlightthickness,
                                matchesFunction=self.matches, autocomplete_list=autocompleteList, listboxLength=6)
        self.entry.pack(side=LEFT, fill=BOTH)

        if entry_font:
            self.entry.configure(font=entry_font)

        self.button = MetroButtonContainer(self, text=button_text, background=button_background,
                                           foreground=button_foreground, font=button_font,
                                           command=self._execute_command, padx=button_ipadx)
        self.button.pack(side=LEFT, fill=X)

        if command is not None:
            self.entry.bind_entry("<Return>", lambda event: self.button.invoke())

    @staticmethod
    def matches(field_value, ac_list_entry):
        pattern = compile(escape(field_value) + '.*', IGNORECASE)
        return match(pattern, ac_list_entry)

    def get_text(self):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            if entry.placeholder_state.contains_placeholder:
                return ""
            else:
                return entry.get()
        else:
            return entry.get()

    def set_text(self, text):
        entry = self.entry
        if hasattr(entry, "placeholder_state"):
            entry.placeholder_state.contains_placeholder = False

        entry.delete(0, END)
        entry.insert(0, text)

    def clear(self):
        self.entry_var.set("")

    def focus(self):
        self.entry.focus()

    def _execute_command(self):
        text = self.get_text()
        self._command(text)
        # Note: close listbox when search
        if self.entry.listbox:
            self.entry.listbox.destroy()
