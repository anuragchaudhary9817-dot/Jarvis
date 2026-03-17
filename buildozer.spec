[app]
title = Jarvis AI
package.name = jarvis_boss
package.domain = boss.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius
orientation = portrait
android.archs = arm64-v8a
android.accept_sdk_license = True
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
[buildozer]
log_level = 2
