menu = '''
+=================================================+
|      HỆ THỐNG QUẢN LÝ NỘI DUNG SHOPEE           |
+=================================================+
|  1. Nhập và thống kê thông tin sản phẩm         |
|  2. Chuẩn hóa tên Shop                          |
|  3. Kiểm tra tính hợp lệ của mã giảm giá        |
|  4. Tìm kiếm và thay thế từ khóa trong mô tả    |
|  5. Thoát chương trình                          |
+=================================================+
'''

list_discount = ""

while True:
    print(menu)
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Vui lòng nhập số nguyên")
        continue
        
    match choice:
        case 1:
            while True:
                shop_name = input("Tên shop: ").strip()
                if shop_name.strip() == "":
                    print("Tên shop không được bỏ trống")
                else:
                    break
                    
            product_name = input("Tên sản phẩm: ").strip().title()
            
            while True:
                description = input("Mô tả sản phẩm: ").strip()
                if description.strip() == "":
                    print("Mô tả sản phẩm không được rỗng")
                else:
                    break
                    
            category = input("Danh mục sản phẩm: ").strip()
            
            keywords = input("Danh sách từ khóa tìm kiếm, cách nhau bởi dấu phẩy: ")
            list_keyword = keywords.split(",")
            list_temp = []
            for keyword in list_keyword:
                keyword = keyword.strip()
                list_temp.append(keyword)
            list_keyword_str = ", ".join(list_temp)
            
            print()
            print("=" * 50)
            print(f"Tên shop: {shop_name}")
            print(f"Tên sản phẩm: {product_name}")
            print(f"Mô tả: {description}")
            print(f"Độ dài mô tả sản phẩm: {len(description)} ký tự")
            print(f"Danh mục sản phẩm: {category.lower()}")
            print(f"Danh sách từ khóa: {list_keyword_str}")
            
            if keywords.strip() == "":
                print("Số lượng từ khóa tìm kiếm: 0")
            else:
                print(f"Số lượng từ khóa tìm kiếm: {len(list_keyword_str.split(', '))}")
                
            print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ thường: {description.lower()}")
            print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa: {description.upper()}")
            print("=" * 50)
            
        case 2: 
            print(f"Tên shop ban đầu: {shop_name}")
            shop_name_normalized = shop_name.lower().replace(" ", "-")
            if not shop_name_normalized.startswith("shop-"):
                shop_name_normalized = "shop-" + shop_name_normalized
            print(f"Tên shop sau khi được chuẩn hoá: {shop_name_normalized}")
        
        case 3:
            input_code = input("Hãy nhập một mã giảm giá: ")
            is_true = False
            
            if input_code.strip() == "":
                print("Mã giảm giá không được rỗng")
            elif " " in input_code:
                print("Mã giảm giá không được chứa khoảng trắng")
            elif len(input_code) < 6 or len(input_code) > 12:
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif not input_code.isupper():
                print("Mã giảm giá phải được viết hoa toàn bộ")
            elif not input_code.isalnum():
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
            elif not input_code.startswith("SALE"):
                print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")
            else:
                if list_discount == "":
                    list_discount = input_code
                else:
                    list_discount += ", " + input_code
                is_true = True
            
            if is_true == True:
                print("Mã giảm giá hợp lệ")
                print(list_discount)
                
        case 4:
            keyword_search = input("Từ khóa cần tìm: ")
            keyword_replace = input("Từ khóa thay thế: ")
            
            count_keyword = 0
            
            for word in description.split(" "):
                if word == keyword_search:
                    count_keyword += 1
            
            if count_keyword > 0:
                description = description.replace(keyword_search, keyword_replace)
                print("Đã thay đổi mô tả")
                print(description)
                print(f"Số lần xuất hiện của từ khóa: {count_keyword}")
            else:
                print(f"Không tìm thấy {keyword_search} trong mô tả")
            
        case 5: 
            print("Thoát chương trình")
            break
        
        case _:
            print("Hãy nhập từ 1-5!!!!!")