import streamlit as st
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import yake

# Function to summarize text using PEGASUS
def summarize_text(text, model_name="google/pegasus-xsum"):
    # Load the PEGASUS model and tokenizer
    model = PegasusForConditionalGeneration.from_pretrained(model_name)
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    
    # Tokenize the input text
    tokens = tokenizer(text, truncation=True, padding='longest', return_tensors="pt")
    
    # Generate the summary (max_length can be adjusted for your needs)
    summary_ids = model.generate(tokens['input_ids'], max_length=150, num_beams=4, length_penalty=2.0)
    
    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Function to extract keywords using YAKE
def extract_keywords(text):
    # Initialize YAKE keyword extractor
    yake_extractor = yake.KeywordExtractor(lan="en", n=3, dedupLim=0.9, top=5)
    
    # Extract keywords
    keywords = yake_extractor.extract_keywords(text)
    
    # Return keywords
    return keywords

# Streamlit UI for the app
def main():
    # Set the title and description of the app
    st.title("🔎Summarizer & Keyword Extractor✍")
    st.markdown("This app uses PEGASUS for text summarization and YAKE for keyword extraction.")
    
    # Add a text input box for the user to input long text
    user_input = st.text_area("Enter your post for Summarization and Keyword Extraction:", height=200)
    
    # When the user presses the "Generate Summary and Keywords" button
    if st.button("Generate Summary and Keywords"):
        if user_input.strip():
            # Step 1: Summarize the text using PEGASUS
            summarized_text = summarize_text(user_input)
            st.subheader("Summarized Text:")
            st.write(summarized_text)

            # Step 2: Extract keywords from the summarized text using YAKE
            keywords = extract_keywords(summarized_text)
            st.subheader("Extracted Keywords:")
            for kw, score in keywords:
                st.write(f"Keyword: {kw}, Score: {score:.4f}")
            
            # Step 3: Suggest hashtags based on extracted keywords
            hashtags = [f"#{kw.replace(' ', '').lower()}" for kw, _ in keywords]
            st.subheader("Suggested Hashtags:")
            st.write(hashtags)
        else:
            st.warning("Please enter some text to summarize.")

# Run the app
if __name__ == "__main__":
    main()
