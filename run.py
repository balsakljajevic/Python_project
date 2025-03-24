from market import app
from market.routes import routes_bp

app.register_blueprint(routes_bp)

if __name__ == '__main__':  # ovako je app stalno aktivna, pa ne moram da prekidam i palim iznova sa ctrl+c.
     app.run(debug=True)    # Isto se moze postici sa FLASK_DEBUG = 1 u CMD-u.
    