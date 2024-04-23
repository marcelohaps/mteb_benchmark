from ...abstasks.AbsTaskClustering import AbsTaskClustering


class BlurbsClusteringP2P(AbsTaskClustering):
    @property
    def description(self):
        return {
            "name": "BlurbsClusteringP2P",
            "hf_hub_name": "slvnwhrl/blurbs-clustering-p2p",
            "description": "Clustering of book titles+blurbs. Clustering of 28 sets, either on the main or secondary genre.",
            "reference": "https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/germeval-2019-hmc.html",
            "type": "Clustering",
            "category": "p2p",
            "eval_splits": ["test"],
            "eval_langs": ["de"],
            "main_score": "v_measure",
            "revision": "b68cda48154cbb7fe30556f445c4a4043f723a00",
        }
