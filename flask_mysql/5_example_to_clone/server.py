from flask_app.controllers import files # Files should be the name of the controler
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)