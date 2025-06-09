#!/usr/bin/env python3
"""
NerdFont Fixup TTF SubFamily weight in TTF Names
Modifies only the English (US) SubFamily entry in TTF name table
"""

import fontforge
import argparse
import sys

def fix_subfamily_weight(input_ttf, output_ttf, weight):
    try:
        print(f'Opening NerdFont to fix: {input_ttf}')
        font = fontforge.open(input_ttf)
        
        # Update only English (US) "SubFamily" to new weight
        sfnt_names = list(font.sfnt_names)
        modified = False
        
        for i, (lang, nameid, value) in enumerate(sfnt_names):
            if nameid == "SubFamily" and lang == "English (US)":
                sfnt_names[i] = (lang, nameid, weight)
                modified = True
        
        if not modified:
            print("Warning: No English (US) SubFamily entry found in name table", file=sys.stderr)
        
        print(f"Preparing to update {input_ttf} weight: {weight}")
        font.sfnt_names = tuple(sfnt_names)
        print(f"Generating output font: {output_ttf}")
        font.generate(output_ttf)
        font.close()
        print(f"Success: Updated SubFamily to '{weight}' in {output_ttf}")
        return 0
    
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="NerdFont Fixup TTF SubFamily weight in TTF Names",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  fontforge -script fix_subfamily.py -i Input.ttf -o Output.ttf --weight Thin"
    )
    parser.add_argument("-i", "--input", required=True, help="Input TTF font file")
    parser.add_argument("-o", "--output", required=True, help="Output TTF font file")
    parser.add_argument("--weight", required=True, help="New SubFamily weight (e.g., 'Thin', 'Bold')")
    
    args = parser.parse_args()
    sys.exit(fix_subfamily_weight(args.input, args.output, args.weight))