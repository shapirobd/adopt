from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():

    pets = Pet.query.all()
    return render_template('home.html', pets=pets, Pet=Pet)


@app.route('/search')
def find_pet():
    name = request.args.get('pet_search')
    pets = Pet.query.filter(Pet.name.ilike(name)).all()
    return render_template('home.html', pets=pets)


@ app.route('/<string:species>')
def species_page(species):

    pets = Pet.query.filter(Pet.species == species).all()
    return render_template('home.html', pets=pets)


@ app.route('/add', methods=['GET', 'POST'])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        data = form.data
        del data['csrf_token']
        pet = Pet(**data)

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_new_pet.html', form=form)


@ app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f'{pet.name} has been successfully editted!')

        return redirect(f'/{pet_id}')
    else:
        return render_template('edit_pet.html', form=form, pet=pet)
