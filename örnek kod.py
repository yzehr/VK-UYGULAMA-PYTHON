import tkinter as tk  # tkinter kütüphanesini içe aktarır

window = tk.Tk()  # Ana pencere oluşturuluyor
window.title('BMI Calculator')  # Pencere başlığı ayarlanıyor
window.minsize(200, 300)  # Pencere minimum boyutu ayarlanıyor
window.config(pady=30, padx=30)  # Pencere kenar boşlukları ayarlanıyor

FONT = ('Arial', 10, 'italic')  # Yazı fontu tanımlanıyor

weight_label = tk.Label(text='Enter Your Weight (kg)', font=FONT)  # Ağırlık etiketi oluşturuluyor
weight_label.pack()  # Ağırlık etiketi pencereye ekleniyor
weight_label.config(padx=15, pady=15)  # Ağırlık etiketi kenar boşlukları ayarlanıyor

weight_entry = tk.Entry(width=15)  # Ağırlık giriş kutusu oluşturuluyor
weight_entry.pack()  # Ağırlık giriş kutusu pencereye ekleniyor

height_label = tk.Label(text='Enter Your Height (cm)', font=FONT)  # Boy etiketi oluşturuluyor
height_label.pack()  # Boy etiketi pencereye ekleniyor
height_label.config(padx=15, pady=15)  # Boy etiketi kenar boşlukları ayarlanıyor

height_entry = tk.Entry(width=15)  # Boy giriş kutusu oluşturuluyor
height_entry.pack()  # Boy giriş kutusu pencereye ekleniyor

# BMI hesaplama fonksiyonu tanımlanıyor
def calculate_bmi():
    weight = float(weight_entry.get())  # Ağırlık değeri alınıyor
    height = float(height_entry.get())  # Boy değeri alınıyor

    global result_label  # result_label değişkeni global olarak tanımlanıyor
    if weight == "" or height == "":  # Eğer ağırlık veya boy değeri boşsa
        result_label.config(text='Please enter weight and height values!')  # Uyarı mesajı gösteriliyor
    else:  # Ağırlık ve boy değeri girilmişse
        try:  # Hesaplama yapılıyor
            bmi_result = weight / (height / 100) ** 2  # BMI hesaplanıyor
            result_text = f'Your BMI is: {round(bmi_result, 2)}. You are'  # BMI sonucu metni oluşturuluyor
            if bmi_result < 18.5:  # BMI değerine göre uygun mesaj gösteriliyor
                result_label.config(text=f'{result_text} under weight.')
            elif 18.5 < bmi_result < 24.9:
                result_label.config(text=f'{result_text} normal weight.')
            elif 25 < bmi_result < 29.9:
                result_label.config(text=f'{result_text} over weight.')
            elif 30 < bmi_result < 34.9:
                result_label.config(text=f'{result_text} obesity (Class 1).')
            elif 35 < bmi_result < 39.9:
                result_label.config(text=f'{result_text} obesity (Class 2).')
            else:
                result_label.config(text=f'{result_text} extreme obesity.')
        except:  # Hesaplama hatası olursa
            result_label.config(text='Enter a valid number')  # Hata mesajı gösteriliyor

# Hesapla düğmesi oluşturuluyor
calculate_button = tk.Button(text='Calculate', command=calculate_bmi)
calculate_button.pack()  # Hesapla düğmesi pencereye ekleniyor

result_label = tk.Label()  # Sonuç etiketi oluşturuluyor
result_label.pack()  # Sonuç etiketi pencereye ekleniyor

window.mainloop()  # Pencere olay döngüsü başlatılıyor
