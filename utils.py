import re
from rake_nltk import Rake

def clean_text(text: str) -> str:
    """
    Clean text by removing special characters and extra spaces.
    """
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()



def extract_keywords(text: str, topic: str) -> list:
    """
    Extract keywords from the text related to the topic.
    """
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()
    
    # Filter keywords related to the topic
    return [word for word in keywords if topic.lower() in word.lower()]

