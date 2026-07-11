import streamlit as st

def render_footer():

    st.markdown("""
    <style>

    .footer{
        margin-top:70px;
        padding:35px 25px 20px 25px;
        border-top:1px solid rgba(255,255,255,.12);
    }

    .footer-bottom{
        margin-top:30px;
        padding-top:20px;
        border-top:1px solid rgba(255,255,255,.08);
        display:flex;
        justify-content:space-between;
        align-items:center;
        flex-wrap:wrap;
        gap:15px;
    }

    .copyright{
        color:#b8b8b8;
        font-size:14px;
    }

    .author{
        color:#FF4B4B;
        font-weight:600;
    }

    .social-links{
        display:flex;
        gap:12px;
    }

    .social-btn{
        display:flex;
        align-items:center;
        gap:8px;
        text-decoration:none;
        color:white;
        background:#222;
        padding:10px 18px;
        border-radius:30px;
        transition:.25s;
    }

    .social-btn:hover{
        background:#FF4B4B;
        color:white;
    }

    </style>

    <div class="footer">

        <div class="footer-bottom">

            <div class="copyright">
                © 2026 <b>FUNDUS</b> • Developed with ❤️ by
                <span class="author">Khushraj Rane</span>
            </div>

            <div class="social-links">

                <a href="https://github.com/khushraj17/FUNDUS-app"
                   target="_blank"
                   class="social-btn">
                    💻 GitHub
                </a>

                <a href="https://www.linkedin.com/in/khushraj-rane-772abb30b/"
                   target="_blank"
                   class="social-btn">
                    💼 LinkedIn
                </a>

            </div>

        </div>

    </div>

    """, unsafe_allow_html=True)