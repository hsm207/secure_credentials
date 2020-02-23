import argparse
from typing import Tuple

import boto3


def classify_text(text: str) -> Tuple[str, float]:
    client = boto3.client("comprehend", region_name="ap-southeast-1")

    response = client.detect_sentiment(Text=text, LanguageCode="en")

    sentiment = response["Sentiment"].title()
    score = response["SentimentScore"][sentiment]

    return sentiment, score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Demo AWS Comprehend for sentiment analysis"
    )
    parser.add_argument("text", help="text to classify its sentiment")

    args = parser.parse_args()
    text = args.text

    sentiment, score = classify_text(text)

    print(
        f"""
The sentiment for the text:
    {text}
is {sentiment} ({round(score, 2)})
"""
    )
