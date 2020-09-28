from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Phoebe", species="cat",
           photo_url="https://i.imgur.com/zMWdYWh.jpg", age="1")
pet2 = Pet(name="Gus", species="cat",
           photo_url="https://www.warrenphotographic.co.uk/photography/bigs/09256-Black-and-white-cat-white-background.jpg", age="5", available=False)
pet3 = Pet(name="Stella", species="dog",
           photo_url="https://miro.medium.com/max/1200/0*vs9mVqlFaYxUT83c.jpeg", age="4")
pet4 = Pet(name="Dosha", species="dog",
           photo_url="https://i.pinimg.com/originals/95/20/14/95201445a5e792a4b21d5ba01ef51211.jpg", age="9", available=False)
pet5 = Pet(name="Ariel", species="cat",
           photo_url="https://i.pinimg.com/originals/5a/dc/6c/5adc6c706259846095a6ae5bbabaf9be.jpg", age="7", available=False)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()
