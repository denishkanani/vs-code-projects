# import re

# url = input("URL: ").strip()

# username = re.sub(r"(?:https?://)?(?:www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")


import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url, re.IGNORECASE):
    print(f"Username:", matches.group(1))

# import re

# url = input("Enter Twitter URL: ")

# match = re.search(r"https?://(www\.)?twitter\.com/([A-Za-z0-9_]+)", url)

# if match:
#     print("Username:", match.group(2))
# else:
#     print("Invalid Twitter URL")