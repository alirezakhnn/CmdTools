import wikipedia

# Get user input for the query
query = input("Enter your search query: ")

try:
    # Search Wikipedia for the query
    results = wikipedia.search(query)

    if len(results) > 0:
        # Prompt the user to choose the desired page
        print("Choose a page from the following options:")
        for i, result in enumerate(results):
            print(f"{i+1}. {result}")

        choice = int(input("Enter the number corresponding to your choice: "))

        # Fetch the summary for the chosen result
        summary = wikipedia.summary(results[choice-1])
        
        # Print the summary
        print(summary)
    else:
        print("No results found.")

except wikipedia.exceptions.DisambiguationError as e:
    print(f"{e.title} may refer to:")
    for option in e.options:
        print("- " + option)
