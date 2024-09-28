# Web Scraping and Summarization Script

## Description

This project is a Python-based web scraping script that extracts content from Wikipedia (or any webpage), summarizes the extracted content using a transformer-based NLP model, and then writes the summarized data to a CSV file. The script uses the following key technologies:
- **BeautifulSoup**: For parsing the HTML content of a webpage.
- **Requests**: To send HTTP requests to a webpage and retrieve its content.
- **HuggingFace Transformers**: Specifically, a summarization model to condense text into a concise summary.
- **CSV module**: To save the extracted headings and summaries into a CSV file.

## Features

- Scrapes headlines and content from a webpage.
- Uses a pre-trained NLP model for summarization of text.
- Outputs the headline and summarized content to a CSV file.
  
## Technologies Used

- Python 3.x
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (for parsing HTML)
- [Requests](https://pypi.org/project/requests/) (for making HTTP requests)
- [HuggingFace Transformers](https://huggingface.co/transformers/) (for summarization)
- CSV Module (for saving the data into a CSV file)

## Setup

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.x installed on your system.
- Install the necessary Python libraries using pip.

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Ekant-Sahu/Data_scraping.git
    cd your-repo-name
    ```

2. Install the required dependencies:
    ```bash
    pip install beautifulsoup4 requests transformers torch lxml
    ```

3. Run the script:
    ```bash
    python scrap.py
    ```

The script will scrape the Wikipedia page or any page you specify, summarize the content, and save the results in a `cms_scrape.csv` file.

## Usage

1. **Scraping**: The script scrapes the page you specify in the `url` variable using BeautifulSoup to parse and extract relevant content.
  
2. **Summarization**: It summarizes each section of the webpage content using the HuggingFace Transformers summarizer model.

3. **CSV Export**: The script writes the extracted headings and summaries into a CSV file called `cms_scrape.csv`.

## Code Breakdown

- **Web Scraping**: 
    The code uses the `requests` library to fetch the webpage and `BeautifulSoup` to parse the HTML for the main content, subheads, and paragraphs.
  
- **Summarization**: 
    A pre-trained transformer-based summarizer pipeline from HuggingFace condenses the extracted text.

- **CSV Export**: 
    The extracted headings and summarized content are saved into a CSV file using the `csv` module.

## Example Output

- The script will generate a CSV file with two columns: `headline` and `summary`. Each row will contain a heading from the webpage and a corresponding summary of that section.

## Modifications

- To modify the target URL, simply update the `url` variable in the script:
    ```python
    url = 'https://en.wikipedia.org/wiki/Technology'
    ```
  
- You can adjust the summarization length by tweaking the `max_length` and `min_length` parameters in the `summarizer` call.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
