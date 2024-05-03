# Lesson 6 // Python Strings
# Problem 1
# Task 1
python_reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                     "I had a bad experience with this product. It didn't meet my expectations.", 
                     "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."
                ]
upper_case_words = []
keywords = ["good", "excellent", "bad", "poor", "average"]

for sentence in python_reviews:
    for word in keywords:
        sentence = sentence.replace(word, word.upper())
        sentence = sentence.replace(word.title(), word.upper())
    upper_case_words.append(sentence)
    print(sentence)


#Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def pos_and_neg_count():
    number_of_positive = 0
    number_of_negative = 0
    for i in python_reviews:
        for word in i.split():
            word = word.replace(".","")
            if word.lower() in python_positive_words:
                number_of_positive += 1

    print(f" The number of positives are {number_of_positive}.")

    for i in python_reviews:
        for word in sentence.split():
            word = word.replace(".","")
            if word.lower() in negative_words:
                number_of_negative += 1
    print(f" The number of negatives are {number_of_negative}.")

pos_and_neg_count()



# task 3
python_reviews = [ "This product is really good. I'm impressed with its quality.",
                   "The performance of this product is excellent. Highly recommended!",
                     "I had a bad experience with this product. It didn't meet my expectations.", 
                     "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."
                ]
# review = []
# part_review = " ".join(python_reviews)
# print(part_review)
# edited = part_review[:29]
# review.append(edited)
# review.append("...")
# finish = " ".join(review)

# print(finish)

reviews = " ".join(python_reviews)
new_reviews = reviews.replace("'","")
sliced_review = new_reviews[:31] + "..."
print(sliced_review)



#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
# game_plan = "Execute play number 9"
# for word in game_plan[8:]:
#     print(word, end=" ")

# Problem 2 User input data Processor
# task 1

first_name = input("Type your first name. ")
last_name = input("Type your last name. ")
if len(first_name) > 2 and len(last_name) > 2:
    print(len(first_name))
    print(len(last_name))
else:
    print("Must be 2 or more characters in either first or last name. ")