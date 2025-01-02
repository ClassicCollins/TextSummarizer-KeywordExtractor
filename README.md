

<br />
<div align="center">
  
  </a>

<h3 align="center"> 📝Summarizer & Keyword Extractor🔍</h3>

  <p align="center">
    This app uses PEGASUS and BART for text summarization and YAKE for keyword extraction.
    The app.py utilizes the PANGASUS model for text summarization, while app2.py uses the BART model for summarization. Both applications leverage YAKE for keyword   extraction. It allows users to input text, which is then summarized, and key topics are extracted. The tool also suggests relevant hashtags based   on the extracted keywords.
    <br />
    <a href="https://github.com/ClassicCollins/TextSummarizer-KeywordExtractor"><strong>Explore the Docs »</strong></a>
    <br />
    <br />
    <a href="https://summarizer-extractor2.streamlit.app/">Check Out app.py</a>
    ·
    <a href="https://summarizer-extractor.streamlit.app/">Check out app2.py</a>
    ·
  </p>
</div>


- `Features`
  
  -  Text Summarization: Uses the PEGASUS and BART model to summarize long texts into concise versions.
  -  Keyword Extraction: Extracts important keywords from the summarized text using the YAKE algorithm.
  -  Hashtag Generation: Suggests hashtags based on the extracted keywords.

- `Installation`

To run the application, you'll need Python installed on your machine. Make sure to install the following dependencies:
1. Clone the repo:
   ```sh
   git clone https://gitlab.com/clasiccollins/TextSummarizer-KeywordExtractor.git
   ```
   ```sh
   cd TextSummarizer-KeywordExtractor.git
   ```
2. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```
The requirements.txt file includes the following dependencies:
  - streamlit - for creating the web application.
  - transformers - for accessing and using the BART model.
  - yake - for keyword extraction.
  
- `Usage:`
1.	Start the Streamlit app by running the following command in your terminal:
2.	streamlit run app.py or app
3.	Open the app in your browser (Streamlit will automatically provide a local URL).
4.	Enter your text into the input box and click on the "Generate Summary and Keywords" button.
5.	The app will display:
  - Summarized Text: A concise version of your input.
  - Extracted Keywords: A list of keywords extracted from the summary, with their relevance scores.
  - Suggested Hashtags: Automatically generated hashtags based on the extracted keywords.

- `Example`

Input:
A long passage of text, such as an article or blog post.
Output:
  - Summarized Text: A shortened version of the text.
  - Keywords: Key terms like "technology," "innovation," and their relevance scores.
  - Hashtags: Suggestions like #technology, #innovation.

- `Code Overview`
  
summarizer.py

  -	summarize_text(text): Summarizes the input text using the BART model.
  - extract_keywords(text): Extracts keywords using the YAKE library.

app.py

  - Streamlit UI: Provides an interface for users to input text and see the results.
  - Generate Summary & Keywords: Processes the text to generate a summary, extract keywords, and suggest hashtags.

- `License`
This project is licensed under the MIT License - see the [LICENSE file](https://github.com/ClassicCollins/TextSummarizer-KeywordExtractor/blob/classic/LICENSE) for details.

