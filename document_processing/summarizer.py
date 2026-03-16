from transformers import pipeline

summarizer = pipeline("summarization")

text = """
Artificial Intelligence helps organizations automate tasks,
improve efficiency, and assist employees with decision making.
"""

summary = summarizer(text, max_length=40, min_length=10, do_sample=False)

print(summary[0]['summary_text'])
