from ...abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class CQADupstackStatsRetrieval(AbsTaskRetrieval):
    @property
    def description(self):
        return {
            "name": "CQADupstackStatsRetrieval",
            "hf_hub_name": "mteb-pt/cqadupstack-stats",
            "description": "CQADupStack: A Benchmark Data Set for Community Question-Answering Research",
            "reference": "http://nlp.cis.unimelb.edu.au/resources/cqadupstack/",
            "type": "Retrieval",
            "category": "s2p",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "ndcg_at_10",
            "revision": "43c0874a06d6755fed030ef1ce446750c861860b",            
        }
