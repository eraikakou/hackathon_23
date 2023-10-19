import streamlit as st
import pandas as pd


def parse_talking_points(s):
    # Split the string by the term "Talking Point"
    points = s.split("Talking Point")

    # Filter out any empty values and strip the results to remove any leading or trailing spaces
    points = [point.split(":")[1].strip() for point in points if ":" in point]

    return points


def display_talking_points_in_streamlit(points):
    # Convert the list of points into a bullet point format using markdown
    bullet_points = "\n".join(f"- {point}" for point in points)

    # Display the bullet points in Streamlit using markdown
    st.markdown(bullet_points)


# Sample dictionary of client names with their corresponding values
clients = {
    "Credit Suisse": 1,
    "JP Morgan": 0,
    "Luis Vuitton": 1,
    "Client D": 0,
    "Client E": 1,
}

# Sample tags detected in text
tags = {
    "python": 2,
    "data": 10,
    "machine learning": 15,
    "analytics": 20,
    "visualization": 12,
    "streamlit": 30,
    "app": 5,
}


def get_tag_style(tag, count):
    base_size = 20
    size = base_size
    color = "#C07156"  # You can also use a color map based on count if you wish
    return (
        f'<span style="font-size: {size}px; color: {color}; margin: 10px;">{tag}</span>'
    )


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
            .btn-red {
                background-color: #A43725;
                color: white;
                border: none;
                margin: 2px;
                padding: 10px;
                display: inline-block;  # To make them display in line
            }

            .btn-white {
                background-color: white;
                color: grey;
                border: 1px solid black;
                margin: 2px;
                padding: 10px;
                display: inline-block;  # To make them display in line
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Trending Topics of Today")

    # Create clickable bubbles using markdown
    if "clicked_bubble" not in st.session_state:
        st.session_state.clicked_bubble = None

    # Create columns to align buttons horizontally
    col1, col2, col3, col4 = st.columns(4)

    # Place each button in its own column
    with col1:
        if st.button("Bubble Text 1"):
            st.session_state.clicked_bubble = "bubble1"
    with col2:
        if st.button("Bubble Text 2"):
            st.session_state.clicked_bubble = "bubble2"
    with col3:
        if st.button("Bubble Text 3"):
            st.session_state.clicked_bubble = "bubble3"
    with col4:
        if st.button("Bubble Text 4"):
            st.session_state.clicked_bubble = "bubble4"

    # Display content based on the clicked bubble
    if st.session_state.clicked_bubble == "bubble1":
        st.write("Hello from Bubble 1!")
    elif st.session_state.clicked_bubble == "bubble2":
        # Sample data: List of articles with titles and summaries
        articles = [
            {
                "title": "Article 1",
                "summary": "This is the summary of Article 1...",
                "points": "Talking Point 1: Canopy Growth's sales performance and strategy in battling inflation is a concern investors should seek answers to.\n\nTalking Point 2: Can the company improve on its negative gross margins, as inflation will likely exacerbate the problem?\n\nTalking Point 3: With its declining revenue, low margins, and the depletion of its cash balance, when will Canopy Growth's cash burn stop, and can it become more efficient and profitable?",
            },
            {
                "title": "Article 2",
                "summary": "Cannabis stocks, in general, have performed poorly since cannabis was legalized. Although the sector got a sales boost from legalization, it was not as big as what investors had hoped for. Additionally, cannabis companies spent many billions of dollars buying up their smaller competitors in the lead-up to legalization, which caused losses to mount in the post-legalization period. ",
                "points": "Talking Point 1: Canopy Growth's sales performance and strategy in battling inflation is a concern investors should seek answers to.\n\nTalking Point 2: Can the company improve on its negative gross margins, as inflation will likely exacerbate the problem?\n\nTalking Point 3: With its declining revenue, low margins, and the depletion of its cash balance, when will Canopy Growth's cash burn stop, and can it become more efficient and profitable?",
            },
            {
                "title": "Article 3",
                "summary": "This is the summary of Article 3...",
                "points": "Talking Point 1: Canopy Growth's sales performance and strategy in battling inflation is a concern investors should seek answers to.\n\nTalking Point 2: Can the company improve on its negative gross margins, as inflation will likely exacerbate the problem?\n\nTalking Point 3: With its declining revenue, low margins, and the depletion of its cash balance, when will Canopy Growth's cash burn stop, and can it become more efficient and profitable?",
            },
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
                # Get the parsed talking points
                talking_points = parse_talking_points(article["points"])

                # Display the parsed talking points as bullet points in Streamlit
                display_talking_points_in_streamlit(talking_points)

        st.subheader("Topics found in the articles")

        tag_html = "".join([get_tag_style(tag, count) for tag, count in tags.items()])

        st.markdown(tag_html, unsafe_allow_html=True)
        sentiment, reason = (
            "negative",
            "This article uses optimistic language and discusses positive events.",
        )
        st.subheader("Sentiment:")
        if sentiment == "positive":
            st.write("Positive 😊")
        elif sentiment == "negative":
            st.write("Negative 😞")
        else:
            st.write("Neutral 😐")

        st.subheader("Reason:")
        st.write(reason)

        st.subheader("Clients Found:")
        # Create columns equal to the number of clients
        cols = st.columns(len(clients))

        # Display each client as a button in its respective column
        for i, (client, value) in enumerate(clients.items()):
            with cols[i]:
                if value == 1:
                    st.markdown(
                        f"<button class='btn-red'>{client}</button>",
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"<button class='btn-white'>{client}</button>",
                        unsafe_allow_html=True,
                    )

    elif st.session_state.clicked_bubble == "bubble3":
        st.write("Hello from Bubble 3!")
    elif st.session_state.clicked_bubble == "bubble4":
        st.write("Hello from Bubble 4!")


if __name__ == "__main__":
    main()
