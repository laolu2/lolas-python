# Write a program that:
# Stores a list of customer reviews:
# python
# Copy code
# reviews = [
#     "The product is amazing and works perfectly!",
#     "Terrible service, would not recommend.",
#     "Good value for money.",
#     "Poor quality, very disappointed."
# ]
# Uses a loop and conditions to classify each review:
# Positive: Contains amazing, perfect, good, or value.
# Negative: Contains terrible, poor, or disappointed.
# Neutral: Anything else.
# Prints a summary:
# mathematica
# Copy code
# Review 1: Positive
# Review 2: Negative


positive_review = ['amazing','perfect', 'good', 'value']
negative_review = ['terrible', 'poor', 'disappointed']
reviews = ["The product is amazing and works perfectly!",
    "Terrible service, would not recommend.",
    "Good value for money.",
    "Poor quality, very disappointed."]
for index , review in enumerate(reviews, start=1):
    review_words = review.split(" ")



positive_review = ['amazing', 'perfect', 'good', 'value']
negative_review = ['terrible', 'poor', 'disappointed']

reviews = ["The product is amazing and works perfectly!",
           "Terrible service, would not recommend.",
           "Good value for money.",
           "Poor quality, very disappointed."]

for index, review in enumerate(reviews, start=1):
    print(review)
    review_words = review.split(" ")
    print(review_words)
    print("\n")

    review_type = "neutral" 
    for word in review_words:
        if word.lower in positive_review:
            review_type = "positive"
        elif word.lower in negative_review: 
            review_type = "negative"

        print(word, review_type, end="\t")
        print("\n")