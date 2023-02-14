class ListItems():
    title = ''
    toggle = False

    def __init__(self, title):
        self.title = title

    def get_list_items(self):
        return self

listItems = ListItems('Little Red Riding Hood')
print(listItems.get_list_items().title)
