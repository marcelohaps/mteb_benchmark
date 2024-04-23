from ...abstasks import AbsTaskClassification


class ToxicConversationsClassification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "ToxicConversationsClassification",
            "hf_hub_name": "mteb-pt/toxic_conversations",
            "description": (
                "Collection of comments from the Civil Comments platform together with annotations if the comment is"
                " toxic or not."
            ),
            "reference": (
                "https://www.kaggle.com/competitions/jigsaw-unintended-bias-in-toxicity-classification/overview"
            ),
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "accuracy",
            "n_experiments": 10,
            "samples_per_label": 32,
            "revision": "a14b45380976f1406d0e7928f0f5e3cbc1d33cb2",
        }
