from streamlit_float import *

def render_ai():

    float_init()

    if "show_ai" not in st.session_state:
        st.session_state.show_ai = False

    floating_btn = st.container()

    with floating_btn:
        if st.button(" 🤖 AI", use_container_width=True):
            st.session_state.show_ai = not st.session_state.show_ai

    floating_btn.float("""
    bottom: 25px;
    right: 25px;
    width: 70px;
    z-index: 9999;
    """)

    if st.session_state.show_ai:

        chat = st.container()

        with chat:

            st.markdown("## 🤖 FUNDUS AI")

            st.write("How can I help you?")

            question = st.chat_input("Ask your question")

            if question:

                st.chat_message("user").write(question)

                st.chat_message("assistant").write(
                    "Coming soon..."
                )

        chat.float("""
            position: fixed;
            bottom: 100px;
            right: 20px;
            width: 380px;
            height: 500px;
            background: white;
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
            z-index:9999;
        """)

