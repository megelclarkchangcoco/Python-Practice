

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end =" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr. ", "Spongebob", "Squarepants", "III",
               street="123 Fake st",
               apt = "100",
               city="Detriot ",
               states="MI",
               zip="54321")
