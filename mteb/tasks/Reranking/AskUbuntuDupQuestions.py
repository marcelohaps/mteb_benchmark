from ...abstasks.AbsTaskReranking import AbsTaskReranking


class AskUbuntuDupQuestions(AbsTaskReranking):
    @property
    def description(self):
        return {
            "name": "AskUbuntuDupQuestions",
            "hf_hub_name": "mteb-pt/askubuntudupquestions",
            "description": (
                "AskUbuntu Question Dataset - Questions from AskUbuntu with manual annotations marking pairs of"
                " questions as similar or non-similar"
            ),
            "reference": "https://github.com/taolei87/askubuntu",
            "type": "Reranking",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": ["pt-br"],
            "main_score": "map",
            "revision": "e7ee6551a0fa8ea98e3f3bdc4136e0edafeb7306",
        }
