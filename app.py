from flask import Flask, render_template, send_file,request,redirect
from PIL import Image
from gtts import gTTS
import pytesseract 
import pyttsx3  
from werkzeug.utils import secure_filename
from flask import *
#from flask_ngrok import run_with_ngrok
import os
from playsound import playsound  
from translate import Translator
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# define a folder to store and later serve the images
UPLOAD_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg','pdf'])



app = Flask(__name__, static_folder='static')
#run_with_ngrok(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def  __repr__(self) -> str:
        return f"{self.email}"

# function to check the file extension


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'
    # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    text = pytesseract.image_to_string(Image.open(filename))
    text = " ".join(text.split("\n"))
    				
    return text


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template("about.html")



@app.route("/records/")

def records():

    allTo=Project.query.all()
    return render_template("records.html",allTo=allTo)



@app.route("/contact/",methods=['GET','POST'])
def contact():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        desc=request.form['desc']
        project=Project(name=name,email=email,desc=desc)
        db.session.add(project)
        db.session.commit() 
        
        
    allPro=Project.query.all()
    return render_template('contact.html',allPro=allPro)


# route and function to handle the upload page


@app.route("/upload/", methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template("upload.html", msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template("upload.html", msg='No file selected')

        if file and allowed_file(file.filename):
            f = request.files['file']
            f.save(secure_filename(f.filename))
            # call the OCR function on it
            extracted_text = ocr_core(file)

            # extract the text and display it
            return render_template("upload.html",
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   )

    elif request.method == 'GET':
        return render_template("upload.html")


@app.route('/text/', methods=['POST', 'GET'])
#@cross_origin()
def speech():
    if request.method == 'POST':
        global f
        text = request.form['speech']
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

        translator= Translator(to_lang='en')
        translation = translator.translate(text)
        sound = gTTS(translation, lang='en',slow=False)
        sound.save('sound.mp3')
        #playsound('my_file.mp3',True)
        #os.remove('my_file.mp3')

        #return send_file('/my_file.mp3', as_attachment=True)
        
        #text_to_speech(text, gender)
        return render_template('text.html')#,audio_filename=audio_filename)
    else:
        
        return render_template('text.html')

@app.route("/download")
def download_file():
    p="sound.mp3"
    return send_file(p,as_attachment=True)


@app.route("/lan/",methods=['POST', 'GET'])
def lang():
    if request.method == 'POST':
        text = request.form['speech']
        lang=request.form['select-language']
        if lang=='ar':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='ar')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='ca':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='ca')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='hr':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='hr')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='en':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='en')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='fr':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='fr')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='de':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='de')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='el':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='el')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='he':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='he')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='hi':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='hi')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='it':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='it')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='ja':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='ja')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='ko':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='ko')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='pt':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='pt')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='ru':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='ru')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='es':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='es')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='th':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='th')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='tr':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='tr')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
        if lang=='vi':
            translator= Translator(to_lang=lang)
            translation = translator.translate(text)
            
            sound = gTTS(translation, lang='vi')
            sound.save('static/'+".mp3")
            return render_template("lan.html",
                                   msg='Successfully translate',
                                   translation=translation
                                   )
    

        return render_template('lan.html')
    else:
        return render_template('lan.html')



@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        desc=request.form['desc']
        project=Project.query.filter_by(sno=sno).first()
        project.name=name
        project.email=email
        project.desc=desc
        db.session.add(project)
        db.session.commit()
        return redirect("/records")
    
    project=Project.query.filter_by(sno=sno).first()
    return render_template('update.html',project=project)

    

@app.route('/delete/<int:sno>')
def delete(sno):
    project=Project.query.filter_by(sno=sno).first()
    db.session.delete(project)
    db.session.commit()

    return redirect("/records")




if __name__ == '__main__':
    app.run(debug=True)
