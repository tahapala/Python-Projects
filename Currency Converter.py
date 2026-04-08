import requests

CURRENCIES = {
    "USD": "Amerikan Doları",
    "EUR": "Euro",
    "TRY": "Türk Lirası",
    "GBP": "İngiliz Sterlini",
    "JPY": "Japon Yeni",
    "CHF": "İsviçre Frangı",
    "CAD": "Kanada Doları",
    "AUD": "Avustralya Doları",
    "CNY": "Çin Yuanı",
    "INR": "Hint Rupisi",
    "SAR": "Suudi Riyali",
    "AED": "BAE Dirhemi",
    "RUB": "Rus Rublesi",
    "BRL": "Brezilya Reali",
    "KRW": "Güney Kore Wonu",
    "MXN": "Meksika Pesosu",
    "SGD": "Singapur Doları",
    "NOK": "Norveç Kronu",
    "SEK": "İsveç Kronu",
    "PLN": "Polonya Zlotisi",
}

def kur_getir(baz="USD"):
    url = f"https://api.frankfurter.app/latest?base={baz}"
    response = requests.get(url, timeout=10)
    data = response.json()
    return data["rates"], data["date"]

def para_birimi_sec(mesaj):
    print(f"\n{mesaj}")
    kodlar = list(CURRENCIES.keys())
    for i, kod in enumerate(kodlar):
        print(f"  {i+1:2}. {kod} — {CURRENCIES[kod]}")
    while True:
        secim = input("\nNumara veya kod girin: ").strip().upper()
        if secim in CURRENCIES:
            return secim
        if secim.isdigit() and 1 <= int(secim) <= len(kodlar):
            return kodlar[int(secim) - 1]
        print("Geçersiz seçim, tekrar deneyin.")

def main():
    print("=" * 50)
    print("       DÖVIZ DÖNÜŞTÜRÜCÜ")
    print("=" * 50)

    kaynak = para_birimi_sec("Kaynak para birimini seçin:")
    hedef = para_birimi_sec("Hedef para birimini seçin:")

    while True:
        miktar_str = input(f"\nDönüştürülecek miktar ({kaynak}): ").strip()
        try:
            miktar = float(miktar_str)
            break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    print("\nKurlar alınıyor...")
    rates, tarih = kur_getir(baz=kaynak)

    if hedef == kaynak:
        sonuc = miktar
    elif hedef in rates:
        sonuc = miktar * rates[hedef]
    else:
        print("Bu para birimi için kur bulunamadı.")
        return

    print("\n" + "=" * 50)
    print(f"  {miktar:,.4f} {kaynak}  →  {sonuc:,.4f} {hedef}")
    print(f"  1 {kaynak} = {rates.get(hedef, 1):,.4f} {hedef}")
    print(f"  Tarih: {tarih}")
    print("=" * 50)

    print("\nTüm para birimlerine karşılıklar:")
    print("-" * 40)
    for kod, isim in CURRENCIES.items():
        if kod == kaynak:
            continue
        if kod in rates:
            deger = miktar * rates[kod]
            print(f"  {kod:4} ({isim:25}): {deger:>14,.4f}")

    print("\nTekrar dönüştürmek ister misin?")
    while input("(e/h): ").strip().lower() == "e":
        main()

if __name__ == "__main__":
    main()