[app]

# (str) Title of your application
title = Fabric Calculator

# (str) Package name
package.name = fcal

# (str) Package domain (reverse domain style)
package.domain = org.hasitha

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 1.0

# (str) Application icon
icon.filename = icon.png

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (str) The main .py file
main.py = main.py

# (list) Application requirements
requirements = python3==3.11.7,kivy==2.3.1

# (str) Presplash image
presplash.filename = presplash.png

# (str) Supported Android API
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a

# (bool) Use latest python-for-android master branch to fix build issues
p4a.branch = master

# (bool) Debug mode
log_level = 2
# (bool) Android permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (str) Packaging format
android.release_artifact = apk

# (bool) Enable accelerated graphics
android.hardware_acceleration = true

# (str) Android package format
android.packaging = apk

[buildozer]

# (int) Number of concurrent jobs for building (optional)
jobs = 4

# (str) Build directory
build_dir = .buildozer

# (bool) Clean build before compilation
clean_build = True
