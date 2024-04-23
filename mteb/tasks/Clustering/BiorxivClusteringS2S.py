from ...abstasks.AbsTaskClustering import AbsTaskClustering


class BiorxivClusteringS2S(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "BiorxivClusteringS2S",
            "hf_hub_name": "mteb-pt/biorxiv-clustering-s2s",
            "description": "Clustering of titles from biorxiv. Clustering of 10 sets, based on the main category.",
            "reference": "https://api.biorxiv.org/",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "v_measure",
            "revision": "d7f1a78904d4b201686f00dcec4fdf88b9ed5d5e",
        }
