from yazim_denetimi import check_spelling

def get_text():
    # Kullanıcıdan metin alıyoruz
    text = input("Lütfen bir metin girin: ")
    return text

def save_to_file(original_text, corrected_text):
    # Çıktıyı ciktilar.txt dosyasına kaydediyoruz
    with open("ciktilar.txt", "a") as file:
        file.write(f"Girilen Metin: {original_text}\n")
        file.write(f"Düzeltilmiş Metin: {corrected_text}\n\n")  # Her kayıt sonrası bir boş satır bırakıyoruz

def main():
    # Kullanıcıdan metin alıyoruz
    text = get_text()

    # Yazım hatalarını kontrol ediyoruz
    corrected_text = check_spelling(text)

    # Düzeltilmiş metni ekrana yazdırıyoruz
    print("\nDüzeltilmiş Metin:")
    print(corrected_text)

    # Kullanıcının girdiği ve düzeltilmiş metni dosyaya kaydediyoruz
    save_to_file(text, corrected_text)

if __name__ == "__main__":
    main()
