[app]

# Uygulama adı ve paket bilgileri
title = Kisisel Panelim
package.name = kisiselpanelim
package.domain = org.kullanici

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Gerekli Python kütüphaneleri (ileride ekleyeceklerimizi buraya virgülle ekleyeceğiz)
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android izinleri (şimdilik gerek yok, ileride ör. dosya kaydetme eklersen buraya eklenir)
android.permissions =

# Android API / SDK ayarları (Buildozer varsayılanları kullanır, genelde dokunmaya gerek yok)
android.api = 34
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
