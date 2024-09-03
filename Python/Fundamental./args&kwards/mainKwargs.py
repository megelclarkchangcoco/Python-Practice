
def print_address(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}:{values}")

print_address(stree="123 Fake st",
              apt = "100",
              city="Detriot ",
              states="MI",
              zip="54321")