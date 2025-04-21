
def clear_layout(layout):
    reversed_layout = reversed(range(layout.count()))
    for i in reversed_layout:
        item = layout.itemAt(i).widget()
        layout.removeItem(item)