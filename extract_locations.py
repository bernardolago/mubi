import spacy
import json

# Load European Portuguese language model
nlp = spacy.load("pt_core_news_lg")

# Function to extract locations from text
def extract_locations(text):
    # Process text with SpaCy
    doc = nlp(text)
    
    # Extract locations
    locations = []
    for ent in doc.ents:
        if ent.label_ == "LOC":  # LOC represents location
            locations.append(ent.text)
    return locations

def extract_gpe(text):
    # Process text with SpaCy
    doc = nlp(text)
    
    # Extract locations
    locations = []
    for ent in doc.ents:
        if ent.label_ == "GPE":  # LOC represents location
            locations.append(ent.text)
    return locations

with open('articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

for link, article in articles.items():
    locations = extract_locations(article['content'])
    article['locations'] = locations

with open('articles_with_locations.json', 'w') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

