from ...abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = ["en", "de", "es", "fr", "hi", "th"]


class MTOPIntentClassification(MultilingualTask, AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MTOPIntentClassification",
            "hf_hub_name": "mteb-pt/mtop_intent",
            "description": "MTOP: Multilingual Task-Oriented Semantic Parsing",
            "reference": "https://arxiv.org/pdf/2008.09335.pdf",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ['pt-br'],
            "main_score": "accuracy",
            "revision": "a51c4909bcc2d97c03afae5d1deac99f93a7930a",
        }
