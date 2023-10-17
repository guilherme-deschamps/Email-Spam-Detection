# Email-Spam-Detection

In this repository, I implemented a small project to practice NLP, specifically for Email Spam classification.  The dataset used for this project is [available in Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset), and the implementation was based on a tutorial presented by [Greg Hogg](https://www.youtube.com/watch?v=hOuvYcw_sVQ).

There are two main artifacts that can be executed here:
 * A **Jupyter Notebook**
 * A **Flask application**

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

## How to run the Jupyter Notebook

 * Clone the repository
 * (Optional but recommended) Create a virtual environment for the project
 * Activate the virtual environment (On Windows: open the /venv/Scripts folder and run *activate*)
 * Install the dependencies:
 ```
 pip install -r requirements.txt
 ```
 * Run your Jupyter server, either:
   * Using a platform like Visual Studio Code, OR
   * Using the terminal, in the venv you created, running the *jupyter notebook* command
 * Open the *Email_Spam_Classification.ipynb* file
 * Have fun 🙂!

## How to run the Flask application

 * Open your terminal
 * Activate the virtual environment created (On Windows: open the /venv/Scripts folder and run *activate*)
 * Run:

```
python app.py
```

## Trying out the end-points

A quick way to try the end-points available is by running the Flask app and executing in terminal the cURL commands below. Please, note that there is a difference for the cURL commands depending if you are using Linux or Windows (did not check for different operating systems): **Linux uses apostrophes, while Windows does not, requiring some small changes on the quotation marks**. Using Windows, the quotation marks inside of the JSON must be replaced by **\"**, while the apostrophes out of the JSON should be replaced by normal quotation marks.

Having this explained, the end-points available are:

### /convert_message

POST end-point that takes a String as input, and returns the tokens present in that message (except [stopwords](https://www.opinosis-analytics.com/knowledge-base/stop-words-explained/#:~:text=Stop%20words%20are%20a%20set,carry%20very%20little%20useful%20information)).

To test via terminal (Linux), run:
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hey, this is a test message!"}' http://127.0.0.1:5000/convert_message
```
**In Windows, the corresponding command would be:**
```
curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"Hey, this is a test message!\"}" http://127.0.0.1:5000/convert_message
```

### /predict

POST end-point that takes a String (something like an email message) as input, and returns the prediction to whether this message is or not a spam according to the classifier trained. **The examples below were prepared using the Linux syntax of cURL, so if you are on Windows, please make the conversion as explained previously**. 

An example of message that would NOT be classified as a spam is in the following cURL command (for Linux):
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hey, this is a test message (not spam)!"}' http://127.0.0.1:5000/predict
```
Opposite to the previous example, if you use the command below you will see a case classified as a spam by the model:
```
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hi there, go get ur free drink today!"}' http://127.0.0.1:5000/predict
```

## Understanding the classifications

Before training the model, some steps were performed over the dataset (you can find them in details in the *Email_Spam_Classification.ipynb* notebook). After counting how often each token appeared in the dataset, 16 tokens were defined as 'important features' which appeared more than 200 times in the dataset. These 16 tokens are the following:
```
['4', 'good', 'go', 'free', 'ok', 'å', 'get', 'gt', 'ur', 'like', 'call', 'day', 'u', '2', 'know', 'lt']
```
When looking at the most common words in messages that were spams, I could find that they are distributed basically as shown in the chart below.

![image](https://github.com/guilherme-deschamps/Email-Spam-Detection/assets/42009124/e1b7f6f5-c75a-431d-9a22-22c33a3e04e8)

So, to create a message that is classified as a spam, you can simply create a message that contains some of these most common spam words and you should have your own spam messages right there to play around!

## To-do

 - [x] Implement a Flask application with end-points:
   - [x] Receives a phrase and returns the vector of tokens after tokenization / lower casing / lemmatization
   - [x] Receives an e-mail message and returns whether it is or not a spam
