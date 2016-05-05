from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db


##############################################################################
# Flask
app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

##############################################################################


@app.route("/", methods=['GET'])
def main_page():
    """tbd"""

    return render_template("main_page.html")



##############################################################################

print "running server :)"

if __name__ == "__main__":
    app.debug = True

    connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run(debug=True)