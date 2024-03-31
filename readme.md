# Mubi Extractor

This project is divided into two main scripts so far.

1. mubi.py: extracts all the content from the mubi.pt website, going through all the pages, getting the links for all the articles and then dumping all the content into a json file with the following information: Title, Date, Tags, Content.

2. extract_locations.py: this is a simple SpaCy script that uses the large Portuguese pre-trained model from SpaCy and with NLP extracts the words that are labeled as Location by the model.
