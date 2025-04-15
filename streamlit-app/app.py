import streamlit as st
from scraper import scrape_website
from report import generate_text_report
from urllib.parse import urlparse
import time

# Basic configuration
st.set_page_config(
    page_title="Universal Web Scraper",
    page_icon="🌐",
    layout="centered"
)

# Hide Streamlit branding
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.title("🌐 Universal Web Scraper")
st.caption("Scrape any website including subpages")

# Inputs
url = st.text_input("Enter website URL:", "https://example.com")
col1, col2 = st.columns(2)
with col1:
    depth = st.selectbox("Scraping depth:", [1, 2, 3], index=0)
with col2:
    delay = st.slider("Delay (seconds):", 0.5, 5.0, 2.0, step=0.5)

if st.button("Start Scraping", type="primary"):
    if not url:
        st.warning("Please enter a URL")
        st.stop()
    
    # Auto-add https:// if missing
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    
    try:
        start_time = time.time()
        with st.spinner(f"Scraping {url} (this may take a while)..."):
            scraped_data = scrape_website(
                url,
                max_depth=depth,
                delay=delay
            )
            
            if not scraped_data:
                st.error("No content scraped. The website might be blocking scrapers.")
                st.stop()
            
            # Generate report
            report = generate_text_report(scraped_data)
            filename = f"scrape_report_{urlparse(url).netloc}.txt"
            
            # Show results
            st.success(f"✅ Scraped {len(scraped_data)} pages in {time.time()-start_time:.1f} seconds")
            
            # Download button
            st.download_button(
                label="📥 Download Full Report",
                data=report,
                file_name=filename,
                mime="text/plain"
            )
            
            # Preview first page
            with st.expander("View first page content"):
                st.text(scraped_data[0]['content'][:2000] + "...")
                
    except Exception as e:
        st.error(f"Scraping failed: {str(e)}")
        st.info("Common issues:\n1. Website blocks scrapers\n2. Invalid URL\n3. Connection timeout")

# Footer
st.markdown("---")
st.caption("Note: Please respect websites' terms of service and robots.txt files")
