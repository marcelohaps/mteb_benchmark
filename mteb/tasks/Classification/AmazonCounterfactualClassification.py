from ...abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = ["EN", "EN-ext"]


class AmazonCounterfactualClassification(MultilingualTask, AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "AmazonCounterfactualClassification",
            "hf_hub_name": "mteb-pt/amazon_counterfactual",
            "description": (
                "A collection of Amazon customer reviews annotated for counterfactual detection pair classification."
            ),
            "reference": "https://arxiv.org/abs/2104.06893",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["validation", "test"],
            "eval_langs": _LANGUAGES,
            "main_score": "accuracy",
            "n_experiments": 10,
            "samples_per_label": 32,
            "revision": "589b8cdf671a2e80745f3443de8e52f70d8c296f",
        }
