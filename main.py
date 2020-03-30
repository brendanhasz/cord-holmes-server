from flask import Flask, request
import holmes_extractor as holmes


app = Flask(__name__)


# Get list of json filenames
dirs = [
    '/kaggle/input/CORD-19-research-challenge/biorxiv_medrxiv/biorxiv_medrxiv/',
    '/kaggle/input/CORD-19-research-challenge/comm_use_subset/comm_use_subset/',
    '/kaggle/input/CORD-19-research-challenge/custom_license/custom_license/',
    '/kaggle/input/CORD-19-research-challenge/noncomm_use_subset/noncomm_use_subset/',
]
fnames = [d+f for d in dirs for f in os.listdir(d)]

def get_text(fname):
    with open(fname) as f:
        text = json.load(f)
    return (
        text['metadata']['title'] + '. ' +
        ' '.join(p['text'] for s in ['abstract', 'body_text'] for p in text[s])
    )

# Full text of each paper
texts = [get_text(f) for f in fnames]

# Unique ID for each paper
ids = [f.split('/')[-1][:-5] for f in fnames]

# Create the holmes manager
holmes_manager = holmes.MultiprocessingManager(
    model='en_core_web_lg',
    overall_similarity_threshold=0.9,
    number_of_workers=4
)


# Uhhh this takes quite a while, just do the first 1000 for now...
ids = ids[:100]
texts = texts[:100]

# Parse and register all the papers
holmes_manager.parse_and_register_documents(
    dict(zip(ids, texts))
)


@app.route("/holmes_search")#, methods=["POST"])
def holmes_search():
    return 'hiya!'
    """
    if request.method == "POST":
        return {
            'response': holmes_manager.topic_match_documents_returning_dictionaries_against(
                request.form.to_dict()['query']
            )
        }
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

