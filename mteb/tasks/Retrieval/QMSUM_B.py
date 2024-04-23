from ...abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class QMSUM_B(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            "name": "QMSUM_B",
            "hf_hub_name": "testzin/qmsum_b",
            "description": "CQADupStack: A Benchmark Data Set for Community Question-Answering Research",
            "reference": "http://nlp.cis.unimelb.edu.au/resources/cqadupstack/",
            "type": "Retrieval",
            "category": "s2p",
            "eval_splits": ["train"],
            "eval_langs": ["en"],
            "main_score": "ndcg_at_10",
            "revision": "ea137946db94d87dc14c5d80c18c9fb2e02dc7b2",            
        }
