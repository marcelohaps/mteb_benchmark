from ...abstasks.AbsTaskClustering import AbsTaskClustering


class MedrxivClusteringS2S(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "MedrxivClusteringS2S",
            "hf_hub_name": "mteb-pt/medrxiv-clustering-s2s",
            "description": "Clustering of titles from medrxiv. Clustering of 10 sets, based on the main category.",
            "reference": "https://api.biorxiv.org/",
            "type": "Clustering",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "v_measure",
            "revision": "5d59be25bd28863381e406998195f254848e8c6a",
        }
