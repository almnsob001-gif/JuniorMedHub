[app]

title = JuniorMed Hub
package.name = juniormedhub
package.domain = com.juniormedhub

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf
source.exclude_dirs = tests,bin,.github,.git,venv

version = 0.1.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 34
android.minapi = 23
android.archs = arm64-v8a
android.allow_backup = False
android.accept_sdk_license = True

android.debug_artifact = apk
android.release_artifact = aab

[buildozer]
log_level = 2
warn_on_root = 1
