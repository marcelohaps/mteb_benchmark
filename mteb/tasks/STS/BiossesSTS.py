from ...abstasks.AbsTaskSTS import AbsTaskSTS


class BiossesSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "BIOSSES",
            "hf_hub_name": "mteb-pt/biosses-sts",
            "description": "Biomedical Semantic Similarity Estimation.",
            "reference": "https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 4,
            "revision": "053e25a56d2cbd79cf651bf05e8b959b5fe47971",
        }
