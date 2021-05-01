from interface.components.multi_column.components.row import Row


class ListOfRows(object):
    def __init__(self, multicolumn_listbox):
        self._multicolumn_listbox = multicolumn_listbox

    def data(self, index):
        return self._multicolumn_listbox.row_data(index)

    def get(self, index):
        return Row(self._multicolumn_listbox, index)

    def insert(self, data, index=None):
        self._multicolumn_listbox.insert_row(data, index)

    def delete(self, index):
        self._multicolumn_listbox.delete_row(index)

    def update(self, index, data):
        self._multicolumn_listbox.update_row(index, data)

    def select(self, index):
        self._multicolumn_listbox.select_row(index)

    def deselect(self, index):
        self._multicolumn_listbox.deselect_row(index)

    def set_selection(self, indices):
        self._multicolumn_listbox.set_selection(indices)

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        return self._multicolumn_listbox.update_row(index, value)

    def __delitem__(self, index):
        self._multicolumn_listbox.delete_row(index)

    def __len__(self):
        return self._multicolumn_listbox.number_of_rows
