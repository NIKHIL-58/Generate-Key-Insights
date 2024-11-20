from transformers import pipeline
from app.utils import clean_text, extract_keywords

# Load the summarization pipeline (using a pre-trained BART model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def process_story(story: str, prompt: str):
    """
    Extract and summarize insights based on a specific prompt.
    """
    cleaned_story = clean_text(story)
    relevant_sections = extract_keywords(cleaned_story, topic=prompt)
    
    # Generate summaries for each relevant section
    insights = []
    for section in relevant_sections:
        summary = summarizer(section, max_length=100, min_length=30, do_sample=False)
        insights.append(summary[0]['summary_text'])
    
    return insights
