movies = {
    'The Empire Strikes Back': 10,
    'A New Hope': 10,
    'The Fellowship of the Ring': 10
}
suggest = input("Enter movies: ").split(", ")
suggest = list(map(str, suggest))
D = dict.fromkeys(suggest, 10)
movies.update(D)
print(movies)
