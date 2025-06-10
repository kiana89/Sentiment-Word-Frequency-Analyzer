import pandas as pd
import re
from collections import Counter

file_path = 'Snappfood - Sentiment Analysis.csv'
df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', encoding='utf-8')
df.dropna(subset=['comment', 'label'], inplace=True)

cleaned_df = df[['comment', 'label', 'label_id']]
cleaned_df.to_csv('cleaned_comments.csv', index=False)
print(" 'cleaned_comments.csv' has been saved.")

basic_stopwords = {
    "the", "is", "in", "and", "to", "a", "of", "it", "for", "on", "with", "this",
    "that", "was", "as", "are", "but", "be", "at", "by", "an", "or", "from", "so",
    "if", "out", "not", "they", "i", "am", "have", "has", "had", "you", "we", "he",
    "she", "them", "their", "my", "me", "do", "did", "does", "will", "would", "can"
}

def preprocess_comment(comment):
    comment = comment.lower()
    comment = re.sub(r'[^\w\s]', '', comment)
    tokens = list(set(comment.split()))
    cleaned = [word for word in tokens if word.isalpha() and word not in basic_stopwords]
    return cleaned

df['processed_comment'] = df['comment'].apply(preprocess_comment)

happy_words = df[df['label'].str.lower() == 'happy']['processed_comment'].explode().tolist()
sad_words = df[df['label'].str.lower() == 'sad']['processed_comment'].explode().tolist()

happy_counts = Counter(happy_words)
sad_counts = Counter(sad_words)
all_counts = Counter(happy_words + sad_words)

top_words = all_counts.most_common(50)

results = []
for word, total in top_words:
    results.append({
        'Word': word,
        'Total Count': total,
        'Happy Count': happy_counts.get(word, 0),
        'Sad Count': sad_counts.get(word, 0)
    })

results_df = pd.DataFrame(results)
print("\n Top 50 most frequent words in happy and sad comments:")
print(results_df)

results_df.to_csv('top_50_sentiment_words.csv', index=False)
print("\n 'top_50_sentiment_words.csv' has also been saved.")
