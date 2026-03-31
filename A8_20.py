webpages = ['homepage', 'aboutpage', 'sitemap']
V = input("Enter three values: ").split()
V = list(map(int, V))
VV = dict(zip(webpages, V))
if V[0] < 0 or V[1] < 0 or V[2] < 0:
    print("Invalid value")
else:
    print(VV)
