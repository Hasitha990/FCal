# Fabric Finishing Calculator - Android Mobile App

## Project Overview
A native Android mobile application built with Python and Kivy for fabric finishing calculations. The app works completely offline and provides professional fabric industry calculations.

## Purpose
This app helps fabric manufacturers calculate:
1. **Forward calculations**: Convert AD (After Dyeing) measurements to finished fabric specifications
2. **Reverse calculations**: Calculate required AD measurements from desired final specifications

## Current State
- ✅ Kivy mobile app implementation complete
- ✅ Both calculation modes implemented and tested
- ✅ Buildozer configuration ready for APK generation
- ✅ Input validation and error handling
- ⚠️ Cannot run on Replit (requires Android device or emulator)

## Technical Architecture

### Stack
- **Language**: Python 3.11
- **Framework**: Kivy 2.3 (cross-platform mobile framework)
- **Build Tool**: Buildozer (for APK packaging)
- **Target**: Android 5.0+ (API 21+)

### Project Structure
```
.
├── main.py              # Main Kivy application
├── buildozer.spec       # APK build configuration
├── README.md            # User documentation
└── .gitignore          # Git ignore rules
```

### Key Features Implemented
1. **Two-tab interface**: Forward and Reverse calculations
2. **Input validation**: Ensures valid ranges for all inputs
3. **Gum/Cut toggle**: Optional 4cm width adjustment
4. **Professional results**: 2 decimal precision display
5. **Mobile-optimized UI**: Scrollable layouts, touch-friendly inputs

### Calculation Logic

**Forward (AD → Finished)**:
- `Finished Width = AD Width × (1 + Width Shrinkage%/100) [- 4cm if Gum/Cut]`
- `Finished GSM = AD GSM / ((1 - Width Shrinkage%/100) × (1 - Length Shrinkage%/100))`

**Reverse (Finished → Required AD)**:
- `Required AD Width = Final Width × (1 + Width Shrinkage%/100) / (1 + Lab Width Shrinkage%/100) [adjusted for Gum/Cut]`
- `Required AD GSM = A/W GSM × ((1 - Width Shrinkage%/100) × (1 - Length Shrinkage%/100))`

## Building the APK

### Why Not Run on Replit?
Kivy apps require graphics libraries (OpenGL, SDL2) that aren't available in Replit's console environment. The app must be built as an APK and run on an Android device.

### Build Methods

**Option 1: GitHub Actions (Recommended)**
- Push code to GitHub
- GitHub Actions will automatically build the APK
- Download from Actions tab
- Free, reliable, no local setup needed

**Option 2: Local Build**
- Requires Linux machine with ~5GB storage
- Install Java, Android SDK/NDK
- Run: `buildozer android debug`
- APK generated in `bin/` folder

**Option 3: Google Colab**
- Free cloud build environment
- Upload project and run build commands
- Download APK directly

See README.md for detailed build instructions.

## Recent Changes
- 2025-11-11: Initial project creation
- 2025-11-11: Implemented complete Kivy mobile app
- 2025-11-11: Added buildozer configuration for APK generation
- 2025-11-11: Created comprehensive documentation

## User Preferences
- Target: Android mobile app for offline use
- Calculation logic: Based on provided Streamlit reference code
- No web interface needed - native mobile only

## Next Steps for User
1. Choose build method (GitHub Actions recommended)
2. Build the APK using instructions in README.md
3. Install APK on Android device
4. Test calculations with real fabric data
5. Distribute to team members as needed

## Notes
- The app requires no internet connection once installed
- All calculations are performed locally on the device
- Input validation prevents calculation errors
- Professional precision (2 decimal places) for industry use
