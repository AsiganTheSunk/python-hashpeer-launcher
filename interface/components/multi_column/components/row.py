
class Row(object):
    def __init__(self, table, index):
        self._multicolumn_listbox = table
        self._index = index

    def data(self):
        return self._multicolumn_listbox.row_data(self._index)

    def delete(self):
        self._multicolumn_listbox.delete_row(self._index)

    def update(self, data):
        self._multicolumn_listbox.update_row(self._index, data)

    def select(self):
        self._multicolumn_listbox.select_row(self._index)

    def deselect(self):
        self._multicolumn_listbox.deselect_row(self._index)

    def __str__(self):
        return str(self.data())

    def __len__(self):
        return self._multicolumn_listbox.number_of_columns
