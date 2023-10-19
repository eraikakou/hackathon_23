import streamlit as st
import pandas as pd


def main():
    # Embed custom CSS
    st.markdown(
        """
        <style>
            .stButton>button {
                background: linear-gradient(to right, #ff7e5f, #feb47b); /* Gradient Color */
                border: none;              /* Remove border */
                color: #FFF;               /* White text color */
                padding: 10px 25px;        /* Some padding */
                text-align: center;        /* Centered text */
                display: inline-block;     /* Inline block */
                cursor: pointer;           /* Pointer/hand cursor on hover */
                border-radius: 50px;       /* Very rounded corners to give bubble effect */
                font-size: 16px;           /* Font size */
                box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); /* Shadow for 3D effect */
                transition: all 0.3s ease 0s; /* Smooth transition effect on hover */
            }

            .stButton>button:hover {
                background: linear-gradient(to right, #feb47b, #ff7e5f); /* Gradient Color on hover (colors reversed) */
                box-shadow: 0px 15px 20px rgba(0, 0, 0, 0.2); /* More pronounced shadow on hover */
                color: #fff;
                transform: translateY(-7px); /* Slight move upwards */
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

        # Convert articles list to DataFrame for table display
        df_articles = pd.DataFrame(articles)[["title"]]  # Only display the title in the table
        st.table(df_articles.reset_index(drop=True))

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