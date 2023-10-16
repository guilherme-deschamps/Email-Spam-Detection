# Email-Spam-Detection

In this repository, I am implementing a small project to practice NLP, specifically for Email Spam classification.  The dataset used for this project is [available in Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset), and the implementation was based on a tutorial presented by [Greg Hogg](https://www.youtube.com/watch?v=hOuvYcw_sVQ).

## Requirements

 * pandas
 * nltk
 * matplotlib
 * seaborn
 * tqdm
 * jupyter
 * flask
 * scikit-learn
 * numpy

## How to run

 * Clone the repository
 * (Optional but recommended) Create a virtual environment for the project
 * Activate the virtual environment (On Windows: open the /venv/Scripts folder and run *activate*)
 * Install the dependencies (*pip install -r requirements.txt*)
 * Run your Jupyter server (with the venv on your project root folder, run *jupyter notebook*)
 * Have fun 🙂!

## To-do

 - [ ] Implement a Flask application with end-points:
   - [x] Receives a phrase and returns the vector of tokens after tokenization / lower casing / lemmatization
   - [ ] Receives a e-mail body and returns whether it is or not a spam
 - [ ] Update README.md to new Flask end-points, with examples for cURL (show for Linux/Windows)
