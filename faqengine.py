import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from exceptions import *


class FAQEngine:
    def __init__(self, csv_file: str):
        """
        FAQEngine constructor
        Takes csv_file: str as input (path)
        CSV should contain ['Question', 'Answer'] columns
        """
        self.data = self.parse_csv_file(csv_file)
        self.model = self.build_model()

    def get_vector(self, query: list):
        """
        Returns a vector for the given query using the vectorizer method that is used to init the FAQEngine class.
        """
        return self.vectorizer.transform(query)

    def build_model(self):
        documents = self.data['Question']
        self.vectorizer = TfidfVectorizer(stop_words='english').fit(documents)
        self.vectors = self.vectorizer.transform(documents)

    # TODO:
    def preprocess_data(self):
        pass

    def parse_csv_file(self, csv_file: str):
        """
        CSV file should contain two columns: Question, Answer
        Remove all NaN values
        """
        try:
            df = pd.read_csv(csv_file)
            if not set(['Question', 'Answer']).issubset(df.columns):
                raise BadCSVFile(
                    "CSV file does not contain ['Question', 'Answer'] columns.")
            df.dropna(inplace=True)

        except Exception as e:
            raise BadCSVFile("Error reading csv file.")

        return df

    def get_cosine_similarity(self, query: list):
        return cosine_similarity(
            self.get_vector(query), self.vectors).flatten()

    # TODO:
    def distance_similarity(self):
        pass

    def perform_query(self, query: str, n: int = 5):
        query = [query]
        cosine_similarities = self.get_cosine_similarity(query)
        related_document_indices = cosine_similarities.argsort()[:-n:-1]
        return self.data[
            self.data.index.isin(related_document_indices.tolist())
        ].reset_index(drop=True).to_dict(orient='records')
