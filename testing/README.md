# Replication results 

## To run the test 

The original data are in `../dataset/*` which is in the format of 

```
WORD UNKNOWN_TAG_1 UNKOWN_TAG_2 NAMED_ENTITY_TAG
```

and each sentence is separated by an empty line. 

To run the experiment using the code in `../README.md`, the format required is a sentence each line. Thus, I need to parse it into sentences which is in `parse_from.py`. After running the experiment, the format is `__LABEL` appended to each word. To use the evaluation software at `../evaluation/conlleval`, we need the format 
```
WORD ANYTHING TRUE_NAMED_ENTITY_TAG PREDICTED_NAMED_ENTITY_TAG
```
and each sentence is separated by an empty line. This is done in `parse_to.py`. One more thing we need to conider is that the tags in the original data contains only `I-LABEL` while the prediction made by the model uses both `B-LABEL` and `I-LABEL`. Thus, we manually change the `B-LABEL` to `I-LABEL` in `parse_to.py`. Finally, we can use `../evaluation/conlleval` to evaluate the result.

I also wrote script `find_error.py` to find the error made by the model by appending a tag to the line that predicted wrong. 

## Results 

### testa 
```
processed 51578 tokens with 5917 phrases; found: 5909 phrases; correct: 5560.
accuracy:  98.94%; precision:  94.09%; recall:  93.97%; FB1:  94.03
              LOC: precision:  96.55%; recall:  96.28%; FB1:  96.42  1825
             MISC: precision:  90.16%; recall:  86.21%; FB1:  88.14  874
              ORG: precision:  90.05%; recall:  92.47%; FB1:  91.24  1377
              PER: precision:  96.56%; recall:  96.62%; FB1:  96.59  1833
```
### testb 
```
processed 46666 tokens with 5616 phrases; found: 5670 phrases; correct: 5115.
accuracy:  97.87%; precision:  90.21%; recall:  91.08%; FB1:  90.64
              LOC: precision:  93.92%; recall:  91.72%; FB1:  92.80  1627
             MISC: precision:  80.58%; recall:  79.32%; FB1:  79.94  690
              ORG: precision:  85.25%; recall:  90.89%; FB1:  87.98  1756
              PER: precision:  96.06%; recall:  95.76%; FB1:  95.90  1597
```
### test a+b
```
processed 98244 tokens with 11533 phrases; found: 11579 phrases; correct: 10675.
accuracy:  98.44%; precision:  92.19%; recall:  92.56%; FB1:  92.38
              LOC: precision:  95.31%; recall:  94.11%; FB1:  94.70  3452
             MISC: precision:  85.93%; recall:  83.22%; FB1:  84.55  1564
              ORG: precision:  87.36%; recall:  91.60%; FB1:  89.43  3133
              PER: precision:  96.33%; recall:  96.21%; FB1:  96.27  3430
```
### train 
```
processed 204567 tokens with 23396 phrases; found: 23386 phrases; correct: 22968.
accuracy:  99.70%; precision:  98.21%; recall:  98.17%; FB1:  98.19
              LOC: precision:  98.89%; recall:  98.58%; FB1:  98.74  7108
             MISC: precision:  96.84%; recall:  95.45%; FB1:  96.14  3357
              ORG: precision:  97.33%; recall:  97.97%; FB1:  97.65  6341
              PER: precision:  99.03%; recall:  99.33%; FB1:  99.18  6580
```