from models import Item, Category, Note, Resource

def seeds():

    item1 = Item(name="Item1", isRecyclable=False, categoryId=None)
    
    return [item1]