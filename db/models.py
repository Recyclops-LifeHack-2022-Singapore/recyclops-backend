from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    isRecyclable = Column(Boolean)
    categoryId = Column(Integer, ForeignKey('categories.id')) 

    # relationships
    category = relationship("Category", back_populates="item")
    notes = relationship("Note", secondary='item_notes', back_populates='items')
    
    def __repr__(self):
        return "<Item(name='%s', categoryId='%s', isRecyclable='%s')>" % (self.name, self.categoryId, self.isRecyclable)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    color = Column(String)

    # relationships
    item = relationship("Item", back_populates="category")
    
    def __repr__(self):
        return "<Category(name='%s', color='%s')>" % (self.name, self.color)

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    resourceId = Column(Integer, ForeignKey('resources.id'))

    # relationships
    items = relationship("Item", secondary='item_notes', back_populates='notes')

    def __repr__(self):
        return "<Note(text='%s', itemId='%s')>" % (self.text, self.itemId)

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)

    def __repr__(self):
        return "<Resource(title='%s', link='%s')>" % (self.title, self.link)

## Intermediary Tables for many-to-many relationships

class ItemNote(Base):
    __tablename__ = "item_notes"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    note_id = Column(Integer, ForeignKey('notes.id'))
