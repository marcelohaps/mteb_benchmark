from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STS13STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STS13",
            "hf_hub_name": "mteb-pt/sts13-sts",
            "description": "SemEval STS 2013 dataset.",
            "reference": "https://www.aclweb.org/anthology/S13-1004/",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
            "revision": "ecfaefd049ac1cb56e0e11e48070152f47755bde",
        }
