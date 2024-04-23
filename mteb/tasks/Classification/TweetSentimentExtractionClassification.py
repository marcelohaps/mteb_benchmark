from ...abstasks import AbsTaskClassification


class TweetSentimentExtractionClassification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "TweetSentimentExtractionClassification",
            "hf_hub_name": "mteb-pt/tweet_sentiment_extraction",
            "description": "",
            "reference": "https://www.kaggle.com/competitions/tweet-sentiment-extraction/overview",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["pt-br"],
            "main_score": "accuracy",
            "n_experiments": 10,
            "samples_per_label": 32,
            "revision": "c519eb949db67f572a7257a1a1a6de505c2425d4",
        }
