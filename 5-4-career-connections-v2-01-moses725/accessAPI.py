import requests
import json

def get_summary(book, chapter):
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
    
    # Clean up the book name (e.g., "1 Nephi" → "1nephi")
    book_clean = book.lower().replace(" ", "")
    
    # Construct the full URL
    url = f"{base_url}{book_clean}/{chapter}"

    response = requests.get(url)
    
    if response.status_code != 200:
        raise KeyError("Invalid book or chapter")
    
    data = response.json()
    
    try:
        # Proper access to the summary field
        summary = data["chapter"]["summary"]
        return summary
    except KeyError:
        raise KeyError("Summary not available for this chapter")

def run_summary_tool():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    while True:
        book = input("Which book of the Book of Mormon would you like? ").strip()
        chapter = input(f"Which chapter of {book} are you interested in? ").strip()

        try:
            summary = get_summary(book, chapter)
            print(f"\nSummary of {book} chapter {chapter}:\n{summary}")
        
        except KeyError:
            print("Sorry, the book or chapter you entered is invalid or does not have a summary.")
        
        again = input("Would you like to view another (Y/N)? ").strip().lower()
        if again != "y":
            print("Thank you for using Book of Mormon Summary Tool!")
            break

# Entry point
if __name__ == "__main__":
    run_summary_tool()