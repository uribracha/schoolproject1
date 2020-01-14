"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from pythonproject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message="Your application description page"
        )
@app.route("/picturealbum")
def picturealbum():
    return render_template(
        "picturealbum.html",
        title="animal picture album",
        picturelist=["https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231410/Labrador-Retriever-On-White-01.jpg","https://cdn.cnn.com/cnnnext/dam/assets/191024091949-02-foster-cat-large-169.jpg","https://www.birds.org.il/Data/Portal%20Images/Foreign%20birds/Bird%20Family%20project/Broad-billedTody-%D7%A2%D7%95%D7%96%D7%97%D7%95%D7%A8%D7%99%D7%9F-%D7%94%D7%99%D7%A1%D7%A4%D7%A0%D7%99%D7%95%D7%9C%D7%94300%D7%90%D7%95%D7%A8%D7%9A_877031878.png","https://miro.medium.com/max/3006/1*KdxlBR9P3mDp9JZ_URMdYQ.jpeg","https://c402277.ssl.cf1.rackcdn.com/photos/18134/images/hero_small/Medium_WW226365.jpg?1574452099","https://upload.wikimedia.org/wikipedia/commons/6/6f/2009-reedbuck.jpg"],
        altlist=["labrdor","cat","bird","panda","leopard","deer"]
        )
