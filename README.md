# Fabric Finishing Calculator

A native Android mobile application for fabric finishing calculations. This app works completely offline and provides two calculation modes:

## Features

- **Forward Calculation (AD → Finished)**: Calculate finished fabric dimensions from after-dyeing (AD) measurements
- **Reverse Calculation (Finished → Required AD)**: Calculate required AD dimensions from desired final specifications
- **Gum/Cut Adjustment**: Optional 4cm width adjustment for both calculation modes
- **Input Validation**: Ensures all values are within acceptable ranges
- **Professional Results**: Displays calculations with 2 decimal precision

## Calculation Logic

### Forward Calculation
Converts AD (After Dyeing) measurements to finished fabric specifications:
- `Finished Width = AD Width × (1 + Width Shrinkage%/100) [- 4cm if Gum/Cut applied]`
- `Finished GSM = AD GSM / ((1 - Width Shrinkage%/100) × (1 - Length Shrinkage%/100))`

### Reverse Calculation
Calculates required AD measurements from desired final specifications:
- `Required AD Width = Final Width × (1 + Width Shrinkage%/100) / (1 + Lab Width Shrinkage%/100) [adjusted for Gum/Cut]`
- `Required AD GSM = A/W GSM × ((1 - Width Shrinkage%/100) × (1 - Length Shrinkage%/100))`

## Testing on Replit

**Note**: The Kivy GUI app requires graphics libraries (OpenGL/SDL2) that are not available in Replit's console environment. The app is designed to run on Android devices after being built as an APK.

To validate the calculation logic on Replit, use the test script:
```bash
python test_app.py
```

This will verify that all calculations are working correctly without requiring a GUI.

## Building APK for Android

### Prerequisites
- Linux environment (Ubuntu/Debian recommended)
- Java Development Kit (JDK 17)
- Android SDK and NDK (~5GB of storage required)

### Method 1: Local Build (Recommended)

1. **Install System Dependencies**:
```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk wget \
    autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

2. **Install Python Dependencies**:
```bash
pip install buildozer cython
```

3. **Initialize Buildozer** (first time only):
```bash
buildozer init
```

4. **Build Debug APK**:
```bash
buildozer android debug
```

The APK will be generated in the `bin/` directory as `fabriccalculator-1.0-arm64-v8a-debug.apk`

5. **Install on Android Device**:
- Copy the APK to your Android device
- Enable "Install from Unknown Sources" in Settings
- Open the APK file to install

### Method 2: GitHub Actions (Cloud Build)

Create `.github/workflows/build-apk.yml`:

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer android debug
          buildozer_version: stable
      
      - name: Upload APK
        uses: actions/upload-artifact@v3
        with:
          name: fabric-calculator-apk
          path: bin/*.apk
```

Push to GitHub and the APK will build automatically. Download from the Actions tab.

### Method 3: Google Colab (Free Cloud Build)

1. Open [Google Colab](https://colab.research.google.com/)
2. Create a new notebook and run:

```python
# Install dependencies
!sudo apt update
!sudo apt install -y openjdk-17-jdk wget unzip
!pip install buildozer cython

# Clone your repository
!git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
%cd YOUR_REPO

# Build APK
!buildozer android debug

# Download the APK
from google.colab import files
!ls -la bin/
files.download('bin/fabriccalculator-1.0-arm64-v8a-debug.apk')
```

## Project Structure

```
.
├── main.py              # Main Kivy application
├── buildozer.spec       # APK build configuration
├── README.md            # This file
└── bin/                 # Generated APK files (after build)
```

## Troubleshooting

### Build Issues

**Problem**: Storage limitations on Replit  
**Solution**: Use GitHub Actions or Google Colab for building (both have better storage)

**Problem**: App crashes on launch  
**Solution**: Make sure you've built with correct architecture (arm64-v8a or armeabi-v7a)

**Problem**: Missing dependencies  
**Solution**: Check that all requirements are listed in `buildozer.spec`

### App Usage

- All input fields accept decimal numbers
- Shrinkage percentages must be between 0-50%
- Width and GSM values must be positive
- Check the "Gum or Cut applied?" checkbox to apply 4cm width adjustment

## Technologies Used

- **Python 3.11**: Core programming language
- **Kivy 2.3**: Cross-platform mobile framework
- **Buildozer**: APK packaging tool for Android
- **Cython**: Python to C compiler (for performance)

## License

This project is open source and available for fabric industry professionals.

## Support

For issues or questions about the calculations, please refer to your fabric finishing specifications or consult with your technical team.
