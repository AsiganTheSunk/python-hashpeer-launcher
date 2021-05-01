
class Column(object):
    def __init__(self, table, index):
        self._multicolumn_listbox = table
        self._index = index

    def data(self):
        return self._multicolumn_listbox.column_data(self._index)

    def delete(self):
        self._multicolumn_listbox.delete_column(self._index)

    def update(self, data):
        self._multicolumn_listbox.update_column(self._index, data)

    def __str__(self):
        return str(self.data())

    def __len__(self):
        return self._multicolumn_listbox.number_of_rows
