import re
from yazim_denetimi import check_spelling

def get_text():
    # Kullanıcıdan metin alıyoruz
    text = input("Lütfen bir metin girin: ")

    # Geçersiz karakterler kontrolü (sayilar, semboller)
    invalid_pattern = re.compile(r'[0-9!@#$%^&*(),.?":{}|<>]')
    if invalid_pattern.search(text):
        print("Geçersiz karakterler tespit edildi: Sayılar veya semboller kullanılamaz.")
        return None  # Geçersiz giriş yapıldığında metni döndürme

    return text

<<<<<<< HEAD
def save_output(original_text, corrected_text):
    # Çıktılar.txt dosyasına kaydetme işlemi
    with open("ciktilar.txt", "a") as file:
        file.write(f"Orijinal Metin: {original_text}\n")
        file.write(f"Düzeltilmiş Metin: {corrected_text}\n\n")
=======
def save_to_file(original_text, corrected_text):
    # Çıktıyı ciktilar.txt dosyasına kaydediyoruz
    with open("ciktilar.txt", "a") as file:
        file.write(f"Girilen Metin: {original_text}\n")
        file.write(f"Düzeltilmiş Metin: {corrected_text}\n\n")  # Her kayıt sonrası bir boş satır bırakıyoruz
>>>>>>> 721f600ae03532459afa46333adc1e0aad43ef1b

def main():
    text = get_text()
    if text is None:
        return  # Geçersiz metin olduğunda programdan çık

    # Yazım hatalarını kontrol ediyoruz
    corrected_text = check_spelling(text)

    # Düzeltilmiş metni ekrana yazdırıyoruz
    print("\nDüzeltilmiş Metin:")
    print(corrected_text)

<<<<<<< HEAD
    # Çıktıları dosyaya kaydediyoruz
    save_output(text, corrected_text)
=======
    # Kullanıcının girdiği ve düzeltilmiş metni dosyaya kaydediyoruz
    save_to_file(text, corrected_text)
>>>>>>> 721f600ae03532459afa46333adc1e0aad43ef1b

if __name__ == "__main__":
    main()
