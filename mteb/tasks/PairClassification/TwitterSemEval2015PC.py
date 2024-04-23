from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class TwitterSemEval2015PC(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "TwitterSemEval2015",
            "hf_hub_name": "mteb-pt/twittersemeval2015-pairclassification",
            "description": "Paraphrase-Pairs of Tweets from the SemEval 2015 workshop.",
            "reference": "https://alt.qcri.org/semeval2015/task1/",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["pt-br"],
            "main_score": "ap",
            "revision": "96a34e0f57b76f0a8a5ad54239329f3602f49edc",
        }
