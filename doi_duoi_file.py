import os

def doi_duoi_tat_ca_file_thanh_webp(thu_muc):
    if not os.path.isdir(thu_muc):
        print("❌ Thư mục không tồn tại.")
        return

    danh_sach_file = [f for f in os.listdir(thu_muc) if os.path.isfile(os.path.join(thu_muc, f))]

    if not danh_sach_file:
        print("⚠️ Không có file nào trong thư mục.")
        return

    so_file_doi = 0

    for ten_file in danh_sach_file:
        duong_dan_cu = os.path.join(thu_muc, ten_file)

        # Tách tên gốc và đuôi hiện tại
        ten_goc, _ = os.path.splitext(ten_file)
        ten_moi = ten_goc + ".webp"
        duong_dan_moi = os.path.join(thu_muc, ten_moi)

        # Nếu file mới đã tồn tại, thêm hậu tố tránh trùng
        if os.path.exists(duong_dan_moi):
            i = 1
            while os.path.exists(os.path.join(thu_muc, f"{ten_goc}_{i}.webp")):
                i += 1
            ten_moi = f"{ten_goc}_{i}.webp"
            duong_dan_moi = os.path.join(thu_muc, ten_moi)

        try:
            os.rename(duong_dan_cu, duong_dan_moi)
            print(f"✅ Đã đổi: {ten_file} → {ten_moi}")
            so_file_doi += 1
        except Exception as e:
            print(f"❌ Không thể đổi: {ten_file} → Lỗi: {e}")

    print(f"\n🎉 Đã đổi đuôi cho {so_file_doi} file.")

if __name__ == "__main__":
    thu_muc = input("📂 Nhập đường dẫn thư mục: ").strip('"')
    doi_duoi_tat_ca_file_thanh_webp(thu_muc)
