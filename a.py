from gui import *


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# cheeseshop("Limburger", "It's very runny, sir.",
#            *["It's really very, VERY runny, sir."],
#            **{"shopkeeper": "Michael Palin", "client": "John Cleese", "sketch": "Cheese Shop Sketch"})
# print('\n')
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")
def test0():
    a = {'a': 1, 'b': 2, 'c': 3}
    for key in a.keys():
        print(key + '-------------' + str(a[key]))
    print("\n")

    for item in a.items():
        print(item)
    print("\n")

    for (k, v) in a.items():
        print(k + '-------------' + str(v))
    print("\n")



print(a)
