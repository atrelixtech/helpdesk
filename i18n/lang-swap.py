#!/usr/bin/env python3

import re
import argparse
import os

def replace_word_in_msgid(msgid, target_word, replacement_word):
    """
    Replace the target word in the msgid with the replacement word.
    """
    return msgid.replace(target_word, replacement_word)

def process_file(input_file, output_file, target_word, replacement_word):
    """
    Process the input file by replacing words in msgid and writing to the output file.
    If msgid contains the target word, modify msgstr; otherwise, leave msgstr empty.
    All other lines from the input are preserved.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Check if the line contains a msgid and msgstr pair
            msgid_match = re.match(r'msgid "((\\"|[^"])*)"', line)
            msgstr_match = re.match(r'msgstr "((\\"|[^"])*)"', line)

            if msgid_match:
                # Found msgid, check for the corresponding msgstr
                msgid = msgid_match.group(1)
                msgstr = ''

                # Write msgid to the output
                outfile.write(f'msgid "{msgid}"\n')

                # Look ahead to the next line to find the msgstr (if present)
                next_line = infile.readline()
                if msgstr_match := re.match(r'msgstr "((\\"|[^"])*)"', next_line):
                    msgstr = msgstr_match.group(1)

                # Replace the target word in msgstr if needed
                if target_word in msgid:
                    modified_msgstr = replace_word_in_msgid(msgid, target_word, replacement_word)
                else:
                    modified_msgstr = msgstr

                # Write the modified msgstr
                outfile.write(f'msgstr "{modified_msgstr}"\n')
            else:
                # Not a msgid line, copy it to the output file as is
                outfile.write(line)

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Process a text file and replace words in msgid.")

    # Required parameters
    parser.add_argument('input_file', help="The input file to process.")
    parser.add_argument('target_word', help="The word to replace in the msgid.")
    parser.add_argument('replacement_word', help="The word to replace the target_word with in the msgid.")

    # Optional parameter for output file
    parser.add_argument('--output_file', help="The output file to save the modified content. If not provided, it will use the input file name with an '.out' suffix.")

    # Parse arguments
    args = parser.parse_args()

    # Set output file name
    if args.output_file:
        output_file = args.output_file
    else:
        # Get the base name and extension of the input file
        base_name, ext = os.path.splitext(args.input_file)

        # If there's an extension, prefix '.out' to it; otherwise, append '.out'
        if ext:
            output_file = f"{base_name}.out{ext}"
        else:
            output_file = f"{base_name}.out"

    # Process the file
    process_file(args.input_file, output_file, args.target_word, args.replacement_word)
    print(f"File processed successfully. Output saved to '{output_file}'.")

if __name__ == "__main__":
    main()

