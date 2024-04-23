---
tags:
- mteb
model-index:
- name: mxbai-embed-large-v1
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification
      config: default
      split: test
      revision: 589b8cdf671a2e80745f3443de8e52f70d8c296f
    metrics:
    - type: EN_accuracy
      value: 61.52238805970149
    - type: EN_ap
      value: 24.71878404588084
    - type: EN_f1
      value: 55.121432337059716
    - type: EN-ext_accuracy
      value: 59.025487256371825
    - type: EN-ext_ap
      value: 12.995597020106947
    - type: EN-ext_f1
      value: 47.64879154001588
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification
      config: default
      split: test
      revision: 695077f4f176f67d6190332b091115fcd40dfd98
    metrics:
    - type: pt-br_accuracy
      value: 26.488000000000007
    - type: pt-br_f1
      value: 26.188597884774694
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 8d444270b78b51ef45c044ba5c61a0adfdb02a15
    metrics:
    - type: accuracy
      value: 65.1038961038961
    - type: f1
      value: 64.6946839254739
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: b794f1180f87495a2362adb692a9a8b61749f720
    metrics:
    - type: accuracy
      value: 26.405
    - type: f1
      value: 23.755884411271463
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 562e20aba5990eb05fa16ac24c7dd924148fd951
    metrics:
    - type: accuracy
      value: 58.504
    - type: ap
      value: 55.0662806190568
    - type: f1
      value: 57.926998556392896
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification
      config: default
      split: test
      revision: 0ae627d70049e0fff537a4a860a6dee152165abf
    metrics:
    - type: default_accuracy
      value: 75.48813868613139
    - type: default_f1
      value: 74.88366260684647
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification
      config: default
      split: test
      revision: a51c4909bcc2d97c03afae5d1deac99f93a7930a
    metrics:
    - type: pt-br_accuracy
      value: 44.04653284671533
    - type: pt-br_f1
      value: 26.55412286267962
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification
      config: default
      split: test
      revision: b5bc0efb7b0eb40576ea6f8040cb299a1b92823c
    metrics:
    - type: default_accuracy
      value: 53.47343644922663
    - type: default_f1
      value: 51.60161768284135
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification
      config: default
      split: test
      revision: 6268db13795aaa0597230b910abf7be149304fd1
    metrics:
    - type: default_accuracy
      value: 58.2985877605918
    - type: default_f1
      value: 57.72710420681555
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: a14b45380976f1406d0e7928f0f5e3cbc1d33cb2
    metrics:
    - type: accuracy
      value: 63.9548
    - type: ap
      value: 10.939680431168778
    - type: f1
      value: 48.871997346904
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: c519eb949db67f572a7257a1a1a6de505c2425d4
    metrics:
    - type: accuracy
      value: 43.58517260894171
    - type: f1
      value: 43.52297751435934
---