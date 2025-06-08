import fontforge

def main():
    font_path = sys.argv[1]
    font = fontforge.open(font_path)
    panose = font.os2_panose
    print(panose)

if __name__ == '__main__':
    import sys
    main()