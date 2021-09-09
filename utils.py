import pdfplumber
import pickle
import re

PICKLE_PATHS = [
    "models/onevrest_knn_model.pkl",
    "models/onevrest_knn_labelencoder.pkl",
    "models/onevrest_knn_tfidfvectorizer.pkl"
]

def extractTextPdf(path):
    """Reads a PDF file and extracts the text data from each of the pages

    Args:
        path (str): Path or FilePointer pointing to the pdf file

    Returns:
        str: Extracted text from the specified pdf file
    """
    text = ""
    with pdfplumber.open(path) as pdfFile:
        for page in pdfFile.pages:
            text += page.extract_text()
    return text

def load_from_pickle():
    """Helper function for loading model, label encoder, and text vectorizer files

    Returns:
        OneVsRestClassifier: Loaded sklearn model object
        LabelEncoder: Loaded label encoder object
        TfidfVectorizer: Loaded vectorizer object
    """

    with open(PICKLE_PATHS[0], "rb") as modelFile:
        model = pickle.load(modelFile)

    with open(PICKLE_PATHS[1], "rb") as labelencoderFile:
        le = pickle.load(labelencoderFile)

    with open(PICKLE_PATHS[2], "rb") as tfidfvectorizerFile:
        vectorizer = pickle.load(tfidfvectorizerFile)

    return model, le, vectorizer

def cleanResumeText(resumeText):
    """Cleans the text in resume by removing URLs, hashtags, special letters,
    and punctuations

    Args:
        resumeText (str): The text to clean

    Returns:
        str: Cleaned resume text
    """

    resumeText = re.sub("http\S+\s*", " ", resumeText)  # Remove URLs
    resumeText = re.sub("RT|cc", " ", resumeText)  # Remove RT and cc
    resumeText = re.sub("#\S+", "", resumeText)  # Remove hashtags
    resumeText = re.sub("@\S+", "  ", resumeText)  # Remove mentions
    resumeText = re.sub("[%s]" % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),
                         " ", resumeText)  # Remove punctuations
    resumeText = re.sub(r"[^\x00-\x7f]", " ", resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # Remove extra whitespace
    return resumeText


if __name__ == "__main__":
    filePath = "C:\\Users\\HP\\Desktop\\M.Tech\\Documents\\Dhyanil_Mehta_Resume_202011032.pdf"

    resumeText = extractTextPdf(filePath)
    model, le, vectorizer = load_from_pickle()

    cleanedText = cleanResumeText(resumeText)
    textFeatures = vectorizer.transform([cleanedText])

    pred = model.predict(textFeatures)

    print("Resume is of category:", le.inverse_transform(pred)[0])
