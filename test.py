import streamlit as st
import pandas as pd


def main():
    # Embed custom CSS
    st.markdown(
        """
        <style>
  .stButton>button {
    background-color: #C07156;
    border: none;
    color: white; /* Color of the text */
    padding: 10px 24px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 15px; /* Adjusted for slightly rounded rectangle */
    box-shadow: 0 9px 18px rgba(0,0,0,0.25);
    transition: transform 0.2s;
    outline: none; /* Removes the default browser outline */
  }

  .stButton>button:hover,
  .stButton>button:active, /* Selector for the active state (i.e., while clicking) */
  .stButton>button:focus, /* Selector for the focus state */
  .stButton>button:hover:focus,
  .stButton>button:active:focus {
    background-color: #C07156; /* Keeps the same background color */
    box-shadow: 0px 15px 20px rgba(0, 0, 0, 0.2);
    transform: translateY(-7px);
    outline: none; /* Removes the default browser outline */
  }

  .stButton>button,
  .stButton>button:hover,
  .stButton>button:active,
  .stButton>button:focus,
  .stButton>button:hover:focus,
  .stButton>button:active:focus {
    color: white !important; /* Ensuring the text color remains white in all states */
  }
</style>

        """,
        unsafe_allow_html=True,
    )

    st.title('Trending Topics of Today')

    # Create clickable bubbles using markdown
    if 'clicked_bubble' not in st.session_state:
        st.session_state.clicked_bubble = None

    # Create columns to align buttons horizontally
    col1, col2, col3, col4 = st.columns(4)

    # Place each button in its own column
    with col1:
        if st.button('Bubble Text 1'):
            st.session_state.clicked_bubble = 'bubble1'
    with col2:
        if st.button('Bubble Text 2'):
            st.session_state.clicked_bubble = 'bubble2'
    with col3:
        if st.button('Bubble Text 3'):
            st.session_state.clicked_bubble = 'bubble3'
    with col4:
        if st.button('Bubble Text 4'):
            st.session_state.clicked_bubble = 'bubble4'

    # Display content based on the clicked bubble
    if st.session_state.clicked_bubble == 'bubble1':
        st.write('Hello from Bubble 1!')
    elif st.session_state.clicked_bubble == 'bubble2':
        # Sample data: List of articles with titles and summaries
        articles = [
            {"title": "Article 1", "summary": "This is the summary of Article 1..."},
            {"title": "Article 2", "summary": "This is the summary of Article 2..."},
            {"title": "Article 3", "summary": "This is the summary of Article 3..."},
            # ... add more articles as needed
        ]

        # Create a list of article titles for selection
        article_titles = [article["title"] for article in articles]

        # Allow the user to select an article title
        selected_title = st.selectbox("Choose an article:", article_titles)

        # Find the selected article and display its summary
        for article in articles:
            if article["title"] == selected_title:
                st.subheader("Summary:")
                st.write(article["summary"])

    elif st.session_state.clicked_bubble == 'bubble3':
        st.write('Hello from Bubble 3!')
    elif st.session_state.clicked_bubble == 'bubble4':
        st.write('Hello from Bubble 4!')


if __name__ == '__main__':
    main()