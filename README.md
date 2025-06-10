# Sentiment-Word-Frequency-Analyzer

A Python script to extract and analyze the **most common words** in customer comments labeled as **happy** or **sad**, using basic text preprocessing and word frequency analysis.

---

## Features

- Cleans and saves a filtered version of the dataset
- Preprocesses text: lowercase, punctuation removal, stopword filtering, and duplicate word removal
- Separates comments by sentiment (`happy`, `sad`)
- Computes word frequency per sentiment
- Saves a table of the **Top 50 most frequent words** with sentiment breakdown

---

## Input

The script expects a CSV file named:

```
Snappfood - Sentiment Analysis.csv
````

Required columns:
- `comment`: the customer’s feedback
- `label`: sentiment label (e.g., `happy`, `sad`, `neutral`)
- `label_id`: optional numerical identifier for the label

File should be tab-separated (`.tsv`) if needed.

---

##  How to Run

```
project.py
````

No external libraries required beyond standard Python packages:

* `pandas`
* `re`
* `collections`

---

## Output

1. **cleaned\_comments.csv**
   Cleaned version of the dataset with `comment`, `label`, and `label_id`.

2. **top\_50\_sentiment\_words.csv**
   Contains the top 50 most frequent words in happy and sad comments, with their individual counts.

| Word  | Total Count | Happy Count | Sad Count |
| ----- | ----------- | ----------- | --------- |
| خوب | 12389       | 8933        | 3456      |
| ارسال   | 4932        | 2265        | 2267      |
| بد  | 4275        | 636         | 3639      |

---

## Use Cases

* Sentiment insight reporting
* Feature selection for ML models
* Understanding customer feedback trends

