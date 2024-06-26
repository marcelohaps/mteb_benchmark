from ...abstasks import AbsTaskClassification


class Banking77Classification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "Banking77Classification",
            "hf_hub_name": "mteb-pt/banking77",
            "description": "Dataset composed of online banking queries annotated with their corresponding intents.",
            "reference": "https://arxiv.org/abs/2003.04807",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["test"],
            "eval_langs": ["en"],
            "main_score": "accuracy",
            "revision": "cbb8cc7f6298e8d6857b6ed36e7097dbb9c85d9b",
        }
