import nltk
from nltk.stem import  WordNetLemmatizer
from nltk.corpus import stopwords

tokenizer = nltk.RegexpTokenizer(r"\w+")
lemmatizer = WordNetLemmatizer()
stopwords = stopwords.words('english')

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