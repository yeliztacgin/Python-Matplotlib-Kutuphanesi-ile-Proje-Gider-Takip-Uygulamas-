import matplotlib.pyplot as plt

def main():
    giderAdlari = []
    giderTutarlari = []
    print("Proje Gider Takip Uygulaması")
    print("--------------------------------")

    while True:
        giderAd = input("Gider adı (çıkmak için 0 yazın): ")
        
        if giderAd == '0':  # giderAd'ı kontrol et
            break
        
        # Gider tutarını al ve listeye ekle
        giderTutar = float(input(f"{giderAd} için gider tutarını girin: "))
        giderAdlari.append(giderAd)
        giderTutarlari.append(giderTutar)

    toplam = sum(giderTutarlari)  # Toplam gideri hesapla
    print(f"\nToplam Gider: {toplam:.2f} TL")

    # Grafik oluşturma
    plt.figure(figsize=(10, 6)) 
    plt.bar(giderAdlari, giderTutarlari, color='orange')  
    plt.title('Proje Giderleri') 
    plt.xlabel('Gider Adları')
    plt.ylabel('Tutar (TL)')  
    plt.grid(axis='y') 
    plt.xticks(rotation=45)  
    plt.tight_layout() 
    plt.show() 

if __name__ == "__main__":
    main()
