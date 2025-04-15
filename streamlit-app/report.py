from datetime import datetime

def generate_text_report(scraped_data):
    """Generate comprehensive text report"""
    report = []
    report.append("=" * 80)
    report.append("WEB SCRAPING REPORT".center(80))
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(80))
    report.append("=" * 80)
    report.append("\n")
    
    # Summary
    report.append(f"Total Pages Scraped: {len(scraped_data)}")
    if scraped_data:
        report.append(f"Main URL: {scraped_data[0]['url']}")
    report.append("\n" + "-" * 80 + "\n")
    
    # Page details
    for i, page in enumerate(scraped_data, 1):
        report.append(f"PAGE {i}: {page['title']}")
        report.append(f"URL: {page['url']}")
        report.append("\nCONTENT:")
        report.append(page['content'])
        report.append("\n" + "-" * 40 + "\n")
    
    return "\n".join(report)