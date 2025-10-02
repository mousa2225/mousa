import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        oldPrice = float(old_price_entry.get())
        oldDays = float(old_days_entry.get())
        newPrice = float(new_price_entry.get())
        newDays = float(new_days_entry.get())
        usedOld = float(used_old_entry.get())
        usedNew = float(used_new_entry.get())
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال قيم صحيحة.")
        return

    oldRate = oldPrice / oldDays
    newRate = newPrice / newDays
    costOld = oldRate * usedOld
    costNew = newRate * usedNew
    total = costOld + costNew
    paid = oldPrice
    remain = paid - total
    remainText = "المتبقي للعميل" if remain >= 0 else "المتبقي على العميل"
    remainValue = abs(remain)

    result_text.set(
        f"سعر اليوم في الباقة السابقة: {oldRate:.2f} ريال\n"
        f"سعر اليوم في الباقة الجديدة: {newRate:.2f} ريال\n"
        f"التكلفة من الباقة السابقة: {costOld:.2f} ريال\n"
        f"التكلفة من الباقة الجديدة: {costNew:.2f} ريال\n"
        f"إجمالي التكلفة: {total:.2f} ريال\n"
        f"المبلغ المدفوع: {paid:.2f} ريال\n"
        f"{remainText}: {remainValue:.2f} ريال"
    )

root = tk.Tk()
root.title("حاسبة تحويل الباقات")

# قسم العميل (اختياري)
tk.Label(root, text="اسم العميل (اختياري)").grid(row=0, column=0, sticky="w")
client_name_entry = tk.Entry(root)
client_name_entry.grid(row=0, column=1)

tk.Label(root, text="رقم العميل (اختياري)").grid(row=1, column=0, sticky="w")
client_number_entry = tk.Entry(root)
client_number_entry.grid(row=1, column=1)

# الحقول الحسابية
tk.Label(root, text="سعر الباقة السابقة").grid(row=2, column=0, sticky="w")
old_price_entry = tk.Entry(root)
old_price_entry.grid(row=2, column=1)

tk.Label(root, text="عدد أيام الباقة السابقة").grid(row=3, column=0, sticky="w")
old_days_entry = tk.Entry(root)
old_days_entry.grid(row=3, column=1)

tk.Label(root, text="سعر الباقة الجديدة").grid(row=4, column=0, sticky="w")
new_price_entry = tk.Entry(root)
new_price_entry.grid(row=4, column=1)

tk.Label(root, text="عدد أيام الباقة الجديدة").grid(row=5, column=0, sticky="w")
new_days_entry = tk.Entry(root)
new_days_entry.grid(row=5, column=1)

tk.Label(root, text="الأيام المستخدمة من الباقة السابقة").grid(row=6, column=0, sticky="w")
used_old_entry = tk.Entry(root)
used_old_entry.grid(row=6, column=1)

tk.Label(root, text="الأيام المستخدمة من الباقة الجديدة").grid(row=7, column=0, sticky="w")
used_new_entry = tk.Entry(root)
used_new_entry.grid(row=7, column=1)

# زر الحساب
tk.Button(root, text="احسب", command=calculate, bg="#0288d1", fg="white").grid(row=8, column=0, columnspan=2, pady=10)

# عرض النتائج
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left", bg="#f1f8e9", width=50, height=10, anchor="nw").grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
