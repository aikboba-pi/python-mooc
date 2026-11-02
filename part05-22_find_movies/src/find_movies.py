# Write your solution here
def find_movies(database: list, search_term: str):
    matches = []
    term = search_term.lower()
    
    for movie in database:
        if term in movie["name"].lower():
            matches.append(movie)
            
    return matches