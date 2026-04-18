def format_report(analysis_data, filename):
    """Return a formatted string report."""

    """
    Analysis Report for: {filename}
    ===============================
    Word Count: {analysis_data['word_count']}
    Line Count: {analysis_data['line_count']}
    Character Count: {analysis_data['character_count']}
    Average Word Length: {analysis_data['avg_word_length']:.2f}
    """

    report = []
    report.append(f"Analysis Report for: {filename}")
    report.append("=" * 30)
    report.append(f"Word Count: {analysis_data['word_count']}")
    report.append(f"Line Count: {analysis_data['line_count']}")
    report.append(f"Character Count: {analysis_data['character_count']}")
    report.append(f"Average Word Length: {analysis_data['avg_word_length']:.2f}")
    
    return "\n".join(report)


def save_report_to_file(report_text, output_path):
    """Save the report text to a file."""

    with open(output_path, 'w') as f:
        f.write(report_text)