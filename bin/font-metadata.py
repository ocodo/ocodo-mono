import fontforge
import configparser
import argparse

# Panose mappings
panose_mapping = {
    0: 'Any',
    1: 'No Fit',
    2: 'Text and Display',
    3: 'Script',
    4: 'Decorative',
    5: 'Pictorial',
}

panose_family_map = {v: k for k, v in panose_mapping.items()}

panose_serif_mapping = {
    0: 'Any',
    1: 'No Fit',
    2: 'Cove',
    3: 'Obtuse Cove',
    4: 'Square Cove',
    5: 'Obtuse Square Cove',
    6: 'Square',
    7: 'Thin',
    8: 'Bone',
    9: 'Exaggerated',
    10: 'Triangle',
    11: 'Normal Sans',
    12: 'Obtuse Sans',
    13: 'Perpendicular Sans',
    14: 'Flared',
    15: 'Rounded',
}

panose_serif_map = {v: k for k, v in panose_serif_mapping.items()}

panose_weight_mapping = {
    2: 'Very Light',
    3: 'Light',
    4: 'Thin',
    5: 'Book',
    6: 'Medium',
    7: 'Demi',
    8: 'Bold',
    9: 'Heavy',
}

panose_weight_map = {v: k for k, v in panose_weight_mapping.items()}

panose_proportion_mapping = {
    2: 'Old Style',
    3: 'Modern',
    4: 'Even Width',
    5: 'Extended',
    6: 'Condensed',
    7: 'Very Extended',
    8: 'Very Condensed',
    9: 'Monospaced',
}

panose_proportion_map = {v: k for k, v in panose_proportion_mapping.items()}

panose_contrast_mapping = {
    2: 'None',
    3: 'Very Low',
    4: 'Low',
    5: 'Medium Low',
    6: 'Medium',
    7: 'Medium High',
    8: 'High',
    9: 'Very High',
}

panose_contrast_map = {v: k for k, v in panose_contrast_mapping.items()}

panose_stroke_variation_mapping = {
    2: 'No Variation',
    3: 'Gradual/Diagonal',
    4: 'Gradual/Transitional',
    5: 'Gradual/Vertical',
    6: 'Gradual/Horizontal',
    7: 'Rapid/Vertical',
    8: 'Rapid/Horizontal',
    9: 'Instant/Vertical',
}

panose_stroke_variation_map = {v: k for k, v in panose_stroke_variation_mapping.items()}

panose_arm_style_mapping = {
    2: 'Straight Arms/Horizontal',
    3: 'Straight Arms/Wedge',
    4: 'Straight Arms/Vertical',
    5: 'Straight Arms/Single Serif',
    6: 'Non-Straight Arms/Horizontal',
    7: 'Non-Straight Arms/Wedge',
    8: 'Non-Straight Arms/Vertical & Single Serif',
    9: 'Non-Straight Arms/Double Serif',
}

panose_arm_style_map = {v: k for k, v in panose_arm_style_mapping.items()}

panose_letterform_mapping = {
    2: 'Normal/Contact',
    3: 'Normal/Weighted',
    4: 'Normal/Boxed',
    5: 'Normal/Flattened',
    6: 'Normal/Rounded',
    7: 'Normal/Off Center',
    8: 'Normal/Square',
    9: 'Oblique/Contact',
    10: 'Oblique/Weighted',
    11: 'Oblique/Boxed',
}

panose_letterform_map = {v: k for k, v in panose_letterform_mapping.items()}

panose_midline_mapping = {
    2: 'Standard/Trimmed',
    3: 'Standard/Pointed',
    4: 'Standard/Serifed',
    5: 'High/Trimmed',
    6: 'High/Pointed',
    7: 'High/Serifed',
    8: 'Constant/Trimmed',
    9: 'Constant/Pointed',
    10: 'Constant/Serifed',
    11: 'Low/Trimmed',
    12: 'Low/Pointed',
    13: 'Low/Serifed',
}

panose_midline_map = {v: k for k, v in panose_midline_mapping.items()}

panose_xheight_mapping = {
    2: 'Constant/Small',
    3: 'Constant/Standard',
    4: 'Constant/Large',
    5: 'Ducking/Small',
    6: 'Ducking/Standard',
    7: 'Ducking/Large',
}

panose_xheight_map = {v: k for k, v in panose_xheight_mapping.items()}

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
    }
    
    config['OS/2 Panose'] = {
        'family': panose_mapping.get(metadata['os2_panose'][0], 'Unknown'),
        'serif': panose_serif_mapping.get(metadata['os2_panose'][1], 'Unknown'),
        'weight': panose_weight_mapping.get(metadata['os2_panose'][2], 'Unknown'),
        'proportion': panose_proportion_mapping.get(metadata['os2_panose'][3], 'Unknown'),
        'contrast': panose_contrast_mapping.get(metadata['os2_panose'][4], 'Unknown'),
        'stroke_variation': panose_stroke_variation_mapping.get(metadata['os2_panose'][5], 'Unknown'),
        'arm_style': panose_arm_style_mapping.get(metadata['os2_panose'][6], 'Unknown'),
        'letterform': panose_letterform_mapping.get(metadata['os2_panose'][7], 'Unknown'),
        'midline': panose_midline_mapping.get(metadata['os2_panose'][8], 'Unknown'),
        'xheight': panose_xheight_mapping.get(metadata['os2_panose'][9], 'Unknown'),
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
        'os2_panose': (
            panose_family_map.get(config['OS/2 Panose']['family'], 2),
            panose_serif_map.get(config['OS/2 Panose']['serif'], 0),
            panose_weight_map.get(config['OS/2 Panose']['weight'], 5),
            panose_proportion_map.get(config['OS/2 Panose']['proportion'], 9),
            panose_contrast_map.get(config['OS/2 Panose']['contrast'], 2),
            panose_stroke_variation_map.get(config['OS/2 Panose']['stroke_variation'], 2),
            panose_arm_style_map.get(config['OS/2 Panose']['arm_style'], 2),
            panose_letterform_map.get(config['OS/2 Panose']['letterform'], 2),
            panose_midline_map.get(config['OS/2 Panose']['midline'], 2),
            panose_xheight_map.get(config['OS/2 Panose']['xheight'], 4),
        ),
        'sfnt-names': dict(config['SFNT Names']),
    }
    return metadata

def main():
    parser = argparse.ArgumentParser(description='Font metadata tool')
    parser.add_argument('font_path', help='Path to the font file')
    parser.add_argument('--write', type=str, help='Output config file for metadata')
    parser.add_argument('--read', type=str, help='Input config file for metadata')
    args = parser.parse_args()

    if args.write:
        metadata = get_metadata(args.font_path)
        write_config(metadata, args.write)
        print("Metadata saved to", args.write)
    elif args.read:
        metadata = read_config(args.read)
        set_metadata(args.font_path, metadata)
        print("Metadata set successfully")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()