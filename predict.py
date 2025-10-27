#!/usr/bin/env python3
"""
Local prediction script for Egyptian Art Analyzer.
Usage: python predict.py <IMAGE_PATH> [--speed fast|regular|super-fast] [--type tomb|temple|other|unknown]
"""

import sys
import os
import base64
import json
import argparse
from pathlib import Path
from dotenv import load_dotenv

from src.gemini_strategy import analyze_egyptian_art_with_gemini


def load_env_file():
    """Load environment variables from env.local file if it exists."""
    env_file = Path(__file__).parent / 'env.local'
    if env_file.exists():
        load_dotenv(env_file)
        return True
    return False


def load_image_as_base64(image_path):
    """Load an image file and convert it to base64."""
    with open(image_path, 'rb') as f:
        image_data = f.read()
    return base64.b64encode(image_data).decode('utf-8')


def print_analysis(result):
    """Pretty print the analysis results."""
    if result.get("failure_status") == "success":
        analysis = result["analysis"]
        
        print("\n" + "="*80)
        print("EGYPTIAN ART ANALYSIS RESULTS")
        print("="*80)
        
        print(f"\n📍 LOCATION:")
        print(f"   {analysis.get('picture_location', 'Unknown')}")
        
        print(f"\n📅 HISTORICAL PERIOD:")
        print(f"   {analysis.get('date', 'Unknown')}")
        
        print(f"\n🔤 ANCIENT TEXT TRANSLATION:")
        translation = analysis.get('ancient_text_translation', 'No text detected')
        for line in translation.split('\n'):
            print(f"   {line}")
        
        characters = analysis.get('characters', [])
        if characters:
            print(f"\n👥 CHARACTERS IDENTIFIED ({len(characters)}):")
            for i, char in enumerate(characters, 1):
                print(f"\n   {i}. {char.get('character_name', 'Unknown')}")
                print(f"      Location: {char.get('location', 'Not specified')}")
                print(f"      Reasoning: {char.get('reasoning', 'N/A')}")
                print(f"      Description: {char.get('description', 'N/A')}")
        
        print(f"\n🔍 INTERESTING DETAIL:")
        detail = analysis.get('interesting_detail', 'None noted')
        for line in detail.split('\n'):
            print(f"   {line}")
        
        print(f"\n⏱️  PROCESSING TIME:")
        print(f"   {result.get('api_call_duration', 0):.2f} seconds")
        
        print("\n" + "="*80 + "\n")
        
    else:
        print("\n" + "="*80)
        print("ANALYSIS FAILED")
        print("="*80)
        print(f"\nError: {result.get('failure_reason', 'Unknown error')}")
        if 'traceback' in result:
            print(f"\nTraceback:\n{result['traceback']}")
        print("\n" + "="*80 + "\n")


def main():
    load_env_file()
    
    parser = argparse.ArgumentParser(
        description='Analyze Egyptian art images using Gemini AI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python predict.py data/sample-egyptian-images/VoK.jpg
  python predict.py data/sample-egyptian-images/VoK2.jpg --speed regular --type tomb
  python predict.py ~/my-photo.jpg --speed fast
        """
    )
    
    parser.add_argument('image_path', type=str, help='Path to the Egyptian art image')
    parser.add_argument('--speed', type=str, default='fast', 
                       choices=['fast', 'regular', 'super-fast'],
                       help='Analysis speed (default: fast)')
    parser.add_argument('--type', type=str, default='unknown',
                       choices=['tomb', 'temple', 'other', 'unknown'],
                       help='Type of Egyptian art (default: unknown)')
    parser.add_argument('--json', action='store_true',
                       help='Output raw JSON instead of formatted text')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.image_path):
        print(f"Error: Image file not found: {args.image_path}")
        sys.exit(1)
    
    api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: No Google API key found!")
        print("Please set GOOGLE_API_KEY in env.local file or as environment variable.")
        sys.exit(1)
    
    print(f"\nAnalyzing image: {args.image_path}")
    print(f"Speed: {args.speed}, Type hint: {args.type}")
    print("Please wait...\n")
    
    try:
        image_base64 = load_image_as_base64(args.image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)
    
    result = analyze_egyptian_art_with_gemini(
        image_data=image_base64,
        speed=args.speed,
        image_type=args.type
    )
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_analysis(result)
    
    sys.exit(0 if result.get("failure_status") == "success" else 1)


if __name__ == "__main__":
    main()

