from ...abstasks import AbsTaskClassification


class AmazonPolarityClassification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "AmazonPolarityClassification",
            "hf_hub_name": "mteb-pt/amazon_polarity",
            "description": "Amazon Polarity Classification Dataset.",
            "reference": "https://dl.acm.org/doi/10.1145/2507157.2507163",
            "category": "p2p",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "accuracy",
            "revision": "66d46512534ce85d43f9144edc92da6a649bd473",
        }
