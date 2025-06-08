import fontforge
import configparser
import argparse

def get_metadata(font_path):
    font = fontforge.open(font_path)
    metadata = {
        'familyname': font.familyname,
        'fontname': font.fontname,
        'fullname': font.fullname,
        'version': font.version,
        'weight': font.weight,
        'copyright': font.copyright,
        'sfnt-names': {
            'copyright-notice': "",
            'font-family-name': "",
            'font-subfamily-name': "",
            'full-font-name': "",
            'version-string': "",
            'postscript-name': "",
            'trademark': "",
            'manufacturer-name': "",
            'designer': "",
            'description': "",
            'vendor-url': "",
            'designer-url': "",
            'license-description': "",
            'license-url': "",
            'preferred-family': "",
        },
        'os2_weight': font.os2_weight,
        'os2_width': font.os2_width,
        'os2_panose': font.os2_panose,
    }
    for name in font.sfnt_names:
        if name[1] == 'Copyright':
            metadata['sfnt-names']['copyright-notice'] = name[2]
        elif name[1] == 'Family':
            metadata['sfnt-names']['font-family-name'] = name[2]
        elif name[1] == 'SubFamily':
            metadata['sfnt-names']['font-subfamily-name'] = name[2]
        elif name[1] == 'Fullname':
            metadata['sfnt-names']['full-font-name'] = name[2]
        elif name[1] == 'Version':
            metadata['sfnt-names']['version-string'] = name[2]
        elif name[1] == 'PostScriptName':
            metadata['sfnt-names']['postscript-name'] = name[2]
        elif name[1] == 'Trademark':
            metadata['sfnt-names']['trademark'] = name[2]
        elif name[1] == 'Manufacturer':
            metadata['sfnt-names']['manufacturer-name'] = name[2]
        elif name[1] == 'Designer':
            metadata['sfnt-names']['designer'] = name[2]
        elif name[1] == 'Description':
            metadata['sfnt-names']['description'] = name[2]
        elif name[1] == 'Vendor URL':
            metadata['sfnt-names']['vendor-url'] = name[2]
        elif name[1] == 'Designer URL':
            metadata['sfnt-names']['designer-url'] = name[2]
        elif name[1] == 'License':
            metadata['sfnt-names']['license-description'] = name[2]
        elif name[1] == 'License URL':
            metadata['sfnt-names']['license-url'] = name[2]
        elif name[1] == 'Preferred Family':
            metadata['sfnt-names']['preferred-family'] = name[2]
    return metadata

def set_metadata(font_path, metadata):
    font = fontforge.open(font_path)
    font.familyname = metadata.get('familyname', font.familyname)
    font.fontname = metadata.get('fontname', font.fontname)
    font.fullname = metadata.get('fullname', font.fullname)
    font.version = metadata.get('version', font.version)
    font.weight = metadata.get('weight', font.weight)
    font.copyright = metadata.get('copyright', font.copyright)
    
    sfnt_names = []
    name_id_map = {
        'copyright-notice': ('English (US)', 'Copyright'),
        'font-family-name': ('English (US)', 'Family'),
        'font-subfamily-name': ('English (US)', 'SubFamily'),
        'full-font-name': ('English (US)', 'Fullname'),
        'version-string': ('English (US)', 'Version'),
        'postscript-name': ('English (US)', 'PostScriptName'),
        'trademark': ('English (US)', 'Trademark'),
        'manufacturer-name': ('English (US)', 'Manufacturer'),
        'designer': ('English (US)', 'Designer'),
        'description': ('English (US)', 'Description'),
        'vendor-url': ('English (US)', 'Vendor URL'),
        'designer-url': ('English (US)', 'Designer URL'),
        'license-description': ('English (US)', 'License'),
        'license-url': ('English (US)', 'License URL'),
        'preferred-family': ('English (US)', 'Preferred Family'),
    }
    for key, value in metadata.get('sfnt-names', {}).items():
        if key in name_id_map and value:
            sfnt_names.append((*name_id_map[key], value))
    font.sfnt_names = tuple(sfnt_names)

    font.os2_weight = metadata.get('os2_weight', font.os2_weight)
    font.os2_width = metadata.get('os2_width', font.os2_width)
    font.os2_panose = tuple(metadata.get('os2_panose', font.os2_panose))
    font.save()

def write_config(metadata, output_file):
    config = configparser.ConfigParser()
    config['Font'] = {
        'familyname': metadata['familyname'],
        'fontname': metadata['fontname'],
        'fullname': metadata['fullname'],
        'version': metadata['version'],
        'weight': metadata['weight'],
        'copyright': metadata['copyright'],
        'os2_weight': str(metadata['os2_weight']),
        'os2_width': str(metadata['os2_width']),
        'os2_panose': ','.join(map(str, metadata['os2_panose'])),
    }
    config['SFNT Names'] = metadata['sfnt-names']
    with open(output_file, 'w') as configfile:
        config.write(configfile)

def read_config(input_file):
    config = configparser.ConfigParser()
    config.read(input_file)
    metadata = {
        'familyname': config['Font']['familyname'],
        'fontname': config['Font']['fontname'],
        'fullname': config['Font']['fullname'],
        'version': config['Font']['version'],
        'weight': config['Font']['weight'],
        'copyright': config['Font']['copyright'],
        'os2_weight': int(config['Font']['os2_weight']),
        'os2_width': int(config['Font']['os2_width']),
        'os2_panose': tuple(map(int, config['Font']['os2_panose'].split(','))),
        'sfnt-names': dict(config['SFNT Names']),
    }
    return metadata

def main():
    parser = argparse.ArgumentParser(description='Font metadata tool')
    parser.add_argument('font_path', help='Path to the font file')
    parser.add_argument('--get-metadata', type=str, help='Output config file for metadata')
    parser.add_argument('--set-metadata', type=str, help='Input config file for metadata')
    args = parser.parse_args()

    if args.get_metadata:
        metadata = get_metadata(args.font_path)
        write_config(metadata, args.get_metadata)
        print("Metadata saved to", args.get_metadata)
    elif args.set_metadata:
        metadata = read_config(args.set_metadata)
        set_metadata(args.font_path, metadata)
        print("Metadata set successfully")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
