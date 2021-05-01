from interface.components.multi_column_list_container.column import Column


class ListOfColumns(object):
    def __init__(self, multicolumn_listbox):
        self._multicolumn_listbox = multicolumn_listbox

    def data(self, index):
        return self._multicolumn_listbox.get_column(index)

    def get(self, index):
        return Column(self._multicolumn_listbox, index)

    def delete(self, index):
        self._multicolumn_listbox.delete_column(index)

    def update(self, index, data):
        self._multicolumn_listbox.update_column(index, data)

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        return self._multicolumn_listbox.update_column(index, value)

    def __delitem__(self, index):
        self._multicolumn_listbox.delete_column(index)

    def __len__(self):
        return self._multicolumn_listbox.number_of_columns