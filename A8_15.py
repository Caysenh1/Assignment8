D = {
    "H": 1,
    "He": 2,
    "Li": 4
}
print(D["H"])
print(D["He"])
D["Li"] = 3
print(D["Li"])
D.update({"Be" : 4,
          "B" : 5
})
print(D)
D.clear()
print(D)
