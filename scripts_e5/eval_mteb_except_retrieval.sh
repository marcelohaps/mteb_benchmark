#!/usr/bin/env bash

set -x
set -e

DIR="$( cd "$( dirname "$0" )" && cd .. && pwd )"
echo "working directory: ${DIR}"


BASE_OUTPUT_DIR="tmp-outputs/"


MODELS=()
while [[ $# -gt 0 && ! "$1" == "--"* ]]; do
    MODELS+=("$1")
    shift
done


for MODEL_NAME_OR_PATH in "${MODELS[@]}"; do
    MODEL_DIR=$(echo ${MODEL_NAME_OR_PATH} | tr '/' '_')  
    OUTPUT_DIR="${BASE_OUTPUT_DIR}${MODEL_DIR}/"
    mkdir -p "${OUTPUT_DIR}"  
    echo "Running evaluation for model: ${MODEL_NAME_OR_PATH}"
    python -u mteb_except_retrieval_eval.py \
        --model-name-or-path "${MODEL_NAME_OR_PATH}" \
        --task-types "STS" "Summarization" "PairClassification" "Classification" "Reranking" "Clustering" "BitextMining" \
        --output-dir "${OUTPUT_DIR}" "$@"
done

echo "done"
