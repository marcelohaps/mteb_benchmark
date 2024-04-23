from mteb import MTEB
#from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from sentence_transformers import SentenceTransformer
from mteb.tasks import *
import torch
from prompt_models import *


torch.cuda.empty_cache()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
 

models = ["Salesforce/SFR-Embedding-Mistral", "mixedbread-ai/mxbai-embed-large-v1", "intfloat/multilingual-e5-large-instruct",
"avsolatorio/GIST-large-Embedding-v0", "BAAI/bge-large-en-v1.5", "avsolatorio/GIST-Embedding-v0", "BAAI/bge-base-en-v1.5",
"llmrails/ember-v1", "jamesgpt1/sf_model_e5", "mixedbread-ai/mxbai-embed-2d-large-v1", "thenlper/gte-large", "avsolatorio/GIST-small-Embedding-v0",
"infgrad/stella-base-en-v2", "thenlper/gte-base", "nomic-ai/nomic-embed-text-v1", "nomic-ai/nomic-embed-text-v1.5", "intfloat/e5-large-v2",
"BAAI/bge-small-en-v1.5", "nomic-ai/nomic-embed-text-v1.5", "intfloat/e5-base-v2", "intfloat/multilingual-e5-large",
"intfloat/e5-large", "nomic-ai/nomic-embed-text-v1-ablated", "thenlper/gte-small", "nomic-ai/nomic-embed-text-v1.5",
"intfloat/e5-base", "jinaai/jina-embeddings-v2-base-en", "intfloat/e5-small-v2", "nomic-ai/nomic-embed-text-v1-unsupervised",
"sentence-transformers/sentence-t5-xxl", "intfloat/multilingual-e5-base", "nomic-ai/nomic-embed-text-v1.5",
"avsolatorio/GIST-all-MiniLM-L6-v2", "sentence-transformers/gtr-t5-xxl", "intfloat/e5-small", "Koat/gte-tiny", "sentence-transformers/gtr-t5-xl",
"sentence-transformers/gtr-t5-large", "jinaai/jina-embeddings-v2-small-en", "intfloat/multilingual-e5-small", "sentence-transformers/sentence-t5-xl",
"sentence-transformers/all-mpnet-base-v2", "jinaai/jina-embedding-l-en-v1", "sentence-transformers/sentence-t5-large",
"TaylorAI/bge-micro-v2", "sentence-transformers/all-MiniLM-L12-v2", "sentence-transformers/all-MiniLM-L6-v2",
"jinaai/jina-embedding-b-en-v1", "sentence-transformers/gtr-t5-base", "nomic-ai/nomic-embed-text-v1.5",
"nthakur/contriever-base-msmarco", "TaylorAI/bge-micro", "sentence-transformers/sentence-t5-base", "Hum-Works/lodestone-base-4096-v1",
"sentence-transformers/msmarco-bert-co-condensor", "jinaai/jina-embedding-s-en-v1", "sentence-transformers/LaBSE",
"sentence-transformers/average_word_embeddings_komninos", "sentence-transformers/average_word_embeddings_glove.6B.300d",
"sentence-transformers/allenai-specter", "consciousAI/cai-lunaris-text-embeddings", "consciousAI/cai-stellaris-text-embeddings",
"deepfile/embedder-100p", "jinaai/jina-embeddings-v2-base-de", "jinaai/jina-embeddings-v2-base-es"]


tasks=["BIOSSES",
    "SICK-R",
    "STS12",
    "STS13",
    "STS14",
    "STS15",
    "STS16",
    "STSBenchmark","SprintDuplicateQuestions",
    "TwitterSemEval2015",
    "TwitterURLCorpus","ArxivClusteringP2P", "ArxivClusteringS2S", "BiorxivClusteringP2P",
    "BiorxicClusteringS2S", "MedrxivClusteringP2P", "MedrxivClusteringS2S", "RedditClustering",
    "StackExchangeClustering", "StackExchangeClusteringP2P", "TwentyNewsgroupsClustering",
    "AmazonCounterfactualClassification", "AmazonPolarityClassification", "AmazonReviewsClassification",
    "Banking77Classification", "EmotionClassification", "ImdbClassification", "MassiveIntentClassification",
    "MassiveScenarioClassification", "MTOPDomainClassification", "MTOPIntentClassification", "ToxicConversationsClassification",
    "TweetSentimentExctractionClassification", "SprintDuplicateQuestionsPC", "TwitterSemEval2015PC", "TwitterURLCorpusPC",
    "AskUbuntuDupQuestions", "SciDocsRR", "StackOverflowDupQuestions", "CQADupstackStatsRetrieval", 
    "QuoraRetrieval", "SummEval"
    ]

model_name = "intfloat/e5-base-v2"
#model = INTFLOAT('intfloat/e5-base-v2', 'classification')


#for model_name in models:
model = SentenceTransformer(model_name).to(device)
evaluation = MTEB(tasks=[TwitterSemEval2015PC()])
results = evaluation.run(model, output_folder=f"results/{model_name.replace('/', '-')}")
