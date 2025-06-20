import streamlit as st


def main():
    st.set_page_config(page_title="PDF Summary Talk", page_icon=":books:")
    st.header("PDF Summary Talk :books:")
    st.text_input("Ask question about Document")
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload PDF Here and Press on Process")
        st.button("Process")




if __name__ == "__main__":
    main()
