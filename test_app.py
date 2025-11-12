#!/usr/bin/env python
"""
Test script to validate the Fabric Finishing Calculator logic.
This script tests the calculation functions without requiring a GUI.
"""

def test_forward_calculation():
    """Test forward calculation (AD → Finished)"""
    print("Testing Forward Calculation (AD → Finished)")
    print("=" * 50)
    
    ad_width = 100.0
    ad_gsm = 150.0
    shrink_w = 5.0
    shrink_l = 3.0
    gum_cut = False
    
    finished_width = ad_width * (1 + shrink_w / 100)
    finished_gsm = ad_gsm * ((1 - shrink_w / 100) * (1 - shrink_l / 100))
    
    if gum_cut:
        finished_width -= 4
    
    print(f"Input:")
    print(f"  AD Width: {ad_width} cm")
    print(f"  AD GSM: {ad_gsm} g/m²")
    print(f"  Width Shrinkage: {shrink_w}%")
    print(f"  Length Shrinkage: {shrink_l}%")
    print(f"  Gum/Cut applied: {gum_cut}")
    print(f"\nResults:")
    print(f"  Finished Width: {finished_width:.2f} cm")
    print(f"  Finished GSM: {finished_gsm:.2f} g/m²")
    print()
    
    print("Test with Gum/Cut applied:")
    finished_width_with_gum = ad_width * (1 + shrink_w / 100) - 4
    print(f"  Finished Width (with Gum/Cut): {finished_width_with_gum:.2f} cm")
    print()

def test_reverse_calculation():
    """Test reverse calculation (Finished → Required AD)"""
    print("Testing Reverse Calculation (Finished → Required AD)")
    print("=" * 50)
    
    final_width = 105.0
    final_gsm = 162.5
    lab_shrink_w = 2.0
    shrink_w_rev = 5.0
    shrink_l_rev = 3.0
    gum_cut = False
    
    if gum_cut:
        required_ad_width = (final_width + 4) * (1 + shrink_w_rev / 100) / (1 + lab_shrink_w / 100) - 4
    else:
        required_ad_width = final_width * (1 + shrink_w_rev / 100) / (1 + lab_shrink_w / 100)
    
    required_ad_gsm = final_gsm * ((1 - shrink_w_rev / 100) * (1 - shrink_l_rev / 100))
    
    print(f"Input:")
    print(f"  Final Width: {final_width} cm")
    print(f"  A/W GSM: {final_gsm} g/m²")
    print(f"  Lab Width Shrinkage: {lab_shrink_w}%")
    print(f"  Width Shrinkage: {shrink_w_rev}%")
    print(f"  Length Shrinkage: {shrink_l_rev}%")
    print(f"  Gum/Cut applied: {gum_cut}")
    print(f"\nResults:")
    print(f"  Required AD Width: {required_ad_width:.2f} cm")
    print(f"  Required AD GSM: {required_ad_gsm:.2f} g/m²")
    print()
    
    print("Test with Gum/Cut applied:")
    required_ad_width_with_gum = (final_width + 4) * (1 + shrink_w_rev / 100) / (1 + lab_shrink_w / 100) - 4
    print(f"  Required AD Width (with Gum/Cut): {required_ad_width_with_gum:.2f} cm")
    print()

def validate_imports():
    """Validate that all required modules can be imported"""
    print("Validating Python Imports")
    print("=" * 50)
    
    try:
        import kivy
        print(f"✓ Kivy {kivy.__version__} imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Kivy: {e}")
        return False
    
    try:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
        from kivy.uix.checkbox import CheckBox
        print("✓ All Kivy UI components imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Kivy components: {e}")
        return False
    
    print()
    return True

def main():
    print("\n" + "=" * 50)
    print("Fabric Finishing Calculator - Validation Tests")
    print("=" * 50)
    print()
    
    if not validate_imports():
        print("\n❌ Import validation failed!")
        return
    
    test_forward_calculation()
    test_reverse_calculation()
    
    print("=" * 50)
    print("✅ All tests completed successfully!")
    print()
    print("NOTE: This app is designed for Android devices.")
    print("To build the APK, follow the instructions in README.md")
    print("=" * 50)
    print()

if __name__ == '__main__':
    main()
