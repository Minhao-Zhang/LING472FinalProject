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
processed 51578 tokens with 5942 phrases; found: 5930 phrases; correct: 5584.
accuracy:  98.94%; precision:  94.17%; recall:  93.98%; FB1:  94.07
              LOC: precision:  96.56%; recall:  96.30%; FB1:  96.43  1832
             MISC: precision:  90.44%; recall:  86.23%; FB1:  88.28  879
              ORG: precision:  90.05%; recall:  92.47%; FB1:  91.24  1377
              PER: precision:  96.63%; recall:  96.63%; FB1:  96.63  1842
```
### testb 
```
processed 46666 tokens with 5648 phrases; found: 5701 phrases; correct: 5144.
accuracy:  97.87%; precision:  90.23%; recall:  91.08%; FB1:  90.65
              LOC: precision:  93.98%; recall:  91.67%; FB1:  92.81  1627
             MISC: precision:  79.60%; recall:  79.49%; FB1:  79.54  701
              ORG: precision:  85.54%; recall:  90.79%; FB1:  88.08  1763
              PER: precision:  96.21%; recall:  95.79%; FB1:  96.00  1610
```
### test a+b
```
processed 98244 tokens with 11590 phrases; found: 11631 phrases; correct: 10728.
accuracy:  98.44%; precision:  92.24%; recall:  92.56%; FB1:  92.40
              LOC: precision:  95.35%; recall:  94.09%; FB1:  94.72  3459
             MISC: precision:  85.63%; recall:  83.31%; FB1:  84.46  1580
              ORG: precision:  87.52%; recall:  91.54%; FB1:  89.48  3140
              PER: precision:  96.44%; recall:  96.24%; FB1:  96.34  3452
```
### train 
```
processed 204567 tokens with 23499 phrases; found: 23477 phrases; correct: 23070.
accuracy:  99.70%; precision:  98.27%; recall:  98.17%; FB1:  98.22
              LOC: precision:  98.92%; recall:  98.59%; FB1:  98.75  7116
             MISC: precision:  97.07%; recall:  95.49%; FB1:  96.28  3382
              ORG: precision:  97.37%; recall:  97.96%; FB1:  97.67  6359
              PER: precision:  99.03%; recall:  99.33%; FB1:  99.18  6620
```