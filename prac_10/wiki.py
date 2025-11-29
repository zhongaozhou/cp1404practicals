"""
Wiki search program using the Wikipedia API.
CP1404 Practical.
"""

import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            # Try to get the page
            page = wikipedia.page(title)

            # print title, summary, and url
            print(page.title)
            print(page.summary)
            print(page.url)
            print()

        except wikipedia.DisambiguationError as e:
            # need a more specific title
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)   # list of suggested pages
            print()

        except wikipedia.PageError:
            # Page does not exist
            print(f'Page id "{title}" does not match any pages. Try another id!\n')

        except Exception as e:
            # other unexpected problem
            print("An unexpected error occurred:", e)
            print()

        title = input("Enter page title: ").strip()
    print("Thank you.")


if __name__ == "__main__":
    main()
