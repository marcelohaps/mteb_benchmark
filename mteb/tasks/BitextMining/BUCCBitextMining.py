from ...abstasks import AbsTaskBitextMining, CrosslingualTask

_LANGUAGES = ["de-pt", "fr-pt", "ru-pt", "zh-pt"]


class BUCCBitextMining(AbsTaskBitextMining, CrosslingualTask):
    @property
    def description(self):
        return {
            "name": "BUCC",
            "hf_hub_name": "mteb-pt/bucc-bitext-mining",
            "description": "BUCC bitext mining dataset",
            "reference": "https://comparable.limsi.fr/bucc2018/bucc2018-task.html",
            "type": "BitextMining",
            "category": "s2s",
            "eval_splits": ["test"],
            "eval_langs": _LANGUAGES,
            "main_score": "f1",
            "revision": "90d28e7f878f475bfd6bab8870c3f807655c70d8",
        }
