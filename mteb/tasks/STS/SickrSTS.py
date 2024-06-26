from ...abstasks.AbsTaskSTS import AbsTaskSTS


class SickrSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "SICK-R",
            "hf_hub_name": "mteb-pt/sickr-sts",
            "description": "Semantic Textual Similarity SICK-R dataset as described here:",
            "reference": "https://www.aclweb.org/anthology/S14-2001.pdf",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 1,
            "max_score": 5,
            "revision": "ca634aef8a0b03488cc4aa958ec8c3bd47802801",
        }
