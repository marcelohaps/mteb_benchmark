from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STS12STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STS12",
            "hf_hub_name": "mteb-pt/sts12-sts",
            "description": "SemEval STS 2012 dataset.",
            "reference": "https://www.aclweb.org/anthology/S12-1051.pdf",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
            "revision": "1bf6a356d3703ce48bd24d5f8839548f56007e16",
        }
