# AutoLabeling

## This repo aims to reproduce the study Want To Reduce Labeling Cost? GPT-3 Can Help (https://arxiv.org/pdf/2108.13487.pdf).




## Instalation

```
pip install git+https://github.com/rafaelsandroni/autolabeling
```

## Usage

```
from AutoLabeling import AutoLabeling

labeling = AutoLabeling(label_df, text_col="review_text", label_col="sentiment")

labeling.execute("nao gostei da qualidade do produto")

label_df["labeling"] = label_df["review_text"].apply(labeling.execute)
```


## Labeling performance evaluation
![image](https://user-images.githubusercontent.com/6341659/135017480-5282d148-f94b-4d26-9505-09fc25293cdb.png)
