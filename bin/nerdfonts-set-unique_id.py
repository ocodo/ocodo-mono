#!/usr/bin/env python3
"""
NerdFont UniqueID Get/Set Tool
"""

import fontforge
import argparse
import sys

def get_unique_id(font):
    for lang, nameid, value in font.sfnt_names:
        if nameid == "UniqueID" and lang == "English (US)":
            return value
    return None

def fix_unique_id(input_ttf, output_ttf, new_id=None):
    try:
        font = fontforge.open(input_ttf)
        current_id = get_unique_id(font)
        
        if new_id is None:  # Just print current ID
            print(current_id or "No UniqueID found")
            return 0
            
        # Update logic
        sfnt_names = list(font.sfnt_names)
        modified = False
        
        for i, (lang, nameid, value) in enumerate(sfnt_names):
            if nameid == "UniqueID" and lang == "English (US)":
                sfnt_names[i] = (lang, nameid, new_id)
                modified = True
        
        if not modified:
            print(f"Warning: No UniqueID found - creating new entry", file=sys.stderr)
            sfnt_names.append(("English (US)", "UniqueID", new_id))
        
        font.sfnt_names = tuple(sfnt_names)
        font.generate(output_ttf)
        font.close()
        print(f"Updated: {current_id} → {new_id}")
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=False)
    parser.add_argument("--id", help="New UniqueID value")
    parser.add_argument("--print-id", action="store_true", help="Just print current ID")
    
    args = parser.parse_args()
    
    if args.print_id:
        font = fontforge.open(args.input)
        print(get_unique_id(font) or "No UniqueID found")
        sys.exit(0)
    
    if not args.output:
        print("Error: Output file required when setting ID", file=sys.stderr)
        sys.exit(1)
        
    sys.exit(fix_unique_id(args.input, args.output, args.id))