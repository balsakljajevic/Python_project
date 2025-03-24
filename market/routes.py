from market import app
from flask import render_template, redirect, url_for, flash, request, Blueprint
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm, ContactForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user 

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')     # pocetna strana kad se ucita app
def home_page():
    return render_template('home.html')

@routes_bp.route('/about')
def about_page():
    return render_template('about.html')

@routes_bp.route('/contact', methods=['GET', 'POST'])
def contact_page():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message sent successfully! We appreciate your feedback!', category='success')

    return render_template('contact.html', form=form)

@routes_bp.route('/projectdescr')
def project_descr_page():
    return render_template('proj_descr.html')

# @app.route('/about/<username>') # dinamicni routing, sta god se unese u url posle "about" ce se uzeti kao parametar,
# def about_page(username):       #  i f-ja ce ga vraiti u tekstu dole.
#    return f"<h1>About Page of {username}</h1>"

@routes_bp.route('/market', methods=['GET', 'POST'])
@login_required  # odvodi nas automatski na login stranicu
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == 'POST':
        # purchase item logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name = purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f'Congratz! You purchased {p_item_object.name} for {p_item_object.price}$', category='success')
            else:
                flash(f'Unfortunately, you dont have enough money to buy {p_item_object.name}', category='danger')
        # sell item logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f'Congratz! You sold {s_item_object.name} back to market!', category='success')
            else:
                flash(f'Unfortunately, something went wrong with selling {s_item_object.name}', category='danger')

        return redirect(url_for('routes.market_page'))

    if request.method == 'GET':
        items = Item.query.filter_by(owner=None) # da bi prikazivalo samo produkte koji nisu kupljeni, nemaju ownera
        owned_items = Item.query.filter_by(owner=current_user.id) # pokazuje produkte trenutni korisnik poseduje
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)

@routes_bp.route('/register', methods=['GET', 'POST']) # metode stavljamo da bi forma koja se koristi u ovom templetu mogla da procesuira post metodf
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                               email = form.email.data,
                              password = form.password1.data) # odavde ide u passwordsetter u modelima
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')

        return redirect(url_for('routes.market_page'))
    
    if form.errors != {}: # if there are no errors from validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating the user: {err_msg}', category='danger') # zasto stavljamo danger ima u basehtmlu 

    return render_template('register.html', form=form) # uzima podatke unete u register.html i unosi ih u RegisterForm preko form instance

@routes_bp.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction( attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')  # kategorija success ce prikazati poruku u zelenom
            return redirect(url_for('routes.market_page'))
        else:
            flash('Username and password do not match! Please, try again!', category='danger') # kategorija danger ce prikazati poruku u crvenom

    return render_template('login.html', form=form)


@routes_bp.route('/logout')
def logout_page():
    logout_user()
    flash('You have logged out!', category='info')
    return redirect(url_for('routes.home_page'))


