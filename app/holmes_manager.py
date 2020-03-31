import holmes_extractor as holmes

from load_data import load_data



class HolmesManager():

    def __init__(self, n_workers=4):

        self.manager = holmes.MultiprocessingManager(
            model='en_core_web_lg',
            overall_similarity_threshold=0.9,
            number_of_workers=n_workers
        )

        self.manager.parse_and_register_documents(
            load_data()
        )


    def search(self, query):
        return self.manager.topic_match_documents_returning_dictionaries_against(
            query
        )
