from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

'''
lists = session.query(MenuItem).all()
for list in lists:
	print list.name
print session.query(MenuItem).all()

no = session.query(func.count(Restaurant.id))
print no

vegburs = session.query(MenuItem).filter_by(name = 'Veggie Burger')

for vegbur in vegburs:
	print vegbur.id
	print vegbur.price
	print vegbur.restaurant.name
	print "\n"
	
	if vegbur.price != '$2.99':
		vegbur.price = '$2.99'
		session.add(vegbur)
		session.commit()
	

print vegburs.price
vegburs.price = '$2.99'
session.add(vegburs)
session.commit()
'''

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name

session.delete(spinach)
session.commit()