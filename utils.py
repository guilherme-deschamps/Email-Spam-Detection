import nltk
import numpy as np
import pickle
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords

tokenizer = nltk.RegexpTokenizer(r"\w+")
lemmatizer = WordNetLemmatizer()
stopwords = stopwords.words('english')

# Load the features from the file
with open('files/features.pkl', 'rb') as file:
    features = pickle.load(file)
# Load the classifier from the file
with open('files/random_forest_classifier.pkl', 'rb') as file:
    rf = pickle.load(file)

token_to_index_mapping = {t:i for t, i in zip(features, range(len(features)))}

def convert_message_to_token(message):
    """
    This function takes a string as input and returns the processed list of tokens from the given string.

    Args:
        input_string (str): The input string to have the tokens extracted.

    Returns:
        str: The list of tokens of the string.
    """
    tokens = tokenizer.tokenize(message)
    lowercased_tokens = [t.lower() for t in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(t) for t in lowercased_tokens]
    useful_tokens = [t for t in lemmatized_tokens if t not in stopwords]
    
    return useful_tokens

def message_to_count_vector(message):
    """
    This function takes a string as input and returns the count of each token in the given string.

    Args:
        input_string (str): The input string to have the tokens counted.

    Returns:
        str: The count of each token in the string.
    """
    count_vector = np.zeros(len(features))
    
    processed_list_of_tokens = convert_message_to_token(message)
    
    for token in processed_list_of_tokens:
        # Verify if the token belongs to the list of 'important' tokens
        if token not in features:
            continue
        index = token_to_index_mapping[token]
        count_vector[index] += 1
        
    return count_vector

def predict(message):
    """
    This function takes a string as input and returns the count of each token in the given string.

    Args:
        input_string (str): The input string to have the tokens counted.

    Returns:
        str: The count of each token in the string.
    """
    count_vector = message_to_count_vector(message)

    X = np.array(count_vector).astype(int)
    prediction = rf.predict(X.reshape(1,-1))
    return prediction[0]