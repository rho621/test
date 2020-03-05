myprofile = {"name": "Ronald",
    "occupation": "librarian",
    "age": "35",
    "hobbies": ["basketball", "football", "pool"],
    "time": {"mon": 8, "tue": 9, "wed": 8} }

print(f'{myprofile["name"]} I have {myprofile[hobbies]} hobbies, I work as a {myprofile["occupation"]} and I wake up at {myprofile["time"]["mon"]}')