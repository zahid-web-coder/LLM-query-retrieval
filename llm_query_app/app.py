import streamlit as st
import json
from utils.document_loader import extract_text
from utils.vector_search import search
from utils.llm_explainer import explain_clause
from utils.decision_engine import infer_decision
from utils.pdf_highlighter import highlight_clauses_in_pdf

# Page config
st.set_page_config(page_title="LLM Query Retrieval", layout="wide")
st.title("🔍 LLM-Powered Intelligent Query–Retrieval System")

# Header
st.markdown("## 📄 Legal Clause Search with AI")
st.markdown(
    "Upload a contract or legal document 📑\n\n"
    "Enter your query in plain English 💬\n\n"
    "Get the most relevant clauses, simplified explanations, and a final decision ✅"
)

st.markdown("---")

# Example queries
with st.expander("💡 Example Queries"):
    st.markdown("- 'Will my knee surgery be covered after 3 months?'")
    st.markdown("- 'Is accident on day 1 eligible for claim?'")

# File Upload + Query Input
uploaded_file = st.file_uploader("📄 Upload Document", type=["pdf", "docx"])
st.caption("Supports PDF or DOCX only. Preferably 1–5 page legal docs for best results.")
query = st.text_input("💬 Enter your natural language query")

# Run Button
if st.button("🚀 Run Query"):
    if not uploaded_file or not query:
        st.warning("⚠️ Please upload a document and enter a query.")
    else:
        # Step 1: Extract document text
        try:
            doc_text = extract_text(uploaded_file, uploaded_file.name)
            st.success("✅ Document processed successfully.")
        except Exception as e:
            st.error(f"❌ Error extracting text: {e}")
            st.stop()

        # Step 2: Vector Search
        try:
            with st.spinner("🔍 Searching matching clauses..."):
                results = search(query)

            explanations = []
            matched_clauses = []

            st.markdown("### 🔍 Top Matched Clauses")
            for idx, res in enumerate(results):
                clause_text = res['chunk_text']
                matched_clauses.append(clause_text)

                st.markdown(f"**{idx+1}. {clause_text}**")

                explanation = explain_clause(query, clause_text)
                explanations.append(explanation)
                st.markdown(f"🔹 *Explanation*: {explanation}")

                st.caption(
                    f"📍 Source: {res['metadata'].get('source', 'N/A')} | "
                    f"Page: {res['metadata'].get('page', 'N/A')} | "
                    f"Score: {res['score']:.4f}"
                )

                if idx < len(results) - 1:
                    st.markdown("---")

            # Step 3: Decision Logic
            decision_data = infer_decision(query, explanations)

            # Step 4: Output JSON
            output_json = {
                "decision": decision_data["decision"],
                "amount": decision_data["amount"],
                "justification": decision_data["justification"],
                "explanations": explanations,
                "metadata": [r["metadata"] for r in results]
            }

            # Step 5: Display Results
            st.markdown("### ✅ Final Decision")

            if decision_data["decision"].lower() == "approved":
                st.success(f"**Decision:** {decision_data['decision']}")
            else:
                st.error(f"**Decision:** {decision_data['decision']}")

            st.write(f"**Estimated Amount:** {decision_data['amount']}")

            st.markdown("### 🧾 Output JSON")
            st.json(output_json)

            # Step 6: Download JSON
            st.download_button(
                "📥 Download Output JSON",
                json.dumps(output_json, indent=2),
                "output.json",
                "application/json"
            )

            # Step 7: Highlight PDF
            if uploaded_file.name.lower().endswith(".pdf"):
                st.markdown("### 🖍️ Highlighted PDF")
                try:
                    uploaded_file.seek(0)
                    highlighted_pdf = highlight_clauses_in_pdf(uploaded_file, matched_clauses)

                    st.download_button(
                        label="📥 Download Highlighted PDF",
                        data=highlighted_pdf,
                        file_name="highlighted_output.pdf",
                        mime="application/pdf"
                    )
                except Exception as e:
                    st.error(f"❌ Failed to generate highlighted PDF: {e}")

        except Exception as e:
            st.error(f"❌ Search failed: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ for HackRx 6.0 by Tech Bytes")
