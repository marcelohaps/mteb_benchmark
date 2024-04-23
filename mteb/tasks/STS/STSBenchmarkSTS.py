from ...abstasks.AbsTaskSTS import AbsTaskSTS


class STSBenchmarkSTS(AbsTaskSTS):
    @property
    def description(self):
        return {
            "name": "STSBenchmark",
            "hf_hub_name": "mteb-pt/stsbenchmark-sts",
            "description": "Semantic Textual Similarity Benchmark (STSbenchmark) dataset.",
            "reference": "http://ixa2.si.ehu.es/stswiki/index.php/STSbenchmark",
            "type": "STS",
            "category": "s2s",
            "eval_splits": ["validation", "test"],
            "eval_langs": ["en"],
            "main_score": "cosine_spearman",
            "min_score": 0,
            "max_score": 5,
            "revision": "0dffa6edb6a2ce20ff9526c94e720c5df92367ef",
        }
