#!/usr/bin/env python3
import sys
from PIL import Image
from PIL import ExifTags

def display_tags(data):
    """Display tag metadata"""
    for tag, value in data.items():
        key = ExifTags.TAGS.get(tag, tag)
        print('Key: ' + str(key) + ', Value: ', str(value) + '\n')

def display_gpstags(data):
    """Display gps tag metadata"""
    for tag, value in data.items():
        key = ExifTags.GPSTAGS.get(tag, tag)
        print('Key: ' + str(key) + ', Value: ', str(value) + '\n')

def check_print_tag():
    """Check for write-out tags"""
    return sys.argv[1] == '-w'

def write_out_to_file(data):
    """Write metadata out to file"""
    f = open('metadata_file.txt', 'w')
    for tag, value in data.items():
        key = ExifTags.TAGS.get(tag, tag)
        f.write('Key: ' + str(key) + '  Value: ' + str(value) + '\n')
    f.close()

def extract_data(file):
    """Returns dictionary of metadata"""
    image = Image.open(file)
    data = image._getexif()
    return data

def check_args():
    """Checks arguments"""
    if len(sys.argv) == 2:
        return sys.argv[1]
    elif len(sys.argv) == 3 and sys.argv[1] == '-w':
        return sys.argv[2]
    else:
        print('insufficient arguments\nexiting program...')
        sys.exit(0)

def main():
    """Extract and handle data if available"""
    file = check_args()
    if file:
        data = extract_data(file)
        if check_print_tag():
            write_out_to_file(data)
        else:
            display_tags(data)
            # uncomment for gps metadata
            # display_gpstags(data)
    else:
        sys.exit(0)

if __name__ == "__main__":
    """Run main()"""
    main()
