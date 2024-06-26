from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STS14STS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STS14",
            "hf_hub_name": "mteb-pt/sts14-sts",
            "description": "SemEval STS 2014 dataset. Currently only the English dataset",
            "reference": "http://alt.qcri.org/semeval2014/task10/",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
            "revision": "8e3d2d1c117dc62273f85cafa1b87c8d5e2587bc",
        }
