from ...abstasks.AbsTaskPairClassification import AbsTaskPairClassification


class SprintDuplicateQuestionsPC(AbsTaskPairClassification):
    @property
    def description(self):
        return {
            "name": "SprintDuplicateQuestions",
            "hf_hub_name": "mteb-pt/sprintduplicatequestions-pairclassification",
            "description": "Duplicate questions from the Sprint community.",
            "reference": "https://www.aclweb.org/anthology/D18-1131/",
            "category": "s2s",
            "type": "PairClassification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["pt-br"],
            "main_score": "ap",
            "revision": "72cf0b6fbbfb1adfe74377a011cdbf293c4ec80a",
        }
