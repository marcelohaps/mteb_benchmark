from ...abstasks import AbsTaskClassification, MultilingualTask

_LANGUAGES = ["en", "de", "es", "fr", "hi", "th"]


class MTOPDomainClassification(MultilingualTask, AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "MTOPDomainClassification",
            "hf_hub_name": "mteb-pt/mtop_domain",
            "description": "MTOP: Multilingual Task-Oriented Semantic Parsing",
            "reference": "https://arxiv.org/pdf/2008.09335.pdf",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ['default'],
            "main_score": "accuracy",
            "revision": "0ae627d70049e0fff537a4a860a6dee152165abf",
        }
