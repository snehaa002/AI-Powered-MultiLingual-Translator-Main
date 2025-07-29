#!/usr/bin/env python3
"""
Test specific problematic translation
"""

import sys
sys.path.append('.')

from IBM_internship import translate

def test_specific_case():
    """Test the specific case that was failing"""
    
    text = "How are you? I hope you're having a great day!"
    src = "en"
    tgt = "hi"
    
    print("🧪 Testing Specific Problematic Case")
    print("=" * 50)
    print(f"📝 Input: '{text}'")
    print(f"🔄 {src} → {tgt}")
    
    result = translate(text, src, tgt)
    print(f"📖 Output: {result}")

if __name__ == "__main__":
    test_specific_case()
