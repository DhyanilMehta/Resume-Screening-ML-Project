import os
import scripts.utils as utils
from flask import Flask, flash, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

if not os.path.exists('uploads'):
    os.mkdir('uploads')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config['SECRET_KEY'] = '12345'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predictCategory(path):
    """Helper function to predict the category from the uploaded resume pdf file

    Args:
        path (str): Path to the uploaded file

    Returns:
        str: The predicted resume category
    """
    # Extract text from pdf
    resumeText = utils.extractTextPdf(path)

    # Load pickled model, label encoder and vectorizer
    model, le, vectorizer = utils.load_from_pickle()

    # Clean and convert text into tfidf word vectors
    cleanedText = utils.cleanResumeText(resumeText)
    textFeatures = vectorizer.transform([cleanedText])

    # Make a prediction from the trained model 
    # and use label encoder to get the category
    prediction = model.predict(textFeatures)
    category = le.inverse_transform(prediction)[0]

    # Delete the saved file
    os.remove(path)

    # Return the predicted category
    return category


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file-upload' not in request.files:
            msg = "No file part"
            flash(msg)
            return render_template('index.html', prediction_text=msg)
        
        try:
            # start request parsing
            file = request.files['file-upload']
        except RequestEntityTooLarge as e:
            # we catch RequestEntityTooLarge exception
            app.logger.info(e)

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            msg = "No selected file"
            flash(msg)
            return render_template('index.html', prediction_text=msg)
        
        if file and allowed_file(file.filename):
            # Save file in the uploads folder in a secure format
            filename = secure_filename(file.filename)
            savePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(savePath)

            # path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

            category = predictCategory(savePath)

            return render_template(
                'index.html', 
                prediction_text=f"Resume category: {category}")
        
        return render_template('index.html', 
                                prediction_text="Please upload pdf file")


if __name__ == "__main__":
    app.run(debug=True)
