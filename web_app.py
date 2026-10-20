import streamlit as st
import json
import urllib.request
import pandas as pd

# Ultra-Safe Local AI Engine Core Connection
def call_local_ai_analyzer(review_text):
    url = "http://localhost:11434/api/generate"
    system_instruction = (
        "Analyze the following customer review and provide your output strictly in a valid JSON structure format. "
        "Do not include any extra text, just output the JSON object with keys: "
        '"Sentiment" (use exactly Positive, Negative, or Neutral), "Topic" (2-3 words), and "Suggestion" (1-2 sentences).'
    )
    full_prompt = f"{system_instruction}\n\nCustomer Review: \"{review_text}\""
    body = {"model": "phi3", "prompt": full_prompt, "stream": False}
    
    try:
        req = urllib.request.Request(
            url, data=json.dumps(body).encode('utf-8'), headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            raw_res = json.loads(response.read().decode('utf-8'))['response'].strip()
            if "```" in raw_res:
                raw_res = raw_res.split("```")[1]
                if raw_res.startswith("json"):
                    raw_res = raw_res[4:].strip()
            return json.loads(raw_res)
    except Exception as e:
        return {
            "Sentiment": "Neutral",
            "Topic": "Product Feedback",
            "Suggestion": f"Parsed analysis directly. Code Log: {str(e)}"
        }

# --- STREAMLIT STATE MANAGER FOR HISTORY LEDGER ---
if "review_history" not in st.session_state:
    st.session_state.review_history = []

# --- STREAMLIT UI LAYOUT PREMIUM DESIGN ---
st.set_page_config(page_title="Enterprise AI Dashboard Pro", page_icon="🤖", layout="wide")

# Sidebar Portfolio Section Layout
with st.sidebar:
    st.title("👨‍💻 Developer Hub")
    st.info("**Dawalsab A. Halyala**\n\nBSc CS AI Platform Architect")
    st.markdown("---")
    st.subheader("🖥️ Hardware Cluster")
    st.success("**Machine:** ASUS TUF A16\n**GPU:** RTX 4050\n**Infrastructure Cost:** ₹0 / Free")

# Main Title Header
st.title("🤖 Advanced Enterprise AI Customer Review Analyzer Pro")
st.caption("🚀 Automated Data Parsing Ecosystem for High-Volume Brands — Scaled locally on ASUS TUF Cluster")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Input Feedback Channel")
    user_review = st.text_area(
        "Paste customer text sheet details below:",
        placeholder="Type or paste customer experience metrics here...",
        height=180
    )
    trigger_btn = st.button("🚀 Execute Neural Extraction", type="primary", use_container_width=True)

with col2:
    st.subheader("📊 Live Analysis Report")
    
    if trigger_btn:
        if user_review.strip() == "":
            st.warning("Please enter a valid review text first!")
        else:
            with st.spinner("Processing deep matrix parameters on RTX 4050 Local GPU..."):
                ai_data = call_local_ai_analyzer(user_review)
            
            sentiment = ai_data.get("Sentiment", "Neutral")
            topic = ai_data.get("Topic", "General Feedback")
            suggestion = ai_data.get("Suggestion", "Review analyzed by the core engine layer.")
            
            # Save into live history state manager
            st.session_state.review_history.append({
                "Review Text": user_review,
                "Sentiment": sentiment,
                "Core Topic": topic,
                "Action Plan": suggestion
            })
            
            # Dynamic Card Alerts with Colors & Emojis
            if "positive" in sentiment.lower():
                st.metric(label="Detected Sentiment Indicator", value=f"😊 {sentiment}")
                st.success(f"**Core Topic:** {topic}")
            elif "negative" in sentiment.lower():
                st.metric(label="Detected Sentiment Indicator", value=f"😡 {sentiment}")
                st.error(f"**Core Topic:** {topic}")
            else:
                st.metric(label="Detected Sentiment Indicator", value=f"😐 {sentiment}")
                st.warning(f"**Core Topic:** {topic}")
                
            st.info(f"**🎯 Strategic Action Suggestion:**\n\n{suggestion}")

# --- NEW ATTRACTIVE FEATURE: LIVE DATABASE HISTORY LEDGER ---
st.markdown("---")
st.subheader("🗃️ Enterprise Review History Ledger")

if st.session_state.review_history:
    # Convert history session to dataframe matrix
    df_history = pd.DataFrame(st.session_state.review_history)
    
    # Live summary quick stats counter grids
    total_reviews = len(df_history)
    pos_count = len(df_history[df_history['Sentiment'].str.lower().str.contains('positive')])
    neg_count = len(df_history[df_history['Sentiment'].str.lower().str.contains('negative')])
    
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    stat_col1.metric("Total Reviews Logged", total_reviews)
    stat_col2.metric("Positive Sentiments", f"😊 {pos_count}")
    stat_col3.metric("Negative Sentiments", f"😡 {neg_count}")
    
    st.markdown("### Detailed Audit Trail Table")
    st.dataframe(df_history, use_container_width=True)
    
    # Export full database stack button configuration
    csv_all = df_history.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Complete History Ledger Data (CSV File)",
        data=csv_all,
        file_name="Enterprise_AI_Review_Database.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    st.info("No reviews have been analyzed in this session yet. Execute your first neural extraction above to build the live database history ledger!")
