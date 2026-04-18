import argparse
import os
from .file_ops import read_text_file, get_all_text_files, is_valid_text_file
from .analyzer import analyze_text
from .reporter import format_report, save_report_to_file

def main():
    parser = argparse.ArgumentParser(description='Analyze text files')
    parser.add_argument('path', help='Path to file or directory')
    parser.add_argument('--output', '-o', help='Output file for report')
    
    args = parser.parse_args()
    
    if is_valid_text_file(args.path):
        # Analyze single file
        text = read_text_file(args.path)
        if text:
            analysis = analyze_text(text)
            report = format_report(analysis, args.path)
            if args.output:
                save_report_to_file(report, args.output)
            else:
                print(report)
    elif os.path.isdir(args.path): # maybe make custom function to check this, inside file_ops.py
        # Analyze all .txt files in directory
        files = get_all_text_files(args.path)
        for file_path in files:
            text = read_text_file(file_path)
            if text:
                analysis = analyze_text(text)
                report = format_report(analysis, file_path)
                print(report)
    else:
        print(f"Error: {args.path} is not a valid file or directory")

if __name__ == '__main__':
    main()