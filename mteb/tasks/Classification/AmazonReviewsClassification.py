from ...abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = ["en", "de", "es", "fr", "ja", "zh"]


class AmazonReviewsClassification(MultilingualTask, AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "AmazonReviewsClassification",
            "hf_hub_name": "mteb-pt/amazon_reviews",
            "description": (
                "A collection of Amazon reviews specifically designed to aid research in multilingual text"
                " classification."
            ),
            "reference": "https://arxiv.org/abs/2010.02573",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["pt-br"],
            "main_score": "accuracy",
            "revision": "695077f4f176f67d6190332b091115fcd40dfd98",
        }
