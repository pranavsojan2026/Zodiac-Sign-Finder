import streamlit as st
def main():
    # Zodiac signs information
    zodiac_signs = {
        1: ("Capricorn", 19, "Aquarius"),
        2: ("Aquarius", 18, "Pisces"),
        3: ("Pisces", 20, "Aries"),
        4: ("Aries", 19, "Taurus"),
        5: ("Taurus", 20, "Gemini"),
        6: ("Gemini", 20, "Cancer"),
        7: ("Cancer", 22, "Leo"),
        8: ("Leo", 22, "Virgo"),
        9: ("Virgo", 22, "Libra"),
        10: ("Libra", 22, "Scorpio"),
        11: ("Scorpio", 21, "Sagittarius"),
        12: ("Sagittarius", 21, "Capricorn"),
    }

    # Separate dictionary for images
    zodiac_images = {
        "Capricorn": "https://i.pinimg.com/736x/ab/ad/a7/abada772e1243ae29ccc07a6af586e4c.jpg",
        "Aquarius": "https://th.bing.com/th/id/OIP.y_cMUSThL1Hi0vsYGocpqgAAAA?rs=1&pid=ImgDetMain",
        "Pisces": "https://i.pinimg.com/736x/98/22/d0/9822d0d814098c2533b306489d2d91a2.jpg",
        "Aries": "https://i.pinimg.com/originals/e5/79/34/e579340c3ba4bd43231b0cda296203cf.png",
        "Taurus": "https://th.bing.com/th/id/OIP.R1OLLakYOObTNB-OzZrc6wAAAA?rs=1&pid=ImgDetMain",
        "Gemini": "https://i1.wp.com/www.wishbonix.com/wp-content/uploads/2013/06/Gemini-2.jpg?ssl=1",
        "Cancer": "https://i.pinimg.com/originals/cc/32/17/cc321792bd9808970beb188d8c64f047.jpg",
        "Leo": "https://i.pinimg.com/736x/eb/da/cb/ebdacb6194ba90b8824d63f7f1d1a975.jpg",
        "Virgo": "https://i.pinimg.com/originals/b6/e1/11/b6e111b12c55475ae48c6f3eb5996e85.png",
        "Libra": "https://th.bing.com/th/id/OIP.po-DcWJYpMrcji0P2c6K9AAAAA?rs=1&pid=ImgDetMain",
        "Scorpio": "https://i.pinimg.com/736x/b8/53/51/b853516662552590984ff10da78d86f2.jpg",
        "Sagittarius": "https://i.pinimg.com/736x/0c/53/87/0c538720fa4bb7db77591c17fc9673da.jpg",
    }

    # Style
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #00dbde, #fc00ff);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Zodiac Sign Finder")

    # Form
    with st.form("zodiac_form"):
        name = st.text_input("Enter your name:")
        month = st.selectbox("Which is your birth month:", [
            "1. January", "2. February", "3. March", "4. April", "5. May", "6. June",
            "7. July", "8. August", "9. September", "10. October", "11. November", "12. December"
        ])
        day = st.number_input("Enter your birth date:", min_value=1, max_value=31, step=1)
        submitted = st.form_submit_button("Submit")

        if submitted and name and month and day:
            month_number = int(month.split(".")[0])
            sign_info = zodiac_signs.get(month_number)
            if day <= sign_info[1]:
                zodiac_sign = sign_info[0]
            else:
                zodiac_sign = sign_info[2]
            
            st.success(f"Hey **{name}**, your Zodiac Sign is **{zodiac_sign}**!")
            st.image(zodiac_images[zodiac_sign], caption=zodiac_sign)

if __name__ == "__main__":
    main()
