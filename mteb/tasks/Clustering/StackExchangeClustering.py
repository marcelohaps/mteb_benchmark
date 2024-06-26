from ...abstasks.AbsTaskClustering import AbsTaskClustering


class StackExchangeClustering(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "StackExchangeClustering",
            "hf_hub_name": "mteb-pt/stackexchange-clustering",
            "description": (
                "Clustering of titles from 121 stackexchanges. Clustering of 25 sets, each with 10-50 classes, and"
                " each class with 100 - 1000 sentences."
            ),
            "reference": "https://arxiv.org/abs/2104.07081",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["en"],
            "main_score": "v_measure",
            "revision": "10dda922f95fa89058fe87ef961e9937b256c55a",
        }
