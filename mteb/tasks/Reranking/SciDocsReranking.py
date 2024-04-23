from ...abstasks.AbsTaskReranking import AbsTaskReranking


class SciDocsReranking(AbsTaskReranking):
    @property
    def description(self):
        return {
            "name": "SciDocsRR",
            "hf_hub_name": "mteb-pt/scidocs",
            "description": "Ranking of related scientific papers based on their title.",
            "reference": "https://allenai.org/data/scidocs",
            "type": "Reranking",
            "category": "s2s",
            "eval_splits": ["test", "validation"],
            "eval_langs": ["pt-br"],
            "main_score": "map",
            "revision": "b5be2d0fbcca3d184cf618365694c9b571333989",
        }
