import requests

def get_summary(book, chapter):
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
    url = f"{base_url}{book.lower()}/{chapter}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract the summary from the JSON structure
        return data["summary"]
    except (requests.exceptions.RequestException, KeyError):
        raise KeyError("Unable to retrieve summary. Please check the book and chapter.")

def run_summary_tool():
    print("Welcome to the Book of Mormon Summary Tool!")

    while True:
        book = input("Which book of the Book of Mormon would you like? ").strip()
        chapter = input(f"Which chapter of {book} are you interested in? ").strip()

        try:
            summary = get_summary(book, chapter)
            print(f"\nSummary of {book} chapter {chapter}:\n{summary}\n")
        except KeyError:
            print("Sorry, that book or chapter could not be found. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        again = input("Would you like to view another (Y/N)? ").strip().lower()
        if again != 'y':
            print("Thank you for using Book of Mormon Summary Tool!")
            break

if __name__ == "__main__":
    run_summary_tool()
