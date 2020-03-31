import os
import json

def load_data():

    # Download data from kaggle
    os.system('kaggle datasets download -d allen-institute-for-ai/CORD-19-research-challenge')
    os.system('unzip CORD-19-research-challenge.zip')

    # Get list of json filenames
    dirs = [
        'CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv/',
        'CORD-19-research-challenge/comm_use_subset/comm_use_subset/',
        'CORD-19-research-challenge/custom_license/custom_license/',
        'CORD-19-research-challenge/noncomm_use_subset/noncomm_use_subset/',
    ]
    fnames = [d+f for d in dirs for f in os.listdir(d)]

    # Full text of each paper
    texts = [get_text(f) for f in fnames]

    # Unique ID for each paper
    ids = [f.split('/')[-1][:-5] for f in fnames]

    # Return map of doc id -> text
    return dict(zip(ids, texts))



def get_text(fname):
    """Get full text of a single paper"""
    with open(fname) as f:
        text = json.load(f)
    return (
        text['metadata']['title'] + '. ' +
        ' '.join(p['text'] for s in ['abstract', 'body_text'] for p in text[s])
    )