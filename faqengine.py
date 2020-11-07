import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from exceptions import *


class FAQEngine:

    def __init__(self, csv_file: str = 'faqs.csv'):
        """
        FAQEngine Constructor
        Takes csv_file: str (input path of csv file)
        CSV file should contain ['Question', 'Answer'] columns
        """
        self.data = self.parse_csv_file(csv_file)
        self.build_model(self.data['Question'])

    def parse_csv_file(self, csv_file: str):
        """
        Reads the csv file
        CSV file should contain ['Question', 'Answer'] columns
        Remove NaN values
        Throw error if format is bad or file does not exist
        """
        try:
            df = pd.read_csv(csv_file)

            if not set(['Question', 'Answer']).issubset(df.columns):
                raise BadCSVFile(
                    "CSV file does not contain ['Question', 'Answer'] columns.")

            df.dropna(inplace=True)

        except Exception as e:
            raise BadCSVFile(
                "Error while reading the csv file. Please check the path of the file or the file might be curropted.")

        return df

    def build_model(self, documents):
        """
        Create a mechanism to vectorize the data
        Create vector for our current dataset
        """
        self.vectorizer = TfidfVectorizer(
            stop_words='english', lowercase=True).fit(documents)
        self.vectors = self.vectorizer.transform(documents)

    def get_vector(self, query: list):
        """
        Returns a vector for a given query
        """
        if len(query) == 0:
            raise BadQueryParameter("Query (list) can not be empty.")

        return self.vectorizer.transform(query)

    def get_cosine_similarity(self, query: list):
        """
        Returns cosine similarity between the input question and our dataset questions
        """
        question_vector = self.get_vector(query)

        return cosine_similarity(question_vector, self.vectors).flatten()

    def perform_query(self, query: str, n: int = 5):
        """
        API function that can be used by other codebase
        It takes query (string) and n top similar questions along with thier answers
        """
        query = [query]
        cosine_similarities = self.get_cosine_similarity(query)
        indices = cosine_similarities.argsort()[:-n-1:-1]
        return self.data[
            self.data.index.isin(indices)
        ].reset_index(drop=True).to_dict(orient='records')
