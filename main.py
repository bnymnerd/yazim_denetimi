from yazim_denetimi import check_spelling


def get_text():
    # Kullanıcıdan metin alıyoruz
    text = input("Lütfen bir metin girin: ")
    return text


def main():
    # Kullanıcıdan metin alıyoruz
    text = get_text()

    # Yazım hatalarını kontrol ediyoruz
    corrected_text = check_spelling(text)

    print("\nDüzeltilmiş Metin:")
    print(corrected_text)


if __name__ == "__main__":
    main()
