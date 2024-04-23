from ...abstasks import AbsTaskSummarization


class SummEvalSummarization(AbsTaskSummarization):
    @property
    def description(self):
        return {
            "name": "SummEval",
            "hf_hub_name": "mteb-pt/summeval",
            "description": "News Article Summary Semantic Similarity Estimation.",
            "reference": "https://tabilab.cmpe.boun.edu.tr/BIOSSES/DataSet.html",
            "type": "Summarization",
            "category": "p2p",
            "eval_splits": ["validation"],
            "eval_langs": ["default"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
            "revision": "b57d536d89da6fc42b3ca40645bb813f538b9ede",
        }
