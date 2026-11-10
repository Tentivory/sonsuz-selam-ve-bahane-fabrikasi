#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Selam ve Bahane Fabrikası
Gerçekten çalışır. Gerçekten yavaştır. Gerçekten saçmadır.
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.15):
    """Harf harf yavaşça yazar. Abartılı yavaş."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def selam_ver():
    selamlar = [
        "Meeeeerhaaaaaabaaaaaa...",
        "Selamlar, bu selam bilerek uzatıldı...",
        "Hoş geldiniz, kapı zili çalıyor ama kimse açmıyor...",
        "Merhaba, bu selam 12 saniye sürdü çünkü öyle istedim."
    ]
    secilen = random.choice(selamlar)
    print("\n=== SELAM BÖLÜMÜ ===")
    yavas_yaz(secilen, 0.12)

def bahane_uret():
    bahaneler = [
        "Trafik vardı ama aslında yoktu, sadece atomlarım geç kaldı.",
        "Uyumadım çünkü yastık bana küs.",
        "Saat durdu. Saatimin içindeki zaman da durdu.",
        "Bir kedi yolu kesti ve felsefi bir konuşma başlattı.",
        "Evrenin genişlemesi yüzünden mesafe arttı.",
        "Kahve bitti. Kahve bitince her şey biter."
    ]
    print("\n=== BAHANE BÖLÜMÜ ===")
    bahane = random.choice(bahaneler)
    yavas_yaz("Bahane: " + bahane, 0.08)

def main():
    print("Sonsuz Selam ve Bahane Fabrikası başlatılıyor...")
    print("(Bu süreç bilerek yavaştır. Sabırlı olun.)")
    time.sleep(1.5)
    
    selam_ver()
    time.sleep(1)
    bahane_uret()
    
    print("\n--- İşlem tamamlandı. Hiçbir şey değişmedi. ---")
    # gizli not: bazen sistemler de geç kalır ve kimse fark etmez

if __name__ == "__main__":
    main()
