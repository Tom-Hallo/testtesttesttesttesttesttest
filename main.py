# Bài tập Python
# Input
# - Tên tài khoản TikTok: str
# - Mô tả video: str
# - Lựa chọn menu: int
# - Từ khóa cần tìm: str
# - Từ khóa thay thế: str

# Output
# - Thông báo lỗi nếu dữ liệu không hợp lệ
# - Mô tả sau khi thay thế
# - Số lần từ khóa xuất hiện
# - Thông báo thoát chương trình

# - Dùng strip() để kiểm tra dữ liệu rỗng
# - Dùng isdigit() để kiểm tra menu có phải số nguyên hay không
# - Dùng count() để đếm số lần xuất hiện của từ khóa
# - Dùng replace() để thay thế từ khóa
# - Dùng while True để chạy menu liên tục

# Bắt đầu chương trình

# Nhập tên tài khoản
# Nếu rỗng -> báo lỗi

# Nhập mô tả video
# Nếu rỗng -> báo lỗi

# Lặp menu:
#   Hiển thị menu
#   Nhập lựa chọn

#   Nếu không phải số:
#       Báo lỗi

#   Nếu chọn 4:
#       Nhập từ khóa cần tìm
#       Nhập từ khóa thay thế

#       Nếu tìm thấy:
#           Đếm số lần xuất hiện
#           Thay thế từ khóa
#           In kết quả
#       Ngược lại:
#           Báo không tìm thấy

#   Nếu chọn 5:
#       Thoát chương trình

#   Nếu khác 4 và 5:
#       Báo lựa chọn không hợp lệ

while True:
    account_name = input("Nhập tên tài khoản TikTok: ").strip()

    if account_name == "":
        print("Tên tài khoản không được rỗng")
    else:
        break

while True:
    description = input("Nhập mô tả video: ").strip()

    if description == "":
        print("Mô tả video không được rỗng")
    else:
        break

while True:
    print("\n===== MENU =====")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice == 4:
        find_keyword = input("Nhập từ khóa cần tìm: ")
        replace_keyword = input("Nhập từ khóa thay thế: ")

        if find_keyword in description:
            total = description.count(find_keyword)
            new_description = description.replace(find_keyword, replace_keyword)

            print("Mô tả sau khi thay thế:")
            print(new_description)

            print("Số lần xuất hiện:", total)
        else:
            print("Không tìm thấy từ khóa")

    elif choice == 5:
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")