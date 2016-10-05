import os
#manipulate python runtime environment
import sys
#Mapper Code
from sqlalchemy import Column, ForeignKey, Integer, String
#configuration and class code
from sqlalchemy.ext.declarative import declarative_base
#foreign key relationship
from sqlalchemy.orm import relationship
#cinfiguration code
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
	__tablename__ = 'restaurant'
	
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	

class MenuItem(Base):
	__tablename__ = 'menu_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	price = Column(String(8))
	course = Column(String(250))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)
	
	# We added this serialize function to be able to send JSON objects in a serializable format
	@property
	def serialize(self):
		
		return {
		'name': self.name,
		'description': self.description,
		'id': self.id,
		'price': self.price,
		'course': self.course,
		}

#at the end of code
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)