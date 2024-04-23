from sentence_transformers import SentenceTransformer
import numpy as np
import torch

class BAAIBGE():
    def __init__(self, model_name: str, prompt: str = "Represent this sentence for searching relevant passages:"):
        self.model = SentenceTransformer(model_name)
        self.prompt = "Represent this sentence for searching relevant passages:"

    def encode(self, sentences: list[str], **kwargs) -> list[np.ndarray] | list[torch.Tensor]:
        if self.prompt:
            sentences = [self.prompt + sentence for sentence in sentences]
        return self.model.encode(sentences, **kwargs)

    def set_prompt(self, prompt: str):
        self.prompt = prompt



class INTFLOAT():
    def __init__(self, model_name: str, task: str):
        self.model = SentenceTransformer(model_name)
        self.task = task

    def encode(self, sentences: list[str], **kwargs) -> list[np.ndarray] | list[torch.Tensor]:
        if self.task == 'retrieval':
            prefixed_sentences = [sentence for sentence in sentences]
        else:
            prefixed_sentences = ['query: ' + sentence for sentence in sentences]
        return self.model.encode(prefixed_sentences, **kwargs)


    def set_prompt(self, prompt: str):
        self.prompt = prompt



