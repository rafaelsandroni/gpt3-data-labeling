# AutoLabeling

This repo aims to reproduce the study from [Want To Reduce Labeling Cost? GPT-3 Can Help](https://arxiv.org/pdf/2108.13487.pdf) in Brazilian Portuguese.

Abstract: Data annotation is a time-consuming and labor-intensive process for many NLP tasks. Although there exist various methods to produce pseudo data labels, they are often task specific and require a decent amount of labeled data to start with. Recently, the immense language model GPT-3 with 175 billion parameters has achieved tremendous improvement across many few-shot learning tasks. In this paper, we explore ways to leverage GPT-3 as a low-cost data labeler to train other models. We find that, to make the downstream model achieve the same performance on a variety of NLU and NLG tasks, it costs 50% to 96% less to use labels from GPT-3 than using labels from humans. Furthermore, we propose a novel framework of combining pseudo labels from GPT-3 with human labels, which leads to even better performance with limited labeling budget. These results present a cost-effective data labeling methodology that is generalizable to many practical applications.


## Experiments

Fow now, the experiment was performed on sentiment analysis task using the [B2W-Reviews Dataset](https://github.com/b2wdigital/b2w-reviews01) just for test purposes. In the next steps we can explore benchmark tasks and datasets.

- [x] GPT3-Label
- [ ] Human-Labeling
- [ ] GPT3-Human-Labeling
- [ ] RawGPT3

### Task

Sentiment analysis on product reviews.

### GPT3-Label performance evaluation
![image](https://user-images.githubusercontent.com/6341659/135017480-5282d148-f94b-4d26-9505-09fc25293cdb.png)


## Library 

This library aims to facilitate to add other language models in future experiments (e.g, GPT-J), and also to open for colaborations since we face low resources for Portuguese language.

```
pip install git+https://github.com/rafaelsandroni/autolabeling
```

### Usage

```
from AutoLabeling import AutoLabeling

labeling = AutoLabeling(label_df, text_col="review_text", label_col="sentiment")

labeling.execute("nao gostei da qualidade do produto")

label_df["labeling"] = label_df["review_text"].apply(labeling.execute)
```



