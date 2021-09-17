# Resume Categorizer

Resume Categorizer is a basic end-to-end Machine Learning Project made by me in one day using Python. 
This project will take as input a pdf resume file and extract the text from it and use that to predict a category which best suits the profile. 
Following are the resume categories on which it was trained:
* Data Science
* HR
* Advocate
* Arts
* Web Designing
* Mechanical Engineer
* Sales
* Health and fitness
* Civil Engineer
* Java Developer
* Business Analyst
* SAP Developer
* Automation Testing
* Electrical Engineering
* Operations Manager
* Python Developer
* DevOps Engineer
* Network Security Engineer
* PMO
* Database
* Hadoop
* ETL Developer 
* DotNet Developer
* Blockchain
* Testing

Models used:
    
* **Vectorizing text:** TfidfVectorizer
* **Encoding labels:** LabelEncoder
* **Machine Learning Model:** KNeighborsClassifier
* **Multiclass Classifier:** OneVsRestClassifier

The project structure is following:
```cmd
.
│   .gitignore
│   app.py                                  # Flask webapp python file
│   LICENSE
│   Procfile                                # Heroku Procfile
│   README.md
│   requirements.txt                        # Python Package requirements
│
├───dataset
│       UpdatedResumeDataSet.csv            # Dataset used for training
│
├───models
│       onevrest_knn_labelencoder.pkl       # Label encoder model
│       onevrest_knn_model.pkl              # KNN model with OneVsRest classifier
│       onevrest_knn_tfidfvectorizer.pkl    # TF-IDF Vectorizer model
│
├───notebooks
│       resume_screening_ml.ipynb           # Notebook containing data analysis and visualization with model training
│
├───scripts
│       utils.py                            # Utility file containing helper functions 
│
├───static
│   ├───css
│   │       style.css                       # CSS stylesheet for webapp
│   └───js
│           script.js                       # JavaScript script for webapp
│
└───templates
        index.html                          # HTML homepage file for webapp
```

The resume dataset was taken from here: [UpdatedResumeDataset](https://www.kaggle.com/dhainjeamita/updatedresumedataset/)

The project was built and tested on Python 3.9.
## Tech Stack

**Web app:** Flask

**PDF Text Extraction:** [pdfplumber](https://github.com/jsvine/pdfplumber)

**Machine Learning:** scikit-learn

**Data Analysis and Visualization:** pandas, numpy, matplotlib, seaborn, wordcloud

**Languages:** Python, HTML/CSS/JavaScript(For web app frontend)
## Deployment

The project is deployed on Heroku cloud platform. You can check it out at:
https://resume-screening-prediction.herokuapp.com/

  
## Acknowledgements
 * [Resume Screening with Python](https://thecleverprogrammer.com/2020/12/06/resume-screening-with-python/)
 * [180 Data Science and Machine Learning Projects with Python](https://medium.com/coders-camp/180-data-science-and-machine-learning-projects-with-python-6191bc7b9db9)