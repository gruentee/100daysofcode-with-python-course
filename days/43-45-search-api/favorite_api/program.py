"""Small script to query the TalkPython search API"""
import api


if __name__ == "__main__":
    query = input("Enter a search term: ")

    results = api.search(query)
    print(f"Got {len(results)} results:")
    for r in results:
        print(r.title)
