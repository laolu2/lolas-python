# Write a program that:
# Accepts a list of customer reviews (strings) as input.
# Counts how many reviews contain positive words ("good", "excellent", "amazing") and how many contain negative words ("bad", "poor", "terrible").
# Prints a summary of positive and negative reviews:
# 	Positive Reviews: 7
# Negative Reviews: 3




customer_reviews = [
    "The product is good and excellent value.",
    "Terrible service, would not recommend.",
    "Amazing experience, highly recommended.",
    "Poor quality, very disappointed.",
    "Good customer service.",
    "Bad product, waste of money.",
    "Excellent product quality.",
    "Terrible experience with this company.",
    "Amazing support from the team.",
    "Poorly designed, not satisfied."
]

positive_words = ["good", "excellent", "amazing"]
negative_words = ["bad", "poor", "terrible"]

positive_count = 0
negative_count = 0

for review in customer_reviews:
    for word in review.lower().split():
        if word in positive_words:
            positive_count += 1
            break
        elif word in negative_words:
            negative_count += 1
            break

print(f"Positive Reviews: {positive_count}")
print(f"Negative Reviews: {negative_count}")