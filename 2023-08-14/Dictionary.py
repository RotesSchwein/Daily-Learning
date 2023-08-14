# Create empty dictionary
empty_dict = {}

# Normal dictionary
dict_1 = {"apple": 1.5, "cherry": 2.0}
print(dict_1)

dict_2 = {
    'fruit': {
        'apple': {  # dict
            'price': 5000,
            'quantity': 10,
            'status': 'fresh'
        },
        'cherry': {
            'price': 14000,
            'quantity': 25,
            'status': 'fresh'
        }
    },
    'vegetable': [  # list
        'radish',
        'lettuce',
        'broccoli'
    ],
    'meat': [  # dict inside list
        {'beef_quantity': 100},
        {'pork_quantity': 500},
        {'fish_quantity': 300}
    ]
}

dict_3 = {
    "MBT": {
        "Russia": {
            "T-90A": 10.7,
            "T-80BVM": 11.7,
            "T-72B3M": 11.3
        },
        "USA": {
            "M1A1": 11.0,
            "M1A1 HC": 11.3,
            "M1A2": 11.3,
            "M1A2 SEP": 11.7
        }
    },
    "Light Tank": {
        "Tracked",
        "Wheeled"
    },
    "IFV": [
        {"M3A3 Bradley": 10.0},
        {"PUMA": 10.0},
        {"CV9030": 9.0}
    ]
}

for _key in dict_3:
    print(f"dict_3, item -- {_key}")

for key, value in dict_3.items():
    print(f"dict_3, key -- {key}. value -- {value}")
print()

for __key in dict_3.keys():
    print(f"_keys -- {__key}")

for __value in dict_3.values():
    print(f"_value -- {__value}")
print()

# Dictionary update
BR_before = {"PUMA": 10.0, "Radkampfwagen 90": 9.3}
BR_after = {"PUMA": 9.7, "Radkampfwagen 90": 9.7}

BR_before.update(BR_after)
print(BR_before)

# Use if ~ in ~ instead of update
if "PUMA" in BR_before:
    BR_before["PUMA"] = 10.0
print(BR_before)

if "Radkampfwagen 90" in BR_before:
    BR_before["Radkampfwagen 90"] = 9.3
print(BR_before)
