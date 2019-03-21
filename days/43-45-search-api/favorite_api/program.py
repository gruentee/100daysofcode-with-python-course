"""Small script to query the TalkPython search API"""
import api
import webbrowser


SITE_URL = "https://talkpython.fm"

if __name__ == "__main__":
    query = input("Enter a search term: ")
    # replace white-space by dash == boolean &
    query = query.replace(" ", "-")
    results = api.search(query)
    print(f"Got {len(results)} results:")
    for i,r in enumerate(results):
        print(f"[{i}] {r.title}")
    
    episode_index = int(input("Which one of these do you want to open? Enter a number: "))
    url_to_open = SITE_URL + results[episode_index].url
    webbrowser.open(url_to_open, 2)
    
