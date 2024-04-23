#!/usr/bin/env bash

set -x
set -e

# Diretório base onde o script está localizado
DIR="$( cd "$( dirname "$0" )" && cd .. && pwd )"
echo "working directory: ${DIR}"

# Diretório de saída padrão para os resultados
BASE_OUTPUT_DIR="tmp-outputs/"

# Coleta todos os argumentos que não começam com "--" como modelos
MODELS=()
while [[ $# -gt 0 && ! "$1" == "--"* ]]; do
    MODELS+=("$1")
    shift
done

# Processa cada modelo fornecido
for MODEL_NAME_OR_PATH in "${MODELS[@]}"; do
    # Cria um diretório específico para os resultados de cada modelo
    MODEL_DIR=$(echo ${MODEL_NAME_OR_PATH} | tr '/' '_')  # Substitui '/' por '_' para evitar problemas de diretório
    OUTPUT_DIR="${BASE_OUTPUT_DIR}${MODEL_DIR}/"
    mkdir -p "${OUTPUT_DIR}"  # Cria o diretório se ele não existir

    echo "Running evaluation for model: ${MODEL_NAME_OR_PATH}"
    python -u mteb_except_retrieval_eval.py \
        --model-name-or-path "${MODEL_NAME_OR_PATH}" \
        --task-types "STS" "Summarization" "PairClassification" "Classification" "Reranking" "Clustering" "BitextMining" \
        --output-dir "${OUTPUT_DIR}" "$@"
done

echo "done"
