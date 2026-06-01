user = input("Tên tài khoản người đăng video: ")
vid_title = input("Tiêu đề video: ")
description = input("Mô tả video: ")
hashtags = input("Nhập hashtag (cách nhau bởi dấu phẩy): ")

user_checked = user.strip()
vid_title_checked = vid_title.strip().title()
description_checked = description.strip()
description_length = len(description)

hastag_checked = hashtags.strip().replace(",,", ",").replace(", ,", ",")

count_word = 0
for char in description_checked:
    if char == ' ':
        count_word+= 1


count_hastags = 0
for char in hastag_checked:
    if char == "#":
        count_hastags += 1

print(f"Tên tài khoản: {user_checked}")
print("-" * 25)
print(f"Tiêu đề vid: {vid_title_checked}")
print("-" * 25)
print(f"Mô tả vid: {description_checked}")
print(f"Độ dài mô tả: {description_length}")
print(f"Số lượng từ trong mô tả: {count_word + 1}")
print("-" * 25)
print(f"Hashtags: {hastag_checked}")
print(f"Số lượng hastags: {count_hastags}")
print("-" * 25)
print("Mô tả in thường: ",description_checked.lower())
print("Mô tả in hoa: ",description_checked.upper())



