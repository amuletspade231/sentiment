import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Amanda Cao
# 4/18/2024
# Sentiment Proof of Concept
# This program demonstrates sentiment analysis on an article

# function to extract text content from a url
def extract_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_title = soup.select('h1')[0].text.strip()
    article_text = soup.select_one('div.RichTextArticleBody-body').get_text(' ', strip=True)
    return article_title, article_text

# function to perform sentiment analysis on the input text
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score['compound']
    if compound_score >= 0:
        sentiment_label = "positive"
    else:
        sentiment_label = "negative"
    return compound_score, sentiment_label

def main():
    website_url = "https://www.abc15.com/news/crime/two-men-dead-another-hurt-in-shooting-near-19th-avenue-and-roeser-road-in-south-phoenix"
    # extract text from url
    subject, website_text = extract_website_text(website_url)
    # perform sentiment analysis on the website text
    compound_score, sentiment_label =analyze_sentiment(website_text)
    # print results
    print(f"Sentiment Analysis Results for: {subject}")
    print(f"Article: {website_text}")
    print(f"Compound Score: {compound_score}")
    print(f"Sentiment Label: {sentiment_label}")

if __name__ == "__main__":
    main()