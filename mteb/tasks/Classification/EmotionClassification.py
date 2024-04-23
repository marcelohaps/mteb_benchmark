from ...abstasks import AbsTaskClassification


class EmotionClassification(AbsTaskClassification):
    @property
    def description(self):
        return {
            "name": "EmotionClassification",
            "hf_hub_name": "mteb-pt/emotion",
            "description": (
                "Emotion is a dataset of English Twitter messages with six basic emotions: anger, fear, joy, love,"
                " sadness, and surprise. For more detailed information please refer to the paper."
            ),
            "reference": "https://www.aclweb.org/anthology/D18-1404",
            "category": "s2s",
            "type": "Classification",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["pt-br"],
            "main_score": "accuracy",
            "n_experiments": 10,
            "samples_per_label": 16,
            "revision": "1c40787f5e1f15b630a4561850b3dc7cf66f1591",
        }
