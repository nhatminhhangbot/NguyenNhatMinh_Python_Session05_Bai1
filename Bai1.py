# Cách duyệt trong đoạn code của thực tập sinh không gom dữ liệu theo từng chi nhánh
# Vì vòng lặp for month... ở ngoài, vòng lặp for branch... ở trong nên sẽ duyệt hết tháng 1 rồi chạy qua tất cả chi nhánh
# Sau đó mới chạy qua tháng 2 rồi chạy qua tất cả chi nhánh, như vậy sẽ không gom dữ liệu theo từng chi nhánh được
# Vòng lặp ngoài nên duyệt theo chi nhánh, vòng lặp trong nên duyệt theo tháng
# Code đúng:

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue = int(
            input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: ")
        )
        print(
            f"Chi nhánh {branch}, tháng {month}: "
            f"{revenue} triệu đồng"
        )