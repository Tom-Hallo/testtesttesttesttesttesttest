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

import re

# Khởi tạo các biến lưu trữ dữ liệu toàn cục trong phiên chạy
username = ""
title = ""
description = ""
hashtags = []
has_data = False  # Cờ kiểm tra xem đã nhập dữ liệu ở Chức năng 1 chưa

while True:
    print("\n" + "="*40)
    print(" HỆ THỐNG KIỂM DUYỆT NỘI DUNG TIKTOK")
    print("="*40)
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản TikTok")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
    print("5. Thoát chương trình")
    print("="*40)

    choice_input = input("Mời đại ka chọn chức năng (1-5): ").strip()

    if not choice_input.isdigit():
        print("❌ Lỗi: Lựa chọn không hợp lệ (phải là số nguyên). Vui lòng nhập lại!")
        continue

    choice = int(choice_input)

    if choice < 1 or choice > 5:
        print("❌ Lỗi: Lựa chọn không nằm trong phạm vi từ 1 đến 5. Vui lòng nhập lại!")
        continue

    # CHỨC NĂNG 1: NHẬP DỮ LIỆU VÀ XEM BÁO CÁO THỐNG KÊ
    if choice == 1:
        # Bẫy 1: Tên tài khoản TikTok rỗng hoặc chỉ có khoảng trắng
        while True:
            username = input("Nhập tên tài khoản người đăng: ").strip()
            if not username:
                print("❌ Tên tài khoản không được rỗng!")
            else:
                break

        title = input("Nhập tiêu đề video: ").strip()

        while True:
            description = input("Nhập mô tả video: ").strip()
            if not description:
                print("❌ Mô tả video không được rỗng!")
            else:
                break

        hashtag_input = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
        if hashtag_input.strip():
            # Tách bằng dấu phẩy và loại bỏ khoảng trắng thừa của từng hashtag
            hashtags = [h.strip() for h in hashtag_input.split(",") if h.strip()]
        else:
            hashtags = []

        has_data = True
        
        print("\n--- BÁO CÁO THỐNG KÊ VIDEO ---")
        print(f"+ Tên tài khoản (đã trim): {username}")
        print(f"+ Tiêu đề (Chuẩn hóa Title Case): {title.title()}")
        print(f"+ Mô tả (đã trim): {description}")
        print(f"+ Độ dài mô tả video: {len(description)} ký tự")
        print(f"+ Số lượng từ trong mô tả: {len(description.split())} từ")
        print(f"+ Danh sách hashtag sau chuẩn hóa: {hashtags}")
        print(f"+ Số lượng hashtag: {len(hashtags)}")
        print(f"+ Mô tả video chuyển sang chữ thường: {description.lower()}")
        print(f"+ Mô tả video chuyển sang chữ hoa: {description.upper()}")

    elif choice == 2:
        if not has_data:
            print("⚠️ Đại ka cần nhập dữ liệu ở Chức năng 1 trước!")
            continue
        
        normalized_username = f"@{username.lower()}"
        print("\n--- CHUẨN HÓA TÊN TÀI KHOẢN ---")
        print(f"Tên tài khoản ban đầu: \"{username}\"")
        print(f"Tên tài khoản sau khi được chuẩn hoá: \"{normalized_username}\"")

    elif choice == 3:
        if not has_data:
            print("⚠️ Đại ka cần nhập dữ liệu ở Chức năng 1 trước!")
            continue

        new_hashtag = input("Nhập một hashtag cần kiểm tra: ").strip()

        if not new_hashtag:
            print("❌ Lỗi: Hashtag không được rỗng")
        elif not new_hashtag.startswith("#"):
            print("❌ Lỗi: Hashtag phải bắt đầu bằng ký tự #")
        elif " " in new_hashtag:
            print("❌ Lỗi: Hashtag không được chứa khoảng trắng")
        elif len(new_hashtag) < 2:
            print("❌ Lỗi: Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
        elif not re.match(r"^#[A-Za-z0-9_]+$", new_hashtag):
            print("❌ Lỗi: Hashtag chỉ nên sử dụng chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #")
        else:
            print("✅ Hashtag hợp lệ")
            hashtags.append(new_hashtag)
            print(f"-> Danh sách hashtag hiện tại của video: {hashtags}")

    elif choice == 4:
        if not has_data:
            print("⚠️ Đại ka cần nhập dữ liệu ở Chức năng 1 trước!")
            continue

        search_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        if search_word in description:
            count_appear = description.count(search_word)
            description = description.replace(search_word, replace_word)
            print("\n--- KẾT QUẢ THAY THẾ ---")
            print(f"Số lần từ khóa \"{search_word}\" xuất hiện: {count_appear}")
            print(f"Mô tả video sau khi thay thế: {description}")
        else:
            print(f"❌ Không tìm thấy từ khóa \"{search_word}\" trong mô tả video.")

    elif choice == 5:
        print("Thoát chương trình")
        break