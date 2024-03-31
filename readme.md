# Mubi Extractor

This project is divided into two main scripts so far.

1. mubi.py: extracts all the content from the mubi.pt website, going through all the pages, getting the links for all the articles and then dumping all the content into a json file with the following information: Title, Date, Tags, Content.

2. extract_locations.py: this is a simple SpaCy script that uses the large Portuguese pre-trained model from SpaCy and with NLP extracts the words that are labeled as Location by the model.

An extra step needs to be done after installing all the required Python libraries on the requirements.txt. You need to install the pre-trained model from spacy running the following command on the terminal, inside your venv:

```python
python -m spacy download en_core_web_sm
```
