# 36 전화번호 목록
def solution_36(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book) -1):
        before = phone_book[idx]
        after = phone_book[idx + 1]
        if(after.startswith(before)):
            return False
    return True
phone_book = ["119", "97674223", "1195524421"]
print(solution_36(phone_book))  # false