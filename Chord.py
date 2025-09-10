from math import pow

def nut_ke_tiep(ds_nut, x, m):
    """
    Trả về nút nhỏ nhất >= x (theo modulo 2^m)
    """
    ds_nut_sap = sorted(ds_nut)
    for n in ds_nut_sap:
        if n >= x:
            return n
    # nếu không có nút nào >= x thì quay vòng lấy nút đầu tiên
    return ds_nut_sap[0]

def tao_bang_ngon_tay(nut, ds_nut, m):
    """
    Tạo bảng ngón tay (finger table) cho 1 nút
    Kết quả: danh sách các bộ (i, bat_dau, nut_ke_tiep)
    """
    bang = []
    khong_gian = 2 ** m
    for i in range(1, m + 1):
        bat_dau = (nut + 2 ** (i - 1)) % khong_gian
        ke_tiep = nut_ke_tiep(ds_nut, bat_dau, m)
        bang.append((i, bat_dau, ke_tiep))
    return bang

def tao_bang_cho_tat_ca(ds_nut, m):
    """
    Tạo bảng ngón tay cho toàn bộ các nút trong vòng Chord
    """
    tat_ca_bang = {}
    for n in sorted(ds_nut):
        tat_ca_bang[n] = tao_bang_ngon_tay(n, ds_nut, m)
    return tat_ca_bang

def in_bang_ngon_tay(cac_bang, m):
    """
    In bảng ngón tay cho từng nút
    """
    khong_gian = 2 ** m
    for nut in sorted(cac_bang.keys()):
        print(f"Nút {nut} (m={m}, ID 0..{khong_gian-1}):")
        print(" i | bắt đầu | nút kế tiếp")
        print("---+---------+-------------")
        for (i, bat_dau, ke_tiep) in cac_bang[nut]:
            print(f"{i:2d} | {bat_dau:7d} | {ke_tiep:11d}")
        print("")

# ----------------- Chạy thử -----------------
m = 4
cac_nut_ban_dau = [1, 5, 9, 12]

print("Các nút ban đầu của vòng Chord:", cac_nut_ban_dau)
bang_ban_dau = tao_bang_cho_tat_ca(cac_nut_ban_dau, m)
print("\nBảng ngón tay cho các nút ban đầu:\n")
in_bang_ngon_tay(bang_ban_dau, m)

# Thêm nút 6
nut_moi = 6
cac_nut_sau_them = sorted(cac_nut_ban_dau + [nut_moi])
print("Thêm nút:", nut_moi)
bang_sau_them = tao_bang_cho_tat_ca(cac_nut_sau_them, m)
print("\nBảng ngón tay sau khi thêm nút 6:\n")
in_bang_ngon_tay(bang_sau_them, m)
