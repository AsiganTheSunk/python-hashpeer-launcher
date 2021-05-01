from tkinter import *
from interface.component_filters.constants import DEFAULT_FILTER_LABELS
from interface.component_filters.frame_input_box import FrameInputBox


class EntryFilterList(object):
    def __init__(self, root, root_selection_var, root_output=None):
        self.root = root
        self.root_output = root_output
        self.root_selection_var = root_selection_var
        self.root_selection_var.trace('w', self.update_options)

        self.previous_selection = None
        self.input_box_list = []
        self.update_options()

    def clear(self):
        if self.input_box_list:
            for input_box in self.input_box_list:
                input_box.close()
        self.input_box_list = []

    def refresh(self, entry_list):
        self.clear()
        self.show(entry_list=entry_list)

    def show(self, entry_list):
        for item in entry_list:

            strict_filter_entry = FrameInputBox(self.root, item, output_frame=self.root_output, entry_type=item)
            strict_filter_entry.pack(padx=2, pady=2, side=LEFT)
            self.input_box_list.append(strict_filter_entry)

    def update_options(self, *args):
        current_selection = self.root_selection_var.get()
        if self.previous_selection is None:
            self.previous_selection = current_selection

        print(f'< Current: {current_selection}, Previous: {self.previous_selection} >')
        if self.input_box_list:
            if self.previous_selection != current_selection:
                print('< status != >')
                self.refresh(DEFAULT_FILTER_LABELS['Category'][current_selection]['strict'])
                self.previous_selection = current_selection
            else:
                print('< status == >')
                self.previous_selection = current_selection

        else:
            self.show(DEFAULT_FILTER_LABELS['Category'][current_selection]['strict'])
