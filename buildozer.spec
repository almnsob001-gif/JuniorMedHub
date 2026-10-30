[app]
title = JuniorMed Hub
package.name = juniormedhub
package.domain = com.juniormedhub
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,txt

# تفعيل الأيقونة الجديدة
icon.filename = %(source.dir)s/assets/icon.png

version = 0.1.0 

requirements = python3==3.10.12,hostpython3==3.10.12,kivy==2.3.0,kivymd==1.2.0,cython==0.29.34,pillow,requests

android.permissions = INTERNET
android.accept_sdk_license = True
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.orientation = portrait 

[buildozer]
warn_on_root = 0
