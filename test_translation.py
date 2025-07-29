#!/usr/bin/env python3
"""
Quick test script for the translation functionality
"""

import sys
sys.path.append('.')

# Import the translation function from our main script
from IBM_internship import translate

def test_translations():
    """Test the translation function with sample inputs"""
    
    test_cases = [
        ("Hello World", "en", "hi"),
        ("Good morning! How are you today?", "en", "fr"),
        ("Thank you very much for your help!", "en", "es"),
        ("How are you? I hope you're having a great day!", "en", "de"),
    ]
    
    print("🧪 Testing Translation Function")
    print("=" * 50)
    
    for text, src, tgt in test_cases:
        print(f"\n📝 Input: '{text}'")
        print(f"🔄 {src} → {tgt}")
        result = translate(text, src, tgt)
        print(f"📖 Output: {result}")
        print("-" * 30)

if __name__ == "__main__":
    test_translations()
