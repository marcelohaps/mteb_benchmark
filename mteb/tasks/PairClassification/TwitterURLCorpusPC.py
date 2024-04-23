from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class TwitterURLCorpusPC(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "TwitterURLCorpus",
            "hf_hub_name": "mteb-pt/twitterurlcorpus-pairclassification",
            "description": "Paraphrase-Pairs of Tweets.",
            "reference": "https://languagenet.github.io/",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["test"],
            "eval_langs": ["pt-br"],
            "main_score": "ap",
            "revision": "f10beafa92b187a6262796c39753376fa5e71b97",
        }
