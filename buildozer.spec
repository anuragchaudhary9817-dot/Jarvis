[app]
title = Jarvis AI
package.name = jarvis_boss
package.domain = boss.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Simplified requirements for stability
requirements = python3,kivy,kivymd,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# Android Stable Config
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, RECORD_AUDIO

[buildozer]
log_level = 2
warn_on_root = 1
