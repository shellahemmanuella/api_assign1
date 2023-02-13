from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def greet():
    return "you are most welcome here today, check out our articles"

@app.route('/articles')
def get_articles():
    articles = {'article1':
        {'id': 1,
        'Title': 'The Deceptive Campaign for Bivalent Covid Boosters',
        'Body':"Vaccine makers could have performed small randomized trials last summer and early fall that tested the bivalents against the original boosters and a placebo group. Results could have been available by the end of September. But the public-health authorities did not want to wait—and now we know why.",
        'author':'Allysia Finley, Member, Editorial Board, The Wall Street Journal'},
        'article2':{
            'id':2,
            'title':'The role of digital technology in surgical home hospital programs',
            'Body':'Remote patient monitoring (RPM) technologies are an important component of HH programs and have the potential to further expand the scope of surgical care delivery in the home. RPM tools record and transmit patient data to providers and can come in the form of wearable or ambient monitoring technologies that collect continuous or intermittent data',
            'author':'Kavya Pathak, Jayson S. Marwaha.'
        }
    }
    return jsonify(articles)