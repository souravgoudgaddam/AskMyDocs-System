import AskMyDocs.UI.streamlit_app as st
import requests

FASTAPI_URL = "http://localhost:8000"

st.set_page_config(page_title="Ask My Docs", layout="centered")

st.title("Ask My Docs")
st.write("Upload a document and ask questions using AI")

# ----------------------------
# Document Upload Section
# ----------------------------
st.header(" Upload Document")

doc_path = st.text_input(
    "Enter full PDF file path",
    placeholder="C:/Users/you/Documents/file.pdf"
)

if st.button("Upload Document"):
    if doc_path.strip() == "":
        st.warning("Please enter a valid file path")
    else:
        with st.spinner("Uploading & indexing document..."):
            res = requests.post(
                f"{FASTAPI_URL}/docAI/doc",
                json={"document": doc_path}
            )

        if res.status_code == 200:
            st.success("Document uploaded and indexed successfully!")
        else:
            st.error(f"Upload failed: {res.text}")

# ----------------------------
# Question Section
# ----------------------------
st.header(" Ask a Question")

question = st.text_input(
    "Ask something about the document",
    placeholder="What are decorators in Python?"
)

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{FASTAPI_URL}/docAI/Question",
                json={"Query": question}
            )

        if res.status_code == 200:
            answer = res.text
            st.subheader("📌 Answer")
            st.write(answer)
        else:
            st.error(f"Query failed: {res.text}")
