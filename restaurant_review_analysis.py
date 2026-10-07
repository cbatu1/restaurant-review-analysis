# Input and output file names

REVIEWS_FILENAME = "restaurant_reviews.txt"
OUTPUT_FILENAME = "complaint_report.txt"

# Dictionary of common complaint categories and keywords
# Each category maps to a list of keywords that are associated with them

complaints = {
    "slow service": ["slow", "waiting", "waited", "took forever", "long wait"],
    "rude staff": ["rude", "attitude", "unfriendly", "jerk", "ignored"],
    "food quality": ["bland", "cold", "overcooked", "raw", "tasteless", 
                     "soggy", "gross,", "bad", "awful", "disappointing"],
    "cleanliness": ["dirty", "messy", "disgusting", "smelled", "hair",
                    "unsanintary"],
    "price": ["overpriced", "expensive", "pricey", "cost too much"]
}

# load_reviews Function
# Reads the input file and puts all reviews into a list

def load_reviews(filename):
    
    reviews = [] 
    
    # Open the file using "with" so it closes automatically.
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            # Remove newline characters and extra spaces
            cleaned = line.strip()
            
            if cleaned:
                reviews.append(cleaned)
    
    return reviews

# categorize_review Function
# Returns a list of complaint categories found in an individual review

def categorize_review(review, complaints_dict):
    
    categories_found = []
    
    # Converting text to lowercase
    lower_review = review.lower()
    
    # Check each complaint category and its keywords in the review
    for category, keywords in complaints_dict.items():
        for word in keywords:
            
            # If a keyword appears, tag its respective category
            if word in lower_review:
                categories_found.append(category)
                
                # Breaking avoids counting the same category twice
                break
            
    return categories_found


# analyze_reviews Function
# Analyzes the reviews and returns the following:
#    1. complaint_counts - dictionary
#    2. categories_per_review - list of lists
#    3. netural_count - number value

def analyze_reviews(reviews, complaints_dict):
    
    # Initialize counters for each complaint type
    complaint_counts = {category: 0 for category in complaints_dict}
    
    # Initialize other return variables
    categories_per_review = []
    neutral_count = 0
    
    # Loop through every review in the data set and find the categories
    # contained in each review
    for review in reviews:
        categories = categorize_review(review, complaints_dict)
        categories_per_review.append(categories)
        
        # If no category is found in the review increase netural count
        if len(categories) == 0:
            neutral_count += 1
        else:
            
            # Otherwise, increase count for each category detected
            for c in categories:
                complaint_counts[c] += 1
                
    return complaint_counts, categories_per_review, neutral_count

# write_report Function
# This function generates a text file report that includes total counts and 
# the most common complaint

def write_report(filename, reviews, categories_per_review, complaint_counts):
    
    total_reviews = len(reviews)
    neutral_count = sum(1 for c in categories_per_review if len(c) == 0)
    
    # Finding the most frequent complaint category
    max_count = max(complaint_counts.values())
    
    most_frequent = []
    
    for c, count in complaint_counts.items():
        if count == max_count:
            most_frequent.append(c)
    
    with open(filename, "w", encoding = "utf-8") as f:
        f.write("RESTAURANT COMPLAINT REPORT: FINAL ANALYSIS\n")
        f.write("\n\n")
        f.write(f"Total Number of Reviews: {total_reviews}\n")
        f.write(f"Neutral (nocomplaints): {neutral_count}\n\n")
        
        f.write("Complaints Count:\n")
        
        for category, count in complaint_counts.items():
            f.write(f"- {category}: {count}\n")
        
        f.write("\nMost Frequent Complaint: " + ", ".join(most_frequent))
        
# print_summary Function
# Prints a summary to the terminal for the user to view

def print_summary(complaint_counts, total_reviews, neutral_count):
    
    print("\nCOMPLAINT ANALYSIS SUMMARY")
    print("\n")
    print(f"Total Reviews: {total_reviews}")
    print(f"Neutral Reviews (No Complaints): {neutral_count}")
    
    print("\nComplaint Counts:")
    
    for category, count in complaint_counts.items():
        print(f"- {category}: {count}")
    
    max_count = max(complaint_counts.values())
    
    most_frequent = []
    
    for c, count in complaint_counts.items():
        if count == max_count:
            most_frequent.append(c)
    
    print("\nMost Common Complaint Types: " + ", ".join(most_frequent))

# Main Program Loop

def main():
    
    # Data set loads once at the start of the program
    reviews = load_reviews(REVIEWS_FILENAME)
    
    complaint_counts = None
    categories_per_review = None
    neutral_count = 0
    
    selection = ""
    
    # Menu will continue to loop until the user exits
    while selection != "4":
        
        print("\nRestaurant Complaint Analyzer")
        print("\n")
        print("1. Analyze reviews")
        print("2. Show summary on screen")
        print("3. Generate detailed complaint report as a file")
        print("4. Exit")
        print("\n")
        
        selection = input("Enter your choice please (1-4): ").strip()
        
        if selection == "1":
            result = analyze_reviews(reviews, complaints)
            complaint_counts, categories_per_review, neutral_count = result
            print("Analysis has been completed!")
        
        elif selection == "2":
            if complaint_counts is None:
                print("Please run the analysis first (select option 1.")
            else:
                print_summary(complaint_counts, len(reviews), neutral_count)

        
        elif selection == "3":
            if complaint_counts is None:
                print("Please run the analysis first (select option 1.")
            else:
                write_report(OUTPUT_FILENAME, reviews, categories_per_review, complaint_counts)
                print(f"Report has been generated to the file {OUTPUT_FILENAME}.")
            
        elif selection == "4":
            print("Thank you! Goodbye!")
            break
        
        else:
            print("Invalid choice, please enter a valid option between 1 and 4 inclusive.")

if __name__ == "__main__":
    main()
        

